# Documentary Craft & The 75-Second Teaser

Fiction asks you to *believe* a constructed world. Documentary asks you to *trust* a recorded one. That single difference reorganizes the entire grammar. In drama, the camera is invisible by convention — we agree not to notice it. In documentary, the camera's *relationship to reality* is the subject of an unspoken contract between filmmaker and viewer, and the form you choose is a declaration of how that contract is honored. Voice-of-God narration says "I will tell you what this means." Vérité says "I will only show you what happened, and stay out of the way." Reflexive documentary says "I will even show you me, filming this, so you can judge my bias yourself."

For the AI filmmaker this is doubly important, because the most powerful aesthetic in synthetic video right now is not photorealism — it is *evidence of process*. A shot with a visible boom mic, a light stand creeping into frame, a crew member half-out of focus, reads as more "real" than a flawless 4K render, precisely because we associate imperfection-with-apparatus with un-staged capture. This chapter teaches documentary's grammar honestly, then weaponizes its most authentic-feeling mode — the reflexive "show the apparatus" look — as a deliberately constructed AI aesthetic. Sibling chapters: shot grammar is `06-shots-framing-composition.md` and `07-camera-angles-and-movement.md`; cutting is `10-editing-theory.md`; the hook psychology underneath the teaser structure is `04-engagement-psychology-hooks.md`.

---

## Part 1 — The Modes of Documentary (Nichols)

Film scholar Bill Nichols gave us the standard taxonomy of documentary *modes* — not genres, but distinct stances toward truth and the audience. They are not mutually exclusive; most real films blend them. But knowing which mode you are in keeps your choices coherent.

| Mode | Stance | Camera/voice signature | Canonical example |
|---|---|---|---|
| **Expository** | "Let me explain reality to you." | Voice-of-God VO over illustrative footage; argument-driven; B-roll subordinated to the narration | Ken Burns' *The Civil War*; most nature docs (Attenborough); the entire News/explainer lineage |
| **Observational (vérité)** | "I will not interfere; you watch what I watched." | No narration, no interviews, no music; long takes; handheld; "fly on the wall" | Frederick Wiseman (*Titicut Follies*); the Maysles' *Salesman* |
| **Participatory / Interactive** | "I am here, and my presence changes things — that's part of the truth." | Filmmaker on camera or audible; interviews are conversations; the encounter is the subject | Nick Broomfield; Michael Moore (*Roger & Me*); Louis Theroux |
| **Reflexive** | "Look at how this film is made; question it." | Shows its own apparatus — crew, cameras, the constructedness — to provoke skepticism | Dziga Vertov's *Man with a Movie Camera*; *The Act of Killing* (Oppenheimer) |
| **Performative** | "Subjective, embodied, emotional truth over objective fact." | First-person, poetic, expressionistic; truth-through-feeling | *Sans Soleil* (Chris Marker); much of Sarah Polley's *Stories We Tell* |

Two distinctions that beginners blur:

**"Vérité" vs "direct cinema."** Both are observational, but French *cinéma vérité* (Rouch, Morin) believed the camera's presence *provokes* truth — the filmmaker stirs the pot. American *direct cinema* (Maysles, Pennebaker) believed in the opposite: minimize your footprint, let the subject forget you. The look is similar (handheld, available light); the philosophy is opposite. The reflexive/participatory move Yuval loves is closer to the *vérité* lineage — the apparatus is admitted because hiding it would be the bigger lie.

**Expository is the natural mode of the teaser.** A 75-second promo is an *argument* ("you need to see this"), driven by a confident VO and illustrated by B-roll. But the most arresting modern teasers steal the reflexive mode's *texture* — visible rig, on-set lighting, the subject "arriving" to be filmed — to make an expository pitch feel like privileged access. That hybrid is the engine of the worked example in Part 4.

→ **AI APPLICATION.** Choose your mode *before* prompting, because each maps to a different generation strategy. Expository → generate disconnected illustrative B-roll clips (Veo 3.1, Kling 3.0) and bind them with a VO track and kinetic text; coherence lives in the edit, not the shots. Observational → prompt for long, uninterrupted single takes with handheld motion and *no* music ("static unbroken 8-second take, available light, no camera movement except slight handheld drift"); the hardest mode for AI because models default to over-cutting and over-lighting. Reflexive → explicitly prompt the apparatus into frame (Part 5). Performative → lean on stylized image models and treat continuity as irrelevant.

---

## Part 2 — A-Roll vs B-Roll: The Load-Bearing Distinction

This is the spine of nonfiction editing, and the terms are used loosely everywhere, so define them precisely.

**A-roll** is your *primary* footage — the content that carries the spine of the piece. In an interview doc, A-roll is the talking head: the subject speaking to camera or to an off-screen interviewer. The *audio* of A-roll is almost always the master track; it dictates the cut. A-roll answers "what is being said / who is the subject."

**B-roll** is *supplementary* footage that illustrates, contextualizes, or covers the A-roll. If the subject says "I grew up by the sea," the B-roll is waves, a childhood house, an old photo. B-roll answers "what are we looking at while we listen."

The terms are historical: in film-era TV news, the A-roll (interview) and B-roll (cutaways) were literally two separate reels of film loaded into two projectors, and the editor switched between them. The word stuck.

### What B-roll actually does (three jobs)

1. **It illustrates.** Show, don't only tell — the waves under "I grew up by the sea."
2. **It covers edits (the real workhorse).** When you cut two pieces of the same interview together, the talking head *jumps* — the subject's head snaps to a new position (a **jump cut**). Lay a piece of B-roll over the splice and the cut becomes invisible; the viewer's eye is on the waves, not the seam. This is why you can compress a 40-minute interview into 90 seconds without it looking butchered. B-roll is the connective tissue that hides the surgery.
3. **It controls pace and emotion.** A held wide of an empty room under a hard sentence lets it breathe; a fast montage of B-roll under a list accelerates.

The grammar rule: **lay B-roll on the audio you want to keep, not the picture you want to lose.** The cut is driven by the A-roll's *sound*; B-roll is the picture you slide over the parts where the talking head would otherwise jump or sag.

### The interview setup (the craft of A-roll capture)

A talking-head interview has a specific, learnable geometry:

- **Eyeline / the "interview look."** The subject looks *just off* the lens, at the interviewer seated beside the camera — never *into* the lens (direct address feels like an ad or a hostage video) and never *far* off (feels evasive). The classic angle is roughly 10–20° off axis. Errol Morris famously broke this with the **Interrotron** — a teleprompter rig that puts the interviewer's live face *over* the lens, so the subject makes true eye contact with the camera (and thus the viewer), creating the unsettling intimacy of *The Fog of War*.
- **Framing.** Usually a medium close-up or close-up, subject's eyes on the upper third, **looking room** (negative space) on the side they face. Eyes are the focus; the lens is wide-open-ish for a soft, separating background.
- **Two-camera setup.** Pros shoot interviews with two cameras at different sizes/angles (e.g., a tight MCU and a wider 3/4). Cutting between two valid angles of the *same answer* lets you remove a stumble or a pause **without any jump cut and without B-roll** — the size change motivates the cut. This is the cleanest way to edit speech.

→ **AI APPLICATION.** Decide up front whether A-roll is *real* (a phone recording of a real person — almost always the right call for trust and lip-sync fidelity) or *synthetic* (an AI talking head). For synthetic A-roll, the best current tools are audio-driven avatar models: **Hedra (Character-3)**, which drives mouth shapes from audio at the phoneme level and is widely rated best-in-class for portrait lip-sync from a single image; **HeyGen**, the all-rounder with the largest avatar library, 4K, and 175+ language translation; and **Synthesia** for enterprise/compliance use *(verify — fast-moving; as of mid-2026)*. Generate the avatar's eyeline slightly off-lens for documentary feel, or straight-to-lens for direct-address ad feel. B-roll is generated separately as short text-to-video clips (Veo 3.1, Kling 3.0) — and crucially, **you do not need continuity between B-roll clips**, because B-roll's job is to cover cuts, not maintain a shot. This is a gift for AI: the form's grammar absorbs the per-clip inconsistency that plagues synthetic video.

---

## Part 3 — Archival Footage and "Showing the Apparatus"

### Archival / stock footage

Archival footage (old film, news clips, home video, photographs) is the third material after A-roll and B-roll. It carries *authority* and *pastness* — a grainy 16mm clip instantly signs "this really happened, long ago." Ken Burns built an entire grammar (the "Ken Burns effect" — slow pushes and pans across still photographs) precisely because the *evidence* of a real photograph plus motion creates emotion that a re-enactment cannot. The honest caveat: archival is also the most *manipulable* material, because footage shot for one purpose can be recontextualized to imply another. Documentary ethics live here.

### The reflexive / "show the apparatus" aesthetic

Here is the move Yuval is drawn to, stated precisely. Normally, film hides its means of production — the **fourth wall** extends to the crew, the lights, the boom. **Reflexive documentary deliberately breaks that wall**: it lets you see the boom mic dipping into frame, the C-stands and softboxes, the second camera, the focus puller, the clapperboard. *Man with a Movie Camera* (1929) is the ur-text — it shows the cameraman filming, the editor cutting, the screen being watched.

**Why does visible apparatus read as *more* authentic, not less?** Three reasons, and one honest correction:

1. **Cost-of-faking heuristic.** Our brains use "how hard would this be to fake?" as a proxy for truth. A pristine ad-perfect frame is *easy* to imagine as staged; a frame cluttered with real gear signals "an actual crew was actually here." (This is a heuristic, not a guarantee — and that is exactly why it can be *spoofed*, which is the point of the AI application below.)
2. **In-group signaling.** Visible gear says "made by people who make things" — it flatters the viewer as an insider being shown behind the curtain. BTS (behind-the-scenes) content rides this entirely.
3. **Imperfection = un-staged.** Lens flare from a real light, a slightly missed focus, a boom shadow — these are the fingerprints of live capture. Their *presence* is counter-evidence against "this was generated/staged."

**The honest correction:** "raw = true" is a *style*, not proof. The reflexive look is itself a constructed aesthetic and has been since 1929. Plenty of staged ads fake a handheld-doc look to borrow its credibility. So when you generate a fake-BTS aesthetic with AI, you are not "cheating documentary" — you are using a stylistic register the form has always used. Just don't confuse the *look of* unmediated truth with the thing itself; that confusion is what makes the technique persuasive, and what makes it ethically loaded.

→ **AI APPLICATION.** For the Ken Burns archival look, generate or source a still, then animate a slow push/pan in post (any NLE, or an image-to-video model with a tiny zoom). To *manufacture* archival texture, prompt for the medium directly: "1970s 16mm home-movie footage, heavy film grain, gate weave, slightly faded color, 4:3." For the apparatus look, see Part 5 — it is the centerpiece.

---

## Part 4 — Structure of a Documentary Teaser

A teaser is not a trailer. A trailer summarizes a finished film; a teaser *creates demand* for something the viewer cannot yet have. Its only job is to install a question and refuse to answer it. The architecture:

| Beat | Function | Why it works (the WHY) |
|---|---|---|
| **Cold-open hook** (0–8s) | Drop the viewer into the most charged image/line *before* any context | The brain is a prediction engine; an unexplained, high-stakes image opens a curiosity gap it is compelled to close. See `04-engagement-psychology-hooks.md`. |
| **The question / stakes** (the premise) | State or imply what is at risk and what we don't know | Curiosity needs a *gap* — a defined hole in knowledge. Vague is not mysterious; vague is ignorable. |
| **Escalation** | Rapid intensification — faster cuts, rising audio, bigger claims | Builds physiological arousal toward a peak; momentum prevents the swipe-away. |
| **The withhold** | Approach the answer, then *cut away* before delivering it | The Zeigarnik effect — unresolved tension is held in memory more strongly than resolution. The withhold *is* the product. |
| **CTA** (call to action) | The promise of resolution, gated behind an action (date, link, "watch now") | Converts installed tension into behavior at the exact moment arousal peaks. |

The cardinal sin of a teaser is *resolving*. The moment you answer the question, the reason to watch evaporates.

---

## Part 5 — Worked Example: A 75-Second Apparatus-Style Teaser

Subject: a single expert/figure ("the Subject"). Concept: the Subject walks onto a lit set, the crew and gear are visible (reflexive texture), they sit, and a confident VO builds an argument while the camera works hard — push-ins, ECUs on the eyes/lips/hands, handheld energy, a crane move — intercut with illustrative B-roll, bound by kinetic text and a rising audio bed. This is expository-mode pitch wearing reflexive-mode clothing.

Conventions below: **shot size** (ECU=extreme close-up, CU=close-up, MCU=medium close-up, MS=medium, WS=wide, EWS=extreme wide); **angle**; **movement**; **sound**; **AI model** to generate that beat. (Model choices are as of mid-2026 — *verify, fast-moving.*)

| # | Time | Beat / on-screen | Shot size | Angle | Movement | Sound | AI model & note |
|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:04 | **Cold open.** Black. A single light flicks on; we glimpse a C-stand and softbox edge, dust in the beam. Subject's silhouette enters frame. | WS | Low, looking up at the rig | Slow push-in | Room tone, single switch *clack*, sub-bass drone begins | Veo 3.1 (best low-light + native audio cue); prompt the rig explicitly |
| 2 | 0:04–0:08 | Boom mic dips in from top of frame; a crew member's shoulder racks out of focus as Subject walks toward the chair. | MS | Eye level, 3/4 | Handheld follow | VO line 1 (the hook question), drone swells | Kling 3.0 (strong handheld "camera-as-actor" motion) |
| 3 | 0:08–0:12 | Subject sits. We see the second camera and operator reflected/at frame edge. Clapper *snaps* (optional). | MCU | Eye level, off-lens eyeline | Settle to static, slight handheld drift | Clap; VO continues; first riser note | Hedra/HeyGen if synthetic A-roll; else real footage |
| 4 | 0:12–0:18 | **The stakes.** Subject begins to speak (A-roll). Eyeline 15° off lens. | CU | Eye level | Slow push-in to ECU | A-roll audio = master; bed under | Hedra (phoneme lip-sync) or real |
| 5 | 0:18–0:22 | **ECU on the eyes** at the key word. | ECU (eyes) | Eye level | Locked / micro-push | A-roll; riser climbs | Veo 3.1 i2v from a still of the eyes |
| 6 | 0:22–0:26 | Cut to **ECU on lips** mid-word; then **ECU on hands** gesturing. | ECU | Slightly high on hands | Locked | A-roll; subtle SFX on gesture | Kling 3.0 (detail motion) |
| 7 | 0:26–0:34 | **B-roll burst #1** — 3 fast illustrative clips (the topic: e.g., a city, a screen, a crowd), each ~2.5s. | WS/MS mix | Varied | Each with its own move (dolly, tilt, drift) | A-roll *continues underneath* (covering the cut); cuts on the beat | Veo 3.1 / Kling 3.0, generated independently |
| 8 | 0:34–0:38 | **Kinetic text slam** — the core claim as full-frame type, hits on a downbeat. | Full-frame text | — | Type scales/snaps in | Impact SFX + bass drop | After Effects / HyperFrames + GSAP |
| 9 | 0:38–0:46 | Back to set: **crane/jib up** revealing the whole lit stage — lights, stands, crew, Subject small in the pool of light. | WS→EWS | High, craning up | Crane up + back | VO escalates; bed thickens | Kling 3.0 ("crane up to reveal environment" is its showcase prompt) |
| 10 | 0:46–0:54 | **Escalation montage** — rapid intercut: A-roll fragments + B-roll + archival/grainy insert, accelerating. | Mixed, tightening | Mixed | Whip-pans / kinetic transitions between | Riser at peak; whooshes on each transition | Multiple; transitions in post |
| 11 | 0:54–1:02 | **The withhold.** Subject leans in, starts the most important sentence… "And the truth is —" | ECU | Eye level | Hard push-in | A-roll peaks; bed *cuts to near-silence* | Hedra / real |
| 12 | 1:02–1:06 | **Smash cut to black** mid-word. Beat of silence. | Black | — | — | Total silence (1s) — the withhold | Edit |
| 13 | 1:06–1:12 | **Kinetic title** of the film/series resolves in. | Full-frame text | — | Type settles | Single sustained note / brand sting | HyperFrames/AE |
| 14 | 1:12–1:15 | **CTA** — date / link / "Watch now," small Subject silhouette or set still behind. | Lower-third + plate | — | Static | Music tag-out | Edit |

The architecture maps cleanly onto Part 4: beats 1–3 are the cold-open hook (apparatus reveal *is* the hook here), 4–6 the stakes, 7–10 the escalation, 11–12 the withhold, 13–14 the CTA. The riser audio is the spine that makes 75 disconnected seconds feel like one rising breath — see how arousal-arc pacing is handled in `05-neuroscience-honest.md`.

→ **AI APPLICATION (beat-level).** Generate every set beat (1, 2, 3, 9) with apparatus language baked into the prompt (Part 5b). Generate A-roll ECUs (4–6, 11) either from real footage or from a single still driven by Hedra; the eyes/lips/hands ECUs can be image-to-video micro-moves so the face stays consistent. Generate B-roll (7, 10) as throwaway independent clips — inconsistency is *fine* because they only flash. Build text/transitions (8, 13) in HyperFrames (HTML/GSAP) or After Effects. Source SFX (risers, whooshes, impacts) from ElevenLabs' text-to-SFX; score the bed with Udio or Suno *(verify)*; cut everything to the audio.

### Part 5b — Generating the "fake BTS / apparatus" look

The whole illusion rests on prompting the rig *into* the frame. Models trained on real footage have seen plenty of behind-the-scenes and documentary material, so the vocabulary works — you just have to ask for it explicitly, because the default is to hide gear.

Prompt fragments that reliably summon apparatus texture:

- **Gear in frame:** `boom microphone dipping into the top of the frame`, `C-stand and softbox light visible at the edge of frame`, `a second camera and operator partially visible`, `light stands and cables on the studio floor`, `a focus puller's hand on the lens`, `clapperboard snaps shut`.
- **Capture imperfection:** `handheld, slight camera shake`, `rack focus, brief moment out of focus`, `lens flare from an off-camera light`, `available light, mixed color temperature`, `visible film grain` (or `digital sensor noise in the shadows`).
- **On-set staging:** `subject walks onto a lit film set and sits in a chair`, `single hard key light with deep shadow`, `documentary behind-the-scenes aesthetic`, `the crew is visible working around the subject`.

Negative/avoid (where the model supports it): `clean studio`, `polished commercial lighting`, `pristine`, `no visible equipment` — to *suppress* the default ad look.

A worked single-clip prompt (beat 2):
> *"Handheld documentary shot, eye level, following a person as they walk across a film set toward a chair. A boom microphone dips into the top of the frame; a C-stand with a softbox is visible at the left edge; a crew member's shoulder racks out of focus in the foreground. Single hard key light, deep shadows, mixed color temperature, subtle camera shake, faint sensor noise in the shadows. Cinematic, behind-the-scenes aesthetic. No music."*

### Part 5c — Assembly: A-roll + AI B-roll + VO + kinetic text

The assembly order matters as much as the assets:

1. **Lay the spine first.** Drop the VO (or A-roll master audio) on the timeline. The *audio* is the edit; everything else hangs off it. Record VO with a cloned/real voice (ElevenLabs); for synthetic A-roll, generate the avatar *from* that VO so lip-sync is locked.
2. **Cut the A-roll to its best fragments**, using two-camera angle changes (or B-roll) to hide every internal jump.
3. **Lay B-roll over every seam and every illustrable line** — picture you want over audio you keep.
4. **Build the audio bed and riser** so the climb peaks exactly at the withhold (beat 11–12); cut the bed to near-silence on the smash to black — the silence is a sound design choice, not an absence.
5. **Add kinetic text on the downbeats** (HyperFrames/GSAP gives frame-accurate control; see the `gsap` and `hyperframes` skills) — text hits land on beats, never floating.
6. **Layer SFX** (risers, whooshes on transitions, impacts on text slams) — these are the glue that makes independently-generated AI clips feel like one piece.
7. **Grade for unity.** Independently generated clips have different color/contrast; a single grade pass (LUT or per-clip match) is what finally makes a Frankenstein of AI clips read as one film.

The deepest practical lesson: in documentary, **the edit is the authorship**, not the shot. That is precisely why the form is the friendliest home for current AI video — per-clip inconsistency, the Achilles' heel of synthetic generation, is exactly what documentary grammar (B-roll over cuts, audio-led editing, archival texture, visible apparatus) is *built to absorb*.

---

## Sources

- Best AI Video Generators 2026 (Kling 3.0, Veo 3.1, Sora status): https://www.getaiperks.com/en/blogs/44-best-ai-video-generators-2026
- Sora discontinuation + model comparison: https://lushbinary.com/blog/ai-video-generation-sora-veo-kling-seedance-comparison/
- Hedra Character-3 phoneme lip-sync: https://plisio.net/ai/hedra
- HeyGen / Synthesia talking-head comparison: https://www.synthesia.io/post/heygen-alternatives-competitors
- Veo 3.1 camera-control prompting (pan/tilt/dolly/crane/handheld, first+last frame): https://www.veo3ai.io/blog/veo-3-camera-control-prompts-2026
- Kling 3.0 "camera as actor" / crane-reveal handheld: https://curiousrefuge.com/blog/kling-vs-veo
- ElevenLabs text-to-SFX (risers, whooshes, impacts): https://elevenlabs.io/sound-effects
- Udio AI music generation (2026 status, UMG settlement): https://www.soundverse.ai/blog/article/what-is-udio-ai-0139
