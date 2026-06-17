# Transitions & Kinetic Sequences

A transition is the join between two shots: the moment one image gives way to another. It is the single most frequent decision in any film — a 90-minute feature has 1,000–2,000 of them, a 30-second trailer can have 80 — and it is the decision most beginners over-think. The deep truth of this chapter is counter-intuitive: **the more visible a transition is, the harder it has to work to justify itself.** A fancy transition is a promise to the audience ("this join *means* something"); break that promise and you look like a wedding video.

For the AI filmmaker the stakes are different and higher than for a live-action editor, because in an AI pipeline the transition is also where you *hide the seams* between independently-generated clips. A match cut or a whip-pan isn't just style — it's the structural trick that lets two clips with slightly different lighting, faces, or physics read as one continuous world. This chapter catalogues every transition, explains *when* each is right and why, then goes deep on the fast-cut kinetic-typography trailer style, on keyframe-and-easing mechanics, and on the AI bridge: what to bake into generation vs. what to do in the edit.

This pairs tightly with **10-editing-theory.md** (cut motivation, rhythm, the Kuleshov effect) — read that for *why we cut at all*; this chapter is *how the cut is shaped*. Cross-references to **06-shots-framing-composition.md** (graphic matching), **07-camera-angles-and-movement.md** (whip-pans, motivated moves), and **05-neuroscience-honest.md** (what fast cutting actually does to attention).

---

## 1. The Cut Is the Default — and Why

A **cut** is an instantaneous switch from shot A to shot B, zero frames of overlap. It is the default not by laziness but by physiology. Your visual system already makes "cuts" constantly: every **saccade** (a fast eye movement from one fixation point to another) is a hard jump, and the brain suppresses vision during the jump (**saccadic masking**) and stitches the before-and-after into a seamless sense of "I just looked over there." A film cut piggybacks on this machinery. When a cut is well-motivated — it answers a question the shot just raised, or follows a movement, or lands on a beat — the brain processes it the same way it processes its own glance, and you *do not consciously see it*. Walter Murch's famous formulation (in *In the Blink of an Eye*) is that a good cut happens where the viewer would naturally blink — at a completed thought.

This is why "the best edit is usually invisible (a cut)." Invisible doesn't mean unnoticeable-because-bland; it means the join is so motivated that attention flows *through* it to the story without snagging on the technique. Every other transition in this chapter is a *deviation* from the cut, and a deviation must buy something — a passage of time, a change of consciousness, a thematic rhyme, a theatrical flourish — or it is just friction.

A myth to kill: that fast cutting is inherently "more engaging." It raises low-level arousal (orienting response to each new image — see **05-neuroscience-honest.md**) but degrades comprehension and emotional depth if there's no underlying motivation; the average shot length (ASL) of modern action films has dropped to ~2 seconds, and the genuinely well-regarded action sequences (the *Mad Max: Fury Road* chases) are fast *but spatially legible* because cuts respect screen direction and center-frame the subject. Speed without geometry is noise.

→ **AI APPLICATION.** In an AI pipeline the cut is also your cheapest, most robust transition: it requires no overlap rendering and no shared frames between clips, so two independently generated shots just butt against each other on the timeline. Do it in the edit (HyperFrames/code timeline), not in generation. The craft work is *choosing the cut point*: cut on a completed action or a peak of motion, never mid-gesture, and keep the subject roughly center-frame across the cut so the eye doesn't have to re-hunt. Because each AI clip is a fresh hallucination, **match your cut points to disguise model drift** — cut away from a face *before* the model starts melting it (clips degrade in the back half), and you'll never show the failure.

---

## 2. The Optical Transition Catalogue

"Optical" transitions are the ones that aren't a hard cut — historically created in the lab on an optical printer, now done in software (or, for us, in CSS/GSAP or by frame-matching). Here is the full set with the *meaning* each one carries and when it earns its place.

| Transition | What it is | What it *means* (when it's right) | When it's wrong |
|---|---|---|---|
| **Cut** | Instant A→B | Continuity, immediacy, default | Almost never wrong |
| **Dissolve / crossfade** | A fades out while B fades in, overlapping | Time passing; soft association; "meanwhile"; memory/dream onset | Between two shots in the same continuous moment (looks like a mistake) |
| **Fade to/from black** | A→black, or black→B | Hard act boundary; the curtain; a breath; finality | Mid-scene (kills momentum) |
| **Fade to white** | A→white | Transcendence, death, flashback, blinding revelation | When you mean ordinary time passing (use dissolve) |
| **Wipe** | B pushes A off with a moving edge | Deliberate theatricality; chapter break; retro/serial register | Drama that wants to feel real (it announces "movie") |
| **Iris** | Circle closes/opens on a point | Archaic/silent-era voice; storybook; focusing attention on one detail | Anything aiming for modern realism |
| **Match cut** | A cuts to B with matched shape or motion | Thematic rhyme; "these two things are linked" | When the two shots have nothing to say to each other |
| **Smash cut** | Abrupt cut to something jarringly different | Shock, punchline, rude awakening | Where you wanted a smooth flow |
| **Whip-pan / swish** | Cut hidden inside a fast motion-blur pan | Energetic transport between spaces; faux-continuity | Slow, contemplative scenes |
| **Morph** | A's pixels deform into B's | Transformation, time-lapse, dream logic, sci-fi | Realism (it's overtly synthetic) |
| **L-cut / J-cut** | Audio leads or lags the picture cut | Smoothing, anticipation, conversational realism | (almost always good — see below) |
| **Invisible/hidden cut** | A cut masked so totally it reads as one shot | The "oner" illusion; immersive unbroken time | When you actually want to feel the edit |

### The dissolve / crossfade — the grammar of time

A **dissolve** (in video, a **crossfade**) overlaps the tail of A with the head of B so they're briefly superimposed. Its inherited meaning is **a gap in time** — "later that day," a montage of weeks passing — and secondarily **association**: the superimposition literally blends two images, so the audience reads a link between them (a face dissolving to the ocean = this person and the sea are one idea). It's also the standard onset of dream/memory. The *length* carries meaning: a 12-frame (½-second) dissolve is a quick soft transition; a 3-second dissolve is luxuriant, dreamlike, the language of *Apocalypse Now*'s opening (Willard's face slowly superimposed with jungle and ceiling fan). Rule of thumb: dissolve when you want to feel *softness and passage*, cut when you want *now*.

### Fades — the act curtain

Fade-out/fade-in to black is the strongest punctuation a film has — the period at the end of a paragraph, sometimes the chapter break. It says *this unit is complete; reset*. Reserve it for genuine structural boundaries (act ends, major time jumps), because if you fade every scene you've made every scene feel like an ending and the film loses propulsion. Fade to *white* substitutes a different emotion: where black is closure/void, white is transcendence, overload, or the bleed into memory.

### The wipe — theatrical on purpose

A **wipe** moves a visible edge across frame to replace A with B. *Star Wars* made it iconic precisely because George Lucas wanted the Flash Gordon serial register — the wipe is honest about being a movie. Use it when your project *wants* to wink at its own artifice (adventure serials, retro pastiche, sports/entertainment montages). Used straight in a drama it reads as amateur, because it foregrounds the mechanism the drama is trying to hide.

### The iris — the museum piece

An **iris** is a contracting/expanding circular mask, a relic of the silent era used to open/close scenes or spotlight a detail. Today it carries "old film" or "storybook." Wes Anderson and *Looney Tunes* both deploy it knowingly. It's almost never the right *neutral* choice — it's always a stylistic statement.

### The smash cut — the rude awakening

A **smash cut** is a hard cut whose *content* is jarring: loud→silent, calm→chaos, dream→alarm clock. The cut itself is ordinary; the violence is in the juxtaposition. It's a comic and horror staple (the build-up to a scare that smash-cuts to a title card). It works because it weaponizes the brain's orienting response — maximal contrast across the join.

→ **AI APPLICATION.** Dissolves, fades, wipes, and irises are all **edit-side** operations — do them in HyperFrames/GSAP with `opacity` tweens, masked `clip-path` sweeps, or shader transitions, never in generation. A crossfade is two clips with overlapping `opacity` keyframes; a wipe is an animated `clip-path: inset()` or `polygon()` on the top clip; an iris is an animating `clip-path: circle()`. This is *better* than asking a video model to "dissolve," because the model has no concept of a clean compositing operation and will smear. **Reserve generation for the shots; reserve compositing for the joins.** The one exception worth baking into generation is the *morph* (next), which models do natively.

### The morph

A **morph** continuously deforms A's geometry/texture into B's — Michael Jackson's *Black or White* faces, the T-1000 in *Terminator 2*. Meaning: transformation, fluid identity, dream logic, time-lapse aging. Classic morphs needed hand-placed correspondence points; AI changed this completely.

→ **AI APPLICATION.** The morph is now a *native superpower* of first-frame/last-frame (FFLF) video models. Give Kling O1, Wan 2.x First+Last, Veo 3.1, or Seedance 1.5/2.0 your A image as the first frame and your B image as the last frame, and the model interpolates a morph between them along a single trajectory (verify — model versions/names current as of mid-2026; see §6). This is the cleanest morph workflow that has ever existed: no rig, no correspondence points. Use it for transformation beats, "ten years later" age-ups, object-to-object metaphors, and seamless scene-to-scene blends where you *want* the dream-logic register.

---

## 3. The Match Cut — The Intellectual Transition

A **match cut** is a hard cut where something *carries across the join*. Two flavors:

- **Graphic match:** the *shape/composition* of the outgoing frame rhymes with the incoming one. The textbook example is *2001: A Space Odyssey* — an ape's thrown bone (vertical, tumbling, against sky) cuts to an orbiting satellite (same shape, same screen position): four million years of human technology in one cut. Also: the spinning newspaper→spinning hubcap, the round porthole→round moon.
- **Action / movement match:** a *motion* continues across the cut. A character begins to sit in shot A and completes sitting in a different location/time in shot B; a door starts to close in one place and finishes closing in another. *Lawrence of Arabia*'s blown-out match cutting to a desert sunrise is the legendary version (technically a graphic+thematic match).

Why it's powerful: it makes the audience's brain do the work of connecting two ideas, and ideas the viewer assembles *themselves* land harder than ideas they're told. It's the editing-table cousin of metaphor.

The match cut is also the **invisible-cut family's smartest member** for AI, because a strong graphic or action match *hides the discontinuity* between two clips. If both clips share a dominant shape in the same screen position, the eye tracks the shape across the join and never audits whether the lighting or the world actually matches.

→ **AI APPLICATION — using a match cut to mask a cut between two AI clips.** This is one of the highest-leverage tricks in the whole pipeline. Procedure:
1. Decide the carry-over element — a circle, a vertical line, a hand reaching, a turning head — and its screen position (e.g. centered, occupying ~40% of frame height).
2. Generate clip A so it *ends* on that element in that position. The cleanest way: render A's intended **last frame as a still in an image model first**, composing the carry element exactly, then drive image-to-video toward it.
3. Generate clip B so it *begins* on a matching element in the same position — again, lock B's **first frame as a still** with the element matched, then animate forward.
4. Hard-cut A→B at the matched frames. Because the shape and position are continuous, the cut reads as intentional rhyme, and any mismatch in style/lighting is forgiven by the brain's shape-tracking.

For an **action match**, the trick is to make the *velocity vector* continue: A ends with the hand moving left-to-right exiting frame right; B begins with the hand entering frame left moving the same direction at the same speed. Models won't give you frame-perfect velocity, so cut on the moment of fastest motion (most blur) where the eye can least audit the seam — which is exactly the whip-pan principle below.

---

## 4. Whip-Pans, Swish Transitions & the Hidden "Oner" Cut

A **whip-pan** (or **swish pan**) is a camera pan so fast the image becomes motion-blur streaks. As a *transition*, you cut during the blur: A whips one way, B whips in the same direction, and the cut hides inside the smear because the eye can't resolve detail at that speed. It reads as one continuous energetic move sweeping you from place to place. This is the engine of *Birdman*'s apparent single take and the workhorse of trailer and music-video editing.

The **invisible / hidden cut** generalizes this: any moment where the frame is briefly unreadable is a place to hide a cut. The toolkit:

- **Motion blur** — the whip-pan (Birdman, every kinetic trailer).
- **Object obstruction** — a body, a wall, a passing truck fills the frame to solid; cut while it's full. *1917* hides most of its ~34 cuts this way (a tree trunk, a soldier's back, walking into a dugout's darkness). Roger Deakins built the blocking around these "pass-throughs."
- **Whip into darkness/light** — pan into a shadow or a blown-out window and cut in the black/white.
- **Match-on-action through a doorway / behind a pillar** — cut as the subject is occluded.

These are the *deliberately invisible* transitions — the goal is for the audience to never know an edit happened, to feel unbroken immersive time. That illusion of one continuous take produces a specific anxiety/presence (you can't escape via a cut), which is why *1917* and *Birdman* feel relentless.

→ **AI APPLICATION — faking the whip-pan and hiding cuts between clips.** Two routes:

- **Edit-side fake whip:** take the last ~6–10 frames of clip A and first ~6–10 of clip B, apply a strong directional motion blur and a fast horizontal slide (in code: a quick `transform: translateX()` + CSS/SVG motion-blur filter, or a GSAP timeline ramping position and blur), cutting at the blur peak. You don't need the model to pan at all — you manufacture the swish in compositing. This is the most reliable way to get a whip transition in an AI workflow.
- **Generation-side real whip:** prompt A to *end* with a fast pan in a direction (`camera whip-pans hard to the right, heavy motion blur`) and B to *begin* with a matching fast pan in the same direction. Then cut at the blurriest frames. Veo 3.1, Kling 3.0, and Runway Gen-4.5 all render convincing whip-blur (verify — as of mid-2026). The blur is your friend twice over: it hides the cut *and* it hides the model's lighting/identity drift between clips. For the **object-obstruction** hidden cut, end A on something passing across the lens (`a figure in a dark coat passes directly in front of the camera, filling the frame`) and start B emerging from the same fill — cut on the solid frame.

See **07-camera-angles-and-movement.md** for whip-pans as a camera move rather than a transition.

---

## 5. L-Cuts, J-Cuts & Sound-Led Transitions

Picture and sound don't have to cut at the same instant — and they usually shouldn't. The two named cases (the names come from the shape the clips make on a two-track timeline):

- **J-cut:** the *audio of shot B starts before its picture*. You hear the next scene's sound first — a phone ringing, the ocean, the next speaker's voice — then the image arrives. It creates **anticipation** and pulls you forward into B. The "J" is the audio track extending left under A.
- **L-cut:** the *audio of shot A continues after its picture has cut to B*. You're now looking at the listener while the speaker is still talking; the previous scene's ambience lingers under the new image. It creates **continuity and reaction** — the bread-and-butter of every dialogue scene (you cut to the reaction while the line finishes).

Why they matter more than any visual transition for *realism*: real perceptual experience never hard-cuts sound and vision together. Splitting the edit points makes the join feel organic and lets sound do narrative work — the J-cut is the single most efficient tool for momentum across a scene change. (Full treatment of sound's role in editing rhythm: **10-editing-theory.md**.)

→ **AI APPLICATION.** This is *purely* an edit/code decision and one AI filmmakers under-use. On your timeline, slide the audio clip's in/out points a few frames off the picture cut: extend the previous clip's dialogue/ambience under the next shot (L-cut), or pull the next shot's sound forward under the current picture (J-cut). In HyperFrames/code, that means decoupling the audio element's `currentTime`/start from the visual scene's start. Generate dialogue and SFX as separate stems where you can (or extract them), so you can freely offset them. A J-cut bringing the next scene's signature sound in early is the cheapest way to make two unrelated AI clips feel causally linked.

---

## 6. The Kinetic-Typography Fast-Cut Trailer Style

This is the in-theatre "prop-montage" trailer register: hard beat-synced cuts, type that *slams* onto the screen on the downbeat, freeze frames, speed ramps, light leaks, glitch/RGB-split, all riding a music bed that drives the entire rhythm. It is the most produced style in modern marketing and the one Yuval explicitly wants. Here is how it's actually built.

### The music bed *is* the edit

The defining principle: **the music is authored first and the cuts are slaved to it.** You do not cut to taste and add music; you find the track (or a stinger/braam-driven trailer cut), mark its beats and structural hits, and place every cut and every text slam on those marks. The relationship is:

- **Cut on the beat** for the body of the montage (every ¼, ½, or whole bar depending on energy).
- **Reserve the big structural hits** (the "braam," the bass drop, the downbeat after a silence) for the *biggest* events — the title card, the hero reveal, the hardest type slam.
- **Use the build → drop structure.** Trailers mirror EDM/score structure: a build with accelerating cuts and rising risers, a moment of **silence/freeze** (1–3 frames or a held black), then the **drop** where the title slams and the montage goes fastest. The silence-before-the-drop is the most important beat in the whole piece — contrast makes the drop hit. (This is the macro arousal-arc from **05-neuroscience-honest.md** rendered as editing.)

### The component vocabulary

| Element | What it is | How it sells the beat |
|---|---|---|
| **Beat-synced hard cuts** | Cuts landing exactly on transients | The spine; the eye learns the pulse and the brain entrains to it |
| **Type-on-impact** | A word/line slams in (scale-down + blur-to-sharp) on the downbeat | The text *hits* with the kick; biggest single payoff per beat |
| **Freeze frame** | Motion stops dead on a hit, often with a flash/sound | Punctuation; gives the eye a held image to read the title against |
| **Speed ramp** | Speed accelerates then snaps to slow (or vice versa) into a beat | Manufactures emphasis; the "ramp into the hit" is the trailer's signature move |
| **Light leak / flash frame** | 1–3 white/colored frames at a cut | Hides the cut *and* punctuates it; reads as energy and analog warmth |
| **Glitch / RGB-split (chromatic aberration)** | Frame tears; red/green/blue channels offset | Digital-tension register; great as a 2–4 frame transition stinger on a beat |
| **Shake / kick** | A quick positional jolt on the transient | Adds physical impact, like the camera got hit |

### Kinetic typography specifics

Kinetic typography is animated text whose *movement and timing carry meaning* — not decoration, but the words performing themselves. For the trailer register the rules are:

- **One idea per card.** A word or a short line, not a paragraph. The eye gets ~0.3–1.0s.
- **Slam, don't drift.** Type that fades in gently has no impact; type that scales down hard with a blur→sharp and a micro-overshoot *hits*. The animation should resolve *on* the beat, not start on it (so the settle lands with the transient).
- **Heavy display type, high contrast.** Condensed/black weights (Anton, Druk-style), mostly uppercase, tracked tight.
- **Choreograph against the music's contour**, not just its beats — text can ride a riser (scale up with the build) and snap on the drop.

Reference styles to study: trailer houses' AAA game/film teasers (the "braam + black + title slam" structure popularized post-*Inception*); Apple/tech keynote sizzle reels (clean type slams on minimal beats); sports-hype edits and the After Effects "velocity edit" school (speed ramps + whip transitions + glitch); music-video lyric videos for pure kinetic-type craft.

→ **AI APPLICATION — building the kinetic trailer.** Split the labor cleanly:

- **Generate** the footage shots (the "props": product hero, character beats, environment) as short clips, *over-generating* options so you can cut the best 0.3–1.0s slivers.
- **Build the kinetic layer in code (HyperFrames/GSAP), never in a video model.** Text animation, glitch, RGB-split, light leaks, freeze frames, speed ramps, and shakes are all deterministic compositing operations — a model will smear them; code makes them frame-exact. RGB-split = three duplicated text layers in `mix-blend-mode` tinted R/G/B with tiny offset `transform`s; glitch = rapid `clip-path` slicing + offset; light leak = a 2–3-frame white/orange overlay flash; type slam = a GSAP tween on `scale`+`filter: blur()` with an `expo`/`back` ease resolving on the beat frame.
- **Beat-sync to an AI music bed:** generate or license the track first, then get its tempo and beat grid. Run an onset/beat-detection pass (e.g. `librosa.beat.beat_track` / `onset_detect`, or `aubio`) over the audio to get beat timestamps in seconds. Convert to frames (`frame = round(t * fps)`) and place every cut and every text-resolve on those frames. In a code timeline this is exact; this is the entire reason the code-driven approach beats hand-editing for this style. Put the title slam on the strongest detected hit after the pre-drop silence.

This style is also the home of the **yuv-fomo-teaser** house pattern referenced in Yuval's memory — this chapter is the craft foundation under it; go there for the brand-specific recipe.

---

## 7. Keyframes & Easing — How a Transition Is *Shaped*

Everything above assumed transitions have a *shape over time*. That shape is controlled by **keyframes** and **easing** — the mechanics any code-driven (or NLE) transition is built from.

### What a keyframe is

A **keyframe** is a marker that says "at *this* time, *this* property has *this* value." If you set two keyframes — opacity 0 at t=0s and opacity 1 at t=1s — the software **interpolates** (computes) every in-between frame. The word comes from traditional animation: the lead animator drew the *key* poses; assistants ("inbetweeners") drew the frames between. Today the computer is the inbetweener. A crossfade is two opacity keyframes; a wipe is two keyframes on a `clip-path` value; a slide is two keyframes on `translateX`.

### What easing is — and why it sells the transition

**Easing** is the *rule for how the value moves between keyframes* — the velocity curve. **Linear** easing means constant speed: the value covers equal distance each frame. Linear motion looks *dead and robotic* because nothing in the physical world starts and stops instantly — objects have mass, they accelerate and decelerate. This is the single most important thing to understand about why amateur animation looks fake: **it's almost always linear easing.**

- **Ease-in (accelerate):** starts slow, speeds up. Feels like something gathering momentum / leaving.
- **Ease-out (decelerate):** starts fast, slows to a stop. Feels like something arriving and settling — the most *satisfying* default for things entering.
- **Ease-in-out:** slow–fast–slow. The natural arc for a complete move.
- **Overshoot / back / elastic:** goes *past* the target then settles back. Adds snap, life, "pop" — the soul of the type-slam (it punches in a hair too far, then settles on the beat).

A transition with the *right easing reads as intentional and physical*; the same transition with linear easing reads as a software default. The trailer type-slam *is* an ease-out/back curve resolving on a beat; a luxurious dissolve is a gentle ease-in-out; a smash is so abrupt it's nearly instantaneous (a steep curve). The shape of the curve carries as much meaning as the transition type.

Under the hood, software easing is usually a **cubic Bézier curve** (two control points defining the velocity profile) — CSS's `cubic-bezier(.17,.67,.83,.67)`, the named `ease`, `power2.out`, `expo.out`, `back.out(1.7)` in GSAP, or AE's graph-editor handles. Same math everywhere: the control points bend the value-vs-time line.

→ **AI APPLICATION.** All easing happens in the **edit layer** — a video model has no easing controls; you get whatever motion it hallucinated (and it tends toward floaty, near-linear drift, which is part of why raw AI clips can feel lifeless). So: (1) for any *text/graphic/transition* element, animate it in GSAP/CSS with deliberate eases — `back.out`/`expo.out` for slams and entrances, `power2.inOut` for dissolves — never leave it linear (see the **gsap** skill for the curve catalogue). (2) for the *generated footage itself*, you can't keyframe the internal motion, but you *can* shape the clip's overall presence — its on-timeline `opacity`, `scale`, and position — with eases to add the snap the model didn't. A speed ramp on an AI clip is an eased remap of its playback time: hold near-frozen, then `expo.in` into real-time on the beat. Easing is where you re-inject the physical intentionality AI generation tends to launder out.

---

## 8. The Decision Rule: Bake-In vs. Edit-In (AI Master Summary)

The organizing question for the AI filmmaker on *every* transition: **does this belong inside generation, or on the edit timeline?**

| Do it in **generation** (first/last-frame, prompt) | Do it in the **edit** (HyperFrames/GSAP/code) |
|---|---|
| **Morph** (FFLF interpolation A→B) | **Cut** (butt two clips) |
| **Real whip-pan blur** (prompt both clips to pan) | **Dissolve / crossfade** (opacity keyframes) |
| **Match-cut content** (compose A's last frame & B's first as stills) | **Fade to black/white** (opacity to solid) |
| **Object-obstruction fill** (end on something covering lens) | **Wipe / iris** (animated `clip-path`) |
| Continuous in-shot camera moves | **Fake whip** (slide + motion-blur on tails) |
| | **Kinetic type, glitch, RGB-split, light leaks, freeze, speed ramp, shake** |
| | **L/J audio offsets** (decouple audio in/out) |
| | **All easing** |

**The three load-bearing AI techniques to internalize:**

1. **First/last-frame matching is your transition control surface.** The most reliable way to control *any* AI transition is to lock the *frames at the join as stills first* (in an image model), then drive video toward/from them. A match cut, a clean morph, a hidden object-fill cut — all become reliable the moment you stop hoping the video model gets the boundary frame right and instead *specify* it.

2. **The match cut (and the whip/obstruction hidden cut) is how you hide clip-to-clip drift.** Shared shape, shared motion vector, or a frame of blur/solid at the join lets two independently-hallucinated clips read as one continuous world. This is structural, not cosmetic — design your shot list so consecutive clips share a carry-over element.

3. **Build the kinetic/transition layer in code, slaved to a beat grid.** Detect the music's beats, convert to frames, and put every cut and every eased text-slam on a beat. Generation provides the imagery; deterministic code provides the rhythm, the type, and the polish — because that is the half AI models smear and code makes frame-exact.

### Current model landscape for transition work (verify — as of mid-2026)

| Model | Transition relevance | Note |
|---|---|---|
| **Kling 3.0 / Kling O1** | FFLF dual-keyframe; O1 is the dedicated first→last frame variant (~$0.112/sec) | Strongest for morph & defined-trajectory transitions |
| **Veo 3.1 / Veo 3.1 Fast** | Optional last frame; native synced audio (helps J/L-cuts) | Best all-rounder; only model doing 48kHz dialogue |
| **Wan 2.x First+Last** | Explicit first+last frame required/optional; multi-image input | Open-ecosystem FFLF workhorse |
| **Seedance 1.5 Pro / 2.0** | Optional last frame; top of quality leaderboards early 2026 | Strong motion for whip/action matches |
| **Runway Gen-4.5** | Keyframes (first/middle/last), motion brush, camera control | Best granular creative control |
| **Pika 2.x (Pikaframes)** | First & last frame control | Good for stop-motion/transition looks |

Note: OpenAI announced Sora's web/app sunset (app April 26, 2026; API Sept 24, 2026) — do not architect a pipeline around it (verify).

---

**Bottom line.** Master the cut first; it is invisible because it mirrors how you already see, and it is also the AI pipeline's cheapest, most drift-tolerant join. Every other transition must *buy something* — time, association, theatricality, rhyme, or the oner illusion — or it is friction. In the AI workflow, push *morphs and frame-matched joins into generation*, push *every composited transition, all kinetic type, and all easing into code on a beat grid*, and use the *match cut and the blur/obstruction hidden cut as your seam-hiders* between independently generated clips. The transition is where the film's rhythm lives and where the AI's seams either show or vanish.

---

### Sources
- StudioBinder — *Types of Editing Transitions in Film*: https://www.studiobinder.com/blog/types-of-editing-transitions-in-film/
- No Film School — *Where Were the Hidden Cuts in '1917'?*: https://nofilmschool.com/1917-camera-edits-oner
- No Film School — *Hidden Editing Techniques in 'Birdman'*: https://nofilmschool.com/2015/10/a-closer-look-hidden-editing-techniques-in-birdman
- ScreenRant — *1917: All 34 Hidden Cuts*: https://screenrant.com/1917-movie-secret-cuts-one-shot-trick-scenes-where/
- Plotwit — *Invisible Editing Techniques*: https://plotwit.com/invisible-editing-techniques/
- IK Agency — *Kinetic Typography: Complete Guide 2026*: https://www.ikagency.com/graphic-design-typography/kinetic-typography/
- Pixflow — *How to Create Kinetic Typography in After Effects*: https://pixflow.net/blog/how-to-create-stunning-kinetic-typography-in-after-effects/
- fal.ai — *Kling O1: First Frame to Last Frame*: https://fal.ai/models/fal-ai/kling-video/o1/image-to-video
- Runway — *Creating with Keyframes on Gen-3*: https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3
- ZSky AI — *First Frame Last Frame AI Video: Complete Guide*: https://zsky.ai/blog/first-frame-last-frame-ai-video
- Get AI Perks — *Best AI Video Generators 2026: Sora 2 vs Veo 3.1 vs Kling 3.0 vs Runway*: https://www.getaiperks.com/en/blogs/44-best-ai-video-generators-2026
- LLM-Stats — *Best AI for Video Generation 2026 (leaderboard)*: https://llm-stats.com/leaderboards/best-ai-for-video-generation
