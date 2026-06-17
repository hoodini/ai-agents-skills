# The Script Doctor — Diagnosing & Fixing a Broken Story

You don't have a writing problem. You have a *diagnosis* problem. When a draft feels "off," "flat," or "boring," the instinct is to rewrite line-by-line — polish dialogue, sharpen prose, add a cool shot. That almost never fixes a story, because the disease is structural and the symptom is surface-level. The boring scene is rarely boring because of bad lines; it's boring because nothing is at stake, no value changes, and the protagonist wants nothing in it. A "script doctor" is a working profession in Hollywood precisely because *fixing* a story is a different skill from *writing* one: it is pattern-matching symptoms to root causes.

This chapter is that skill as a checklist. Each entry follows the same triage form — **Symptom** (what you notice when watching/reading), **Root cause** (the underlying structural failure), **Fix** (the concrete intervention). It builds directly on the theory in [01-story-structure.md](01-story-structure.md), [02-pixar-22-rules.md](02-pixar-22-rules.md), [03-character-and-scene-craft.md](03-character-and-scene-craft.md), and [04-engagement-psychology-hooks.md](04-engagement-psychology-hooks.md); here we run those principles *backwards* — from broken output to the violated principle. This is the source material for the interrogation Phase in [19-the-grilling-workflow.md](19-the-grilling-workflow.md).

A note on order: these failures are roughly ranked by leverage. Fixing #1 (whose story is this?) can dissolve five downstream symptoms at once. Always diagnose top-down — structure before scene before line.

---

## The Diagnostic Checklist

### 1. No clear protagonist / "Whose story is this?"

**Symptom.** Viewers can't say who the movie is "about." The piece cuts between three or four people with equal weight; in a test screening, different viewers name different characters as the lead. The emotional center keeps moving.

**Root cause.** No single character carries the spine of *desire* through the whole story. The audience locates *itself* by attaching to one consciousness — we feel the story through the person whose goal we're tracking. With no anchor, there's no one to root for and no yardstick for whether things are going well or badly.

**Fix.** Pick the character who *changes the most* and who *wants something hardest*, and demote everyone else to support. Ensure the protagonist is the one who drives the climax (makes the final decisive choice) rather than watching it happen. If you genuinely have two co-leads (a love story, a buddy film), they must share *one* unified goal or be in direct conflict over the *same* object — not run on parallel unrelated tracks.

> **→ SHORT-FORM.** In a 60-second piece there is room for exactly *one* point-of-view. The first 2 seconds must lock the camera (literal or figurative) onto one face/agent. Ensemble openings are death in short form — the viewer scrolls before they've found someone to be.

> **→ AI APPLICATION.** First interrogation question the assistant asks: *"In one sentence — whose story is this, and what do they want?"* If the user names more than one person or can't answer, the assistant flags **NO PROTAGONIST** and refuses to proceed to beats until resolved.

### 2. Passive protagonist / no active WANT

**Symptom.** Things *happen to* the hero. They react, get rescued, are carried by coincidence or by other characters' decisions. Watching them feels like watching a passenger. The story has events but no *pursuit*.

**Root cause.** No concrete, external, actively-pursued **want** (the conscious goal that generates plot) — see want vs. need in [01-story-structure.md](01-story-structure.md). A character with only an internal *need* and no external *want* cannot generate action, because need is realized through pursuit of a want.

**Fix.** Give the protagonist a *specific, external, hard-to-get* objective they chase by their own decisions: win the case, escape the island, get the girl back by Friday. Convert reactive beats into active ones — instead of "the hero is told to go to X," have the hero *decide* to go to X to get something. Test every scene: *what is the protagonist trying to make happen here?* If the answer is "nothing, they're absorbing information," the scene is inert.

> **→ SHORT-FORM.** A passive subject in a teaser reads as a stock-footage human, not a character. Even in a product ad, the on-screen person must *want* something visible in the first beat (to fix a frustration, to reach a result) — desire is what makes 5 seconds feel like a story rather than a slideshow.

> **→ AI APPLICATION.** The assistant runs an *active-verb audit* on the beat sheet: every beat should have the protagonist as the subject of a transitive action verb (chases, steals, confronts, lies to). Beats where the protagonist is the *object* ("is captured," "is told") get flagged as passivity risks.

### 3. No stakes / the "So what?" failure

**Symptom.** The plot advances but you feel nothing. A test reader asks, "Okay… so what? Why do I care if they fail?" Nothing bad seems to follow from losing.

**Root cause.** The cost of failure is undefined, trivial, or never made concrete. Stakes are the *answer to "what is lost if the want is not achieved?"* — and they must be both **real** and **felt** (we must understand them emotionally, not just be told them).

**Fix.** Define what the protagonist loses if they fail, and escalate it. The strongest stakes are personal and specific (this child, this home, this last shred of self-respect), not abstract ("the world ends"). Make the audience *see* the thing that can be lost before it's threatened — we can't fear for what we haven't been shown to value. McKee's frame: a scene only matters if a **value** at stake (life/death, love/hate, freedom/slavery, truth/lie) actually shifts.

> **→ SHORT-FORM.** Stakes in a teaser are compressed into a single concrete image of loss or gain: the empty chair, the deadline clock, the rival's smug face. You don't explain the stakes — you *show one object* that embodies them. Talky stakes-explanation is the #1 way a short turns into a bloated micro-film.

> **→ AI APPLICATION.** Diagnostic prompt: *"Complete this sentence: 'If the protagonist fails, then ______.'"* If the user's answer is vague ("it's bad") or cosmic-but-impersonal ("everyone dies"), the assistant pushes for a *specific, personal, on-screen* consequence.

### 4. Weak or absent opponent

**Symptom.** The hero gets what they want too easily; tension never tightens; the "villain" is offscreen, generic, or stupid. The story feels soft.

**Root cause.** No worthy **opponent** — and the most common error is misunderstanding what an opponent *is*. In John Truby's *The Anatomy of Story*, the true opponent is the character who *wants the same goal as the hero* and competes directly for it, attacking the hero's greatest weakness. A weak opponent means a weak hero, because we measure a protagonist by the force they overcome.

**Fix.** Strengthen the opposition until it is *stronger* than the hero at the start. Make the opponent want the *same thing* (so the conflict is structural, not incidental). Give the opponent a coherent, even sympathetic, justification — the best antagonists believe they're the hero of their own story. The opponent should attack precisely the hero's flaw/lie (see [03-character-and-scene-craft.md](03-character-and-scene-craft.md)).

> **→ SHORT-FORM.** The "opponent" in a short can be a force, a clock, or an internal resistance — but it must be present and pressing in nearly every beat. A 60s piece with no antagonistic pressure is just footage. The friction *is* the watch-time.

> **→ AI APPLICATION.** The assistant asks: *"Who or what wants to stop the protagonist — and are they stronger?"* It flags opponents that are absent, offscreen, or trivially weak, and proposes raising opponent strength or unifying the goal.

### 5. "And then" episodic structure — no causality

**Symptom.** The story is a list of events: "this happens, **and then** this happens, **and then** this." Scenes could be reordered without much damage. It feels like a travelogue or a highlight reel, not a story.

**Root cause.** Beats are connected by *chronology* (and time-then) instead of *causality* (and-so / but-so). This is the central lesson of the Pixar "but/therefore" principle in [04-engagement-psychology-hooks.md](04-engagement-psychology-hooks.md): each beat should *cause* the next.

**Fix.** Run the **but/therefore test** (detailed below): rewrite the spine so that between every two beats you can insert *"therefore"* or *"but"* — never *"and then."* If a scene can be cut or moved with no consequence, it isn't load-bearing; cut it or make its outcome cause the next scene. Causality is what converts a sequence into a *plot*.

> **→ SHORT-FORM.** A short literally cannot survive "and then" — there's no runway for filler. Three beats, two connectives, both must be "but" or "therefore." Hook → complication (but) → turn (therefore) → payoff.

> **→ AI APPLICATION.** The assistant inserts a connective between each pair of beats and reports the ratio of "and then" links. A high ratio = **EPISODIC** flag. It then proposes specific causal rewrites for the weakest joints.

### 6. The saggy / boring MIDDLE

**Symptom.** The opening grabs, the ending lands, but the middle drags. Viewers check the time / drop off. Beats feel repetitive — the hero faces the *same* obstacle at the *same* intensity over and over. Nothing is *worse* than it was twenty minutes ago.

**Root cause.** No **escalation** — the second act has no rising arc. The middle is where most stories die because it's the hardest stretch to keep *cause-and-effect tension* climbing. Often the protagonist is in a holding pattern (gathering info, waiting) rather than being progressively cornered.

**Fix.** Four reliable interventions, usually in combination:
1. **Raise the stakes** — each setback should cost more than the last (escalating value-charges, positive to negative and back, per McKee).
2. **Add a ticking clock** — impose a deadline that shrinks the available time/space (the bomb timer, the wedding date, the oxygen running out). Time pressure manufactures urgency cheaply and honestly.
3. **Midpoint reversal** — at the center, flip the situation: a false victory that becomes a trap, or a low point that reframes the whole goal. This is the Save the Cat "Midpoint" and "All Is Lost" logic from [01-story-structure.md](01-story-structure.md). The midpoint should change the *meaning* of the chase, not just its difficulty.
4. **Force a worse choice** — keep narrowing options until the hero must choose between two things they want, or two evils (a *true dilemma*, not a no-brainer). Choice under pressure is character, and character is what we watch.

> **→ SHORT-FORM.** A 60s "middle" is one beat: the **turn** — the single moment the situation flips (the reveal, the reversal, the escalation). If your short feels flat, you're missing the turn. Don't add more content; add one *change of direction*.

> **→ AI APPLICATION.** The assistant maps the value-charge of each midsection beat (+/−) and flags **FLAT MIDDLE** if charges don't escalate or alternate. It then suggests one of the four fixes by name, asking the user to choose.

### 7. Theme stated, not dramatized (on-the-nose)

**Symptom.** A character announces the moral: "You see, family is the only thing that matters." It feels like a TED talk. The audience is *told* what to think instead of *experiencing* it.

**Root cause.** The **theme** (the story's argument about how to live) is delivered as dialogue rather than *proven through events*. In Lajos Egri's *The Art of Dramatic Writing*, the **premise** ("great love defies even death," etc.) is something the *plot must demonstrate* through cause and effect — not something a character recites. Robert McKee's term for the same idea is the **controlling idea**: the theme is dramatized when the *ending value + the cause of it* are shown, not spoken.

**Fix.** Delete the speech. Re-stage the theme as a *choice*: put the protagonist in a situation where acting on the theme costs them, and let their choice (and its consequence) make the argument. If "honesty matters," show honesty costing the hero dearly and ultimately saving them — let the *plot* be the proof. Dramatize, don't declare.

> **→ SHORT-FORM.** Theme in a short is carried by a single contrasting image or a final reversal — never by VO that explains the meaning. The "moral" lands as a feeling, not a sentence.

> **→ AI APPLICATION.** The assistant scans dialogue/VO for lines that *state the lesson* and flags them as **ON-THE-NOSE THEME**, proposing a behavioral/visual substitution (a choice or image that implies the same idea).

### 8. Setups with no payoff / payoffs with no setup

**Symptom.** Either (a) a detail is emphasized and then never used (a "loaded gun" that never fires), leaving a nagging "why did they show me that?"; or (b) a solution/object appears at the climax that we never saw before, feeling arbitrary ("where did *that* come from?").

**Root cause.** Broken **setup/payoff** symmetry — a violation of Pixar Rule #14's plant-and-payoff discipline (see [02-pixar-22-rules.md](02-pixar-22-rules.md)). Audiences subconsciously track promises; an unpaid setup feels like a lie, an unprepared payoff feels like cheating.

**Fix.** Make a two-column ledger: **every setup → its payoff**, and **every payoff → its setup**. For each orphaned setup, either pay it off or cut it (Chekhov's gun: remove what doesn't fire). For each unprepared payoff, plant it *earlier* — and plant it *casually*, so it reads as world-texture on first pass and as inevitability on the second.

> **→ SHORT-FORM.** A short usually has room for exactly one setup/payoff pair — and it's often the hook itself. Whatever the first 2 seconds promise *is* the setup; the last beat *is* the payoff. (See #10.)

> **→ AI APPLICATION.** The assistant builds the setup/payoff ledger automatically from the beat sheet and reports orphans in both directions, naming the exact beats.

### 9. Unearned ending / deus ex machina

**Symptom.** The ending resolves too neatly, too suddenly, or by means the hero didn't earn — a sudden rescue, a coincidence, a previously-unmentioned power, a character who just *decides* to change. The audience feels cheated rather than satisfied.

**Root cause.** The resolution comes from *outside the established logic* of the story rather than *out of the protagonist's own choices*. This is the oldest named flaw in dramaturgy: Aristotle, in the *Poetics*, insists the resolution must arise "from the plot itself, and not from a contrivance"; Horace, in *Ars Poetica*, warned poets not to bring on a *deus ex machina* ("a god from the machine") unless the knot truly merits it. The literal device — a crane lowering a god to fix the plot — became the name for *any* unearned external resolution.

**Fix.** The climax must be solved by the *protagonist's own agency*, using capacities/objects the story has already established, and the cost must be paid (often the want is achieved through, or sacrificed for, the *need* — see arc in [03-character-and-scene-craft.md](03-character-and-scene-craft.md)). Strip out coincidences that *help* the hero (coincidences that *hurt* are fair). If a tool is used to win, it must have been planted (back to #8). The change in the hero must be visibly *earned* by the gauntlet they've passed through.

> **→ SHORT-FORM.** Even in 60 seconds the payoff must feel *caused* by the turn, not bolted on. A product that magically solves everything with no friction shown reads as a deus ex machina — and viewers disbelieve it.

> **→ AI APPLICATION.** The assistant checks the climax beat: *Is the decisive action taken by the protagonist? Does it use only previously-established means?* If a new element appears at the end with no earlier plant, it flags **UNEARNED RESOLUTION**.

### 10. The hook promises X but the film delivers Y

**Symptom.** The opening (or thumbnail/title/first line) sets up one kind of story — a thriller, a comedy, a mystery — and the body delivers something tonally or topically different. High initial attention, then a steep drop-off and a vague sense of betrayal. Reviews say "not what I expected" (and not in a good way).

**Root cause.** A broken **promise of the premise** — the hook (see [04-engagement-psychology-hooks.md](04-engagement-psychology-hooks.md)) opens a *curiosity gap* or genre expectation that the story never honors. This is also a **genre-convention** failure: per the Story Grid (Shawn Coyne), a genre carries **obligatory scenes and conventions** the audience is *promised*; skip the love story's confession scene, or the thriller's hero-at-the-mercy-of-the-villain scene, and the audience feels shortchanged even if they can't name why.

**Fix.** Decide what the hook *promises* (tone, genre, central question) and audit whether the body *delivers and answers* it. Either change the hook to match the film, or change the film to keep the hook's promise — but they must agree. Then confirm you've delivered the *obligatory scenes* of your declared genre.

> **→ SHORT-FORM.** This is the single most important short-form test. The hook is a *promise*; the last beat must *keep it*. A bait-and-switch (clickbait hook, unrelated payoff) trains the algorithm and the viewer to distrust you. Promise → keep, in under 60 seconds.

> **→ AI APPLICATION.** The assistant states the hook's implied promise back to the user, then checks the final beat against it: *"Your hook promises [X]; your ending delivers [Y]. Do these match?"* Mismatch = **BROKEN PROMISE** flag.

### 11. Flat character — no flaw, no arc

**Symptom.** The protagonist is competent, likable, and *unchanging*. They're the same person at the end as the beginning. Nothing inside them is at risk. We admire them but don't *care*.

**Root cause.** No **flaw / lie / misbelief** to overcome, therefore no **arc**. A character without an internal weakness has nothing to learn, so there's no inner story — only external plot. Truby pairs the hero's **psychological need** (self-harm) with a **moral need** (a flaw that *harms others*); the richest arcs fix both, climaxing in a **self-revelation** the hero couldn't have reached at the start.

**Fix.** Give the protagonist a **lie they believe** about themselves or the world (e.g., "I don't need anyone"), let that lie *cause* their early failures, and structure the story so the climax forces them to *abandon the lie* to win (or cling to it and lose). Add a moral dimension: show the flaw *hurting someone*. The arc is the gap between who they are at the start and the self-revelation at the end.

> **→ SHORT-FORM.** A full arc rarely fits in 60s — instead, imply a *micro-shift*: one expression, one decision that signals change. A single before/after contrast (skeptical face → convinced face) is the short-form arc. Don't attempt a full transformation; imply one pivot.

> **→ AI APPLICATION.** The assistant asks: *"What false belief does your protagonist hold at the start, and what do they realize by the end?"* If there's no lie or no change, it flags **FLAT CHARACTER** and offers candidate flaws derived from the want.

### 12. On-the-nose dialogue

**Symptom.** Characters say exactly what they feel and mean: "I'm so angry at you for leaving." "I'm scared." Dialogue functions as a status report. No subtext, no friction, nothing left for the audience to infer.

**Root cause.** No **subtext** — the gap between what's said and what's meant (see subtext in [03-character-and-scene-craft.md](03-character-and-scene-craft.md)). Real people pursue goals *obliquely*; they deflect, perform, and conceal. On-the-nose lines also often smuggle in exposition or theme (overlap with #7).

**Fix.** Two surgical tools. (1) Give the scene a goal the dialogue *dances around* rather than states — let characters talk about the dishes while the real subject is the divorce. (2) The **"cut the first and last line"** test (below): trim the lines where characters announce entrances/intentions and summarize takeaways. Trust the audience to read behavior. Replace "I'm scared" with an action that *shows* fear.

> **→ SHORT-FORM.** Most strong shorts carry little to no dialogue — image and sound do the work. If a line is needed, it should be a *hook* or a *button* (a sharp closing line), never an explanation. When in doubt, cut the line and let the picture say it.

> **→ AI APPLICATION.** The assistant flags lines that *name an emotion* or *explain a plot point* and proposes a subtextual or behavioral replacement. It is conservative — flags only the clearest offenders to avoid stripping intentional flatness.

---

## The Rapid Tests

When you don't have time for the full checklist, these five fast diagnostics catch the majority of structural failures. Run them in order.

### The But/Therefore test
State the story as a beat list. Between every two beats, force a connective: **"therefore"** (this caused that) or **"but"** (this complicated that). If you find yourself writing **"and then,"** that joint is dead — it's chronology, not causality (failure #5). A healthy plot is a chain of *but / therefore*. (Origin: Trey Parker & Matt Stone's articulation, popularized as a Pixar-adjacent rule; see [04-engagement-psychology-hooks.md](04-engagement-psychology-hooks.md).)

### The Want / Obstacle test
For the whole story *and* for every scene, answer two questions: **"What does the protagonist WANT here, and what is stopping them?"** If either answer is blank, you've found inertia (failures #2 and #4). A scene with a want and a blocker has tension by construction.

### The Value-shift-per-scene test
For each scene, name the **value** at stake and its **charge at the start vs. the end** (e.g., *trust*: + → −). If a scene opens and closes on the *same* charge, *nothing happened* — it's a transit scene and should be cut or merged. This is McKee's scene-as-value-change made operational (see [03-character-and-scene-craft.md](03-character-and-scene-craft.md)). Bonus: charges should *alternate and escalate* across the act, not flatline (failure #6).

### The Cut-first-and-last-line test
Mechanically delete the first and last line of dialogue in *every* scene, then read it. Usually the scene is *better*: writers reflexively pad the top (characters announcing why they're there) and the bottom (summarizing the takeaway). What's left starts later and ends sooner — entering the scene late and leaving early is the heart of crisp screenwriting and a fast fix for on-the-nose dialogue (failure #12).

### The Spine-in-one-sentence test
Can you state the story as **one sentence** of the form: *"A [protagonist] wants [want] but [obstacle], so [action], leading to [outcome/cost]"*? If you can't — if it takes a paragraph, or you keep adding "and also…" — the story has no single spine (failures #1 and #5). If you *can*, that sentence is your North Star: every scene must serve it.

### The 13-thumbnail / silhouette test (visual variety)
Pull 13 representative frames across the cut and view them as thumbnails — or reduce each key shot to a black **silhouette**. If they all look the same (same framing, same staging, same value of light/dark), the film is *visually monotonous* regardless of how good the story is, and the eye disengages. Strong visual storytelling produces *distinct, readable silhouettes* and varied compositions. This is a visual-rhythm diagnostic — see [06-shots-framing-composition.md](06-shots-framing-composition.md) and the keyframe/storyboard discipline in [17-ai-storyboard-prompting-and-keyframes.md](17-ai-storyboard-prompting-and-keyframes.md). For AI films it's doubly critical: prompt drift tends to collapse shots toward the model's "average" framing, so silhouette-checking the storyboard *before* generation catches monotony cheaply.

---

## → SHORT-FORM: The 60-Second Triage

You cannot run twelve diagnostics on a 60-second piece — and you shouldn't, because forcing feature theory onto a short is exactly how it bloats into a talky micro-film. Compress the entire checklist into **four questions**:

1. **One WANT?** Is there a single agent pursuing a single, visible desire from second one? (Failures #1, #2.)
2. **One TURN?** Is there exactly one moment where the situation flips — a reveal, reversal, or escalation? (Failure #6.)
3. **One PAYOFF?** Does the ending *cause-and-effect resolve* the turn (not bolt on, not deus ex machina)? (Failures #8, #9.)
4. **Does the HOOK keep its promise?** Does the last beat deliver what the first 2 seconds promised? (Failure #10 — the single highest-leverage short-form test.)

If all four are *yes*, the short works structurally. If any is *no*, fix *that one thing* — do not add content. Shorts are fixed by *subtraction and sharpening*, almost never by addition.

---

## → AI APPLICATION: The Checklist as Interrogation Script

This chapter is engineered to be executed, not just read. An LLM story-assistant runs it as a **gated interrogation** over the user's concept and beat sheet, in the spirit of the "grill, don't please" mandate of [19-the-grilling-workflow.md](19-the-grilling-workflow.md):

- **One question per failure mode**, asked bluntly, in leverage order (start with #1 "Whose story is this?"). Do not soften. The assistant's job is to find the break, not to validate the idea.
- **Refuse to advance on a hard fail.** No protagonist, no want, no stakes, broken hook-promise → the assistant *stops* and reports the flag with its name (e.g., `EPISODIC`, `FLAT MIDDLE`, `UNEARNED RESOLUTION`) rather than generating beats on a broken foundation. Generating storyboards for a story with no spine wastes the most expensive resource in the pipeline (compute on video generation).
- **Run the rapid tests mechanically.** The but/therefore connective audit, the active-verb audit, the value-charge map, and the setup/payoff ledger are all *programmatic* — the assistant computes them over the beat list and returns structured flags, not vibes.
- **Propose named fixes, let the human choose.** For the saggy middle it offers the four interventions (raise stakes / ticking clock / midpoint reversal / worse choice) and asks which fits the story — diagnosis is automatable, but the creative *choice* of fix stays with the author.
- **Silhouette-check before generation.** For AI video specifically, the assistant runs the 13-thumbnail test on the *storyboard prompts* before any frame is rendered, catching visual monotony while it's still free to fix.

The deepest point: a model is a far better *diagnostician* than *author*. It can't reliably write a moving climax, but it can flawlessly detect that your climax is solved by a coincidence, your middle is flat, and your hook writes a check your ending doesn't cash. Used as a script doctor — not a script writer — the LLM is at its most valuable.

---

## Sources

- Robert McKee, *Story* — "the gap" between expectation and result, scene-as-value-change, the controlling idea: [Emily Short, "Story (Robert McKee) and the Expectation Gap"](https://emshort.blog/2019/02/05/story-robert-mckee/); [Notes on McKee's *Story* 19: "Mind the Gap"](https://www.tumblr.com/writing-prompts-for-friends/611033879695982592/notes-on-robert-mckees-story-19-mind-the-gap)
- John Truby, *The Anatomy of Story* — moral vs. psychological need, the true opponent, designing principle, self-revelation: [Decoding Creativity, "Truby's 22 Steps"](https://www.decodingcreativity.com/trubys-22-steps/); [Arc Studio, "22 Building Blocks – John Truby"](https://www.arcstudiopro.com/blog/22-building-blocks-john-truby)
- Shawn Coyne, *The Story Grid* — obligatory scenes & conventions, genre as audience expectation: [Story Grid Store, "Conventions and Obligatory Moments"](https://store.storygrid.com/product/conventions-and-obligatory-moments/); [Story Grid, "Nine Must-Haves"](https://storygrid.com/969/)
- Aristotle, *Poetics* & Horace, *Ars Poetica* — resolution must arise from the plot, not a contrivance; origin of *deus ex machina*: [Deus ex machina — Wikipedia](https://en.wikipedia.org/wiki/Deus_ex_machina)
- Lajos Egri, *The Art of Dramatic Writing* — the "premise" as the argument the plot must prove (cross-referenced from existing bible chapters; concept summarized here)
