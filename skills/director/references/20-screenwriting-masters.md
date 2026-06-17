# The Screenwriting Masters & The Meta-Framework

You do not have a craft problem. You have a *story* problem. AI now renders any image you can describe; the bottleneck moved upstream, to the script. And the script is where every theorist below has been fighting the same war for 2,300 years. The trap for an advanced, AI-native reader is to treat these names as interchangeable buzzwords ("just use Save the Cat") or, worse, to apply all of them at once and produce a bloated, theory-clotted mess. This chapter does the opposite: it isolates each master's *one real idea*, names what it is genuinely best for, and — critically — names its **blind spot**, so you know when to put it down. Then it reconciles all of them into a single operating model.

This chapter is a survey and a synthesis. It deliberately does **not** re-derive the mechanics already taught elsewhere: 3-act / Hero's Journey / Harmon's Story Circle / Save the Cat's 15 beats / McKee's value shifts live in `01-story-structure.md`; Pixar's 22 rules and the Story Spine in `02-pixar-22-rules.md`; flaw/lie/arc and scene-as-value-change in `03-character-and-scene-craft.md`; the gated production pipeline in `19-the-grilling-workflow.md`. Here we go up a level: *who said what, why, and which tool to reach for.*

---

## Aristotle — *Poetics* (c. 335 BCE): plot is the soul

**The big idea.** Aristotle analyzed Greek tragedy and concluded that *mythos* (the structure of the incidents — what we now call plot) is "the first principle, and as it were the soul of a tragedy." His ranking is blunt and counterintuitive to modern, character-obsessed sensibilities: **plot over character.** A tragedy can exist without strong character but never without action — "without action there cannot be a tragedy; there may be one without character." Character, for Aristotle, is revealed *by what a person does under pressure*, not by interiority.

Three of his terms are load-bearing for everything that follows:
- **Peripeteia** — a *reversal*, where an action produces the opposite of its intended result. (Oedipus sends for the messenger to *reassure* himself; the messenger's news *destroys* him.)
- **Anagnorisis** — a *recognition*, a shift from ignorance to knowledge, often paired with the reversal. (Oedipus recognizes that *he* is the murderer he hunts.)
- **Catharsis** — the audience's purgation of *pity and fear*, the emotional payoff a tragedy exists to deliver.

He also demands the **unity of action**: every incident must be causally necessary, so that "if any one of them is displaced or removed, the whole will be disjointed and disturbed." A complex plot (his preference) is one that turns on a peripeteia, an anagnorisis, or both.

**Best for:** diagnosing whether your story has a *spine of cause and effect* at all, and whether your climax lands a genuine reversal-plus-recognition (the most reliably satisfying shape in existence).

**Blind spot:** it is a theory of *tragedy and structure*, not of psychology, theme-as-argument, or the slow interior arc modern audiences crave. Aristotle would not help you write a quiet character study.

> **→ SHORT-FORM.** The peripeteia/anagnorisis pair is the most compressible dramatic device there is — it *is* the twist. A 20-second ad can be one reversal: a man confidently does X, X backfires, he realizes Y. Don't try to dramatize a full tragedy in a teaser; steal *one* reversal and one recognition and stop. Unity of action in short form means: if a shot doesn't cause the next, cut it.

> **→ AI APPLICATION.** "Unity of action" is the single best lint rule for an LLM story-assistant. After it drafts beats, prompt: *"For each beat, name the prior beat that causes it. Flag any beat with no cause."* Beats with no cause are the AI's signature failure mode — pretty, disconnected tableaux. This is also why the **but/therefore** chain (see `04`) works: it operationalizes Aristotle.

---

## Lajos Egri — *The Art of Dramatic Writing* (1946): start from the premise

**The big idea.** Egri's seed is the **premise** — a single sentence asserting a cause-and-effect *moral proposition* that the whole play will prove. His canonical example: *"Great love defies even death."* A premise names a quality (great love), a conflict, and an end (defeats death). Egri insists you cannot write well without one: it is your thesis, and the play is the argument. (Note: what Egri calls *premise*, others call *theme* or *controlling idea* — see McKee below; the overlap is real and intentional.)

His second contribution is **character "bone structure"**: a character must be conceived in three dimensions — **physiology** (body, age, health), **sociology** (class, job, upbringing, religion), and **psychology** (ambitions, frustrations, temperament, the inner life that the first two produce). Flat characters fail because the writer skipped one dimension.

Third: **orchestration of conflict.** A drama needs opponents who are *forcefully opposed* and roughly matched — "unbreakable" wills pushing against each other. A weak antagonist produces a weak play, because conflict cannot escalate.

**Best for:** the *foundation* — knowing what your story is arguing and building characters with enough interior pressure to drive it.

**Blind spot:** Egri is pre-cinema and proudly didactic; "prove the premise" can tip into preachy, schematic writing if the argument shows through the seams. He is light on scene-level and visual craft.

> **→ SHORT-FORM.** A teaser doesn't need a full bone structure for every face — it needs *one* legible dimension per character (the rumpled detective; the polished CEO). Egri's gift to short form is the premise: a 60-second piece with no implicit proposition feels like noise. Pick the proposition, render its proof in three beats.

> **→ AI APPLICATION.** Force the model to write the premise *first*, as one cause-effect sentence, then check every beat against it. Egri's three dimensions also make a clean character-sheet schema for prompt consistency: physiology feeds the *image* prompt (see `16-ai-character-consistency.md`); psychology feeds the *behavior*.

---

## Syd Field — *Screenplay* (1979): the paradigm made structure teachable

**The big idea.** Field didn't invent three acts; he *measured* them and gave Hollywood a shared map called **the Paradigm**: Act I **Setup** (~first 25%), Act II **Confrontation** (~middle 50%), Act III **Resolution** (~last 25%), with the acts hinged by two **plot points** — events that "spin the action around into another direction." Plot Point 1 ends Act I; Plot Point 2 ends Act II. He later added the **Midpoint** (a major event at the center that re-energizes the sagging middle) and **pinch points** between. The genius was *positional*: Field told you roughly *where on the page* each turn should fall.

**Best for:** pacing and diagnosis. If your middle drags, Field tells you you're probably missing a midpoint. It's the lingua franca of the writers' room.

**Blind spot:** the paradigm is descriptive turned prescriptive. Treated as a template it produces the "everything happens on schedule" feel; it says little about *why* a character changes — only *when* the plot should turn. (Truby's whole project is a revolt against exactly this.)

> **→ SHORT-FORM.** Field scales down cleanly because it's proportional. A 90-second film: incident by ~9s, midpoint by ~45s, PP2 by ~67s, climax by ~80s (this exact mapping is in `01`). The danger is forcing *all* the furniture (pinch points, B-story) into 90 seconds — don't. Keep the two plot points and the midpoint; drop the rest.

> **→ AI APPLICATION.** Field's percentages are a gift to a runtime-aware generator: convert act proportions to timecodes, assign one beat per turn, and you have a shot list with a built-in pacing check. But for *anything under ~2 minutes*, prefer Harmon's circle (see synthesis) — Field's machinery has more moving parts than a short can carry.

---

## Robert McKee — *Story* (1997): the gap, and what the ending proves

**The big idea.** McKee's most quoted concept is the **controlling idea**: a single sentence of *value plus cause* that the climax proves — e.g. *"Justice prevails when the ordinary person fights the system."* You find it by asking: as a result of the climactic action, what value (positive or negative) enters the protagonist's world, and what *caused* it? Everything in the film argues for that sentence.

His most *mechanically useful* idea is **the gap**: "the substance of story" is the gap that opens between what a character *expects* when they act and what *actually* happens. A character takes a minimum, conservative action expecting a result; reality returns something worse; the gap forces a larger, riskier action; the gap widens again. Story is the staircase of widening gaps. (This is Aristotle's peripeteia, generalized into the engine of every scene.)

Supporting tools: the **inciting incident** (the event that knocks life out of balance and raises the central dramatic question); **turning points** (each scene must turn a value charge from + to − or back, *irreversibly* — see `01` and `03`); **exposition as ammunition** (never dump backstory; *dole it out as weapons* characters use against each other, so information arrives charged with conflict — the idea is in *Story*, but McKee sharpens the "ammunition" phrasing in his later *Dialogue: The Art of Verbal Action*, 2016); the **quest** (the spine: a protagonist pursues an object of desire against forces of antagonism); and the **negation of the negation** — the deepest point a story can reach, where the value isn't merely lost (tyranny vs. freedom) but corrupted into something *worse than its simple opposite* (e.g. not just slavery, but "slavery experienced as freedom" / self-deception). The "good ↔ bad ↔ negation of the negation" progression is how you measure whether your stakes go all the way down.

**Best for:** depth and rigor at feature length — meaning, escalation, the moral floor of the antagonist's world.

**Blind spot:** McKee is *heavy*. The full apparatus (negation of the negation, the four levels of conflict) is overkill for anything short, and over-applied it can intellectualize a writer into paralysis. It's a feature-film instrument.

> **→ SHORT-FORM.** Use exactly two McKee tools and ignore the rest: the **controlling idea** (so the piece means something) and **the gap** (so each of your handful of shots escalates — expectation, worse reality, repeat). Skip the negation of the negation; a teaser has no room to reach the moral floor.

> **→ AI APPLICATION.** "Exposition as ammunition" is a precise anti-pattern detector. LLMs *love* to open scenes with characters explaining the situation to each other. Prompt: *"Rewrite any line whose only job is to inform the audience so that it is instead a weapon one character uses to get something from another."* And demand a value-charge (`open → close`) per scene — it makes McKee's "the gap" machine-checkable.

---

## John Truby — *The Anatomy of Story* (2007): organic structure, not templates

**The big idea.** Truby explicitly **rejects the three-act template** as mechanical "arbitrarily imposed from without," and replaces it with structure that grows *organically* from a specific story. His seed is the **designing principle** — the single deep, original line that organizes the whole story and makes *this* story unlike any other (e.g. *The Godfather*: "use the classic fairy-tale strategy of showing how the youngest of three sons becomes the new 'king'" — the corruption-of-power theme, a force for good becoming the very evil it once fought, is the story's moral arc *layered over* that principle, not the principle itself). The designing principle is more specific than a premise; it's the *unique strategy* of the telling.

Truby's spine is the **seven key steps**, which he argues are organic — they're the steps any human works through to solve a life problem, not a grid stamped on top:
1. **Weakness and need** (a moral *and* psychological lack the hero doesn't yet see)
2. **Desire** (the concrete external goal)
3. **Opponent** (who wants the same goal — competition for one thing, not a generic "bad guy")
4. **Plan** (the strategy to defeat the opponent and get the desire)
5. **Battle** (the final conflict)
6. **Self-revelation** (the hero learns the truth about themselves — the psychological and moral payoff)
7. **New equilibrium** (life at a new, higher or lower level)

These seven sit inside his fuller **22 building blocks** (subtitle: *22 Steps to Becoming a Master Storyteller*). Two more Truby signatures: the **moral argument** — story as the author's *argument about how to live*, made by showing the hero's moral choices and their consequences, not by sermonizing; and the **character web** — characters defined *in relation* to each other (hero, opponent, allies, fake-ally opponents) so each pressures the hero's weakness from a different angle.

**Best for:** *character-driven* stories where the change is internal and moral; building an antagonist who is the hero's true mirror; escaping formula.

**Blind spot:** the 22 steps are a lot to hold, and "organic" can become an excuse for shapelessness in inexperienced hands. Truby is weaker on the *positional* pacing discipline that Field nails.

> **→ SHORT-FORM.** Truby's *seven* steps compress beautifully — they are almost the same shape as Harmon's circle (see synthesis). For a short, use a **Truby-lite**: weakness/need → desire → opponent → one failed plan → battle → self-revelation. Six beats, six shots, one arc. Skip the 22; skip the full character web (a short has room for one opponent).

> **→ AI APPLICATION.** This is the recommended default *content* model for an AI shorts assistant, paired with Harmon's circle as the *positional* skeleton. The 7 steps map cleanly to fields in a JSON beat sheet, and "weakness/need ≠ desire" is the exact distinction LLMs flatten — they collapse want and need into one goal. Force them apart explicitly: *"State the external desire and the deeper internal need as two different sentences; the ending must satisfy the need, not the desire."*

---

## Christopher Booker — *The Seven Basic Plots* (2004): the deep archetypes

**The big idea.** After 34 years of writing, Booker argued (through a Jungian lens) that all stories reduce to **seven basic plots**:
1. **Overcoming the Monster** — hero confronts and defeats a threatening evil (*Jaws*, *Star Wars*).
2. **Rags to Riches** — an unremarkable figure realizes hidden greatness (*Cinderella*, *Slumdog Millionaire*).
3. **The Quest** — a journey toward a distant, vital goal (*The Lord of the Rings*).
4. **Voyage and Return** — hero enters a strange world, then escapes back home, changed (*Alice in Wonderland*, *The Wizard of Oz*).
5. **Comedy** — confusion and miscommunication resolved into harmony/union (light tone, not just "funny").
6. **Tragedy** — overreaching protagonist falls (*Macbeth*).
7. **Rebirth** — a dark figure is redeemed (*A Christmas Carol*).
(Booker also floats two extras he treats as incomplete or modern: **Rebellion** and **Mystery**.)

**Best for:** *fast genre orientation*. Naming the plot tells you instantly what the audience already expects and emotionally craves.

**Blind spot:** it's descriptive taxonomy, not a writing method — knowing you're writing "Rebirth" doesn't tell you how to write a *scene*. (And the book's prescriptive, moralizing second half is widely criticized.)

> **→ SHORT-FORM.** Hugely useful as a *one-word brief*. "This teaser is a 30-second Overcoming the Monster" instantly fixes tone, antagonist, and the shape of the win. Pick the plot before you write a word.

> **→ AI APPLICATION.** A perfect *classifier and retrieval key*. Tag the concept with one of seven plots; the system then pulls genre conventions, the obligatory beats, and reference loglines for that archetype. It's the cheapest, highest-leverage piece of story metadata an AI pipeline can store.

---

## Campbell / Vogler & Snyder — the mythic and the commercial (brief)

**Joseph Campbell** (*The Hero with a Thousand Faces*, 1949) described the **monomyth** — the recurring cross-cultural Hero's Journey (Departure → Initiation → Return). **Christopher Vogler** (*The Writer's Journey*, 1992) adapted it into a 12-stage screenwriting tool. The mechanics live in `01-story-structure.md`; what matters here is the *idea*: a single deep pattern of leaving the known, being transformed in the unknown, and returning with a boon. **Blind spot:** mythic scope fits epics and fantasy; force it onto small, realist stories and it bloats.

**Blake Snyder** (*Save the Cat!*, 2005) gave Hollywood the 15-beat sheet (in `01`), but his *underappreciated* contribution is **genre**. Snyder argued films don't sort by Hollywood's marketing labels but into **10 story genres** defined by their internal problem — e.g. *Monster in the House*, *Golden Fleece* (a quest/road story), *Dude with a Problem*, *Rites of Passage*, *Buddy Love*, *Whydunit*. His point: every genre carries *audience expectations you must satisfy*, and the fastest way to fix a broken script is to ask "what genre is this actually, and am I delivering its promises?" **Blind spot:** the 15 beats, slavishly applied, are the single biggest source of the "every movie feels the same" complaint — a diagnostic grid mistaken for a recipe.

> **→ AI APPLICATION.** Snyder's genre lens and Booker's seven plots together form a two-axis tag (archetype × commercial-genre) that lets an assistant load the right *conventions* before writing a single beat.

---

## John Yorke — *Into the Woods* (2013): change is the essence, and it's fractal

**The big idea.** Yorke synthesizes everyone above into a **five-act structure** and argues two things. First, **change** is the irreducible essence of story: a character wants something, is put through the wringer pursuing it, and is changed — the satisfaction lives in that change. Stories dramatize how minds learn: *thesis → antithesis → synthesis* (we encounter the new, resist it, integrate it). Second — his most original claim — structure is **fractal**: the same five-act shape (and the same want-vs-need engine) repeats at every scale — the beat, the scene, the act, the whole film all share one shape. Zoom in or out and you see the same curve. Yorke also sharpens the **want vs. need** distinction (the conscious external goal vs. the unconscious thing the character actually requires to be whole) that underlies modern character arc.

**Best for:** *seeing the unity* behind the competing frameworks, and for nesting structure — making a single scene satisfying because it has its own miniature arc.

**Blind spot:** five acts is one more abstraction layer; for practical drafting many writers find three or Harmon's eight more tactile. Yorke is a brilliant *unifier*, less a step-by-step recipe.

> **→ SHORT-FORM.** The fractal insight is *the* short-form principle: a 15-second clip should still have a beginning/middle/end and a tiny change, because the fractal goes all the way down. A teaser is one scene-sized fractal of the feature.

> **→ AI APPLICATION.** Fractality justifies recursive generation: generate the global arc, then generate each beat *as its own mini-arc* with the same prompt template. And want-vs-need becomes a hard schema constraint (two separate fields), the same fix Truby demands.

---

## Shawn Coyne — *The Story Grid* (2015): the editor's lens

**The big idea.** Coyne, a veteran editor, built a *diagnostic* system from the editor's chair. Two pillars. First, the **Five Commandments of Storytelling** — the unit every working story-chunk must contain *at every scale* (scene, sequence, act, global story): **Inciting Incident → Progressive Complication(s) → Crisis → Climax → Resolution.** The **Crisis** is the keystone Coyne stresses: a genuine *dilemma* (a "best bad choice" or an "irreconcilable goods") that forces a real decision; the Climax is the *answer* to that crisis question. (Coyne notes the unmarked sixth element, the **turning point**, the complication that triggers the crisis.) This is explicitly fractal — same five parts in a scene as in the whole book. Second, **obligatory scenes & conventions**: every **genre** makes promises, and audiences will feel cheated if you skip the scenes that genre *requires* (a crime story must have the detective expose the criminal; a love story must have the lovers' first meeting and the proof of love). Know your genre's must-have scenes, then deliver them with a fresh twist.

**Best for:** *editing and diagnosis* — finding the broken scene. If a scene feels flat, run the five commandments on it; one is almost always missing (usually the crisis or the value turn).

**Blind spot:** Story Grid is an *analysis/revision* tool more than a generative one — it tells you what's wrong far better than it conjures something from nothing.

> **→ SHORT-FORM.** The five commandments are the best *scene-level QA pass* for a short. Each shot-cluster, however tiny, should have a provocation, an escalation, a hard choice, an action, and a new state. The "crisis as real dilemma" is what separates a dramatic short from a pretty montage.

> **→ AI APPLICATION.** The single most powerful *verifier* in this whole chapter. Have the LLM generate freely, then run a Story-Grid pass: *"For this scene, name the inciting incident, the progressive complication, the crisis (state the dilemma as two bad options), the climax, and the resolution value. If any is missing or weak, rewrite."* It converts vibes into a checklist. The genre-conventions lens also seeds a "must-include scenes" list per project.

---

## The Synthesis: they're all describing one elephant

Strip the vocabularies and every theorist is mapping the same underlying motion:

> **A flawed protagonist pursues a WANT (a concrete external desire), is forced by escalating OPPOSITION to confront a deeper NEED (the thing they actually lack), and CHANGES — or fails to, which is tragedy.**

Watch the same machine wear different names across the table:

| Concept (the one elephant) | Aristotle | Egri | Field | McKee | Truby | Yorke | Coyne |
|---|---|---|---|---|---|---|---|
| The flaw / what's lacking | (character revealed by action) | psychological dimension | — | the inner gap | **weakness & need** | the unfinished self | the value to be tested |
| The external goal | the agent's intent | desire in the premise | the dramatic need | object of desire / **quest** | **desire** | **want** | the global want |
| The deeper truth | — (implicit) | psychology | — | self-knowledge | **need / self-revelation** | **need** | revealed via crisis |
| The engine of escalation | **peripeteia** | orchestrated conflict | rising action | **the gap** | opponent + plan + battle | conflict of desires | **progressive complication** |
| The hinge of change | recognition (**anagnorisis**) | proving the premise | plot points / midpoint | turning point | **self-revelation** | thesis→antithesis→synthesis | **crisis → climax** |
| What it all proves | — | **premise** | — | **controlling idea** | **moral argument** | the change | genre's value at stake |

This is why arguing "Truby vs. Snyder" is mostly a category error. They emphasize different faces of one solid: Aristotle and Coyne stress the *mechanics of the unit*; Egri, McKee, and Truby stress *meaning and character*; Field stresses *position*; Booker and Snyder stress *archetype/genre*; Yorke stresses the *unifying principle and its fractality*. A complete storyteller holds all faces, but **deploys one at a time, for the job it's best at.**

### The master comparison table

| Theorist | One-line big idea | Best for | Blind spot |
|---|---|---|---|
| **Aristotle** | Plot is the soul; reversal + recognition produce catharsis. | Cause-and-effect spine; a climax that truly turns. | Says nothing about psychology or slow interior arcs. |
| **Egri** | Start from a premise; build characters in three dimensions; orchestrate opposed wills. | Foundations: thesis + driven characters. | Can preach; pre-cinema, light on visual craft. |
| **Field** | Three acts, two plot points, a midpoint — at fixed proportions. | Pacing diagnosis; a shared map. | Template-thinking; explains *when*, not *why*. |
| **McKee** | The gap between expectation and result, proving a controlling idea. | Feature-length depth, escalation, meaning. | Heavy apparatus; over-applies to short content. |
| **Truby** | Organic 7-step growth from a designing principle and moral argument. | Character-driven internal change; mirror-opponent. | 22 steps overwhelm; weak on positional pacing. |
| **Booker** | All stories reduce to seven basic plots. | Instant genre/archetype orientation. | Taxonomy, not a method; moralizing second half. |
| **Campbell / Vogler** | The monomyth: depart, transform, return with a boon. | Myth, fantasy, epic, identity journeys. | Bloats small, realist stories. |
| **Snyder** | 15 beats + 10 internal *genres* with audience promises. | Commercial structure; genre expectations. | Rote application → sameness. |
| **Yorke** | Change is the essence, and structure is fractal (want vs. need). | Seeing the unity; nesting arcs at every scale. | One more abstraction layer; not step-by-step. |
| **Coyne** | Five commandments per unit; deliver genre's obligatory scenes. | Editing/diagnosis; finding the broken scene. | Analytic, not generative. |

### Which framework should an AI assistant default to?

**Default to Harmon's Story Circle (positional skeleton) + a Truby-lite 7-step (content engine), verified by Coyne's Five Commandments — and reserve full McKee for the rare feature.** The reasoning is mechanical, not aesthetic:

- **Harmon over Field** for shorts because the circle's 8 steps are *self-balancing* and map to ~8 shots at the native single-clip length of today's models (see `01`); Field's pinch points and B-story are dead weight under two minutes.
- **Truby-lite over full McKee** because McKee's power tools (negation of the negation, four levels of conflict) require runtime a short doesn't have, and they tempt the model into talky, over-explained micro-films — the #1 failure when feature theory is poured into 60 seconds. Truby's seven steps give you *internal change* (the thing AI scripts most lack) in six checkable fields.
- **Coyne as the verifier, not the generator.** Generate with Harmon+Truby, then run the Five Commandments as a lint pass on each scene. This split — *generate organically, verify mechanically* — is the architecture of the grilling workflow in `19-the-grilling-workflow.md`.
- **Booker + Snyder as metadata.** Tag every concept with one of the seven plots and one Snyder genre *before* drafting, so the assistant loads the right conventions and obligatory scenes up front.

The non-negotiable schema constraint across all of them: **want ≠ need, stated as two separate sentences, and the ending must satisfy the need.** Every master above converges on this distinction, and it is precisely the one an LLM collapses by default. Enforce it and most of the storytelling problem solves itself.

---

## Sources

- Aristotle, *Poetics* — overview, *mythos*, peripeteia, anagnorisis, catharsis, unity of action: [Poetics (Aristotle), Wikipedia](https://en.wikipedia.org/wiki/Poetics_(Aristotle)); [SparkNotes: Aristotle, Poetics](https://www.sparknotes.com/philosophy/aristotle/section11/)
- Lajos Egri, *The Art of Dramatic Writing* — premise, three-dimensional character / bone structure, orchestration: [Notes on The Art of Dramatic Writing (Brian Lee, Medium)](https://medium.com/@brianpatricklee/notes-on-the-art-of-dramatic-writing-by-lajos-egri-written-1945-eb7a690ebf95); [Neil Oseman: The Art of Dramatic Writing](https://neiloseman.com/the-art-of-dramatic-writing-by-lajos-egri/)
- Syd Field, *Screenplay* — the Paradigm, plot points, midpoint, pinch points: [Arc Studio Blog: Syd Field's Paradigm](https://www.arcstudiopro.com/blog/syd-fields-paradigm); [How-to-Write-a-Book-Now: Syd Field on structure](https://www.how-to-write-a-book-now.com/Syd-Field.html)
- Robert McKee, *Story* — controlling idea, the gap, inciting incident, turning points, exposition as ammunition (phrasing sharpened in McKee's *Dialogue: The Art of Verbal Action*, 2016), negation of the negation: [McKee // Story (Andrew Kortina notes)](https://kortina.nyc/notes/mckee--story/); [Story and the Expectation Gap (Emily Short)](https://emshort.blog/2019/02/05/story-robert-mckee/); [Exposition as Ammunition — McKee, *Dialogue* (Medium)](https://medium.com/@pirangy/exposition-as-ammunition-robert-mckee-dialogue-the-art-of-verbal-action-for-the-page-stage-and-e9b38a4d2361)
- John Truby, *The Anatomy of Story* — designing principle, seven key steps, 22 steps, moral argument, character web, rejecting three-act: [Truby Writers Studio: The Anatomy of Story](https://truby.com/the-anatomy-of-story/); [The Anatomy of Story (Emily Short)](https://emshort.blog/2019/04/02/the-anatomy-of-a-story-john-truby/); [Be a Brilliant Writer: 22 Steps](https://www.beabrilliantwriter.com/anatomy-of-story-truby/)
- Christopher Booker, *The Seven Basic Plots* — the seven plots (+ Rebellion, Mystery): [The Seven Basic Plots, Wikipedia](https://en.wikipedia.org/wiki/The_Seven_Basic_Plots); [ChangingMinds: Booker's Seven Basic Plots](http://www.changingminds.org/disciplines/storytelling/plots/booker_plots/booker_plots.htm)
- Joseph Campbell / Christopher Vogler — monomyth / Writer's Journey: [The Hero with a Thousand Faces, Wikipedia](https://en.wikipedia.org/wiki/The_Hero_with_a_Thousand_Faces); [The Writer's Journey, Wikipedia](https://en.wikipedia.org/wiki/The_Writer%27s_Journey:_Mythic_Structure_for_Writers)
- Blake Snyder, *Save the Cat!* — the 10 genres: [Save the Cat! Genres overview](https://savethecat.com/genres)
- John Yorke, *Into the Woods* — five-act structure, change, fractal structure, want vs. need: [John Yorke Story: Five-Act Structure](https://www.johnyorkestory.com/five-act-structure/); [Arc Studio Blog: Roadmap of Change](https://www.arcstudiopro.com/blog/roadmap-of-change-john-yorke)
- Shawn Coyne, *The Story Grid* — Five Commandments, obligatory scenes & conventions: [Story Grid: The 5 Commandments of Storytelling (Revisited)](https://storygrid.com/5-commandments-storytelling-revisited/); [Story Grid Writing Guide (iWrity)](https://www.iwrity.com/writing-story-grid-guide)
