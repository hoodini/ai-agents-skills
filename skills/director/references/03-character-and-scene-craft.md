# Character & Scene Craft

Story is not "stuff that happens." Story is the record of a person being forced, against their will, to change. Everything in this chapter serves that single sentence. Character is the engine; scene is the piston. Plot is just the smoke coming out the back — it is the *visible* trace of pressure applied to an interior life. If you remember only one thing: **audiences do not bond with events, they bond with people under pressure, making choices that cost them something.**

This chapter has two halves. The first builds a character that an audience cannot look away from. The second builds the scene — the irreducible structural unit where character is *tested*. At the end, the AI bridge: how to compress all of this into a machine-readable "character bible" entry that drives both your *writing* and your *visual consistency pipeline*, and how to spec scenes as value-shift units a model can actually storyboard.

For how these units assemble into a feature-length shape, see `01-story-structure.md`; for how the cut expresses a turn, see `10-editing-theory.md`.

---

## PART ONE — CHARACTER

### The three-layer spine: Want, Need, and the Lie

A compelling protagonist is built from a contradiction between what they *pursue* and what they *require*. Define three things and almost everything else falls out of them.

- **The Want (the external goal / "desire line"):** the concrete, visible, plot-driving objective. Win the case. Get to Mordor. Get Marty back to 1985. The Want is what the audience can *watch* the character chase. It is the spine of the plot.
- **The Need (the internal truth):** the psychological/moral lesson the character must learn to become whole. The Need is invisible and usually the character does not know they have it. Woody in *Toy Story* *wants* to be Andy's favorite toy again; he *needs* to learn that love isn't a zero-sum competition.
- **The Lie the character believes:** the false worldview, installed by a past wound, that the character mistakes for truth. This is the keystone concept popularized by Lisa Cron and K.M. Weiland. The Lie is *why* the character pursues the wrong Want, or pursues the right Want for the wrong reasons. Example: in *Casablanca*, Rick's Lie is "I stick my neck out for nobody" — a defensive crust over the wound of being abandoned by Ilsa in Paris.

The relationship is causal and stackable:

| Layer | Question it answers | *Casablanca* (Rick) |
|---|---|---|
| **Wound** | What happened in the past that broke them? | Ilsa abandoned him at the train station in Paris. |
| **Lie** | What false belief did the wound install? | "Caring about anything gets you hurt — I look out for me." |
| **Want** | What do they consciously chase? | To stay neutral, keep his bar, avoid the war. |
| **Need** | What must they learn to be whole? | That sacrifice for others is what gives a life meaning. |
| **Fatal flaw** | How the Lie manifests as behavior | Cynicism, isolation, performative indifference. |

**Why this works (the WHY, not the what):** the Lie creates *dramatic irony at the character level*. The audience can sense the character is wrong about themselves before the character can. That gap — between who they are and who they could be — is the source of nearly all emotional tension in character drama. We lean in because we are waiting for the moment the Lie breaks. The "fatal flaw" (Greek *hamartia*, the "missing of the mark") is simply the Lie expressed as repeated, costly behavior.

> **→ AI APPLICATION:** When you brief an LLM (Claude, GPT) to draft a character or a scene, do **not** give it adjectives ("brave, witty, haunted"). Adjectives produce generic stock characters because they describe surface, not engine. Give it the four-layer spine as named fields: `WOUND`, `LIE`, `WANT`, `NEED`. Then instruct: *"Every line of dialogue and every choice must either express the Lie or test it. The character does not know the Need exists until Act 3."* This single constraint is the difference between a model emitting a cardboard cutout and a model emitting behavior that *coheres*. Store these four fields verbatim in the character bible entry (see Part Three) so they propagate to every scene prompt.

---

### The character arc: positive, negative, flat

An **arc** is the trajectory of the character's *relationship to the Lie* across the story.

- **Positive change arc** (most common): character starts believing the Lie, suffers, and ends embracing the Truth (the Need). Rick chooses sacrifice; Woody chooses generosity; Michael Corleone's *brother* Neil — no. Most heroes' journeys are this.
- **Negative arc** (the fall): character starts with a chance at Truth and instead descends deeper into the Lie. *Michael Corleone* across *The Godfather* I–II is the canonical example: he wants to protect his family and ends destroying it, embracing the Lie that power equals safety. *Breaking Bad*'s Walter White is the modern textbook negative arc — "I did it for my family" curdles into "I did it for me. I liked it. I was good at it."
- **Flat / "steadfast" arc:** the protagonist already knows the Truth and does *not* change — instead, they *change the world around them*. The pressure of the story tests their conviction, and by holding firm they convert or defeat others. James Bond, Indiana Jones, Atticus Finch, Mad Max in *Fury Road* (Furiosa arcs; Max is the flat catalyst). Flat-arc heroes work when the *world* is the thing that needs to change, not the hero.

A common myth worth puncturing: "**every** protagonist must have a positive change arc." False. Whole successful genres (most action franchises, many procedurals) run on flat arcs precisely *because* audiences want a fixed point of competence to watch the world break against. Choose the arc deliberately based on whether your *theme* says people can change, can't change, or shouldn't have to.

> **→ AI APPLICATION:** Encode the arc as an explicit waypoint list, not a vibe. For a positive arc, give the model the Lie-strength at each act: e.g. `Act1: Lie 100% / Truth glimpsed 0%`, `Midpoint: Lie cracks, Truth 30%`, `Act3 climax: Truth chosen at maximum cost`. When generating scene-by-scene, pass the *current* Lie/Truth ratio as a parameter so each scene's behavior is calibrated to where the character *is* on the curve, not an averaged personality. This prevents the most common AI-writing failure: a character who is identically "themselves" in scene 4 and scene 40, with no felt change.

---

### The antagonist as the protagonist's mirror

Weak antagonists are obstacles. Strong antagonists are *arguments*. The most resonant villain embodies the **same thematic question** as the hero but answers it the opposite way — they are what the hero could become if the hero embraced the Lie instead of overcoming it.

- *The Dark Knight*: Batman and the Joker both believe Gotham is broken. Batman's answer: order through sacrifice and rules. Joker's answer: "the only sensible way to live in this world is without rules." They are the same diagnosis, opposite prescriptions. The film is a *debate*, and Harvey Dent is the test case.
- *Black Panther*: T'Challa and Killmonger both love Wakanda and both grieve injustice. Killmonger is the path of vengeance; T'Challa must integrate Killmonger's *valid critique* without his methods. That's why Killmonger is the best Marvel villain — he's *right* about the problem.

The principle: **the antagonist should be able to win the argument on paper.** If your villain is just "evil for evil's sake," your hero's victory means nothing, because nothing was genuinely at stake intellectually. Give the antagonist their own Want, Lie, and (crucially) a coherent justification *they* believe.

> **→ AI APPLICATION:** Build the antagonist with the *same* four-field spine as the hero, and add an explicit field: `SHARED_THEMATIC_QUESTION` and `ANTAGONIST_ANSWER` vs `PROTAGONIST_ANSWER`. Prompt: *"Write the antagonist as the protagonist's dark mirror. They must believe they are the hero of their own story. Never let them act irrationally to make the protagonist look good."* Models default to mustache-twirling villainy because training data is full of it; the mirror constraint forces a rounded opponent.

---

### Want, obstacle, stakes — the atomic drama

At any scale (story, scene, beat), drama exists only when these three are present:

1. **Want / objective** — what the character is trying to *get* or *do*, expressible as an active verb ("to confess," "to escape," "to humiliate").
2. **Obstacle** — what stands in the way (another character's opposing want, the environment, the character's own flaw).
3. **Stakes** — what it *costs* if they fail (or succeed). No stakes, no tension. Stakes must be *specific and personal*, not abstract ("the world ends" is weaker than "your daughter dies").

**Agency** is the multiplier. A protagonist with agency *drives* the plot through choices; a passive protagonist gets dragged through events. The single most common note professional readers give amateur scripts is "the protagonist is passive." Marty McFly doesn't *want* to be in 1955, but every scene he is *trying* something — agency under unwanted circumstances is the sweet spot.

---

### The "Save the Cat" beat — and the honest version

Blake Snyder's "Save the Cat" beat: early on, show the protagonist doing something *kind or clever* (literally, saving a cat) so the audience roots for them. The accurate, deeper version: the beat is not about *likability* — it's about establishing **rooting interest** and demonstrating the character's *values under no pressure*, which sets up the contrast for when pressure comes.

Be skeptical of the cult around it. Many great protagonists are *not* likable (Travis Bickle, Amy Dunne, Tony Soprano). What they have instead is one of: **competence** (we admire skill — Sherlock), **want we understand** (we share the goal), **victimhood** (someone is treating them unjustly), or **wit/charisma** (Deadpool, Jordan Belfort). "Save the cat" is *one* tool for *one* of these (sympathy). The honest principle is broader: **give the audience a reason to invest in the next 90 minutes of this person's life within the first 10.**

> **→ AI APPLICATION:** In the opening-scene prompt, specify *which* rooting-interest lever you're pulling — `ROOTING_HOOK: competence` or `: sympathy` or `: wit` — rather than vaguely asking for a "likable intro." Then generate a small *action* (not dialogue) that demonstrates it. "Show, don't tell" (below) applies hardest here.

---

### Subtext and "show, don't tell" — with real before/after

**Subtext** is the gap between what a character *says/does* and what they *mean/feel*. On-the-nose writing collapses that gap; great writing widens it and trusts the audience to read it. **"Show, don't tell"** is the same principle applied to information: dramatize behavior rather than narrate states.

| Telling (on-the-nose) | Showing (subtext) |
|---|---|
| "I'm so nervous about this interview." | She buttons her cuff, unbuttons it, buttons it again. Wipes her palm on her skirt before she reaches for the door. |
| "I don't love you anymore." | "There's leftovers in the fridge." She doesn't look up from her phone. |
| "I'm the most dangerous man in this room." (villain announces) | He's the only one who doesn't reach for a weapon when the gun goes off. |
| "Our marriage is failing." | Two toothbrushes; only one is wet. *(Pure visual — perfect for AI.)* |

Note the last row: the *richest* subtext is often **visual and prop-based**, which is exactly what AI image/video models render well. A wet toothbrush, an empty second chair, a wedding ring on the wrong hand — these are *objects that carry emotional information*. This is the bridge between literary subtext and a storyboard.

> **→ AI APPLICATION:** AI text models *love* to write on-the-nose because dialogue stating emotion is the statistical center of training data. Counter it with an explicit negative instruction: *"No character may name their own emotion. Convey all interior states through action, prop, or what is left unsaid."* For the *visual* pipeline, translate each subtext beat into a **single image-able object or gesture** and put it in your shot prompt (e.g. Veo 3.1 / Nano Banana prompt: "two toothbrushes in a glass, only one wet, morning light, shallow depth of field"). Subtext you can photograph is subtext the AI can deliver.

---

### Stock archetypes vs rounded characters

Archetypes (the Mentor, the Trickster, the Threshold Guardian — Jung via Campbell via Vogler) are *useful scaffolding*, not destinations. An archetype tells you a character's **function** in the story machine. It becomes a *stock character* (cliché) when function is all there is. It becomes a *rounded character* (E.M. Forster's term: capable of *surprising us convincingly*) when you give the archetype a contradiction.

- Stock Mentor: wise old man dispenses wisdom, dies. (Obi-Wan as written badly.)
- Rounded Mentor: a wise guide who is *also* a liar hiding what really happened to the hero's father (Obi-Wan as actually written — "from a certain point of view").

The technique: **take the archetype, then add one trait that contradicts the expectation.** A gruff bounty hunter who is tender with a child (Mando + Grogu). A brilliant detective who is socially monstrous (House, Holmes). The contradiction is what makes a character feel *real* rather than *typed*.

> **→ AI APPLICATION:** Name the archetype as a *seed* (`ARCHETYPE: Mentor`) but always pair it with `CONTRADICTION:` as a required field. Prompt the model to "honor the archetype's narrative function while undercutting its surface with the contradiction." Without the contradiction field, LLMs regress hard to the stock version, because the archetype's clichéd form is over-represented in training data.

---

## PART TWO — SCENE

### What a scene actually is: a unit where a value changes

This is the most important structural idea in the chapter, from Robert McKee's *Story*: **a scene is the smallest unit of story in which a value-charged condition turns.** A "value" is a binary an audience cares about — alive/dead, loved/unloved, free/trapped, winning/losing, hope/despair, truth/lie.

If a value does *not* change across a scene — if the character is at "losing" at the start and still "losing" at the end with nothing shifted — **it is not a scene, it is an event**, and it should probably be cut or compressed. This is McKee's brutal, clarifying test. The change can be small (from "+slightly hopeful" to "−worried") but it must occur and the audience must feel it.

| Scene | Value | Charge at open | Charge at close |
|---|---|---|---|
| *Jaws* — Brody on the beach | Safety | + (calm) | − (shark attack) |
| *The Godfather* — restaurant | Michael's innocence | + (civilian) | − (murderer) |
| *When Harry Met Sally* — diner | Their connection | neutral | + (undeniable) |

### Scene anatomy: goal, conflict, turn, button

Operationally, build every scene with four parts:

1. **Scene goal** — the POV character's *want* for this scene (an active verb). Distinct from the story-level Want; it's the local objective.
2. **Conflict** — opposition to that goal. *Every scene needs conflict.* If two characters agree and nothing opposes the goal, the scene is dead air.
3. **The turn** — the moment the value flips and the scene's direction reverses. This is the scene's reason to exist.
4. **The button** — the final line/image that "punctuates" the scene and ideally propels into the next (a question raised, a threat issued, an ironic kicker). Aaron Sorkin and the Coen brothers are masters of the button.

### The Scene–Sequel model (Dwight Swain)

Swain (*Techniques of the Selling Writer*, 1965) gives the most precise micro-architecture for prose, and it translates cleanly to screen. He alternates two units:

**SCENE (proactive — outward action):**
- **Goal** — character pursues a clear objective.
- **Conflict** — obstacles escalate.
- **Disaster** — the scene ends in a *setback or complication* (rarely clean success; success kills tension). The "yes, but…" or "no, and…" outcome.

**SEQUEL (reactive — inward processing):**
- **Reaction** — emotional fallout from the disaster.
- **Dilemma** — character faces a hard choice among bad options.
- **Decision** — character commits to a new goal → which launches the next Scene.

This creates the **causal chain**: Disaster → Reaction → Dilemma → Decision → new Goal → new Disaster. The sequel is what amateur writers omit (they cut from action to action), and its absence is *why* a fast-paced story can feel emotionally hollow — the audience never gets to *metabolize* what happened or watch the character *choose*. In film, sequels are often compressed (a single reaction shot, a quiet walk, one line of decision) but they are still *there*. The "and then… and then…" of a bad plot becomes the "therefore… but…" of a good one (the South Park "but/therefore" rule is the same idea).

| Unit | Mode | Beats | Function |
|---|---|---|---|
| **Scene** | Proactive | Goal → Conflict → Disaster | Advances plot |
| **Sequel** | Reactive | Reaction → Dilemma → Decision | Advances character + motivates next plot move |

### Entering late, leaving early ("late in, early out")

The professional rule: **start a scene as late as possible and leave as early as possible.** Enter *after* the setup, on the edge of the conflict; exit *on the turn or button*, before the energy dissipates. Skip the hellos, the sitting down, the "so, what did you want to talk about." Drop us in mid-tension and cut out the moment the value has flipped — let the next scene's context fill the gap. This is the single fastest way to make a scene feel propulsive, and it respects the audience's intelligence.

### Beats within a scene

A **beat** is the smallest unit of action/reaction — one exchange of behavior (an action and its response). Within a scene, beats are where the *action* (in the acting sense — the pursuit of a tactic) shifts. As a character's tactic to get their goal fails, they switch tactics — a new beat. A well-written scene is a *staircase of beats*, each escalating, building to the turn. Tracking beats is how you find where a scene sags (two beats doing the same job → cut one).

### Dialogue craft: dialogue as action

The central insight: **dialogue is not characters exchanging information; it is characters trying to *get something* from each other.** Every line is a *tactic* in pursuit of a want. "Nice tie" can be flirtation, mockery, a stalling tactic, or a threat, depending on what the speaker *wants*. When you write or prompt dialogue, the question is never "what would they say?" but "what are they *doing* to the other person with this line?"

- **On-the-nose dialogue** says exactly what the character means and feels. It's the death of tension. ("I'm angry at you because you betrayed me and I feel hurt.")
- **Subtextual dialogue** says one thing and means another, forcing the audience to read between lines. (The classic: a couple arguing about *the dishes* while actually fighting about *the affair*.)

Real conversation is also *oblique* — people deflect, interrupt, don't answer the question, talk past each other. Mamet and Pinter built careers on this. Compare:

> **On-the-nose:** "I'm scared you're going to leave me like everyone else has."
> **Subtext (Mamet-ish):** "You packed light." / "It's a short trip." / "Sure."

> **→ AI APPLICATION:** Give the dialogue model each character's *scene goal as a verb* and instruct it to write every line **as a tactic toward that goal**, never as a statement of feeling. Add: *"Characters may interrupt, deflect, and leave thoughts unfinished. At least one character should want something they never directly ask for."* For performance in AI video (Veo 3.1, Sora 2 in ChatGPT), keep on-screen dialogue *short* — current models render 1–2 spoken sentences per clip convincingly; long monologues drift in lip-sync and identity. Push the rest into subtext, reaction shots, and the button.

---

## PART THREE — AI APPLICATION (synthesis)

> Current-tool note (researched June 2026; AI capabilities change fast — verify model names/versions before relying on them): the dominant consistency stack is **Nano Banana Pro** (Google's Gemini-3-class image model) for stills/keyframes, **Midjourney V8.x** with **Omni Reference** (the `--cref` parameter is deprecated for V7+; roll back to `--v 6` only for strict character-only retention), and for video **Veo 3.1** ("Ingredients to Video," up to ~4 reference images, first/last-frame bridging) and **Kling 3.0** (Multi-Shot Storyboard). **Sora 2's standalone "cameo" API was confirmed shutting down March 24, 2026**, though the model remains inside ChatGPT — so do not architect a pipeline around the Sora API.

### The character bible entry (the verbal identity sheet)

The same document must do *two jobs*: drive the **writing** (the four-layer spine) AND drive **visual consistency** (the physical/wardrobe lock that every image and video prompt re-injects). AI models have no memory between generations — *every* shot prompt must re-state the identity, or the character drifts. The bible entry is your single source of truth you paste (or template-inject) into every prompt.

```yaml
character:
  name: Mara Vance
  # --- WRITING SPINE (drives dialogue, choices, arc) ---
  archetype: Reluctant Mentor
  contradiction: teaches courage but is a physical coward
  wound: watched her unit die because she froze
  lie: "If I never commit, I can never fail anyone again."
  want: to get the recruit off her base and out of her life
  need: to learn that showing up imperfectly beats not showing up
  arc: positive   # Lie 100% -> cracks at midpoint -> Truth chosen at climax
  rooting_hook: competence   # we admire her skill before we like her
  voice: clipped, deflective, dark humor; never states a feeling

  # --- VISUAL LOCK (drives image + video consistency, re-injected every prompt) ---
  visual_anchor: |
    woman, 40s, East-Asian, close-cropped grey-streaked black hair,
    deep scar through left eyebrow, weathered olive skin, sharp jaw,
    grey-green eyes, lean wiry build, 5'7"
  wardrobe: |
    faded olive field jacket, dog tags, fingerless gloves, charcoal tee
  reference_images: [mara_front.png, mara_3q.png, mara_profile.png]  # for Veo Ingredients / Omni Ref
  negative: "no makeup, no smiling, no clean clothes"
```

**Why split it this way:** the writing fields are *semantic* and go to your LLM; the visual fields are *descriptive tokens* plus *reference image filenames* and go to your image/video model. Keeping them in one file with two clearly-labeled blocks means a single character can't develop "two personalities" between your script and your visuals. The `visual_anchor` block should be **token-stable** — write it once, never paraphrase it shot to shot, because models are sensitive to wording and re-phrasing causes drift. Pair the text anchor with **2–3 reference images** (front, 3/4, profile) fed to Veo 3.1 Ingredients or Midjourney Omni Reference; text alone holds *type*, reference images hold *identity*.

### Writing scenes as value-shift units the AI can storyboard

Spec each scene as a structured object the model can both *write* and *break into shots*. The value-shift is the scene's contract; the shot list is its rendering plan.

```yaml
scene:
  id: 1.07
  location: motor pool, dusk
  pov: Mara
  value: trust            # the binary that must change
  open_charge: "-"        # Mara distrusts the recruit
  close_charge: "+"       # forced into reluctant respect
  scene_goal: "Mara wants to prove the recruit is useless and send him home"
  conflict: "recruit fixes the dead generator she couldn't"
  turn: "the lights come back on — her competence is no longer the only competence in the room"
  button: "She tosses him a wrench. 'Don't get comfortable.'"  # propels next scene
  subtext_object: "she keeps her back to him while he works"   # image-able
  late_in: "open ON the dead generator, not on greetings"
  early_out: "cut on the wrench mid-air"
  shotlist:
    - "WIDE dark motor pool, single work-lamp, Mara's silhouette [visual_anchor + wardrobe]"
    - "CU recruit's hands on the generator, grease, focused"
    - "MS lights snap on, Mara turns, grey-green eyes catch the light [visual_anchor]"
    - "OTS wrench leaves her hand toward camera — CUT"
```

Each shot line **re-injects the `visual_anchor`** (shown as `[visual_anchor]`) so identity holds across the cut — this is the operational core of AI character consistency. The `open_charge`/`close_charge` pair is McKee's value-turn made into a field the model can verify against: if your generated scene ends on the same charge it opened with, the model (or you) should flag it as a non-scene and rewrite. `late_in`/`early_out` become literal first-frame and last-frame instructions for Veo 3.1's first/last-frame bridging. The `subtext_object` is the show-don't-tell beat rendered as a single photographable choice.

Build characters as contradictions, build scenes as turns, and make the bible the one file that keeps both your *meaning* and your *faces* from drifting — that is the whole craft, compressed for a machine that forgets everything between frames.

---

### Sources

- McKee, *Story* (scene = value-change unit); Snyder, *Save the Cat!*; Swain, *Techniques of the Selling Writer* (scene/sequel); Weiland & Cron (the Lie/Wound/Want/Need framework); Forster, *Aspects of the Novel* (flat vs round); Vogler, *The Writer's Journey* (archetypes).
- Scene & sequel structure: [September C. Fawkes](https://www.septembercfawkes.com/2021/09/scene-structure-according-to-dwight-v.html), [Wikipedia: Scene and sequel](https://en.wikipedia.org/wiki/Scene_and_sequel)
- Veo 3.1 Ingredients / consistency: [Atlas Cloud](https://www.atlascloud.ai/blog/guides/how-to-use-veo-3-1-ingredients-to-video-transforming-static-photos-into-cinematic-ai-clips), [Superprompt](https://superprompt.com/blog/google-veo-3-1-update-4k-vertical-video-ingredients)
- Midjourney character reference / Omni Ref deprecation of --cref: [Midjourney docs](https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference), [prompting.systems](https://prompting.systems/blog/how-to-use-midjourney-cref-for-consistent-characters)
- Nano Banana Pro identity mechanism: [prompting.systems guide](https://prompting.systems/blog/nano-banana-pro-character-consistency-guide), [The Neural Post](https://theneuralpost.com/2026/01/28/nano-banana-vs-the-world-why-character-consistency-is-finally-solved/)
- Sora 2 cameo + API shutdown (Mar 24 2026): [AI/ML API blog](https://aimlapi.com/blog/google-veo-3-1), [Vexa Video](https://vexavideo.com/blog/sora2-shutdown-veo31-alternative)
- Kling 3.0 Multi-Shot Storyboard: [aimlapi best-of-2026](https://aimlapi.com/blog/best-ai-video-generators-2026-veo-3-1-kling-sora-2-seedance-more-compared)
