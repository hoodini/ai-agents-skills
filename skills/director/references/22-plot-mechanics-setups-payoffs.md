# Plot Mechanics — Setups, Payoffs, Reversals & Irony

Structure (`01-story-structure.md`) tells you *where* the big beats land. Character craft (`03-character-and-scene-craft.md`) tells you *who* is changing and why. This chapter is about the **wiring between the beats** — the moment-to-moment machinery that makes an audience lean forward ("what happens next?") and then snap back in satisfaction ("oh, of *course*"). It is the most undervalued layer for technical, AI-native makers, because it feels like it should be automatable and isn't: causality, planting, and irony are where generated scripts most visibly fall apart into "and then... and then... and then."

The whole chapter rests on one claim: **a plot is not a list of events. It is a chain of consequences.** Everything below is a technique for building, hiding, or detonating links in that chain.

---

## 1. Causality — the "But / Therefore" chain vs. "And Then"

The single most useful diagnostic in all of plotting comes from Trey Parker and Matt Stone (*South Park*), delivered to an NYU film class in 2011. Watch how you connect your beats. If the connective tissue between two events is the word **"and then,"** you have a list, not a story. If it's **"but"** or **"therefore,"** you have a plot.

- **Therefore** = consequence. This event *caused* the next ("He missed the train, *therefore* he stole a car").
- **But** = complication / reversal. The next event obstructs or contradicts the expectation ("He stole a car, *but* it belonged to a cop").
- **And then** = mere sequence. Things happen in order but nothing causes anything ("He missed the train, *and then* he had a coffee, *and then* he saw a friend").

Parker's blunt version: if "and then" is your connector, "you've got something pretty boring." The intuition is that **causality is what the brain rewards** — each "therefore" confirms the audience's model of the world (a small prediction-met hit) and each "but" violates it productively (a prediction-error spike; see `05-neuroscience-honest.md` on prediction error). "And then" delivers neither. It is narrative white noise.

This is the engine-room version of the same principle Pixar's "scene-builds-on-scene" rule expresses (`02-pixar-22-rules.md`) and the academic version McKee frames as *cause and effect* over *coincidence*. Coincidence is allowed to *start* trouble (a plane crash strands the hero) but must never *solve* it — a coincidence that rescues the protagonist is the deus ex machina the audience feels cheated by.

**Practical test:** write your beat sheet as a single paragraph and force every connector to be "but" or "therefore." Any beat that will only accept "and then" is either redundant (cut it) or unmotivated (find its cause).

> **→ SHORT-FORM:** In a 60-second teaser you may have only 4–6 beats, but the rule is *more* ruthless, not less. A teaser is one "but" and one "therefore": *Normal world → BUT something invades it → THEREFORE everything is now at stake → [withhold].* The classic failure mode of AI-made shorts is the "and then" montage — pretty shot, pretty shot, pretty shot — which has zero causal pull and is forgotten in seconds. If your 30s spot can be reordered without breaking, it has no causality and no spine.

> **→ AI APPLICATION:** Make "but/therefore" a hard lint rule. An LLM story-assistant should generate the beat sheet, then run a second pass labeling each inter-beat connector as `BUT | THEREFORE | AND_THEN` and flag every `AND_THEN` for rewrite. This is a cheap, mechanical check that catches the most common generation failure before any image or video is rendered.

---

## 2. Setup & Payoff — planting and harvesting

A **setup** is information, an object, or a capability planted early. A **payoff** is the later moment when that plant becomes decisive. The pleasure of payoff is the pleasure of a closed loop: the audience's memory is rewarded, and the story feels *designed* rather than improvised.

### Chekhov's gun

Anton Chekhov's rule, in his own words: *"If in the first act you have hung a pistol on the wall, then in the following one it should be fired. Otherwise don't put it there."* Two halves, both load-bearing:

1. **What you plant, you must fire.** A prominent object that never pays off is a broken promise — the audience filed it as "important" and you defaulted on the debt.
2. **What you fire, you should have planted.** The deeper, more-violated half. The gun that solves the climax must have been visible earlier, or the resolution feels arbitrary.

### The cardinal rule: set up, but do not telegraph

The art lives in the gap between *planted* and *telegraphed*.

- **Telegraphed** = the audience consciously predicts the payoff. The lingering close-up on the loose floorboard screams "treasure under here." Prediction met too early = no surprise, and often a feeling of being condescended to.
- **Planted** = the audience *registers* the detail without flagging it as a Chekhov's gun. On payoff they think, "I saw that — I just didn't know what it was."

The technique for hiding a plant is **camouflage through function**: give the setup a *present-tense reason to exist* so it reads as texture, not foreshadowing. In *Shaun of the Dead* nearly every climactic gag is set up in the first act as throwaway dialogue or background business ("we're not doing 'fast' zombies"; the route to the pub; the rifle that "isn't even real") — each line is funny *in the moment*, which is why nobody clocks it as a plant. This is the **plant-in-conflict / plant-as-comedy** rule: bury the setup inside a scene whose surface purpose is something else.

### Foreshadowing vs. the callback

- **Foreshadowing** seeds tone or expectation ("it's not safe out there"), tuning the audience's antennae without a specific object.
- **The callback** is a payoff whose pleasure is *recognition itself* — a repeated line, image, or motif that returns transformed. In *Casablanca*, "Here's looking at you, kid" lands harder each return because the meaning shifts under it. A callback that returns *unchanged* is a catchphrase; one that returns *with new weight* is a payoff.

> **→ SHORT-FORM:** The whole game of a great short is **one setup, one payoff, maximum distance between them.** The cold-open detail — a glance, an object, a line — that detonates on the final button. A product teaser: open on a tiny, unexplained frustration (the spinning loader); spend 45 seconds elsewhere; close on the *same frame* now resolved. The loop closing in under a minute is what makes a short feel authored instead of assembled.

> **→ AI APPLICATION:** Maintain an explicit **setup/payoff ledger** as structured state alongside the beat sheet: every `setup` gets an id, a beat index, and a `paid_by: null` field. Before "locking" a script the assistant asserts that no setup has `paid_by: null` (Chekhov's first half) and no payoff references an unplanted element (second half). This converts a craft instinct into a graph-completeness check an LLM can actually run. Bonus check: flag setups whose camera/prose emphasis is so heavy they are likely *telegraphed*.

---

## 3. Dramatic Irony vs. Surprise vs. Mystery — who knows what

These three are distinguished by **the gap between what the audience knows and what the characters know.** Choosing the gap is one of the most powerful and least-understood levers a storyteller has.

### Hitchcock's bomb under the table

Alfred Hitchcock's illustration to François Truffaut is the canonical teaching. Two people talk at a table; a bomb is underneath.

- **Surprise:** the audience doesn't know about the bomb. They chat, then — *boom*. Hitchcock: this buys *"fifteen seconds of surprise"* at the blast.
- **Suspense (dramatic irony):** the audience *saw the anarchists plant the bomb* and there's a clock in the shot. Now the same dull conversation is unbearable — the viewer is "longing to warn the characters." This buys *"fifteen minutes of suspense."*

The lesson: **giving the audience superior knowledge converts a flat scene into tension.** Suspense is not about hiding information; it is most often about *revealing* it to the audience and withholding it from the characters.

Hitchcock's crucial caveat: *"except when the surprise is a twist"* — i.e., when the unexpected reveal is itself the climax of the story, you withhold from the audience too. So the three modes:

| Mode | Audience knows | Character knows | Effect | Use when |
|---|---|---|---|---|
| **Dramatic irony / suspense** | Yes | No | Dread, tension, "don't open that door" | You want sustained anxiety over a stretch of screen time |
| **Surprise** | No | No (or yes) | A short jolt | A single beat needs a shock; cheap if overused |
| **Mystery** | No (but knows there's something to know) | Varies | Curiosity, active theorizing | You want the audience *investigating* (whodunits, puzzle-box) |

**Mystery** is the third sibling: the audience knows a fact is being withheld and is invited to guess. It powers the curiosity gap (`04-engagement-psychology-hooks.md`). The risk is that mystery makes the audience *spectators of a puzzle*; dramatic irony makes them *participants in a relationship*. The latter usually binds harder emotionally.

> **→ SHORT-FORM:** Dramatic irony is the most efficient tension tool in short form because it needs no setup time to *generate* tension — only to *reveal* the gap. Show the audience the thing the character can't see (the crack in the dam, the message they haven't read), and a 20-second clip carries dread it could never earn through plot. The micro-version: a split-screen or a cutaway that tells *us* what the on-screen person doesn't know.

> **→ AI APPLICATION:** Encode a per-beat **knowledge-state model**: for each key fact, track `audience_knows` and `character_knows` as booleans across the timeline. The assistant can then *choose* the mode deliberately ("this scene should be dramatic irony → set `audience_knows=true, character_knows=false` and ensure an earlier beat does the revealing"). It can also detect accidental irony loss — e.g., a "twist" the audience could already infer because a prior beat leaked the fact.

---

## 4. Reversal (Peripeteia) and Recognition (Anagnorisis)

From Aristotle's *Poetics*, the two devices he rated most powerful — the marks of what he called a **complex plot** (a plot whose change of fortune comes *with* reversal and/or recognition, superior to a "simple" plot that merely changes fortune).

- **Peripeteia (reversal):** *"a change by which the action veers round to its opposite,"* and crucially *"subject always to our rule of probability or necessity."* It is a reversal of *circumstances* — the situation flips. The messenger arrives to relieve Oedipus's fear and, by his very reassurance, reveals the horror.
- **Anagnorisis (recognition):** a change *"from ignorance to knowledge"* — a reversal of *understanding*. Oedipus recognizes that he is the murderer he hunts.

Aristotle's highest praise is for the moment when **the two fire together**: the recognition *causes* the reversal. That simultaneity is the most concussive beat available to a dramatist — the character learns the truth and the world inverts in the same instant. Note the phrase *"probability or necessity"*: a reversal that violates the established logic isn't peripeteia, it's a cheat (see §5).

The modern descendants: the "all is lost" / lowest-point reversal, the midpoint flip (§7), and the recognition scene where a protagonist finally sees their own lie (the "self-revelation," tied to the want-vs-need engine in `01-story-structure.md` and `03-character-and-scene-craft.md`). Truby frames the strongest stories as building toward exactly this fused moment of self-revelation arriving with the decisive battle.

> **→ SHORT-FORM:** A teaser can hold *one* reversal, and that's the whole product. Structure: establish a frame, then peripeteia flips it — "This is a cooking tutorial. BUT the chef is a robot." The recognition variant: the final two seconds recontextualize everything before it (the "it was X all along" button). Resist the urge to add a second reversal; in 60 seconds it reads as confusion, not complexity.

> **→ AI APPLICATION:** The "fused reversal+recognition" is generatable if you separate the two questions: (1) *What does the character believe?* (2) *What single fact, if learned, both inverts their situation and exposes that belief as false?* An LLM prompted to find the intersection of "situation-flipping fact" and "belief-destroying fact" produces far stronger turns than one asked vaguely for "a twist." Track the protagonist's stated belief in state so the recognition can be aimed at it.

---

## 5. The Twist that is "Surprising yet Inevitable" — and the difference from a cheat

The gold standard for a twist, rooted in Aristotle's demand that an ending be both *"inevitable and unexpected,"* and popularized in screenwriting by Robert McKee in *Story*: a great turn is **surprising yet inevitable.**

- **Surprising:** the audience did not predict it.
- **Inevitable:** *looking back*, it's the only thing that could have happened. The clues were all there.

These feel contradictory but are reconciled by **direction of attention.** You make it surprising by directing the audience's conscious attention *away* from the truth (misdirection, red herrings, a more obvious interpretation of the same clues). You make it inevitable by planting the real clues *in plain sight*, available on rewatch. McKee's framing: at the inciting incident anything seems possible; at climax, looking back, the path taken should seem the *only* path.

### Twist vs. cheat — the fair-play line

The difference is a single question: **could a sharp viewer have figured it out from information already given?**

- **Twist (fair):** *The Sixth Sense* — Malcolm is dead. On rewatch: nobody but the boy speaks to him; the restaurant scene; the door that won't open; the unchanged clothes. The information was *all there*, camouflaged by a more obvious reading. *The Usual Suspects* — Kint's tale is woven from the names on the bulletin board behind him, shown to us repeatedly.
- **Cheat (unfair):** the killer is a character introduced in the last two minutes; the resolution depends on a power/fact the audience was never shown; "it was all a dream." These violate Aristotle's *"probability or necessity"* — the audience can't replay the film and find the seams, so they feel conned rather than fooled.

The fair-play doctrine is formalized in detective fiction (Ronald Knox's "Decalogue," the Detection Club rules) but applies to every twist: **the clue must precede the reveal and be discoverable.** A twist is a payoff (§2) whose setups were deliberately disguised. That's why twist and setup/payoff are the same machinery viewed from opposite ends.

> **→ SHORT-FORM:** The most shareable shorts *are* a single fair twist — the button recontextualizes the whole clip, and the "wait, watch it again" rewatch is the engagement engine. Inevitability in short form means the clue is *on screen the entire time* (it must be — there's no room to hide it elsewhere), just unnoticed. The cheat in short form is the bait-and-switch with no relationship to the setup; it converts delight into "clickbait" resentment fast.

> **→ AI APPLICATION:** Verifying fair play is a concrete check. After generating a twist, the assistant lists the 2–4 facts the twist *depends on*, then asserts each appears in an *earlier* beat (the setup ledger from §2 does exactly this). If a dependency has no earlier appearance, the twist is currently a cheat — auto-insert a camouflaged plant. To generate the twist itself, prompt for "the second-most-obvious interpretation of the clues already on the table," which structurally yields surprising-yet-inevitable rather than out-of-nowhere.

---

## 6. Escalation — try/fail cycles and the "things get worse" engine

A plot doesn't just move; it **intensifies.** The mechanism is the **try/fail cycle**, which is the Story Spine "because of that" beats (`02-pixar-22-rules.md`) made adversarial: the hero pursues the goal, fails, and the failure *raises* the stakes or *narrows* the options.

The strongest version follows the **"yes, but / no, and"** rule (from improv and adopted by screenwriters):

- **"Yes, but..."** — the character gets what they tried for, *but* it triggers a worse problem. (They escape the building, *but* now the police think they're the bomber.)
- **"No, and..."** — they fail, *and* things get worse on top of the failure. (They don't reach the antidote, *and* now the lab is on fire.)

Notice these are just "but" and "therefore" (§1) operating at the scene level — every try/fail link is causal. A flat answer ("yes, and they succeed" / "no, and nothing changes") kills momentum; it's "and then" in disguise.

**Raising stakes** has a ceiling problem: you can't escalate *magnitude* forever (the world can only end once). So escalate along other axes instead — **personal cost** (now it's their child), **moral compromise** (now winning requires betrayal), **shrinking time** (§7), **narrowing options** (the exits close one by one). McKee's "progressive complications" and the gap between expectation and result widening with each beat is the same idea: each turn should demand *more* of the protagonist than the last.

> **→ SHORT-FORM:** You get *one* escalation, maybe two. The structure is "problem → bigger problem," not a full try/fail ladder. A vertical ad: "the dishwasher's broken (annoying) → the in-laws arrive in an hour (catastrophe)." Escalate the *stakes*, not the *number of attempts* — there's no time for attempts. The trap is the talky micro-film that tries to stage three try/fail beats and ends up explaining instead of escalating.

> **→ AI APPLICATION:** Constrain each try/fail beat to a `yes_but | no_and` outcome type, forbidding flat `yes` / `no`. Track a monotonic **stakes-and-pressure vector** across beats — `magnitude`, `personal_cost`, `time_remaining`, `options_left` — and require that *at least one* dimension worsens every cycle. This catches the most common mid-act sag: scenes where the character is busy but nothing actually got worse.

---

## 7. Tension devices — the Ticking Clock, the Time Lock, and the Midpoint reversal

### The ticking clock / time lock

A **time lock** is a deadline imposed on the action: the bomb detonates at 1:00; the wedding is at noon; the oxygen lasts six hours. It works because it **converts an open situation into a closing one**, manufacturing urgency and making every wasted moment painful. The clock in Hitchcock's bomb scene (§3) is the device that *makes the irony unbearable* — irony + a deadline is a tension multiplier.

Design notes:
- The clock must be **visible and quantified.** "Soon" doesn't tick; "ninety seconds" does. Make the audience able to *count*.
- It must be **periodically reasserted** — cut back to it so dwindling time is felt.
- It should **shrink the option space**, not just add pressure: as time runs out, plans must get more desperate (which feeds escalation, §6).

Related devices: **the time bomb of dramatic irony** (audience knows the deadline the character doesn't), **the trap/confinement** (space lock instead of time lock — the shrinking room, the besieged house), and **the ticking emotional clock** (he proposes tomorrow; she leaves the country tonight).

### The midpoint reversal

In Save the Cat and most modern feature structure (`01-story-structure.md`), the **midpoint** is a major peripeteia that flips the story's polarity and resets the engine for Act Two-B. Two flavors:

- **False victory → real danger:** things have been going well; at the midpoint a reveal shows the true threat. The hero stops *reacting* and starts *acting* (often shifting from "want" toward "need").
- **False defeat → new resolve:** things look lost; a midpoint discovery gives a new plan or raises the stakes to personal.

The midpoint's job is structural: it prevents the dreaded "muddy middle" by giving Act Two its own inciting incident. It is usually where the *stakes are raised* and the *clock starts ticking* — the two devices in this section frequently coincide here.

> **→ SHORT-FORM:** The ticking clock is *the* short-form tension device because it needs no backstory — "47 seconds left" is instantly legible, and an on-screen countdown literally syncs the audience's anxiety to the runtime. Many great shorts *are* a countdown. You won't have a "midpoint" in 30 seconds, but you can use its logic: the halfway flip ("this fun video... is actually a warning") is the single reversal of §4 placed at the clip's center.

> **→ AI APPLICATION:** Model the clock as explicit state: `deadline`, `time_remaining`, and a `reassert_at` list of beat indices, with a check that the gap between reassertions never gets so large the clock is "forgotten." For the midpoint, the assistant can assert that the beat at ~50% changes the protagonist's *mode* (reactive→active) and *raises a tracked stakes dimension* — a measurable definition of "the midpoint did its job."

---

## 8. Red Herrings — misdirection that plays fair

A **red herring** is a deliberately planted false lead: a clue engineered to point the audience toward the wrong conclusion, protecting a fair twist (§5) by giving the conscious mind something else to chase. The professor with the obvious motive; the suspiciously over-explained alibi.

The discipline: **a red herring must have an honest in-story reason to exist.** The professor *did* hate the victim — that's true, just not the cause of death. A red herring that exists *only* to mislead, with no organic place in the world, reads as authorial cheating the moment it's debunked. Misdirection is legitimate; lying to the audience is not. (Hence red herrings are the mirror image of camouflaged plants in §2 — one hides the true setup behind ordinary function, the other foregrounds a false setup that *also* has ordinary function.)

> **→ SHORT-FORM:** Usually too expensive — a red herring needs runtime to plant *and* debunk. The compressed version is the **frame fake-out**: the clip presents as one genre/situation (cooking, ASMR, a tutorial) and the button reveals another. The "genre" itself is the herring.

> **→ AI APPLICATION:** Track red herrings as a `misdirection` field linked to the true setup they protect, with a required `honest_reason` so the assistant can't plant a lead with no diegetic justification. On twist verification (§5), confirm at least one herring is drawing attention away from the real clue — under-misdirected twists are the ones that feel "too obvious."

---

## 9. Exposition — delivering information without dumping

**Exposition** is the necessary background — who, where, the rules, the history — that the audience must absorb to follow the story. An **info-dump** is exposition delivered as a lecture: characters telling each other things they already know ("As you know, Captain, our reactor's been failing since the war"), or a narrator front-loading a wiki page. It's deadly because it stops the *present-tense* story to service the past.

The craft rules for invisible exposition:

1. **Dramatize, don't state.** Show the rule operating instead of explaining it. We learn the *Gattaca* world is genetically stratified by *watching* a vacuumed eyelash get someone fired — no lecture needed.
2. **Hide it inside conflict.** This is the master technique. When two characters *argue*, the audience absorbs the facts as ammunition without registering them as exposition. The fact rides in on the emotion. (This is the scene-as-value-change principle of `03-character-and-scene-craft.md`: a scene whose surface is a fight can deliver its facts for free.)
3. **Make the audience want it first.** Withhold a fact until a question is burning, then the answer lands as payoff, not homework (the curiosity gap, `04-engagement-psychology-hooks.md`).
4. **Ration it.** Deliver the minimum needed *now*; trust the audience to hold questions. Mystery (§3) is exposition deliberately delayed.
5. **Put it in the mouth of someone who'd say it.** Exposition spoken for the *listener's* benefit reads false; spoken because the *speaker* has a reason to say it reads true.

The "**on a need-to-know basis**" maxim: give the audience exactly the information required to understand the *next* beat's stakes, no more. Excess backstory is the most common reason early scenes drag.

> **→ SHORT-FORM:** Near-zero tolerance for exposition. There is no time to explain the world — you must *imply* it through one vivid concrete image and let the audience fill the rest. The mistake that bloats AI shorts into "talky micro-films" is treating the teaser as a place to explain the premise; the teaser's job is to make the premise *felt and unexplained* so the viewer needs the full thing. If your short has a line that begins "Let me explain," cut it.

> **→ AI APPLICATION:** LLMs *love* to dump — explaining is their native mode, so this needs an explicit guardrail. Tag each exposition fact with `needed_by_beat` and forbid delivering it earlier than one beat before it's required (rationing). Then run a **"dramatize vs. state" pass**: flag any line whose function is purely informational and whose surface action is just "telling," and rewrite it to ride inside a conflict beat. A simple heuristic flag: dialogue containing "as you know," "remember when," or "let me explain" is almost always a dump.

---

## 10. Putting it together — the mechanic's checklist

These devices are not a menu; they interlock. Setup/payoff, the twist, and the red herring are *the same graph* (plant → disguise → harvest) seen from different angles. Causality (but/therefore) is the rule that *every link* in that graph must obey. Dramatic irony and the clock are levers on *who knows what, and how much time is left*. Reversal+recognition is the highest-voltage node you can build, and exposition discipline is what keeps the wires from showing.

A pre-lock pass for any script (and a literal validation routine for an AI pipeline):

1. Every inter-beat connector is **but/therefore**, never "and then." (§1)
2. Every **setup is paid**; every payoff was **planted and camouflaged**, not telegraphed. (§2)
3. Each tense scene has a deliberate **knowledge gap** — you chose irony, surprise, or mystery on purpose. (§3)
4. The story climaxes on a **reversal and/or recognition**, ideally fused. (§4)
5. The central **twist is fair** — every fact it depends on appeared earlier. (§5)
6. The middle **escalates** (yes-but / no-and); at least one pressure dimension worsens each cycle. (§6)
7. A **clock** is visible, quantified, and reasserted; the **midpoint** flips polarity. (§7)
8. **Red herrings** have honest reasons to exist. (§8)
9. **Exposition** is dramatized, rationed, and hidden in conflict. (§9)

If all nine hold, "what happens next?" and "oh, of course" will both be true — which is the entire job of plot.

---

## Sources

- The But & Therefore Rule (David Perell) — https://perell.com/note/but-therefore-rule/
- Writing Advice from Matt Stone and Trey Parker (Go Into The Story / Scott Myers) — https://gointothestory.blcklst.com/writing-advice-from-matt-stone-and-trey-parker-30941b2cd98c
- Chekhov's gun (Wikipedia, exact quote) — https://en.wikipedia.org/wiki/Chekhov%27s_gun
- Peripeteia (Wikipedia) — https://en.wikipedia.org/wiki/Peripeteia
- Anagnorisis — Aristotle: Poetics (Univ. of Hawaiʻi, CriticaLink) — https://www.english.hawaii.edu/criticalink/aristotle/terms/anagnorisis.html
- Peripeteia — Aristotle: Poetics (Univ. of Hawaiʻi, CriticaLink) — https://www.english.hawaii.edu/criticalink/aristotle/terms/peripeteia.html
- Poetics, Chapters 10–12 (complex vs. simple plot) — SparkNotes — https://www.sparknotes.com/philosophy/poetics/section5/
- Alfred Hitchcock and François Truffaut Explain Surprise vs. Suspense (No Film School) — https://nofilmschool.com/alfred-hitchcock-and-francois-truffaut-explain-surprise-vs-suspense
- The Bomb Under the Table (Alec Nevala-Lee, full Hitchcock/Truffaut passage) — https://nevalalee.wordpress.com/2011/10/26/the-bomb-under-the-table/
- How to Write an Ending that is Surprising Yet Inevitable (Electric Literature; Aristotle "inevitable and unexpected") — https://electricliterature.com/surprising-yet-inevitable-ending-read-like-a-writer/
- Notes on Robert McKee's *Story* — How to Climax ("inevitable and unexpected") — https://writing-prompts-for-friends.tumblr.com/post/629123437104955392/notes-on-robert-mckees-story-31-how-to-climax
- Knox's Decalogue / fair-play detective rules (Wikipedia, Ronald Knox) — https://en.wikipedia.org/wiki/Ronald_Knox#Ten_Commandments_of_Detective_Fiction
- Writing 101: What Is Chekhov's Gun? (MasterClass) — https://www.masterclass.com/articles/writing-101-what-is-chekhovs-gun-learn-how-to-use-chekhovs-gun-in-your-writing
