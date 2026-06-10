#!/usr/bin/env python3
"""
fix_dialogue_tags.py — automatic repair of dialogue-tag punctuation in the
Permafrost manuscripts (.docx), preserving character formatting.

THE PROBLEM
    "It helps me think." She said.      ->   "It helps me think," she said.
    'I could go out.' He thought.       ->   'I could go out,' he thought.
    "How long?" He asked.               ->   "How long?" he asked.
    "Run!" She shouted.                 ->   "Run!" she shouted.

HOW IT WORKS
  * Periods before a closing quote followed by a speech tag become commas.
  * The tag's first word is lowercased when it is a pronoun/article
    (he, she, they, the, a, an, his, her, their, it, one, someone, ...).
    Proper names (Cain, Muse, Thane Aldrich...) keep their capital.
  * After ? ! or ellipsis, only the lowercasing is applied (punctuation kept).
  * SAFETY: a match is only converted when the words after the tag verb look
    like a tag continuation (punctuation, an -ly adverb, or a whitelisted
    preposition/conjunction). Anything else — "He said nothing", "He said it
    softly enough...", "He continued walking" — is NOT changed and is written
    to the review file for a human decision.
  * Every change is a same-length character substitution mapped back into the
    original .docx runs, so bold/italic/style formatting is fully preserved.

OPTIONAL EXTRA FIXES
  --hoard      hoard/hoards -> horde/hordes  (use on Book 2 ONLY — Book 1's
               single "hoard" is the correct verb in Naika's scripture)
  --ellipsis   two-dot ellipses ("but.. I", "Spark.. Spark..") -> proper "…"
  --quotes     straight apostrophes inside words ("Didn't", "They're") -> curly

OUTPUT (next to the input file, or in --outdir)
  <name> [fixed].docx   the repaired manuscript
  <name>.changes.csv    every change: chapter, paragraph-in-chapter, before, after
  <name>.review.txt     near-miss tag patterns left untouched, for manual review

USAGE
  pip install python-docx
  python3 tools/fix_dialogue_tags.py "Permafrost 1 Full.docx" --ellipsis
  python3 tools/fix_dialogue_tags.py "Permafrost 2 Full.docx" --ellipsis --hoard
"""

import argparse
import csv
import re
import sys
from pathlib import Path

try:
    import docx
except ImportError:
    sys.exit("python-docx is required:  pip install python-docx")

# ---------------------------------------------------------------- patterns

VERBS = (
    "said|asked|replied|answered|muttered|growled|grumbled|snapped|whispered|"
    "shouted|called|murmured|added|continued|agreed|admitted|offered|countered|"
    "breathed|hissed|barked|sighed|groaned|managed|repeated|echoed|confirmed|"
    "pressed|warned|observed|noted|stated|announced|insisted|demanded|begged|"
    "pleaded|thought"
)

# First tag word that should be lowercased (pronouns/articles, not names).
LOWERABLE = {
    "he", "she", "they", "the", "a", "an", "his", "her", "their", "its", "it",
    "one", "someone", "everyone", "somebody", "everybody", "both", "all",
    "another", "each", "that", "this",
}

# What may follow the verb for the match to be treated as a real dialogue tag.
# Anything else (e.g. "said nothing", "said it", "continued walking") is sent
# to the review file instead of being changed.
SAFE_AFTER = (
    r"(?=\s*$|\s*[.,;:—–-]|\s+(?:\w+ly\b|from\b|to\b|without\b|after\b|"
    r"back\b|as\b|again\b|between\b|through\b|over\b|at\b|around\b|out\b|"
    r"aloud\b|before\b|into\b|with\b|under\b|once\b|twice\b|when\b|and\b|"
    r"but\b|toward\b|towards\b|across\b|behind\b|beside\b|against\b|down\b|"
    r"up\b|in\b))"
)

CLOSERS = "”\"’"  # curly double, straight double, curly single (thought-quotes)

SUBJ = r"(?P<first>[A-Z][\w’']*)(?P<rest>(?:\s+[\w’']+){0,2}?)"

RX_PERIOD = re.compile(
    rf"(?P<dot>\.)(?P<q>[{CLOSERS}])\s+{SUBJ}\s+(?P<verb>{VERBS})\b{SAFE_AFTER}"
)
RX_PUNCT = re.compile(
    rf"(?P<dot>[?!…])(?P<q>[{CLOSERS}])\s+{SUBJ}\s+(?P<verb>{VERBS})\b{SAFE_AFTER}"
)
RX_COMMA = re.compile(
    rf"(?P<dot>,)(?P<q>[{CLOSERS}])\s+{SUBJ}\s+(?P<verb>{VERBS})\b{SAFE_AFTER}"
)
# Broad version (no SAFE_AFTER guard) used to detect near-misses for review.
RX_BROAD = re.compile(
    rf"(?P<dot>[.?!…])[{CLOSERS}]\s+(?P<first>[A-Z][\w’']*)"
    rf"(?:\s+[\w’']+){{0,2}}?\s+(?:{VERBS})\b"
)

RX_HOARD = re.compile(r"\b(?P<w>[Hh]oard)(?P<s>s?)\b")
RX_TWODOT = re.compile(r"(?<!\.)\.\.(?!\.)")
RX_APOS = re.compile(r"(?<=[A-Za-z])'(?=[A-Za-z])")

CHAPTER_RX = re.compile(r"^Chapter\s+[A-Za-z-]+(?:\s+[A-Za-z-]+)?$")


# ---------------------------------------------------------------- mechanics

def char_ops_for_paragraph(text, fix_hoard):
    """Return (ops, changes) where ops = [(index, new_char)] same-length
    substitutions, and changes = [(fix_type, before_snip, after_snip)]."""
    ops, changes = [], []

    def snip(start, end):
        a, b = max(0, start - 30), min(len(text), end + 35)
        return text[a:b].replace("\n", " ")

    for rx, kind in ((RX_PERIOD, "period->comma"),
                     (RX_PUNCT, "lowercase tag"),
                     (RX_COMMA, "lowercase tag")):
        for m in rx.finditer(text):
            first = m.group("first")
            local = []
            if kind == "period->comma":
                local.append((m.start("dot"), ","))
            if first.lower() in LOWERABLE:
                local.append((m.start("first"), first[0].lower()))
            if not local:
                continue  # e.g. "?" + proper name: already correct
            ops.extend(local)
            before = snip(m.start(), m.end())
            after = before
            for idx, ch in local:
                rel = idx - max(0, m.start() - 30)
                if 0 <= rel < len(after):
                    after = after[:rel] + ch + after[rel + 1:]
            changes.append((kind, before, after))

    if fix_hoard:
        for m in RX_HOARD.finditer(text):
            w = m.group("w")          # hoard / Hoard
            new = ("H" if w[0] == "H" else "h") + "orde"
            for i, ch in enumerate(new):
                if text[m.start("w") + i] != ch:
                    ops.append((m.start("w") + i, ch))
            changes.append(("hoard->horde", snip(m.start(), m.end()),
                            snip(m.start(), m.end()).replace(w + m.group("s"),
                                                             new + m.group("s"))))
    # dedupe by index (keep first)
    seen, unique = set(), []
    for idx, ch in ops:
        if idx not in seen:
            seen.add(idx)
            unique.append((idx, ch))
    return unique, changes


def apply_ops_to_runs(paragraph, ops):
    """Apply same-length char substitutions to the paragraph's runs."""
    runs = paragraph.runs
    bounds, pos = [], 0
    for r in runs:
        bounds.append((pos, pos + len(r.text), r))
        pos += len(r.text)
    for idx, ch in ops:
        for s, e, r in bounds:
            if s <= idx < e:
                t = r.text
                r.text = t[: idx - s] + ch + t[idx - s + 1:]
                break


def fix_document(path, outdir, fix_hoard, fix_ellipsis, fix_quotes):
    doc = docx.Document(path)
    chapter, para_in_ch = "Front matter", 0
    n_tag = n_hoard = n_ellipsis = n_quotes = n_skipped = 0
    change_rows, review_rows = [], []

    for paragraph in doc.paragraphs:
        text = paragraph.text
        if CHAPTER_RX.match(text.strip()):
            chapter, para_in_ch = text.strip(), 0
            continue
        para_in_ch += 1
        if not text:
            continue

        # runs must reassemble to the paragraph text for safe surgery
        if "".join(r.text for r in paragraph.runs) != text:
            if RX_BROAD.search(text):
                review_rows.append((chapter, para_in_ch,
                                    "SKIPPED (complex runs) — fix by hand", text[:160]))
                n_skipped += 1
            continue

        ops, changes = char_ops_for_paragraph(text, fix_hoard)
        fixed_indices = {idx for idx, _ in ops}
        if ops:
            apply_ops_to_runs(paragraph, ops)
            for kind, before, after in changes:
                change_rows.append((chapter, para_in_ch, kind, before, after))
                if kind == "hoard->horde":
                    n_hoard += 1
                else:
                    n_tag += 1

        # Near-misses the strict rules refused — humans decide these.
        # Evaluated on the ORIGINAL text; matches we just fixed are excluded,
        # as are "?/! + proper name" tags, which are already correct.
        for m in RX_BROAD.finditer(text):
            if any(m.start() <= idx < m.end() for idx in fixed_indices):
                continue  # converted by the strict rules
            dot, first = m.group("dot"), m.group("first")
            if dot != "." and first.lower() not in LOWERABLE:
                continue  # e.g. ?" Carina asked — correct as written
            seg = text[m.start(): m.end() + 45]
            review_rows.append((chapter, para_in_ch, "possible tag — verify",
                                seg.replace("\n", " ")))

        if fix_ellipsis:
            for r in paragraph.runs:
                if RX_TWODOT.search(r.text):
                    n_ellipsis += len(RX_TWODOT.findall(r.text))
                    r.text = RX_TWODOT.sub("…", r.text)

        if fix_quotes:
            for r in paragraph.runs:
                if RX_APOS.search(r.text):
                    n_quotes += len(RX_APOS.findall(r.text))
                    r.text = RX_APOS.sub("\u2019", r.text)

    stem = Path(path).stem
    outdir.mkdir(parents=True, exist_ok=True)
    fixed_path = outdir / f"{stem} [fixed].docx"
    doc.save(fixed_path)

    with open(outdir / f"{stem}.changes.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["chapter", "paragraph_in_chapter", "fix", "before", "after"])
        w.writerows(change_rows)

    with open(outdir / f"{stem}.review.txt", "w") as f:
        f.write("Near-miss tag patterns left UNCHANGED — review by hand.\n"
                "Location = chapter + paragraph number counted from the chapter heading.\n\n")
        for ch, p, why, seg in review_rows:
            f.write(f"[{ch} · ¶{p}] ({why})\n    {seg}\n\n")

    print(f"{path}")
    print(f"  dialogue-tag fixes : {n_tag}")
    if fix_hoard:
        print(f"  hoard -> horde     : {n_hoard}")
    if fix_ellipsis:
        print(f"  '..' -> '…'        : {n_ellipsis}")
    if fix_quotes:
        print(f"  straight apostroph : {n_quotes}")
    print(f"  left for review    : {len(review_rows)} (see {stem}.review.txt)")
    if n_skipped:
        print(f"  skipped paragraphs : {n_skipped} (complex formatting)")
    print(f"  saved              : {fixed_path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", help=".docx manuscript(s)")
    ap.add_argument("--hoard", action="store_true",
                    help="also fix hoard->horde (Book 2 only!)")
    ap.add_argument("--ellipsis", action="store_true",
                    help="also fix two-dot ellipses to '…'")
    ap.add_argument("--quotes", action="store_true",
                    help="also fix straight apostrophes between letters to '\u2019'")
    ap.add_argument("--outdir", default="fixed", help="output directory (default: fixed/)")
    args = ap.parse_args()
    for f in args.files:
        fix_document(f, Path(args.outdir), args.hoard, args.ellipsis, args.quotes)


if __name__ == "__main__":
    main()
