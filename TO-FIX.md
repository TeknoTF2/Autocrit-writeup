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


---

# Book 1


## High priority

### Chapter One · ¶55 — Continuity

> … of habit. ‘Eighteen days of food. Crimson Port is at least five days south on foot in good weather. This isn’t good weather. Double it…

- **Problem:** Direction error: Muse computes Crimson Port as south; the city is east (Aldrich says “East” in the same scene; the gate guard later confirms Velldale is southwest of the Port).
- **Fix:** Change “south” to “east”.

### Chapter Four · ¶78 — Continuity

> …he trade route. Scouting parties west toward Wolkenfeld and Bloodridge to assess conditions. And…” He paused, and the quality of t…

- **Problem:** Town name spelled “Bloodridge” here but “Bloomridge” five paragraphs later in the same speech. Book 2 settled on Bloomridge.
- **Fix:** Change to “Bloomridge” (this paragraph and the second occurrence below).

### Chapter Four · ¶85 — Continuity

> “To Wolkenfeld, maybe three weeks on foot. Bloodridge, another week past that. Solarspire…” Paper shuffled. “Ten …

- **Problem:** Second “Bloodridge” in the same Harbormaster speech; the same sentence then gives distances “from Bloomridge”.
- **Fix:** Change to “Bloomridge”.

### Chapter Four · ¶52 — Continuity

> After three days on the open road where the loudest thing was wind and foots…

- **Problem:** Travel-day math: the walk to Crimson Port is depicted as two days/two nights (depart dawn, one camp, arrive dusk) but is called three days here.
- **Fix:** Either add a skipped day on the road in Ch. 2–3 or change the three references to “two days” (see the two entries below).

### Chapter Four · ¶72 — Continuity

> …arked that as unreachable two weeks ago. You walked here in three days?”

- **Problem:** Harbormaster: “You walked here in three days?” — same discrepancy.
- **Fix:** Conform with the decision above.

### Chapter Seven · ¶11 — Continuity

> … but as a unit. A fighting force. They’d been lucky so far. Three days on the road to Crimson Port and nothing had tried to kill t…

- **Problem:** “Three days on the road to Crimson Port” — same discrepancy.
- **Fix:** Conform with the decision above.

### Chapter Five · ¶4 — POV

> …p, still asleep. Carina, a shapeless tangle of blankets and silver hair on the cot, so still she might have been dead if not for th…

- **Problem:** Blind-POV violation: Muse perceives Carina's “silver hair” and a silent “twitch” — the only hard sight-break in her chapters.
- **Fix:** Re-render through sound/touch: breathing rhythm, the rustle of blankets, the heat of the cot.


## Medium

### Chapter Three · ¶17 — Continuity

> “Yes.” Five voices said at once, and even Uthesia’s mouth twitched.

- **Problem:** “Five voices said at once” — Carina is the one being answered; only four other party members exist.
- **Fix:** “Four voices”.

### Chapter Nine · ¶27 — Continuity

> …tal limits. The seal had held Cain and Muse underground for thousands of years, but Barbatos hadn’t needed a seal. Barbatos could have sim…

- **Problem:** “Thousands of years” contradicts “a thousand years” / “a millennium” used everywhere else for the seal.
- **Fix:** “a thousand years”.

### Chapter Eleven · ¶8 — Timeline

> “You have fifty thousand people in this city.” Muse said. “Two months ago it was a hundred and twenty thousand. You know where the ot…

- **Problem:** “Two months ago it was a hundred and twenty thousand” — the dome fell roughly five weeks before this scene (see the “two months” sweep below).
- **Fix:** “A month ago” / “Five weeks ago”, or explicitly date the plague pre-dome.

### Chapter Twelve · ¶2 — Continuity

> …ugh pain was something his body did without consulting him. Twenty years of war had wired that in deep. You got hit. You stood up. You kept…

- **Problem:** “Twenty years of war had wired that in deep” sits oddly against Cain's much longer pre-seal career stated elsewhere.
- **Fix:** “Decades of war”, or align with his stated service span.

### Chapter Twelve · ¶74 — World

> … “And growing up, my favorite story was always that of King Midas. A man who could turn anything he touched to gold. Wonderfu…

- **Problem:** Real-world bleed: “Even Midas never had one of these” cites an Earth myth inside a secondary world.
- **Fix:** Replace with an in-world figure (a legendary ancestor of the Lord of Gold would do the same work).

### Chapter Eight · ¶46 — Logic

> …in knew the title before anyone said it because there was a crest on the wall behind the chair, the old heraldry, the bloodli…

- **Problem:** “Cain knew the title before anyone said it because there was a crest on the wall” — a crest explains the title, not the personal name “Andromalius”, which no one has spoken yet.
- **Fix:** Put the name on the banner/crest, or delay the name until it's spoken.

### Chapter Six · ¶4 — Logic

> …n the group’s pace, the slight drag that came from carrying three weeks on your back instead of three days. Gormund’s stride was sh…

- **Problem:** Rations issued (three weeks for five) don't cover the briefed one-way itinerary (~4.5 weeks to Solarspire); nobody remarks on the gap.
- **Fix:** One line acknowledging planned resupply at Wolkenfeld — or let Gormund grumble the math.

### Chapter Nine · ¶7 — Draft fossil

> “We don’t—” She stopped walking. “Seventy thousand people are dead, Cain. Not because of th…

- **Problem:** “She stopped walking” inside a room scene — Ch. 9 re-opens earlier in the evening Ch. 8 already closed, and this beat is left over from a street-scene draft.
- **Fix:** Re-anchor Ch. 9's opening after Ch. 8's close; cut or convert the movement beat.

### Chapter Nine · ¶106 — Dropped thread

> …essed.“There’s a problem,” Uthesia continued. “The keep has wards around his bedroom. Old ones, probably placed by a previous…

- **Problem:** The bedroom wards are the stated reason Carina must infiltrate solo — and they are never triggered, disabled, or mentioned again.
- **Fix:** One line in Ch. 10/11 of Carina bypassing them, or cut the ward rationale. (This paragraph also has a missing break between two speakers — see the merged-paragraph sweep.)

### Chapter Ten · ¶95 — Logic

> The third floor had a second bell.

- **Problem:** A third-floor alarm bell ambushes the party after Uthesia's recon was declared complete (“everything mapped and timed”).
- **Fix:** Have the recon note an unverified upper floor, or let Uthesia own the miss in interiority.

### Chapter Six · ¶122 — Dropped thread

> Tomorrow. He’d tell Cain tomorrow.

- **Problem:** Gormund resolves to tell Cain about the stalking sound “tomorrow”; the report never happens on-page (and Cain independently conceals his own sighting in Ch. 3).
- **Fix:** A two-line exchange on the next morning's march closes the loop and lets both men learn the other heard it too.

### Chapter Eleven · ¶82 — Prose

> …e the plank of wood Carina imagined in her head, the maid's skull exploded upon impact, through the shield and directly into …

- **Problem:** The maid's death sentence is garbled: the sequencing of punch → shield → maid → Andromalius is unclear, and “the blow not meant to kill him” reads ambiguously against the woman just killed.
- **Fix:** Rewrite in strict sequence: the punch goes through the shield, the maid dies, the remaining force carries into Andromalius.

### Chapter Twenty-Three · ¶98 — Derivation

> …ake? My lack of imagination. 50 degrees below zero meant 80 degrees of frost. Such information told me it was cold and uncomfortable, bu…

- **Problem:** The interstitial epigraph is an unattributed close paraphrase of Jack London's ‘To Build a Fire’; its math also assumes water freezes at 30° (−50° → “80 degrees of frost”; it's 82).
- **Fix:** Attribute it, rework it into original phrasing, or frame it as an in-world text — and fix the arithmetic if the Fahrenheit logic stays.


## Minor / copyedit

### Chapter Two · ¶60 — Diction

> …m the stream. Muse silently thanked the girl for having the grace period of a kicked hornet’s nest. The interruption was welcome.

- **Problem:** Malapropism: “the grace period of a kicked hornet's nest”.
- **Fix:** Probably “the grace of a kicked hornet's nest”.

### Chapter Four · ¶18 — Typo

> Five more minutes past. The goat moved. The line shuffled. Carina’s right foot was…

- **Problem:** “Five more minutes past.” — wrong word.
- **Fix:** “passed”.

### Chapter Five · ¶110 — Artifact

> …t after the last few weeks I’m grading on a generous curve.”-+

- **Problem:** Stray characters after the closing quote: ‘…a generous curve.”-+’
- **Fix:** Delete “-+”.

### Chapter Nine · ¶104 — Formatting

> …d. “Planning implies I’d decided. I hadn’t. Not until now.”“How?” Gormund asked. “You can’t exactly have been walking throu…

- **Problem:** Two speakers merged into one paragraph: ‘…Not until now.”“How?” Gormund asked.’
- **Fix:** Insert a paragraph break before ““How?”” (see merged-paragraph sweep for all instances).

### Chapter Eleven · ¶72 — Prose

> Stone fragments hit her back like scattershot. One embedded into her shoulder and the pain was bright and immediate. Sh…

- **Problem:** Awkward: “One embedded into her shoulder”.
- **Fix:** “One buried itself in her shoulder” (or similar).

### Chapter Thirteen · ¶19 — Consistency

> She caught it. Hands open, feet planted, the ki catching the force the way a river catches a stone, splittin…

- **Problem:** “ki” used here; “qi” everywhere else in Book 1 (Book 2 then uses “ki” throughout).
- **Fix:** Pick one romanization for the series and conform both books.

### Chapter Thirteen · ¶45 — Typo

> Heat. More heat than his fathers shop, more than the burning pyres, more than anything. The hide …

- **Problem:** Missing apostrophe: “his fathers shop”.
- **Fix:** “his father's shop”.

### Chapter Fifteen · ¶56 — Prose

> So they all still settled into a fighting stance.

- **Problem:** “So they all still settled into a fighting stance.” — “still” is doing unclear work.
- **Fix:** Cut “still” or rephrase (“So they settled into fighting stances anyway.”).

### Chapter Seventeen · ¶34 — Typo

> “Then how's it look, doc? In your experienced opinion”

- **Problem:** Missing terminal punctuation: “In your experienced opinion”
- **Fix:** Add the period/question mark.

### Chapter Seventeen · ¶35 — Tense

> She gave a slight smile at that. Even in this state he keeps trying to make her feel better.

- **Problem:** Present tense in past narration: “Even in this state he keeps trying to make her feel better.”
- **Fix:** “kept trying”.

### Chapter Twenty · ¶40 — Diction

> …information from inside. For all you know you’d be dropping ordinance directly on a refugee camp.”

- **Problem:** “ordinance” (a law) for “ordnance” (munitions).
- **Fix:** “ordnance”.

### Chapter Twenty-Two · ¶7 — Tense

> …g and he’d meant it. Every barrel got a number. Every crate has a destination. He worked with charcoal on the walls, scratching tallies a…

- **Problem:** Present tense in past narration: “Every crate has a destination.”
- **Fix:** “had”.

### Chapter Twenty-Four · ¶49 — Typo

> …his hand against it and the pressure helped but his fingers thick and clumsy inside gloves that had been adequate an hour ago and were n…

- **Problem:** Dropped verb: “his fingers thick and clumsy inside gloves”.
- **Fix:** “his fingers were thick and clumsy…”

### Chapter Twenty-Four · ¶50 — Typo

> He shoved his under his armpits and kept walking.

- **Problem:** Missing word: “He shoved his under his armpits.”
- **Fix:** “He shoved his hands under his armpits.”

### Chapter Twenty-Five · ¶3 — Typo

> Cain was already awake.The satyr sat against the wall near the door, halberd across hi…

- **Problem:** Missing space: “Cain was already awake.The satyr…”
- **Fix:** Add the space.

### Chapter Twenty-Six · ¶109 — Typo

> … hole she’d made in the mountain, and the expression on her mothers face was not anger.

- **Problem:** Missing apostrophe: “the expression on her mothers face”.
- **Fix:** “her mother's face”.

### Chapter Thirty · ¶28 — Tense

> …ayers. Each one enchanted, treated, or reinforced. Each one is necessary.

- **Problem:** Present tense in past narration: “Each one is necessary.”
- **Fix:** “was”.


## Sweeps (every occurrence)

### “two months” timeline references — 5 occurrence(s)
*The dome fell ~3 weeks before Ch. 1 and ~6–7 weeks before Book 1's end (fixed by the outside-world chapters). Every “two months” below overstates it — decide the canonical timeline, then conform each.*

- Chapter Seventeen · ¶18: “… grim, sardonic rumble she’d spent two months memorizing. She turned toward it, …”
- Chapter Seventeen · ¶65: “…aised her voice, had never once in two months raised her voice, and the sound of…”
- Chapter Eighteen · ¶46: “…ady heartbeat she’d maintained for two months, for a hundred miles, through froz…”
- Chapter Twenty-Five · ¶52: “…n’t any animal she’d catalogued in two months of traveling through this country.…”
- Chapter Twenty-Eight · ¶66: “…t four sentences about yourself in two months.”…”

### merged speech (missing break or space) — 2 occurrence(s)
*A quote opening glued directly onto preceding text — either two speakers sharing a paragraph or a missing space/break before dialogue. Insert a paragraph break (or space) at each.*

- Chapter Nine · ¶104: “…d decided. I hadn’t. Not until now.”“How?” Gormund asked. “You can’t exa…”
- Chapter Nine · ¶106: “… was larger than anyone had guessed.“There’s a problem,” Uthesia continu…”

### double spaces — 4 occurrence(s)
*Collapse to single spaces.*

- Chapter One · ¶2: “…ap that clung to her gloves, making  her grip uncertain. She positioned …”
- Chapter Ten · ¶67: “…She sent the spirit  ahead. Clear to the servants’ passa…”
- Chapter Ten · ¶86: “…ng but twenty feet was twenty feet.  His hand was already on the chain a…”
- Chapter Eleven · ¶11: “…our concern.” Andromalius said, and  he spoke with the rehearsed authori…”


---

# Book 2


## High priority

### Chapter Four · ¶47 — Continuity

> … locked, the tendons standing out against his forearms. His eyes were bloodshot, the capillaries bursting from strain, his vision turning r…

- **Problem:** Cain is one-eyed (“the only one he had left”, this same chapter): “His eyes were bloodshot”.
- **Fix:** “His eye was bloodshot” — also at the next entry and Ch. 13.

### Chapter Four · ¶47 — Continuity

> … locked, the tendons standing out against his forearms. His eyes were bloodshot, the capillaries bursting from strain, his v…

- **Problem:** Second “eyes” plural for Cain in the same sequence.
- **Fix:** Singular.

### Chapter Thirteen · ¶8 — Continuity

> His eyes opened.

- **Problem:** Cain's wake-up: “His eyes opened.”
- **Fix:** “His eye opened.”


## Medium

### Chapter Fifteen · ¶25 — Continuity

> …. You hold the lowest position any Dantalion has ever held. Our grandmother was fifty-third. Our great-grandfather was forty-first. If …

- **Problem:** Genealogy slip: Elizabeth tells her father “Our grandmother was fifty-third. Our great-grandfather was forty-first.” His grandmother is her GREAT-grandmother.
- **Fix:** “Your grandmother… your great-grandfather” (or “Grandmother was…” from her own reference point, shifted one generation).

### Chapter Twelve · ¶21 — Magic rules

> …gh his coat. “Fortunately, the target is a peasant. Roughly thirty percent of a resurrection scroll is more than sufficient for a corp…

- **Problem:** Suppression math: the resurrection scroll (top-tier magic) runs at “roughly thirty percent”, but the stated rule is that higher-tier spells retain “upward of fifty percent efficiency”.
- **Fix:** Adjust one number, or have Dantalion note that scrolls degrade differently from live casting.

### Chapter Seventeen · ¶68 — Magic rules

> “Well, as long as I finish up within ten minutes or so, Dantalion could probably still resurrect them.” The …

- **Problem:** Ghislaine cites a ~10-minute revival window, but Carina is revived after a cross-city carry, well outside it.
- **Fix:** Loosen the window (“within the hour”), or show the carry beating the clock.

### Chapter Six · ¶101 — Continuity

> …y’s crew walked in loose formation around the convoy, maybe forty people in total, a ragged collection of outlaws in mismatch…

- **Problem:** Crew arithmetic: ~40 here, “thirty-odd” at Ch. 11, “thirty people and three working firearms” at Ch. 15 vs Ch. 14's “two or three with basic revolvers” — no on-page attrition.
- **Fix:** Pick one headcount/armament and conform, or add one line of attrition.

### Chapter Six · ¶107 — Logic

> … mess around, we lost a good ten men to those walking metal war machines. Would take a siege crew to get inside, and we ain’t got on…

- **Problem:** Jane says the crew lost ten men to the ship's “walking metal war machines” weeks earlier — yet security is dormant for hours when the party boards.
- **Fix:** One line distinguishing external golems (active) from internal Angels (dormant until the keycard areas are breached) closes it.

### Chapter Eight · ¶66 — Logic

> “I believe in you.” He said. “It won’t fire into the medical bay, the security system excludes this room. So just...” He ste…

- **Problem:** Gormund asserts the Angel “won't fire into the medical bay” with no stated basis.
- **Fix:** Give him one: Gragorgan signage, the ship's manifest, design doctrine he knows from home.

### Chapter Twenty-One · ¶92 — Continuity

> “And she said she’s not ready. She asked me not to tell you where she went.”

- **Problem:** Fafnir tells Yoo that Carina “doesn't want to see you” (four paragraphs up) and “asked me not to tell you where she went” — Carina never asked either on-page; in Ch. 20 she only asked him to relay a message (“Tell her I'm ok. And that I'll find her when I'm ready.”).
- **Fix:** Either have Carina say it in Ch. 20, or soften Fafnir's wording to his own inference (“I don't think she's ready to see you”).

### Chapter Twenty-Two · ¶23 — Logic

> Hundreds of them. A mass of bodies that had been accumulating for weeks, the…

- **Problem:** Dungeon-intel strain: the Sunken Grave spillage is “hundreds” and mindless, yet the same dungeon produced a ~4,000-strong organized army days from the capital, unnoticed despite Guild scrying and three weeks of siege.
- **Fix:** One line — miasma blocks scrying, or Dantalion masked the muster — seals it.

### Chapter Twenty-Three · ¶53 — Continuity

> …e Cain as they were guided through the inner gatehouse. “Is the King sending his army?”

- **Problem:** Ostervik soldiers ask about “the King sending his army”, though the King is later said to have died early in the dome. Plausible they wouldn't know — but flag for intent.
- **Fix:** Optional one-liner about how slowly news travels under the dome.

### Chapter Twenty-Three · ¶101 — Continuity

> …ch puts civilian pressure back on the Guild. We already got Barbatos out of the city, I need preferably one more walking disaster to…

- **Problem:** Dantalion claims “We already got Barbatos out of the city” — Ch. 21 shows Barbatos leaving on his own initiative. Boast or error?
- **Fix:** If boast, let Elizabeth needle it; if real, plant one line in Ch. 21.

### Chapter Thirty-One · ¶14 — Timeline

> “It’s been weeks, Muse. Maybe a few months. We’ve been awake for what, the length of a single season? …

- **Problem:** Cain: “It's been weeks, Muse. Maybe a few months” — the series needs one canonical statement of dome-age vs. the party's waking.
- **Fix:** Conform after writing the canonical timeline (see Decisions).

### Chapter Thirty-Six · ¶51 — Timeline

> …know where Muse was. She’d checked out of her barracks room days ago, no forwarding location. He checked the other medical tents…

- **Problem:** First receptionist: Muse left “days ago”; two paragraphs later: “about two weeks ago”; Gormund's counted spiral runs ~11 days.
- **Fix:** Make both witnesses agree (~two weeks), or have the second correct the first.

### Chapter Thirty-Six · ¶61 — Continuity

> He pulled the weapon from the pack. Checked the ammo box. Nine rounds.

- **Problem:** Ammo ledger: 20 rounds → 1 spent (Sunken Grave) → wall-run count starts at “Seventeen” (one phantom round) → Elder shot → “Nine rounds” here.
- **Fix:** Add one unnumbered shot to the Kissing Peaks fight, or start the wall count at “Eighteen”.


## Minor / copyedit

### Chapter Two · ¶30 — Prose

> … hole through an impenetrable barrier. The girl couldn’t be older than Carina, couldn’t be older than twenty, and yet something ab…

- **Problem:** Redundant double comparison: “couldn't be older than Carina, couldn't be older than twenty” (Carina is nineteen).
- **Fix:** Keep one comparison.

### Chapter Six · ¶66 — Typo

> …eople on the rope, pulling the weight of a seven-foot satyr in full as gravity worked against them.

- **Problem:** Missing word: “pulling the weight of a seven-foot satyr in full as gravity worked against them”.
- **Fix:** “in full armor”.

### Chapter Twelve · ¶101 — Typo

> …e composure of the Lightning shattering under the weight of a accusation that struck at the core of everything she’d built her life …

- **Problem:** “under the weight of a accusation”.
- **Fix:** “an accusation”.

### Chapter Fifteen · ¶89 — Tense

> … gauge drop to the limit of the instrument itself. And he's sure it continued to drop past that.

- **Problem:** Tense slip: “And he's sure it continued to drop past that.”
- **Fix:** “he was sure”.

### Chapter Fifteen · ¶142 — Continuity

> It wasn’t sudden. The heaviness had been building since Drachenburg, his right leg went stiff, then his left, the cold seizing …

- **Problem:** “The heaviness had been building since Drachenburg” — they never reached Drachenburg; it's buried.
- **Fix:** “since the riverbank” or “since Drachenburg's grave”.

### Chapter Seventeen · ¶80 — Typo

> Fear. Pure, unprocessed, a  animal response that lived beneath everything else. Her body had c…

- **Problem:** Article error plus double space: “a  animal response”.
- **Fix:** “an animal response”.

### Chapter Twenty-Four · ¶22 — Typo

> The plan was clean. Everyone nodded. Accptance that this was the best option among several bad ones.

- **Problem:** “Accptance”.
- **Fix:** “Acceptance”.

### Chapter Twenty-Four · ¶38 — Clarity

> Uthesia’s ring. And hers.

- **Problem:** “Uthesia's ring. And hers.” — the antecedent (her late wife) is unclear; reads as a grammar error on first pass.
- **Fix:** “Uthesia's ring. And her wife's.”

### Chapter Twenty-Four · ¶52 — Typo

> She folded her hands in her land. Her voice was tense and awkward.

- **Problem:** “She folded her hands in her land.”
- **Fix:** “in her lap”.

### Chapter Twenty-Four · ¶70 — Typo

> “Hmm.” The voice considered the question was care. “That’s not the word I would use. But the mortal dictionar…

- **Problem:** “The voice considered the question was care.”
- **Fix:** “with care”.

### Chapter Twenty-Five · ¶30 — Typo

> … Thunder from somewhere on the northern wall. The King Head wobbled before falling to the ground

- **Problem:** Missing period at the end: “The King Head wobbled before falling to the ground”
- **Fix:** Add the period.

### Chapter Twenty-Seven · ¶9 — Staging

> He stopped brushing. His hand went to the top of her head and ruffled, the care…

- **Problem:** Stage-direction muddle: Dantalion “stopped brushing” after he'd already stopped and was ruffling her hair in the previous paragraph.
- **Fix:** Reorder the beats (ruffle → resume brush → stop).

### Chapter Twenty-Eight · ¶87 — Prose

> …ght solidifying into surfaces that were translucent. Arches formed above the walls as it formed a cathedral. Ethereal, golden,…

- **Problem:** Repetition with unclear antecedent: “Arches formed above the walls as it formed a cathedral.”
- **Fix:** “…as the light took the shape of a cathedral.”

### Chapter Twenty-Nine · ¶22 — Logic

> …air. “What are you— I didn’t ask for— send Ghislaine, she’s right here in the—”

- **Problem:** Carina asserts Ghislaine is “right here in the—” without any way to know her whereabouts.
- **Fix:** Soften to a question (“Isn't Ghislaine still in the city?”) or cut.

### Chapter Thirty-Eight · ¶63 — Prose

> …he Death Knight would be hit if he shot through the shield. Firing a shot, the shield was immediately punched through, the round hit …

- **Problem:** Dangling participle / subject confusion: “Firing a shot, the shield was immediately punched through, the round hit the arm at the elbow.”
- **Fix:** “He fired. The shot punched through the shield and hit the arm at the elbow.”

### Chapter Forty · ¶55 — Consistency

> “We’re both Murimites, Mom.” She said. “You’re right. We’re bad at this.”

- **Problem:** “Murimites” appears once as a demonym — nowhere else in the series.
- **Fix:** Confirm it's intended, or standardize (“Murim-born”, “people of Murim”).


## Sweeps (every occurrence)

### “two months” timeline references — 6 occurrence(s)
*Check each against the canonical timeline (some, like the Mage College's sealing, may be intentional).*

- Chapter Two · ¶71: “…ion.’ They’ve been ‘assessing’ for two months.”…”
- Chapter Fourteen · ¶28: “…her with spit and stubbornness for two months, looked at the Sword God and the M…”
- Chapter Sixteen · ¶26: “…more tired, the weight of the last two months visible in the lines around his ey…”
- Chapter Twenty-Four · ¶1: “…ey’d been sleeping on for the last two months.…”
- Chapter Thirty-Three · ¶111: “…of the faculty have returned after two months, something happened to them. Which…”
- Chapter Thirty-Seven · ¶81: “…limmerhold Mage College. They left two months ago to investigate the dome and ne…”

### merged speech (missing break or space) — 0 occurrence(s)
*Same fix: paragraph break (or space) before the opening quote.*


### double spaces — 6 occurrence(s)
*Collapse to single spaces.*

- Chapter Thirteen · ¶101: “…                     * * *…”
- Chapter Fifteen · ¶87: “…                    * * *…”
- Chapter Seventeen · ¶80: “…Fear. Pure, unprocessed, a  animal response that lived beneath …”
- Chapter Eighteen · ¶17: “…                      * * *…”
- Chapter Twenty-Five · ¶70: “…                    * * *…”
- Chapter Thirty-Four · ¶38: “…e four pieces of a plan that would,  if executed correctly, bury her fat…”

### straight quotes amid curly typography — 55 occurrence(s)
*Straight apostrophes inside words are auto-fixed by the script's --quotes flag; any straight DOUBLE quotes listed below need manual open/close orientation.*

(showing first 40 of 55)

- Chapter Six · ¶89: “…thesia said, flexing her foot. “Didn't expect to not be able to break gla…”
- Chapter Seven · ¶21: “…ithout killing the Royal Guard. They're just doing what the Crown ordered…”
- Chapter Eight · ¶24: “…moving. Just follow the wall and you'll make your way back to the medical…”
- Chapter Nine · ¶8: “…d for your family relationship, that's all.”…”
- Chapter Eleven · ¶119: “…cademy’s got more prestige, but that's halfway across the world.”…”
- Chapter Fifteen · ¶89: “…mit of the instrument itself. And he's sure it continued to drop past tha…”
- Chapter Sixteen · ¶61: “…esia is a gold rank and assuming she's willing to vouch for you, all thre…”
- Chapter Seventeen · ¶89: “… The touch was warm. “Don’t worry, I'll have Fafnir revive you. Let this …”
- Chapter Eighteen · ¶20: “…. ‘That’s a military transport. They're built to be pretty fast.’…”
- Chapter Eighteen · ¶77: “…She doesn’t have an answer. She wasn't taught something like that.…”
- Chapter Eighteen · ¶121: “…answer for his accusations. She wasn't taught something like that.…”
- Chapter Nineteen · ¶12: “…ng her. You had every advantage. She's a child with one hand and you are …”
- Chapter Nineteen · ¶67: “… the infection took her. These weren't the same, of course. Billy had use…”
- Chapter Nineteen · ¶94: “…ed the lead wagon in the convoy. She'd been offered a horse several times…”
- Chapter Twenty-One · ¶4: “…hey find their way home. Please, don't think so highly of me.”…”
- Chapter Twenty-Three · ¶9: “…“Yes, Carina, I noticed. You're up one to zero against gravity, g…”
- Chapter Twenty-Three · ¶10: “…“I thought you'd be more impressed!”…”
- Chapter Twenty-Three · ¶11: “…h, ok, fine. I was very impressed. I'm just trying not to stroke your ego…”
- Chapter Twenty-Three · ¶99: “…the city, Fafnir responds. And if he's about to lose one of his few remai…”
- Chapter Twenty-Four · ¶34: “…ply, medicine. The holy trinity that'd get them through this.…”
- Chapter Twenty-Eight · ¶22: “…Except it wasn't empty anymore.…”
- Chapter Twenty-Eight · ¶69: “…y yards ahead, directly in the Elder's path, his hooves carving trenches …”
- Chapter Twenty-Eight · ¶70: “…oming fast. Cain dropped the halberd's guard and lunged, both hands reach…”
- Chapter Twenty-Eight · ¶70: “…both hands reaching for the creature's torso, going for the grapple, goin…”
- Chapter Twenty-Eight · ¶71: “… lethal charge building in the Elder's palm. Whatever that spell did on c…”
- Chapter Twenty-Eight · ¶71: “…ever that spell did on contact, Cain's instincts had screamed at him twic…”
- Chapter Twenty-Eight · ¶71: “…him twice now to avoid it. He couldn't grab the creature without getting …”
- Chapter Twenty-Eight · ¶72: “…He backstepped. The Elder's fist passed through the space his …”
- Chapter Twenty-Eight · ¶73: “…Cain's hand slid down the halberd's shaft…”
- Chapter Twenty-Eight · ¶73: “…Cain's hand slid down the halberd's shaft. Past the grip, past the bal…”
- Chapter Twenty-Eight · ¶73: “…e very tip of the handle, the weapon's full length extended in front of h…”
- Chapter Twenty-Eight · ¶74: “…The hook caught the Elder's shoulder. At full extension, at a …”
- Chapter Twenty-Eight · ¶74: “…ension, at a range the creature hadn't accounted for, the axe head biting…”
- Chapter Twenty-Eight · ¶75: “… Shadow Assassin rose from the Elder's shadow in the same instant, attack…”
- Chapter Twenty-Nine · ¶84: “…s and necromantic implements that he'd moved in place of the royal family…”
- Chapter Twenty-Nine · ¶84: “…d moved in place of the royal family's more traditional arcane artifacts.…”
- Chapter Thirty · ¶31: “…nd Muse’s face. Maybe the symbol isn't what I remember. Maybe Muse manife…”
- Chapter Thirty-One · ¶15: “…ived inside me is hollow. Empty. She's gone.”…”
- Chapter Thirty-Two · ¶9: “… they address. But don’t worry, they're genuinely the most peaceful peopl…”
- Chapter Thirty-Two · ¶56: “…I came through here before, I couldn't get in.” Carina said. “The barrier…”


---

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
