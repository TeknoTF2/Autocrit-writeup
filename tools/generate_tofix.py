#!/usr/bin/env python3
"""
generate_tofix.py — builds TO-FIX.md, the manual-fix worklist for the
Permafrost manuscripts.

Every issue is located as:  Book · Chapter · ¶N  (paragraph number counted
from the chapter heading, headings excluded) plus a verbatim quote you can
Ctrl+F in Word. Quotes are pulled live from the .docx files, so locations
are verified at generation time; any entry whose anchor text can't be found
is flagged [LOCATION NOT VERIFIED].

Also writes STYLE-PASS.md: every occurrence of the manuscript's repeated
prose constructions ("Not X. Not Y.", "the kind of", the "of a man who..."
characterization formula, etc.), located the same way, for the
de-repetition pass.

Usage:
  pip install python-docx
  python3 tools/generate_tofix.py    # writes TO-FIX.md + STYLE-PASS.md in repo root
"""

import re
import sys
from pathlib import Path

try:
    import docx
except ImportError:
    sys.exit("python-docx is required:  pip install python-docx")

ROOT = Path(__file__).resolve().parent.parent
BOOKS = {1: ROOT / "Permafrost 1 Full.docx", 2: ROOT / "Permafrost 2 Full.docx"}
CHAPTER_RX = re.compile(r"^Chapter\s+[A-Za-z-]+(?:\s+[A-Za-z-]+)?$")


def load(book):
    """Return (paras, chapter_of, para_in_chapter_of) — all 1-based by
    paragraph index matching the editorial reports' line numbers."""
    paras = [p.text for p in docx.Document(BOOKS[book]).paragraphs]
    chapter, pin = "Front matter", 0
    chapters, pins = [], []
    for t in paras:
        if CHAPTER_RX.match(t.strip()):
            chapter, pin = t.strip(), 0
        else:
            pin += 1
        chapters.append(chapter)
        pins.append(pin)
    return paras, chapters, pins


# --------------------------------------------------------------------------
# Issue database. line = paragraph index in the docx (1-based, headings
# included), anchor = text that must appear in that paragraph (re-verified
# at generation time; ±5-paragraph drift tolerated).
# --------------------------------------------------------------------------

ISSUES = [
    # --- BOOK 1 — continuity (High) ---
    dict(book=1, line=57, anchor="five days south", sev="HIGH", cat="Continuity",
         problem="Direction error: Muse computes Crimson Port as south; the city is east "
                 "(Aldrich says “East” in the same scene; the gate guard later confirms "
                 "Velldale is southwest of the Port).",
         fix="Change “south” to “east”."),
    dict(book=1, line=377, anchor="Bloodridge", sev="HIGH", cat="Continuity",
         problem="Town name spelled “Bloodridge” here but “Bloomridge” five paragraphs "
                 "later in the same speech. Book 2 settled on Bloomridge.",
         fix="Change to “Bloomridge” (this paragraph and the second occurrence below)."),
    dict(book=1, line=384, anchor="Bloodridge", sev="HIGH", cat="Continuity",
         problem="Second “Bloodridge” in the same Harbormaster speech; the same sentence "
                 "then gives distances “from Bloomridge”.",
         fix="Change to “Bloomridge”."),
    dict(book=1, line=351, anchor="three days", sev="HIGH", cat="Continuity",
         problem="Travel-day math: the walk to Crimson Port is depicted as two days/two nights "
                 "(depart dawn, one camp, arrive dusk) but is called three days here.",
         fix="Either add a skipped day on the road in Ch. 2–3 or change the three "
             "references to “two days” (see the two entries below)."),
    dict(book=1, line=371, anchor="three days", sev="HIGH", cat="Continuity",
         problem="Harbormaster: “You walked here in three days?” — same discrepancy.",
         fix="Conform with the decision above."),
    dict(book=1, line=708, anchor="Three days", sev="HIGH", cat="Continuity",
         problem="“Three days on the road to Crimson Port” — same discrepancy.",
         fix="Conform with the decision above."),
    dict(book=1, line=426, anchor="silver hair", sev="HIGH", cat="POV",
         problem="Blind-POV violation: Muse perceives Carina's “silver hair” and a silent "
                 "“twitch” — the only hard sight-break in her chapters.",
         fix="Re-render through sound/touch: breathing rhythm, the rustle of blankets, "
             "the heat of the cot."),
    dict(book=1, line=209, anchor="Five voices", sev="MED", cat="Continuity",
         problem="“Five voices said at once” — Carina is the one being answered; only "
                 "four other party members exist.",
         fix="“Four voices”."),
    dict(book=1, line=990, anchor="thousands of years", sev="MED", cat="Continuity",
         problem="“Thousands of years” contradicts “a thousand years” / “a millennium” "
                 "used everywhere else for the seal.",
         fix="“a thousand years”."),
    dict(book=1, line=1220, anchor="Two months ago", sev="MED", cat="Timeline",
         problem="“Two months ago it was a hundred and twenty thousand” — the dome fell "
                 "roughly five weeks before this scene (see the “two months” sweep below).",
         fix="“A month ago” / “Five weeks ago”, or explicitly date the plague pre-dome."),
    dict(book=1, line=1317, anchor="Twenty years of war", sev="MED", cat="Continuity",
         problem="“Twenty years of war had wired that in deep” sits oddly against Cain's "
                 "much longer pre-seal career stated elsewhere.",
         fix="“Decades of war”, or align with his stated service span."),
    dict(book=1, line=1389, anchor="Midas", sev="MED", cat="World",
         problem="Real-world bleed: “Even Midas never had one of these” cites an Earth myth "
                 "inside a secondary world.",
         fix="Replace with an in-world figure (a legendary ancestor of the Lord of Gold "
             "would do the same work)."),
    dict(book=1, line=894, anchor="crest", sev="MED", cat="Logic",
         problem="“Cain knew the title before anyone said it because there was a crest on "
                 "the wall” — a crest explains the title, not the personal name "
                 "“Andromalius”, which no one has spoken yet.",
         fix="Put the name on the banner/crest, or delay the name until it's spoken."),
    dict(book=1, line=574, anchor="three weeks", sev="MED", cat="Logic",
         problem="Rations issued (three weeks for five) don't cover the briefed one-way "
                 "itinerary (~4.5 weeks to Solarspire); nobody remarks on the gap.",
         fix="One line acknowledging planned resupply at Wolkenfeld — or let Gormund "
             "grumble the math."),
    dict(book=1, line=970, anchor="stopped walking", sev="MED", cat="Draft fossil",
         problem="“She stopped walking” inside a room scene — Ch. 9 re-opens earlier in "
                 "the evening Ch. 8 already closed, and this beat is left over from a "
                 "street-scene draft.",
         fix="Re-anchor Ch. 9's opening after Ch. 8's close; cut or convert the movement beat."),
    dict(book=1, line=1069, anchor="wards", sev="MED", cat="Dropped thread",
         problem="The bedroom wards are the stated reason Carina must infiltrate solo — "
                 "and they are never triggered, disabled, or mentioned again.",
         fix="One line in Ch. 10/11 of Carina bypassing them, or cut the ward rationale. "
             "(This paragraph also has a missing break between two speakers — see the "
             "merged-paragraph sweep.)"),
    dict(book=1, line=1173, anchor="bell", sev="MED", cat="Logic",
         problem="A third-floor alarm bell ambushes the party after Uthesia's recon was "
                 "declared complete (“everything mapped and timed”).",
         fix="Have the recon note an unverified upper floor, or let Uthesia own the miss "
             "in interiority."),
    dict(book=1, line=694, anchor="tomorrow", sev="MED", cat="Dropped thread",
         problem="Gormund resolves to tell Cain about the stalking sound “tomorrow”; the "
                 "report never happens on-page (and Cain independently conceals his own "
                 "sighting in Ch. 3).",
         fix="A two-line exchange on the next morning's march closes the loop and lets "
             "both men learn the other heard it too."),
    dict(book=1, line=1294, anchor="skull", sev="MED", cat="Prose",
         problem="The maid's death sentence is garbled: the sequencing of punch → shield → "
                 "maid → Andromalius is unclear, and “the blow not meant to kill him” "
                 "reads ambiguously against the woman just killed.",
         fix="Rewrite in strict sequence: the punch goes through the shield, the maid dies, "
             "the remaining force carries into Andromalius."),
    dict(book=1, line=2290, anchor="degrees of frost", sev="MED", cat="Derivation",
         problem="The interstitial epigraph is an unattributed close paraphrase of Jack "
                 "London's ‘To Build a Fire’; its math also assumes water freezes at 30° "
                 "(−50° → “80 degrees of frost”; it's 82).",
         fix="Attribute it, rework it into original phrasing, or frame it as an in-world text "
             "— and fix the arithmetic if the Fahrenheit logic stays."),
    # --- BOOK 1 — minor mechanics ---
    dict(book=1, line=148, anchor="grace period", sev="MINOR", cat="Diction",
         problem="Malapropism: “the grace period of a kicked hornet's nest”.",
         fix="Probably “the grace of a kicked hornet's nest”."),
    dict(book=1, line=317, anchor="minutes past", sev="MINOR", cat="Typo",
         problem="“Five more minutes past.” — wrong word.",
         fix="“passed”."),
    dict(book=1, line=532, anchor='-+', sev="MINOR", cat="Artifact",
         problem="Stray characters after the closing quote: ‘…a generous curve.”-+’",
         fix="Delete “-+”."),
    dict(book=1, line=1067, anchor="How", sev="MINOR", cat="Formatting",
         problem="Two speakers merged into one paragraph: ‘…Not until now.”“How?” "
                 "Gormund asked.’",
         fix="Insert a paragraph break before ““How?”” (see merged-paragraph sweep for "
             "all instances)."),
    dict(book=1, line=1284, anchor="embedded", sev="MINOR", cat="Prose",
         problem="Awkward: “One embedded into her shoulder”.",
         fix="“One buried itself in her shoulder” (or similar)."),
    dict(book=1, line=1416, anchor=" ki ", sev="MINOR", cat="Consistency",
         problem="“ki” used here; “qi” everywhere else in Book 1 (Book 2 then uses "
                 "“ki” throughout).",
         fix="Pick one romanization for the series and conform both books."),
    dict(book=1, line=1442, anchor="fathers shop", sev="MINOR", cat="Typo",
         problem="Missing apostrophe: “his fathers shop”.",
         fix="“his father's shop”."),
    dict(book=1, line=1586, anchor="still settled", sev="MINOR", cat="Prose",
         problem="“So they all still settled into a fighting stance.” — “still” is doing "
                 "unclear work.",
         fix="Cut “still” or rephrase (“So they settled into fighting stances anyway.”)."),
    dict(book=1, line=1672, anchor="experienced opinion", sev="MINOR", cat="Typo",
         problem="Missing terminal punctuation: “In your experienced opinion”",
         fix="Add the period/question mark."),
    dict(book=1, line=1673, anchor="keeps trying", sev="MINOR", cat="Tense",
         problem="Present tense in past narration: “Even in this state he keeps trying to "
                 "make her feel better.”",
         fix="“kept trying”."),
    dict(book=1, line=1968, anchor="ordinance", sev="MINOR", cat="Diction",
         problem="“ordinance” (a law) for “ordnance” (munitions).",
         fix="“ordnance”."),
    dict(book=1, line=2109, anchor="has a destination", sev="MINOR", cat="Tense",
         problem="Present tense in past narration: “Every crate has a destination.”",
         fix="“had”."),
    dict(book=1, line=2340, anchor="thick and clumsy", sev="MINOR", cat="Typo",
         problem="Dropped verb: “his fingers thick and clumsy inside gloves”.",
         fix="“his fingers were thick and clumsy…”"),
    dict(book=1, line=2341, anchor="shoved his under", sev="MINOR", cat="Typo",
         problem="Missing word: “He shoved his under his armpits.”",
         fix="“He shoved his hands under his armpits.”"),
    dict(book=1, line=2377, anchor="awake.The", sev="MINOR", cat="Typo",
         problem="Missing space: “Cain was already awake.The satyr…”",
         fix="Add the space."),
    dict(book=1, line=2597, anchor="mothers face", sev="MINOR", cat="Typo",
         problem="Missing apostrophe: “the expression on her mothers face”.",
         fix="“her mother's face”."),
    dict(book=1, line=2930, anchor="is necessary", sev="MINOR", cat="Tense",
         problem="Present tense in past narration: “Each one is necessary.”",
         fix="“was”."),

    # --- BOOK 2 — continuity (High) ---
    dict(book=2, line=347, anchor="eyes were bloodshot", sev="HIGH", cat="Continuity",
         problem="Cain is one-eyed (“the only one he had left”, this same chapter): "
                 "“His eyes were bloodshot”.",
         fix="“His eye was bloodshot” — also at the next entry and Ch. 13."),
    dict(book=2, line=358, anchor="eyes", sev="HIGH", cat="Continuity",
         problem="Second “eyes” plural for Cain in the same sequence.",
         fix="Singular."),
    dict(book=2, line=1303, anchor="eyes opened", sev="HIGH", cat="Continuity",
         problem="Cain's wake-up: “His eyes opened.”",
         fix="“His eye opened.”"),
    dict(book=2, line=1622, anchor="Our grandmother", sev="MED", cat="Continuity",
         problem="Genealogy slip: Elizabeth tells her father “Our grandmother was "
                 "fifty-third. Our great-grandfather was forty-first.” His grandmother is "
                 "her GREAT-grandmother.",
         fix="“Your grandmother… your great-grandfather” (or “Grandmother was…” from "
             "her own reference point, shifted one generation)."),
    dict(book=2, line=1187, anchor="thirty percent", sev="MED", cat="Magic rules",
         problem="Suppression math: the resurrection scroll (top-tier magic) runs at "
                 "“roughly thirty percent”, but the stated rule is that higher-tier spells "
                 "retain “upward of fifty percent efficiency”.",
         fix="Adjust one number, or have Dantalion note that scrolls degrade differently "
             "from live casting."),
    dict(book=2, line=1960, anchor="ten minutes", sev="MED", cat="Magic rules",
         problem="Ghislaine cites a ~10-minute revival window, but Carina is revived after "
                 "a cross-city carry, well outside it.",
         fix="Loosen the window (“within the hour”), or show the carry beating the clock."),
    dict(book=2, line=621, anchor="forty", sev="MED", cat="Continuity",
         problem="Crew arithmetic: ~40 here, “thirty-odd” at Ch. 11, “thirty people and "
                 "three working firearms” at Ch. 15 vs Ch. 14's “two or three with basic "
                 "revolvers” — no on-page attrition.",
         fix="Pick one headcount/armament and conform, or add one line of attrition."),
    dict(book=2, line=627, anchor="war machines", sev="MED", cat="Logic",
         problem="Jane says the crew lost ten men to the ship's “walking metal war "
                 "machines” weeks earlier — yet security is dormant for hours when the "
                 "party boards.",
         fix="One line distinguishing external golems (active) from internal Angels "
             "(dormant until the keycard areas are breached) closes it."),
    dict(book=2, line=814, anchor="medical bay", sev="MED", cat="Logic",
         problem="Gormund asserts the Angel “won't fire into the medical bay” with no "
                 "stated basis.",
         fix="Give him one: Gragorgan signage, the ship's manifest, design doctrine he "
             "knows from home."),
    dict(book=2, line=2513, anchor="not to tell you where", sev="MED", cat="Continuity",
         problem="Fafnir tells Yoo that Carina “doesn't want to see you” (four paragraphs "
                 "up) and “asked me not to tell you where she went” — Carina never asked "
                 "either on-page; in Ch. 20 she only asked him to relay a message "
                 "(“Tell her I'm ok. And that I'll find her when I'm ready.”).",
         fix="Either have Carina say it in Ch. 20, or soften Fafnir's wording to his own "
             "inference (“I don't think she's ready to see you”)."),
    dict(book=2, line=2553, anchor="Hundreds of them", sev="MED", cat="Logic",
         problem="Dungeon-intel strain: the Sunken Grave spillage is “hundreds” and "
                 "mindless, yet the same dungeon produced a ~4,000-strong organized army "
                 "days from the capital, unnoticed despite Guild scrying and three weeks "
                 "of siege.",
         fix="One line — miasma blocks scrying, or Dantalion masked the muster — seals it."),
    dict(book=2, line=2696, anchor="the King", sev="MED", cat="Continuity",
         problem="Ostervik soldiers ask about “the King sending his army”, though the King "
                 "is later said to have died early in the dome. Plausible they wouldn't "
                 "know — but flag for intent.",
         fix="Optional one-liner about how slowly news travels under the dome."),
    dict(book=2, line=2742, anchor="Barbatos out", sev="MED", cat="Continuity",
         problem="Dantalion claims “We already got Barbatos out of the city” — Ch. 21 "
                 "shows Barbatos leaving on his own initiative. Boast or error?",
         fix="If boast, let Elizabeth needle it; if real, plant one line in Ch. 21."),
    dict(book=2, line=3539, anchor="few months", sev="MED", cat="Timeline",
         problem="Cain: “It's been weeks, Muse. Maybe a few months” — the series needs one "
                 "canonical statement of dome-age vs. the party's waking.",
         fix="Conform after writing the canonical timeline (see Decisions)."),
    dict(book=2, line=4109, anchor="days ago", sev="MED", cat="Timeline",
         problem="First receptionist: Muse left “days ago”; two paragraphs later: “about "
                 "two weeks ago”; Gormund's counted spiral runs ~11 days.",
         fix="Make both witnesses agree (~two weeks), or have the second correct the first."),
    dict(book=2, line=4119, anchor="Nine rounds", sev="MED", cat="Continuity",
         problem="Ammo ledger: 20 rounds → 1 spent (Sunken Grave) → wall-run count starts "
                 "at “Seventeen” (one phantom round) → Elder shot → “Nine rounds” here.",
         fix="Add one unnumbered shot to the Kissing Peaks fight, or start the wall count "
             "at “Eighteen”."),
    # --- BOOK 2 — minor mechanics ---
    dict(book=2, line=117, anchor="older than", sev="MINOR", cat="Prose",
         problem="Redundant double comparison: “couldn't be older than Carina, couldn't be "
                 "older than twenty” (Carina is nineteen).",
         fix="Keep one comparison."),
    dict(book=2, line=586, anchor="in full as", sev="MINOR", cat="Typo",
         problem="Missing word: “pulling the weight of a seven-foot satyr in full as "
                 "gravity worked against them”.",
         fix="“in full armor”."),
    dict(book=2, line=1267, anchor="a accusation", sev="MINOR", cat="Typo",
         problem="“under the weight of a accusation”.",
         fix="“an accusation”."),
    dict(book=2, line=1686, anchor="sure it continued", sev="MINOR", cat="Tense",
         problem="Tense slip: “And he's sure it continued to drop past that.”",
         fix="“he was sure”."),
    dict(book=2, line=1739, anchor="since Drachenburg", sev="MINOR", cat="Continuity",
         problem="“The heaviness had been building since Drachenburg” — they never reached "
                 "Drachenburg; it's buried.",
         fix="“since the riverbank” or “since Drachenburg's grave”."),
    dict(book=2, line=1972, anchor="animal", sev="MINOR", cat="Typo",
         problem="Article error plus double space: “a  animal response”.",
         fix="“an animal response”."),
    dict(book=2, line=2770, anchor="Accptance", sev="MINOR", cat="Typo",
         problem="“Accptance”.",
         fix="“Acceptance”."),
    dict(book=2, line=2786, anchor="And hers", sev="MINOR", cat="Clarity",
         problem="“Uthesia's ring. And hers.” — the antecedent (her late wife) is "
                 "unclear; reads as a grammar error on first pass.",
         fix="“Uthesia's ring. And her wife's.”"),
    dict(book=2, line=2800, anchor="her land", sev="MINOR", cat="Typo",
         problem="“She folded her hands in her land.”",
         fix="“in her lap”."),
    dict(book=2, line=2818, anchor="was care", sev="MINOR", cat="Typo",
         problem="“The voice considered the question was care.”",
         fix="“with care”."),
    dict(book=2, line=2901, anchor="wobbled", sev="MINOR", cat="Typo",
         problem="Missing period at the end: “The King Head wobbled before falling to the "
                 "ground”",
         fix="Add the period."),
    dict(book=2, line=3104, anchor="brushing", sev="MINOR", cat="Staging",
         problem="Stage-direction muddle: Dantalion “stopped brushing” after he'd already "
                 "stopped and was ruffling her hair in the previous paragraph.",
         fix="Reorder the beats (ruffle → resume brush → stop)."),
    dict(book=2, line=3272, anchor="formed", sev="MINOR", cat="Prose",
         problem="Repetition with unclear antecedent: “Arches formed above the walls as it "
                 "formed a cathedral.”",
         fix="“…as the light took the shape of a cathedral.”"),
    dict(book=2, line=3315, anchor="right here", sev="MINOR", cat="Logic",
         problem="Carina asserts Ghislaine is “right here in the—” without any way to "
                 "know her whereabouts.",
         fix="Soften to a question (“Isn't Ghislaine still in the city?”) or cut."),
    dict(book=2, line=4303, anchor="Firing a shot", sev="MINOR", cat="Prose",
         problem="Dangling participle / subject confusion: “Firing a shot, the shield was "
                 "immediately punched through, the round hit the arm at the elbow.”",
         fix="“He fired. The shot punched through the shield and hit the arm at the "
             "elbow.”"),
    dict(book=2, line=4516, anchor="Murimites", sev="MINOR", cat="Consistency",
         problem="“Murimites” appears once as a demonym — nowhere else in the series.",
         fix="Confirm it's intended, or standardize (“Murim-born”, “people of Murim”)."),
]

# Sweeps: multi-occurrence patterns listed exhaustively at generation time.
SWEEPS = [
    dict(book=1, rx=r"two months", label="“two months” timeline references",
         note="The dome fell ~3 weeks before Ch. 1 and ~6–7 weeks before Book 1's end "
              "(fixed by the outside-world chapters). Every “two months” below "
              "overstates it — decide the canonical timeline, then conform each."),
    dict(book=2, rx=r"two months", label="“two months” timeline references",
         note="Check each against the canonical timeline (some, like the Mage College's "
              "sealing, may be intentional)."),
    dict(book=1, rx=r"[”’][“‘]|[.!?…][“‘]", label="merged speech (missing break or space)",
         note="A quote opening glued directly onto preceding text — either two speakers "
              "sharing a paragraph or a missing space/break before dialogue. Insert a "
              "paragraph break (or space) at each."),
    dict(book=2, rx=r"[”’][“‘]|[.!?…][“‘]", label="merged speech (missing break or space)",
         note="Same fix: paragraph break (or space) before the opening quote."),
    dict(book=1, rx=r"  +", label="double spaces", note="Collapse to single spaces."),
    dict(book=2, rx=r"  +", label="double spaces", note="Collapse to single spaces."),
    dict(book=2, rx=r"[A-Za-z]'[A-Za-z]|\"", label="straight quotes amid curly typography",
         note="Straight apostrophes inside words are auto-fixed by the script's --quotes "
              "flag; any straight DOUBLE quotes listed below need manual open/close "
              "orientation."),
]

# --------------------------------------------------------------------------
# Prose tics for STYLE-PASS.md. Each is a construction that works in
# isolation and becomes a visible fingerprint at current frequency.
# --------------------------------------------------------------------------

TICS = [
    dict(name="The “Not X. Not Y.” negation cascade",
         rx=r"\bNot [^.!?\n]{1,45}\.\s+Not [^.!?\n]{1,45}\.(?:\s+[^.!?\n]{1,45}\.)?",
         why="Defining something by what it isn't, twice, before saying what it is. "
             "Devastating at the knock on the cabin door; numbing by the twentieth use.",
         target="Keep roughly a third — the horror beats and the chapter-defining "
                "moments. Convert the rest to a single direct statement."),
    dict(name="The “of a man/woman/someone who…” characterization formula",
         rx=r"\b\w+ of (?:a man|a woman|someone|people) who(?:’d|'d| had| was| ha[sd]n’t|)\b[^.!?\n]{0,60}",
         why="“The voice of a man who had been making decisions for weeks…” — the "
             "series' favorite way to characterize through a noun. 90 uses in Book 1, "
             "150 in Book 2; at that rate readers start seeing the machine.",
         target="Aim for once or twice per chapter. The cut test: if the sentence "
                "still lands when the clause is replaced by a concrete behavior, cut."),
    dict(name="“the kind of X that…”",
         rx=r"\bthe kind of \w+[^.!?\n]{0,55}",
         why="Same engine as the formula above; heavily clustered in Book 1's "
             "first half.",
         target="Keep the strongest one per chapter."),
    dict(name="“the particular X of a Y”",
         rx=r"\bthe particular \w+[^.!?\n]{0,55}",
         why="Book 2's variant of the formula (“the particular irritation of a "
             "craftsman…”).",
         target="Same treatment: one per chapter, best instance wins."),
    dict(name="Single-word sentence cascades",
         rx=r"(?:\b[A-Z]\w{1,9}\.\s+){3,}",
         why="“Wake. Walk. Work. Walk. Drink. Sleep.” — superb when the rhythm IS "
             "the meaning (Cain's burial, Gormund's relapse), flattening when used "
             "as a default beat.",
         target="Keep the arc-defining ones (B2 Ch. 1 and Ch. 36 are untouchable); "
                "review the rest case by case."),
    dict(name="“the way…” similes",
         rx=r"\bthe way (?:a|an|the|you|other|water|stone)\b[^.!?\n]{0,55}",
         why="“…the way water parts around a stone” — good similes that cluster "
             "into a pattern.",
         target="Thin where two occur within a few pages of each other."),
    dict(name="“filed it away” as the shared cognitive verb",
         rx=r"\bfiled (?:it|that|the \w+) away\b[^.!?\n]{0,40}",
         why="Four different POV characters all “file things away”, eroding voice "
             "separation.",
         target="Keep it for Uthesia (it fits her); give the others their own verbs."),
    dict(name="“did the math”",
         rx=r"\bdid the (?:same )?math\b[^.!?\n]{0,40}",
         why="On-theme (the survival-arithmetic motif) but repeated verbatim.",
         target="Vary the phrasing; the motif survives the synonym."),
    dict(name="“something that might/could have been…”",
         rx=r"\b[Ss]omething that (?:might|could) have been\b[^.!?\n]{0,50}",
         why="The vagueness tax: the specific noun is usually stronger.",
         target="Replace with the concrete noun unless the uncertainty is the point."),
    dict(name="Duplicated similes (verbatim repeats)",
         rx=r"stone (?:dropped )?in(?:to)? still water|moving guide to (?:a|that) stationary wall",
         why="The same image recurs nearly word-for-word — reads as accidental "
             "self-plagiarism rather than motif.",
         target="Keep the first instance of each; rewrite the repeat."),
]

STYLE_HEADER = """\
# Permafrost — Style Pass Worklist (STYLE-PASS)

Companion to TO-FIX.md, generated by `tools/generate_tofix.py`. This file
locates every occurrence of the manuscript's repeated prose constructions —
the “fingerprint” tics flagged in the beta read. None of these is an error;
each works in isolation. The problem is frequency, so the fix is curation:
**keep the best instance(s), rewrite the rest.** Suggested targets are given
per tic.

Locations are *Chapter · ¶N* (paragraph counted from the chapter heading);
the snippet is verbatim — Ctrl+F it in Word.

**Not listed here (too frequent to itemize; use Word's search):** filter
words. Search for ` looked `, ` felt `, ` heard `, ` watched `, ` knew ` —
keep them in Muse's POV (her perception verbs are diegetic), trim them in
sighted POVs where the sentence works without the filter
(“He watched her cross the room” → “She crossed the room”). Counts per book
are on the Beta Read page of the writeup site.
"""


def emit_style_pass(docs):
    out = [STYLE_HEADER]
    for tic in TICS:
        rx = re.compile(tic["rx"])
        total = {}
        sections = []
        for book in (1, 2):
            paras, chapters, pins = docs[book]
            hits = []
            for j, t in enumerate(paras):
                if CHAPTER_RX.match(t.strip()):
                    continue
                for m in rx.finditer(t):
                    seg = m.group(0).strip()
                    if len(seg) > 95:
                        seg = seg[:95] + "…"
                    hits.append((chapters[j], pins[j], seg))
            total[book] = len(hits)
            if not hits:
                continue
            lines = [f"\n**Book {book} — {len(hits)} occurrence(s)**\n"]
            cur = None
            for ch, p, seg in hits:
                if ch != cur:
                    lines.append(f"- *{ch}*")
                    cur = ch
                lines.append(f"    - ¶{p}: “{seg}”")
            sections.append("\n".join(lines))
        out.append(f"\n---\n\n## {tic['name']}  "
                   f"(B1: {total.get(1, 0)} · B2: {total.get(2, 0)})\n")
        out.append(f"*Why it matters:* {tic['why']}\n")
        out.append(f"*Suggested target:* {tic['target']}\n")
        out.extend(sections)
    Path(ROOT / "STYLE-PASS.md").write_text("\n".join(out))
    return sum(len(re.compile(t["rx"]).findall("\n".join(docs[b][0])))
               for t in TICS for b in (1, 2))


DECISIONS = """\
## Decisions needed (no single line to point at)

These aren't typos — they're author calls. Each lists where the thread lives.

1. **The “…go…” syllable** (B1 Ch. 1) — Muse's one fragment from “Naika” is never
   revisited in either book. Decide: was it Naika's last word, or Xeroc's first?
   One line in B2 Ch. 24 (the Xeroc scene) pays it either way. Leaving it
   unpaid is the series' oldest broken promise to the reader.
2. **The canonical timeline** — write one dateline (dome-fall → waking → Velldale
   → Crimson Port → Valdara → bridge → Solarspire → Ostervik → finale), then
   conform every “X days/weeks/months” reference (see the two-months sweep,
   the three-days entries, B1 ¶ 1220, B2 ¶ 3539 and ¶ 4109/4111).
3. **The route briefing vs. Valdara** (B1 Ch. 4 vs. Ch. 8) — the Harbormaster
   briefs Wolkenfeld → Bloomridge → Solarspire and never mentions Valdara, a
   120k-person city days up the same road, which the party then walks into.
   Either add Valdara to his intelligence or have the party leave the briefed
   route on-page.
4. **Plan vs. parley** (B1 Ch. 9–11) — the operation is planned as a killing,
   then opens as a negotiation, and nobody reacts to the change. One line from
   Cain or Muse (“We offer him the way out first.”) reconciles it.
5. **Gormund's whiskey** — present through B1's first half, absent its entire
   back half, then B2 Ch. 36 is a full relapse arc. If the back half of B1 is
   meant as sobriety, make it visible (a refused flask); absence reads as a
   dropped prop, not a choice.
6. **The Gragorgan classified documents** (B1 Ch. 19; B2 ship arc) — the
   summit makes the lost transport's documents a stated international stake;
   the party owns the ship for five chapters and the hold's papers are never
   mentioned. Either pay it in B3 deliberately or have Fafnir collect them
   on-page so the thread is visibly parked.
7. **The river-sail plan** (B2 Ch. 11) — Gormund plans to sail the loop to
   Drachenburg/Solarspire; the party marches instead with no on-page reason.
   One line (ice too thick, draft too deep) closes it.
8. **Wendigo backtrail** (B1 Ch. 28) — “It's been following since Velldale”
   means it tracked them across the temperature wall the book treats as a
   hard threshold. If that's the point (it's from the deep cold), one line
   from Uthesia saying so converts a hole into lore.
9. **Carina's surname** — “Carina Yeon, daughter of Yoo Yeon” treats Yeon as
   the family name, but her mother is addressed as “Senior Sister Yoo”
   (surname Yoo). Pick the convention and conform.
10. **ki vs. qi** — Book 1 uses “qi” (with one “ki” slip); Book 2 uses “ki”
    throughout. Choose one romanization for the series.
"""

HEADER = """\
# Permafrost — Manual Fix Worklist (TO-FIX)

Companion to `tools/fix_dialogue_tags.py`, which auto-repairs the mechanical
layer (dialogue-tag punctuation, optional hoard→horde and two-dot ellipses).
**Run the script first** — everything in this document is what the script
can't safely decide for you.

**How to find each item:** locations are given as *Chapter · ¶N*, where ¶N
is the paragraph number counted from the chapter heading (the heading itself
is ¶0; scene-break `* * *` lines count as paragraphs). The fastest method is
simply **Ctrl+F the quoted text** in Word — every quote below is verbatim
from the manuscript.

Also work through the script's `*.review.txt` files (in `fixed/`): those are
near-miss dialogue tags the script deliberately left alone (“She said it
without bitterness” is a sentence, not a tag — but a few in there are real
tags with unusual continuations, e.g. “She said more quietly”).

Severity: **HIGH** = readers/agents will notice; **MED** = continuity or
logic that careful readers catch; **MINOR** = copyedit-level.

**Prose tics are in the companion file `STYLE-PASS.md`** — the repeated
constructions (“Not X. Not Y.”, “the kind of”, the “of a man who…” formula,
single-word cascades, duplicated similes) with every occurrence located.
This file stays focused on errors; that one is the curation pass.
"""


def main():
    docs = {b: load(b) for b in BOOKS}
    out = [HEADER]
    not_verified = 0

    for book in (1, 2):
        paras, chapters, pins = docs[book]
        out.append(f"\n---\n\n# Book {book}\n")
        for sev in ("HIGH", "MED", "MINOR"):
            items = [i for i in ISSUES if i["book"] == book and i["sev"] == sev]
            if not items:
                continue
            label = {"HIGH": "High priority", "MED": "Medium",
                     "MINOR": "Minor / copyedit"}[sev]
            out.append(f"\n## {label}\n")
            for it in items:
                line = it["line"] - 1  # 0-based
                # verify anchor; tolerate small drift
                idx = None
                for cand in [line] + [line + d for d in
                                      (-1, 1, -2, 2, -3, 3, -4, 4, -5, 5)]:
                    if 0 <= cand < len(paras) and it["anchor"] in paras[cand]:
                        idx = cand
                        break
                if idx is None:
                    hits = [j for j, t in enumerate(paras) if it["anchor"] in t]
                    idx = hits[0] if len(hits) == 1 else None
                if idx is None:
                    loc, quote = "[LOCATION NOT VERIFIED]", it["anchor"]
                    not_verified += 1
                else:
                    loc = f"{chapters[idx]} · ¶{pins[idx]}"
                    t = paras[idx]
                    p = t.find(it["anchor"])
                    a, bnd = max(0, p - 60), min(len(t), p + len(it["anchor"]) + 60)
                    quote = ("…" if a > 0 else "") + t[a:bnd] + \
                            ("…" if bnd < len(t) else "")
                out.append(f"### {loc} — {it['cat']}\n")
                out.append(f"> {quote}\n")
                out.append(f"- **Problem:** {it['problem']}")
                out.append(f"- **Fix:** {it['fix']}\n")

        # sweeps for this book
        out.append("\n## Sweeps (every occurrence)\n")
        for sw in [s for s in SWEEPS if s["book"] == book]:
            rx = re.compile(sw["rx"])
            hits = []
            for j, t in enumerate(paras):
                if CHAPTER_RX.match(t.strip()):
                    continue
                for m in rx.finditer(t):
                    a, bnd = max(0, m.start() - 35), min(len(t), m.end() + 35)
                    hits.append((chapters[j], pins[j],
                                 t[a:bnd].replace("\n", " ")))
            out.append(f"### {sw['label']} — {len(hits)} occurrence(s)")
            out.append(f"*{sw['note']}*\n")
            if len(hits) > 40:
                out.append(f"(showing first 40 of {len(hits)})\n")
            for ch, p, seg in hits[:40]:
                out.append(f"- {ch} · ¶{p}: “…{seg}…”")
            out.append("")

    out.append("\n---\n\n" + DECISIONS)
    Path(ROOT / "TO-FIX.md").write_text("\n".join(out))
    print(f"Wrote TO-FIX.md  ({len(ISSUES)} located issues; "
          f"{not_verified} could not be verified)")

    n_tics = emit_style_pass(docs)
    print(f"Wrote STYLE-PASS.md  ({n_tics} located tic occurrences across "
          f"{len(TICS)} constructions)")


if __name__ == "__main__":
    main()
