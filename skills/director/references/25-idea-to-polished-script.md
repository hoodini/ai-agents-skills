# From Idea to Polished Script — Process & Formats

Most aspiring writers think the job is "having an idea and typing it up." That misconception is the single biggest reason scripts fail: they treat writing as a *one-pass* act of inspiration when it is actually a *multi-pass* act of engineering. This chapter is the assembly line. It walks the artifacts in the exact order a professional produces them — idea → logline → premise → treatment → outline/beat sheet → first draft → rewrite → table read → formatted screenplay — and then pivots to the formats that actually matter for AI video: the shooting script and the two-column A/V script.

The reason this chapter is the most useful in the wing for an AI-native reader is simple. You can prompt a video model in thirty seconds. You cannot prompt your way out of a story that was never engineered. The artifacts below are the engineering. Each one is a *checkpoint* that catches a class of failure before it metastasizes into a finished, expensive, unwatchable film.

A note on why the order is fixed: each artifact is *cheaper to fix than the next one down*. Changing a logline costs one sentence. Changing a beat sheet costs an afternoon. Changing a first draft costs a week. Changing a finished, voiced, AI-rendered film costs your weekend and your render credits. The whole pipeline is a strategy for **front-loading the cheap edits** so the expensive ones never happen. (Chapter 19, `19-the-grilling-workflow.md`, turns this exact order into a gated, adversarial pipeline; chapter 27 turns it into a state machine an LLM walks.)

---

## 1. The Idea — the "what if"

An idea is not a plot, a theme, or a character. It is a **destabilizing question** — a "what if" that takes a stable world and pokes it. *What if a shark stalked a beach town that refused to close?* *What if your memories could be erased after a breakup?* *What if toys were secretly alive and terrified of being replaced?*

The test of a real idea versus a non-idea: **does it imply conflict and a question the audience wants answered?** "A movie about friendship" is a topic, not an idea — nothing is destabilized, nothing is asked. "What if your best friend was the one framing you for murder?" destabilizes (trust → threat) and asks (will he find out in time?). Topics describe; ideas *provoke*.

Capture ideas as questions, not statements. The interrogative form forces the conflict to the surface and makes the next step — the logline — almost write itself.

> **→ SHORT-FORM.** For a 15–90s teaser or ad, the "what if" is even more important *and* more constrained: it must be resolvable (or sharply suspendable) in seconds. "What if the thing you trust most is lying to you?" is a perfect short-form engine — it sets a single hook (see `04-engagement-psychology-hooks.md`) without promising a three-act payoff you don't have time to deliver. The trap is choosing a "what if" that *needs* a feature to resolve; you'll end up with a bloated, talky micro-film that explains instead of detonates.

> **→ AI APPLICATION.** When an LLM story-assistant receives a vague brief ("make a video about our new app"), its first job is to convert the topic into 3–5 competing "what if" questions and force a choice. This is the cheapest decision in the pipeline and the highest-leverage. Generate ideas as questions, present them as a menu, commit to one before writing a single beat.

---

## 2. The Logline — the contract

The **logline** is one or two sentences that sell the whole film. It is the most compressed, highest-stakes artifact you will write, because everyone downstream — financiers, collaborators, and (for our purposes) the AI pipeline — uses it as the controlling spec. A workhorse formula:

> **A [flawed protagonist] must [specific goal] before [stakes / ticking clock], or else [consequence] — but [the ironic obstacle].**

Example (*Jaws*): *A water-fearing sheriff must hunt and kill a man-eating great white before it devours more swimmers and destroys the town's economy — even though the town won't let him close the beach.* Example (*The Social Network*, as written in `01-story-structure.md`): *When he's dumped by his girlfriend, a brilliant, resentful Harvard student builds the website that makes him the world's youngest billionaire — and costs him every friend he has.*

### The four things a logline must do (Blake Snyder)

In *Save the Cat!*, Blake Snyder argues a sellable logline must satisfy four requirements. Get these right and the logline is the only pitch you'll ever need:

1. **Irony.** The most important ingredient. The premise should contain a built-in contradiction — a "social" network that destroys its creator's friendships; a hitman who can't kill; a wedding planner who can't find love. Irony is what makes a logline *bloom* instead of sit flat.
2. **A compelling mental picture.** When someone hears it, a whole movie should appear in their mind, usually including a time frame. If they have to ask "wait, what kind of movie is this?", the picture isn't there.
3. **Audience and cost.** The logline should signal tone, target audience, and a sense of scale/budget, so a buyer knows whether it can make money. (For us: it tells the pipeline whether we're making a tense thriller teaser or a warm brand spot — which cascades into shot, music, and pacing choices.)
4. **A killer title.** A title that "says what it is" cleverly. The one-two punch of logline + title is the unit that sells.

Snyder also stresses that the protagonist's goal should rest on a **primal stake** — survival, love, protecting family, status, revenge. Primal goals are universally legible; abstract goals ("achieve self-actualization") are not.

### Stress-testing a logline

Run every logline through this gauntlet before you write another word:

- **Is there irony?** No contradiction → likely a weak premise (the lesson from `01-story-structure.md`).
- **Can you see it?** Read it to someone; if no mental picture forms, it's too abstract.
- **Is the protagonist *active*?** "A man learns his wife is a spy" is passive (things happen *to* him). "A man must out-spy his spy wife before she completes her mission" is active.
- **Are the stakes concrete and primal?** "Or else everything changes" is a non-stake. "Or else the town goes bankrupt and more children die" is a stake.
- **Is there a clock or pressure?** Not mandatory, but pressure ("before the deal closes," "before sundown") converts interest into urgency.

> **→ SHORT-FORM.** For a teaser, the logline *is* the script's skeleton. You often won't write a separate treatment — you'll go logline → A/V script. Compress the formula to its irony plus its mental picture: "The AI that learned to lie — and the one person who can prove it." That single line is enough to spec a 45-second piece.

> **→ AI APPLICATION.** The logline is the LLM's primary control surface. Lock it as a structured object (`protagonist`, `goal`, `stakes`, `clock`, `irony`, `tone`, `title`) and *refuse to proceed* until each field is non-empty and survives the stress-test. Every later artifact must be checkable against it. If a generated beat doesn't serve the logline's goal/stakes/irony, it's a darling to kill (see §7).

---

## 3. The Premise / Controlling Idea

The **premise** is the causal engine — the one sentence that makes the story feel inevitable rather than arbitrary. The **controlling idea** (Robert McKee's term, detailed in `01-story-structure.md`) is the *meaning the ending proves*, stated as **value + cause**: not "love," but "Love endures when we stop trying to control it," or its cynical inversion "Obsession destroys us when we let it override reason."

Two relatives worth naming precisely, because writers conflate them:

- **Lajos Egri's "premise"** (*The Art of Dramatic Writing*, 1946) is explicitly a cause-and-effect *moral proposition* — e.g., "Great love defies even death" (his reading of *Romeo and Juliet*). Egri insists every play proves one premise and that the premise dictates character and structure.
- **John Truby's "designing principle"** (*The Anatomy of Story*) is different: it's the single organizing *strategy* that gives the story its unique shape — e.g., Truby's designing principle for *The Godfather* is "use the classic fairy-tale strategy of showing how the youngest of three sons becomes the new 'king.'" It's the *how* of the telling, not the moral *what*. (Beware the popular line "a good man becomes the thing he set out to destroy" — that's a fine *controlling idea*, but it is **not** Truby's designing principle; see [21-theme-premise-moral-argument.md](21-theme-premise-moral-argument.md).)

You don't need all three labels. You need one sentence of meaning (controlling idea) and one sentence of organizing strategy (designing principle). Together they keep the rewrite honest: every scene either advances the strategy or proves the meaning, or it's cut.

> **→ SHORT-FORM.** A teaser rarely *proves* a controlling idea — there's no time for an ending that earns a thesis. Instead it *promises* one. Pick the value (trust, fear, hope, freedom) and let the visuals charge it. The designing principle becomes the format choice itself: "a countdown," "a single unbroken reveal," "a before/after."

> **→ AI APPLICATION.** Store the controlling idea as a one-line invariant the LLM checks the final cut against ("Does the last beat land on the value this film promised?"). It's the cheapest theme-pass guardrail available.

---

## 4. The Treatment / Synopsis

A **treatment** is the story told as *prose*, present tense, no formatting — typically 1–5 pages (a full studio treatment can run longer), reading like a short story with the dramatic beats showing. Its job is to prove the story *works as a story* before you commit to scene-by-scene labor. You read a treatment and feel the build, the turns, the payoff — or you feel the sag, which is exactly what you want to find here and not in the draft.

A treatment surfaces a specific failure the beat sheet hides: **emotional flatness**. A beat sheet can be structurally perfect and still feel like a spreadsheet. Prose forces you to write the *experience* of watching, which exposes where the audience would get bored.

> **→ SHORT-FORM.** Usually skipped. A 60-second piece's "treatment" is a single paragraph: "We open on X. Tension builds through Y. The turn is Z. We button on the CTA." If you can't write that paragraph compellingly, the piece isn't ready.

> **→ AI APPLICATION.** The treatment is the LLM's "does this hold together emotionally?" checkpoint. Have it write the prose synopsis *and then critique its own sag points* before generating the beat sheet — a cheaper place to find the boring middle than after rendering.

---

## 5. The Outline / Beat Sheet / Step Outline

Now you convert prose into a **structured plan**. Three granularities, increasingly fine:

- **Outline** — major movements (acts, sequences). Coarse.
- **Beat sheet** — the named structural beats. Use Blake Snyder's 15-beat sheet or Dan Harmon's 8-step Story Circle (both in `01-story-structure.md`). This is where you place Catalyst, Midpoint, All Is Lost, Finale — and check that each *turns a value* per McKee.
- **Step outline** — every *scene*, one line each ("Scene 12: Brody confronts the mayor; loses; resolves to go to sea"). This is the densest pre-draft artifact and the best place to spot a scene that doesn't change anything.

The discipline that makes outlines work is the **but/therefore test** (see `04-engagement-psychology-hooks.md` and Pixar's spine in `02-pixar-22-rules.md`): adjacent beats should connect with "but" or "therefore," never "and then." "And then" is the sound of an episodic, causeless story. If your step outline reads "this happens AND THEN this happens," you have events, not a plot.

> **→ SHORT-FORM.** The beat sheet collapses to 3–5 beats: Hook → Escalation → Turn → Payoff/CTA. Don't import a 15-beat feature structure into 60 seconds; you'll get a rushed, talky miniature that gestures at acts it has no room to deliver. One want, one turn, one button.

> **→ AI APPLICATION.** The beat sheet is the natural gate boundary (chapter 27): the LLM produces it as a list of objects (`beat_name`, `value_in`, `value_out`, `one_line`), and a verifier rejects any beat whose `value_in == value_out` (nothing changed) or that connects to its neighbor with "and then." This single check kills most generated-story flatness.

---

## 6. The First Draft — the "vomit draft"

Now you *write the thing*, fast and badly, on purpose. Anne Lamott named this in *Bird by Bird* (1994): the **"shitty first draft."** Her framing is the most liberating idea in writing — *"the only way I can get anything written at all is to write really, really shitty first drafts."* She breaks drafts into three: the **down draft** (just get it down), the **up draft** (fix it up), the **dental draft** (check every tooth). The first draft's *only* job is to exist.

Why this matters mechanically: the part of your brain that *generates* and the part that *judges* cannot run at full power simultaneously. Trying to write and edit in the same pass produces paralysis — you polish sentence one for an hour and never reach the climax. The vomit draft deliberately silences the editor so the generator can sprint to the end, where you finally see the *whole shape* — which is the only thing you can actually rewrite.

Permission to be bad is not indulgence; it's throughput.

> **→ SHORT-FORM.** Even a 45-second A/V script gets a vomit pass: dump every VO line and visual idea into the columns without judging, then cut to the bone. The draft might be 90 seconds of material you compress to 40.

> **→ AI APPLICATION.** LLMs are *natural vomit-draft engines* — they generate without ego or paralysis. Lean into it: let the model produce a fast, overlong, imperfect full draft from the beat sheet, because the model's real value is in the cheap, fast, complete pass. Then route to the rewrite passes below, which are where quality is actually made.

---

## 7. The Rewrite — where writing actually happens

The maxim every screenwriter repeats: **"Writing is rewriting."** A script is not *written*; it is *rewritten*. The first draft is raw ore; the rewrite is the metallurgy. Crucially, you do **not** rewrite everything at once — you make **focused passes**, each hunting one class of problem. Trying to fix structure, character, theme, and dialogue simultaneously is how rewrites stall.

| Pass | Hunts for | Key question |
|---|---|---|
| **1. Structure / story** | Sagging acts, missing turns, scenes that don't change value, "and then" connections | Does every scene turn a value and connect by but/therefore? |
| **2. Character** | Inconsistent motivation, passive protagonist, weak arc, unclear flaw/lie | Does the protagonist *drive* the plot, and does their lie/need pay off? (see `03-character-and-scene-craft.md`) |
| **3. Theme** | Scenes that ignore or contradict the controlling idea; on-the-nose moralizing | Does the ending *prove* the controlling idea without stating it? |
| **4. Dialogue** | On-the-nose lines, every character sounding the same, missing subtext | Could you cut the line and play it in action instead? Does each voice differ? |
| **5. Polish** | Typos, formatting, overlong action blocks, pacing micro-issues | Is every word earning its place? |

**Kill your darlings.** The phrase descends from Arthur Quiller-Couch's 1914 lecture "On Style" (collected in *On the Art of Writing*, 1916): *"Murder your darlings."* (It is frequently misattributed to Faulkner, King, and others — the original is Quiller-Couch.) It means: the line, shot, or scene you're proudest of is often the one serving *your* ego rather than the *story's* needs — and those are the hardest, most necessary cuts. A darling that doesn't serve the logline's goal/stakes/irony goes, no matter how good it is in isolation.

> **→ SHORT-FORM.** The five passes survive, but compressed into minutes. You still do them — structure (is there a turn?), character (whose POV?), theme (what value?), dialogue/VO (cut every wasted word — at ~2.5 words/second, a 45s VO is ~110 words, so every word is load-bearing), polish. The *order* is the discipline; the *duration* shrinks.

> **→ AI APPLICATION.** Make each pass a *separate* LLM call with a *single* objective and the relevant rubric. A combined "improve this script" prompt produces mush; a "structure pass only — flag every scene whose value doesn't change" prompt produces surgical, checkable edits. This is the architecture chapter 27 formalizes: the rewrite is N gated single-purpose passes, not one omnibus rewrite.

---

## 8. The Table Read

You gather people, hand out parts, and **read the script aloud**. Nothing else exposes problems this cheaply. Dialogue that looked fine on the page reveals itself as stilted the instant a human says it. Jokes that don't land go silent. Scenes that drag make readers shift in their seats. You're not looking for compliments — you're listening for the *moments the room loses energy*.

> **→ SHORT-FORM.** Read the VO aloud *against a stopwatch*, in the actual voice/persona (or your cloned TTS voice). You'll catch tongue-twisters, lines that overrun the shot, and a hook that lands a beat too late — all before you render.

> **→ AI APPLICATION.** This is the killer move for AI video: **generate the VO with TTS at the script stage** and listen. AI voices expose pacing and phrasing problems exactly like a table read, for free, instantly. Lay the TTS against your planned shot durations to verify audio and video actually fit *before* you spend render budget. (This is why the A/V format below plans both columns together.)

---

## 9. Screenplay Format Basics

Standard screenplay format isn't bureaucratic fussiness — it encodes the **one page ≈ one minute** convention. That ratio exists because the format (Courier 12pt, fixed margins) was calibrated so a page of action and dialogue plays at roughly a minute of screen time. It lets anyone estimate runtime by flipping pages. The elements:

- **Scene heading / slugline** — `INT.` (interior) or `EXT.` (exterior), LOCATION, TIME OF DAY. Example: `INT. BEACH HOUSE - NIGHT`. It orients the reader in space and time and signals a new setup.
- **Action / description** — present tense, only what the audience can **see or hear**. This is the home of *show, don't tell*: you cannot write "Brody is terrified," because the camera can't film an internal state. You write "Brody's hand trembles on the rifle; he can't get the round chambered." (More in `03-character-and-scene-craft.md`.)
- **Character cue** — the speaking character's name, centered/uppercased above their lines. Extensions like `(O.S.)` off-screen, `(V.O.)` voice-over, `(CONT'D)`.
- **Dialogue** — the spoken words, in a center column.
- **Parenthetical** — a brief `(beat)` or `(whispering)` under the cue; use sparingly. Over-parentheticalizing is amateur tell — it directs the actor's job for them.
- **Transition** — `CUT TO:`, `SMASH CUT TO:`, `FADE TO BLACK.` Modern scripts use these rarely; the cut between scenes is assumed. Use one only as a deliberate stylistic beat.

Minimal example:

```
EXT. AMITY BEACH - DAY

Crowded sand. Kids shriek in the surf. BRODY (40s, sweating
in a buttoned shirt) scans the water, jumpy.

A dark shape glides between two swimmers. Brody half-rises.

                    BRODY
              (low, to himself)
          Get out of the water. Get out of
          the water...

He's on his feet now. No one hears him.

                                        SMASH CUT TO:

INT. MAYOR'S OFFICE - CONTINUOUS
```

> **→ AI APPLICATION.** Screenplay format is *human-facing*. For an AI pipeline you rarely render from a `.fountain` file directly — you translate the screenplay into per-shot prompts and the A/V grid below. But the format's discipline (only what's seeable/hearable; one page ≈ one minute) is exactly the constraint that keeps AI prose from drifting into un-filmable interiority.

---

## 10. The Formats That Matter for AI Video

### The Shooting Script

A **shooting script** is the locked screenplay annotated for production: numbered scenes, sometimes numbered shots, inserts, and technical notes. Scene numbers let everyone reference "Scene 14" unambiguously. For AI video, the equivalent is the script broken into **numbered shots**, each becoming one generation unit (one clip / one keyframe set), so you can re-roll Shot 7 without disturbing the rest (see `13-production-pipeline.md` and `17-ai-storyboard-prompting-and-keyframes.md`).

### The Two-Column A/V Script — the workhorse for ads, docs, and short-form

The **A/V script** (audio-visual; also "two-column" or "split-page") is *the* format for commercials, explainers, documentaries, and short-form. It puts **VIDEO** in the left column and **AUDIO** in the right column, row by row, so that what the audience *sees* and what they *hear* are planned **together, on the same line.** This is its superpower for AI video: it forces VO, music, and SFX to be specced against the exact visual they accompany — no more discovering in the edit that your 6-second shot has 11 seconds of narration over it.

A filled template (a 30-second product teaser):

| # | VIDEO (left) | AUDIO (right) | Dur |
|---|---|---|---|
| 1 | Black screen. A single cursor blinks. | SFX: low hum rising. VO: "Every tool promised to save you time." | 0:00–0:04 |
| 2 | Fast montage: cluttered tabs, spinning loaders, a frustrated face lit by screen-glow. | MUSIC: tense pulse in. VO: "They lied." | 0:04–0:09 |
| 3 | Hard cut to clean UI. One click. Everything organizes itself. | SFX: satisfying snap. MUSIC: resolves to warm pad. | 0:09–0:15 |
| 4 | Slow push-in on the result: a calm, finished workspace. | VO: "Meet [Product]. The work, done — before you finish your coffee." | 0:15–0:23 |
| 5 | Logo on bone-white. URL + tagline animate in. | MUSIC: button hit. VO: "[Product]. Try it free today." | 0:23–0:30 |

Note how every audio cue is bound to a specific visual and a duration — the document is simultaneously a script, a shot list, and a timing sheet.

### Short-form (≤90s) script template

For the fastest pieces, collapse further into a four-field skeleton:

```
HOOK LINE (0–3s):   [One line that creates the curiosity gap. Said or shown.]
VO BEATS:           [3–6 short narration lines, each ≤ ~12 words]
ON-SCREEN TEXT:     [Kinetic text per beat — what the eye reads, distinct from VO]
CTA (last 3–5s):    [Single, specific action. One verb.]
```

Filled:

```
HOOK LINE:   "Your AI assistant is lying to you. Here's the proof."
VO BEATS:    1) "It sounds confident."  2) "It cites a source."
             3) "The source doesn't exist."  4) "We caught it on camera."
ON-SCREEN:   [CONFIDENT] → [SOURCE: ████] → [404 NOT FOUND] → [BUSTED]
CTA:         "Run the test yourself — link below."
```

> **→ SHORT-FORM.** This *is* the short-form process. The pipeline collapses to: **idea → logline → A/V two-column (or four-field skeleton) → done.** You still rewrite — but the rewrite is the five passes from §7 run in minutes against a one-page grid, plus a TTS table read against the stopwatch. No treatment, no step outline, no formatted screenplay. The artifact you ship *is* the production document.

> **→ AI APPLICATION.** Two payoffs. (1) **Gated walk:** the LLM produces idea → logline → treatment → beat sheet → A/V script as discrete, verifiable steps, each gated against the locked logline object (this is the spine of chapter 27). (2) **Generate natively in A/V format** so audio and video are planned on the same row from the start — the model emits `{shot_n, video_prompt, vo_line, sfx, music, duration}` tuples, the VO is TTS'd and length-checked against `duration`, and only then do shots go to the video model. Planning both columns together is what stops the classic AI-video failure of beautiful footage with mistimed, overstuffed narration glued on afterward.

---

## Sources

- Blake Snyder, *Save the Cat!* — logline craft (irony, mental picture, audience/cost, killer title): [How and Why to Write a Good Logline | Save the Cat!®](https://savethecat.com/tips-and-tactics/how-and-why-to-write-a-good-logline) and [Save the Cat! (Wikipedia)](https://en.wikipedia.org/wiki/Save_the_Cat!:_The_Last_Book_on_Screenwriting_You'll_Ever_Need)
- Anne Lamott, *Bird by Bird* (1994) — "Shitty First Drafts" (down/up/dental draft): [Shitty First Drafts (PDF, Univ. of Kentucky)](https://wrd.as.uky.edu/sites/default/files/1-Shitty%20First%20Drafts.pdf)
- Arthur Quiller-Couch, "On Style," *On the Art of Writing* (1916) — origin of "murder your darlings" and the Faulkner misattribution: [Slate: "Kill your darlings" — who really said it](https://slate.com/culture/2013/10/kill-your-darlings-writing-advice-what-writer-really-said-to-murder-your-babies.html) and [Murder Your Darlings — Lisa Spangenberg](https://www.lisaspangenberg.com/writing/murder-your-darlings/)
- Two-column A/V script format (commercials, docs, explainers): [StudioBinder — Ultimate AV Script Template](https://www.studiobinder.com/blog/av-script-template/), [Celtx — What is an AV Script?](https://blog.celtx.com/essential-av-script-template-for-better-video-scripts/), [MasterClass — How to Write a TV Commercial Script (AV format)](https://www.masterclass.com/articles/how-to-write-a-tv-commercial-script)
- "One page ≈ one minute" / Courier convention and split-page format: [Stream Semester — Two-Column, Split-Page Script Format Guide](https://www.streamsemester.com/articles/two-colum-split-page-script-format)
- Screenplay format elements (slugline/scene heading, action, character cue, parenthetical, dialogue, transition; INT./EXT., O.S./V.O.): [Final Draft — Screenplay Formatting and Elements](https://www.finaldraft.com/learn/screenplay-formatting-elements/) and [MasterClass — Learn How to Format a Screenplay](https://www.masterclass.com/articles/what-is-a-screenplay-formatting-tips-and-tricks)
- Robert McKee, *Story* — controlling idea (value + cause); cross-referenced in `01-story-structure.md`.
- Lajos Egri, *The Art of Dramatic Writing* (1946) — "premise" as moral proposition; John Truby, *The Anatomy of Story* — "designing principle" as organizing strategy (e.g., *The Godfather*).
