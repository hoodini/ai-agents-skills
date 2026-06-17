# Story Structure — The Skeleton of Every Film

Structure is not a template you pour story into. It is the *shape of the audience's changing emotional state over time*. When a screenwriter says "act break," they are really naming the moment the viewer's expectation flips. Every framework in this chapter — Aristotle, Field, Freytag, Campbell, Harmon, Snyder — is a different attempt to chart the same underlying curve: how human attention is captured, held under tension, paid off, and released. Learn the curve first; the named frameworks become interchangeable vocabularies for it.

This matters doubly for AI filmmaking. A generative model has no instinct for stakes or causality. If you do not impose the skeleton *before* you generate a single frame, the model will hand you beautiful, disconnected, meaningless footage — the visual equivalent of a sentence with perfect grammar and no point. Structure is the one thing AI cannot improvise for you. It is your job.

## The engine underneath every framework

Before the named models, understand the parts that *all* of them are made of. Master these and you can collapse or expand any structure on demand.

### Premise and logline

The **premise** is the single causal sentence that makes a story inevitable: "What if a great white shark stalked a beach town that refused to close?" The **logline** is the premise dressed for selling — it names the protagonist, their goal, the opposition, and the irony, in one or two sentences. Format that works almost universally:

> *When [inciting incident], a [flawed protagonist] must [goal] before [stakes/deadline], or else [cost of failure].*

Example (*The Social Network*): *When he's dumped by his girlfriend, a brilliant, resentful Harvard student builds the website that will make him the world's youngest billionaire — and cost him every friend he has.* Notice the logline already contains the want (status/revenge), the need (connection), and the irony (he builds a "social" network while destroying his social life). A logline that doesn't contain a contradiction is usually a premise that won't sustain a film.

### Theme / controlling idea

Robert McKee's term **controlling idea** is the most useful in the room: a one-sentence statement of *value + cause*. Not "love" but "Love conquers all when we surrender to instinct" — or its cynical inversion, "Obsession destroys us when we let it override reason." The controlling idea is the meaning the *ending* proves. Every scene either supports or complicates it. If you can't state yours, your film will feel like it's "about" nothing, even when a lot happens.

### The dramatic question

The **dramatic question** is the binary suspense hook the audience is unconsciously asking the whole time: *Will Marlin find Nemo? Will the heist succeed? Will they get together?* It is answered — yes or no — at the climax, and the film ends shortly after. A film can have a *minor* dramatic question per scene and one *major* one spanning the whole runtime. If a viewer can't tell you what question they're waiting to see answered, your structure has no spine. This is the single most important concept in the chapter for short-form AI video: **a 30-second clip needs a dramatic question by second 3.**

### Want vs. Need (the two-track protagonist)

- **Want** = the external, conscious goal. Concrete, visible, often achievable: win the championship, get the diamond, escape the island.
- **Need** = the internal, often unconscious lesson the character must learn to become whole: humility, self-forgiveness, the courage to trust.

The engine of character drama is that **the want and the need are usually in conflict** — pursuing the want is exactly what blocks the need. *Up*: Carl *wants* to get his house to Paradise Falls (a monument to his dead wife); he *needs* to let her go and live again. The climax forces a choice between want and need; which he chooses defines whether the film is redemptive or tragic. Michael Corleone *wants* to protect his family and *needs* to stay out of the killing — *The Godfather* is a tragedy because the want devours the need.

### Stakes, escalating conflict, and try/fail cycles

**Stakes** are the answer to "so what if they fail?" — and they must be specific and personal, not abstract ("the world ends" is weaker than "his daughter dies"). **Escalation** means each obstacle is harder than the last; a flat difficulty curve reads as boredom. The mechanism of escalation is the **try/fail cycle**: the protagonist attempts a solution, it fails (or succeeds *with a worse complication*), forcing a harder attempt. The cleanest articulation is the "**but / therefore**" test (from *South Park*'s Trey Parker and Matt Stone): a strong story connects beats with "but" and "therefore," never "and then." "And then" is a list; "but/therefore" is causality, and causality is what the brain reads as *story*.

### The value-charge shift per scene (McKee)

McKee's most rigorous tool: **every scene must turn a value from positive to negative or vice versa.** A "value" is any charged human condition — alive/dead, together/apart, hopeful/despairing, free/trapped, winning/losing. If a scene begins and ends on the same charge, *nothing happened* and the scene should be cut or rewritten. Test it: write the value-charge of the scene's opening and closing as a polarity (e.g. "trust (+) → betrayal (−)"). A film is a chain of these turns building to the largest turn of all, the climax. This single discipline will fix more limp AI scripts than any other.

> **→ AI APPLICATION.** Make the LLM compute the value-charge before writing prose. Prompt: *"For each beat, output a line `[value]: open-charge → close-charge`. Reject any beat whose charge does not flip."* This forces causality into a model that otherwise happily generates atmospheric scenes where nothing changes. For a 75-second piece, demand at minimum three charge flips (setup −, midpoint reversal, climax +/−).

## Aristotle: the original three parts plus the two turns

Aristotle's *Poetics* (~335 BCE) is the root of all Western structure. Two ideas survive intact:

1. **Beginning, middle, end** — but his definition is causal, not chronological. The beginning *requires nothing before it*; the end *requires nothing after it*; the middle is caused by the beginning and causes the end. This is the original "but/therefore."
2. **Peripeteia and anagnorisis** — the **reversal** (a sudden swing of fortune, ideally born from the protagonist's own action) and the **recognition** (a shift from ignorance to knowledge). In *Oedipus Rex* they fire simultaneously: Oedipus learns the murderer he hunts is himself. The most satisfying climaxes still detonate reversal and recognition together.

**When to use:** as a sanity check, always. If your climax has neither a reversal nor a recognition, it's a stopping point, not an ending.

> **→ AI APPLICATION.** Aristotle is your minimum viable structure for very short pieces. A 15-second AI clip can't hold a 15-beat sheet, but it *can* hold "stable situation → reversal → new understanding." Lock those three as your shotlist before prompting any video model.

## Freytag's five-act pyramid

Gustav Freytag (1863) analyzed five-act classical tragedy into: **exposition → rising action → climax → falling action → catastrophe/dénouement.** His real contribution is the *symmetric pyramid* — the idea that after the peak, energy releases on the way down. Modern screen storytelling has largely abandoned the long falling action (audiences leave the moment the dramatic question is answered), so Freytag is more useful as a *theory of release* than as a working template. Use it for tragedy, prestige drama, and anything where the *aftermath* of the climax is the point (the slow unwinding in *There Will Be Blood*).

## The three-act paradigm (Syd Field)

Syd Field's *Screenplay* (1979) reverse-engineered the dominant structure of the feature film and gave it coordinates. It maps cleanly onto a ~110-page script (≈ 110 minutes, 1 page ≈ 1 minute):

| Element | Page / % | Function |
|---|---|---|
| Act 1 — Setup | 1–30 / 0–25% | Establish hero, world, want; ordinary status quo |
| Inciting Incident | ~10–12 / ~10% | The event that disturbs the equilibrium |
| Plot Point 1 | ~25–30 / ~25% | Hero locks into the journey; no going back |
| Act 2 — Confrontation | 30–90 / 25–75% | Escalating obstacles; the bulk of try/fail |
| Midpoint | ~55–60 / ~50% | Major reversal; raises stakes, shifts goal |
| Plot Point 2 | ~85–90 / ~75% | Lowest moment / new information that sets up the finale |
| Act 3 — Resolution | 90–110 / 75–100% | Climax answers the dramatic question; dénouement |

The **midpoint** is Field's most underused gift. It is a false victory or false defeat that *changes the nature of the goal* — Marion is murdered in *Raiders* and the hunt turns personal; Neo is told he's not the One in *The Matrix*. A saggy Act 2 is almost always a missing or weak midpoint.

**When to use:** the default for any narrative 60 seconds and up. It's the lingua franca; even people who've never read Field intuitively expect its rhythm.

> **→ AI APPLICATION.** The page-as-minute math is your timeline grid. For a 90-second piece, scale the percentages: inciting incident ~9s, PP1 ~22s, midpoint ~45s, PP2 ~67s, climax ~80s. Hand the LLM this exact second-grid and require one shot-prompt per beat. See [06-shots-framing-composition.md] for translating each beat into camera language.

## The Hero's Journey: Campbell → Vogler

Joseph Campbell's *The Hero with a Thousand Faces* (1949) proposed the **monomyth**: a deep cross-cultural pattern of departure, initiation, and return. **Honest caveat:** Campbell's universality is overstated — it's strongest for Western quest myth and weakest for many non-Western and non-quest narratives, and "this is in all cultures' myths" is a popular myth itself. It is a powerful *generative* pattern, not a law of the human mind. Treat it as one excellent template, not the structure of all story.

Christopher Vogler's *The Writer's Journey* (1992) distilled Campbell into 12 Hollywood-usable stages: (1) Ordinary World, (2) Call to Adventure, (3) Refusal of the Call, (4) Meeting the Mentor, (5) Crossing the Threshold, (6) Tests/Allies/Enemies, (7) Approach to the Inmost Cave, (8) The Ordeal, (9) Reward, (10) The Road Back, (11) Resurrection, (12) Return with the Elixir. *Star Wars*, *The Lion King*, and *The Matrix* are textbook fits.

**When to use:** mythic, aspirational, transformation-driven stories — origin films, fantasy, brand "hero's journey" ads. Avoid forcing it onto ensemble pieces, slow character dramas, or ironic/anti-heroic stories, where it feels like a corset.

> **→ AI APPLICATION.** The journey's recurring locations (Ordinary World vs. Special World) are a *visual* gift for AI: you can lock a color/lighting palette per world (muted home, saturated adventure) and feed it as a style anchor to keep generated shots coherent across the cut. See [08-lenses-lighting-color.md].

## Dan Harmon's Story Circle — the best tool for short content

Dan Harmon (*Community*, *Rick and Morty*) compressed the monomyth into an eight-step circle that maps a character moving down into the unconscious and back, divided by two axes (order/chaos, comfort/need):

1. **You** — a character in a zone of comfort,
2. **Need** — but they want something,
3. **Go** — they enter an unfamiliar situation,
4. **Search** — adapt to it,
5. **Find** — getting what they wanted,
6. **Take** — paying a heavy price,
7. **Return** — back to their familiar situation,
8. **Change** — having changed.

Why it's the most practical structure for short-form: it's **fractal and self-similar**. Every step is itself a mini-circle, so you can run the same eight beats whether you have 8 minutes or 8 seconds — you just allocate less time per beat. It also bakes in want vs. need (steps 2 and 8) and the cost (step 6) automatically. The phrasing is plain enough to hand directly to an LLM without it tangling in jargon.

> **→ AI APPLICATION.** This is the recommended default skeleton for AI shorts. Prompt the LLM: *"Write the story as Harmon's 8 steps, one sentence each, ensuring step 6 (the price paid) and step 8 (the change) reflect the protagonist's internal need, not just their external want."* Then expand each of the 8 into one shot. Eight shots × ~9 seconds ≈ a 72-second film that actually has an arc — and ~8s is right at the native single-clip ceiling of today's strongest models (Veo 3.1 ~8–10s; Kling 3.0 ~15s across up to 6 shots).

## Blake Snyder's "Save the Cat!" — the 15-beat sheet

Snyder's *Save the Cat!* (2005) is the most granular mainstream beat sheet, calibrated to a 110-page screenplay. Memorize the positions; they are the closest thing the industry has to a shared clock.

| # | Beat | Page | % |
|---|---|---|---|
| 1 | Opening Image | 1 | ~1% |
| 2 | Theme Stated | 5 | ~5% |
| 3 | Set-Up | 1–10 | 1–10% |
| 4 | Catalyst (inciting incident) | 12 | ~10% |
| 5 | Debate | 12–25 | 10–22% |
| 6 | Break into Two | 25 | ~22% |
| 7 | B Story | 30 | ~27% |
| 8 | Fun and Games (the "promise of the premise") | 30–55 | 27–50% |
| 9 | Midpoint | 55 | ~50% |
| 10 | Bad Guys Close In | 55–75 | 50–68% |
| 11 | All Is Lost | 75 | ~68% |
| 12 | Dark Night of the Soul | 75–85 | 68–77% |
| 13 | Break into Three | 85 | ~77% |
| 14 | Finale | 85–110 | 77–100% |
| 15 | Final Image | 110 | ~100% |

Two beats deserve note. **"Theme Stated"** (often a line of dialogue early on whose truth the hero doesn't yet believe) is what the finale will prove — it's the controlling idea, planted. **"Save the Cat"** itself is the *title's* trick, not a numbered beat: an early moment where the hero does something likable (saving a cat) to buy audience allegiance. **Honest caveat:** the sheet's ubiquity in Hollywood is real, but so is the critique that slavish adherence produces formulaic, samey films. It is a diagnostic grid, not a recipe — use it to find what's *missing*, not to fill every box.

**When to use:** commercial features, anything that must hit four-quadrant expectations, and as a *checklist* against your draft.

> **→ AI APPLICATION.** Opening Image and Final Image are a gift for AI shorts because they're *single frames* — generate them first as bookends (the Final Image should visually invert the Opening to show change), then let everything between bridge them. Ask the LLM to specify both images concretely before any motion is generated.

## Compressing to 15–90 seconds: which beats survive

When runtime collapses, beats don't shrink uniformly — most get *deleted*. The brain still needs the core curve, so prioritize ruthlessly. The hierarchy of what survives, by budget:

| Format | Surviving spine | What to cut |
|---|---|---|
| **15s** | Hook (dramatic question by ~s3) → single reversal → button/payoff. Aristotle's 3 parts, nothing more. | Subplots, mentor, debate, dénouement. One character, one want. |
| **30s** | Setup → catalyst → one try/fail → reversal → resolution. ~5 beats. | Midpoint as separate beat; B-story; multiple obstacles. |
| **60s** | Harmon's 8 steps, ~7s each — or Field's 3 acts with a single clear midpoint. | "Fun and games" expansion; second try/fail cycle. |
| **90s** | Field 3-act scaled (incident ~9s, midpoint ~45s, PP2 ~67s, climax ~80s), or full Harmon circle with breathing room. | Still no room for a true B-story; keep one protagonist, one need. |

The non-negotiables at *every* length: **(1) a dramatic question established almost immediately, (2) at least one value-charge flip, (3) a payoff that answers the question.** A short that's all vibe and no question is a moving wallpaper, not a film. The most common failure in AI shorts is spending the precious first seconds on a slow establishing shot instead of the hook — open *on* the disturbance, not before it.

> **→ AI APPLICATION.** For ultra-short, invert the order of operations: write the *final* payoff line/image first, then reverse-engineer the single question that makes it land. Tell the LLM the runtime in seconds and forbid more beats than the budget allows: *"This is 20 seconds. You get exactly 3 beats. Cut anything that isn't hook, turn, or payoff."* See the arousal-arc pacing in the existing cinematic-ai-video skill for how to time the emotional spike within these beats — this chapter sets the skeleton; that skill tunes the nervous-system curve on top of it.

## AI APPLICATION: locking the spine before you generate

The discipline that separates competent AI films from incoherent ones is **freezing the structural spine in text before touching any image or video model.** Generation is expensive and stochastic; you want it converging on a fixed target, not improvising the plot. Use a strong reasoning-and-prose model for this stage — as of mid-2026 the Claude Opus 4.x line and GPT-5.5 are the leaders for plot logic and prose respectively *(verify — model names/versions change fast)*; whichever you use, the *protocol* matters more than the brand.

A reliable lock sequence:

1. **Force the one-liners first.** Have the model output, and you approve, exactly these before anything else:
   - **Logline** (the formula above, containing an irony).
   - **Controlling idea** (value + cause, one sentence — what the ending proves).
   - **Dramatic question** (one binary sentence).
   - **Want vs. Need** (two lines, ideally in tension).
   - **Stakes** (specific, personal cost of failure).
2. **Gate the structure on the lock.** Instruct: *"Do not write any scene, shot, or visual description until I approve the five lines above. If they're weak, ask me; do not proceed."* This single guardrail prevents the model's strongest failure mode — racing ahead to pretty footage.
3. **Choose the skeleton by runtime** (Harmon 8 for ≤90s shorts; Field 3-act for features) and make the model emit beats *with value-charges* (`open → close`) so causality is checkable at a glance.
4. **Self-critique pass.** Prompt: *"For each beat, name which try/fail cycle it belongs to and whether its value-charge flips. Flag any 'and then' connective and rewrite it as 'but' or 'therefore.'"*
5. **Only then expand each beat to a shot prompt** for the video model, carrying the locked logline and palette as a fixed style anchor across every generation (consistent seeds / reference frames keep characters stable across stitched clips, since single-clip limits still sit around 8–25 seconds in 2026).

The mental model: **the LLM is your story editor, the video model is your camera department.** Editors don't shoot; cameras don't decide the plot. Keep that wall, and structure stops being the thing AI breaks and becomes the thing that makes AI footage mean something. For how these beats become edited rhythm and shot transitions, see [10-editing-theory.md]; for turning beats into camera grammar, [06-shots-framing-composition.md].

---

### Sources
- Best AI for Creative Writing, June 2026 — https://www.buildmvpfast.com/articles/best-llms-2026-guide/creative-writing-ai
- Best AI Models for Novel Writing 2026 — https://www.inkfluenceai.com/blog/best-ai-models-for-novel-writing-2026
- AI Video Generation 2026: Sora 2 vs Veo 3.1 vs Kling 3.0 — https://lushbinary.com/blog/ai-video-generation-sora-veo-kling-seedance-comparison/
- Veo 3.1 vs Sora 2 (2026): Length, Consistency, Audio — https://www.glbgpt.com/hub/veo-3-1-vs-sora-2/
- Best AI Video Generators 2026 (AI/ML API) — https://aimlapi.com/blog/best-ai-video-generators-2026-veo-3-1-kling-sora-2-seedance-more-compared
