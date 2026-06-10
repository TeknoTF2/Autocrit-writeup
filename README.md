# Permafrost — AutoCrit-Style Writeup

A static website containing a full editorial workup of the **Permafrost** series (Books 1 & 2, manuscripts in this repository as `.docx` files).

## The site

Open `site/index.html` in any browser — no build step, no dependencies.

| Page | Contents |
|---|---|
| `site/index.html` | Series overview, verdict, score dashboard |
| `site/analysis.html` | Story & structure analysis, themes & motifs, character arcs, chapter-by-chapter notes for all 70 chapters, world/setting dossier |
| `site/beta-read.html` | Detailed beta reader feedback: reader-experience report, AutoCrit-style prose metrics (pacing charts, adverb/filter-word/repetition data computed from the manuscripts), continuity & error log with line references, prioritized revision roadmap |
| `site/market-fuel.html` | Market positioning, comp titles, target readership, publishing-path recommendation, tagline/blurb/query drafts, categories & keywords, risk register, extractable marketing assets |

## Fix tooling

| File | Purpose |
|---|---|
| `tools/fix_dialogue_tags.py` | Auto-repairs the mechanical issues in the `.docx` manuscripts while preserving formatting: dialogue-tag punctuation (`"Text." She said.` → `"Text," she said.` — 1,225 fixes across both books), plus optional `--hoard` (horde misspelling, Book 2 only), `--ellipsis` (`..` → `…`), and `--quotes` (straight apostrophes → curly). Ambiguous near-misses ("She said it flatly…") are never changed — they go to a review file. |
| `tools/generate_tofix.py` | Regenerates `TO-FIX.md` and `STYLE-PASS.md` from the manuscripts, verifying every issue location at generation time. |
| `TO-FIX.md` | The manual worklist: 69 located issues (chapter + paragraph + verbatim quote you can Ctrl+F in Word), exhaustive sweeps (timeline references, merged speech, double spaces), and 10 author decisions with no single line to point at. |
| `STYLE-PASS.md` | The de-repetition worklist: 440 located occurrences of the 10 prose-tic constructions ("Not X. Not Y." cascades, the "of a man who…" formula, "the kind of", duplicated similes, etc.), grouped by chapter, with per-tic guidance on what to keep. |
| `fixed/` | Output of a full run: `[fixed].docx` manuscripts, per-change CSV logs, and the manual-review files. |

```bash
pip install python-docx
python3 tools/fix_dialogue_tags.py "Permafrost 1 Full.docx" --ellipsis --quotes
python3 tools/fix_dialogue_tags.py "Permafrost 2 Full.docx" --ellipsis --quotes --hoard
python3 tools/generate_tofix.py
```

## Methodology

Both manuscripts (227,934 words across 70 chapters) were read in full. Quantitative metrics — word counts, sentence statistics, dialogue share, adverb and filter-word frequencies, repeated n-grams, dialogue-tag audit — were computed directly from the extracted manuscript text. All quotations on the site are verbatim from the manuscripts; line references in the error log point to plain-text extractions of the `.docx` files (one paragraph per line).
