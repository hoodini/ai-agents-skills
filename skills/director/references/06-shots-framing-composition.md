# Shot Sizes, Framing & Composition

The frame is the only thing the audience can see. Everything outside it does not exist for them. That single fact is the root of all framing craft: every decision about what you include, exclude, and where you place it is a decision about what the viewer is *allowed* to think and feel. This chapter is the grammar of that decision. It moves from the shot-size ladder (how much of the world you show), through composition (where you put things inside the rectangle), to the continuity grammar that keeps multiple frames legible as one continuous space — the part most AI filmmakers break without noticing — and ends with aspect ratio and the AI pipeline for executing all of it.

A first principle, before any rule: framing is a tool for directing **attention** and assigning **psychological distance**. Wide = "observe this world." Close = "feel this person." Everything else is gradation between those poles. Hold that intuition; the rules below are just refinements of it.

---

## 1. The Shot-Size Ladder

Shot size is defined relative to the human figure — how much of a person (and how much surrounding space) the frame contains. The reason size maps to emotion is **proxemics**: anthropologist Edward T. Hall showed that humans assign social meaning to physical distance. Intimate distance (under ~0.5m) is reserved for lovers, family, threat. Personal distance (~0.5–1.2m) is for friends. Social distance (~1.2–3.6m) is for acquaintances and strangers. Public distance (3.6m+) is for performers and authorities. A camera inherits these codes. A close-up *is* intimate distance — that is literally why it feels intimate. This is not mysticism; it is your nervous system reading the same spatial cue it reads in life.

| Shot | Abbrev | Frames | Primary job | Emotional register |
|---|---|---|---|---|
| Extreme close-up | ECU | An eye, lips, a detail of the face/object | Force attention onto one element; reveal micro-emotion | Maximum intensity / unease |
| Close-up | CU | Head and a little shoulder | Read emotion; the "money" reaction shot | Intimacy, identification |
| Medium close-up | MCU | Head to mid-chest | The conversational default; reaction + a little body language | Engaged, neutral-intimate |
| Medium shot | MS | Waist up | Subject + gesture + some context | Conversational, balanced |
| Medium-long / "cowboy" | MLS | Mid-thigh up | Body language with a touch of environment | Confident, ready |
| Long / full shot | LS / FS | Whole body, head to feet | Subject *in* a space; physical action | Observational |
| Wide shot | WS | Subject small within a large space | Geography, isolation, scale | Detached, contemplative |
| Extreme wide / establishing | EWS | Subject tiny or absent; the world dominates | Set place, time, scale; orient the viewer | Epic, lonely, or ominous |

The "cowboy" shot (MLS) is named for Westerns: framed at mid-thigh so the gun belt and holster are in frame, ready to draw. That is the lesson in miniature — shot size is chosen for *what the story needs you to see*.

### Why the close-up is the most powerful weapon

The CU has no equivalent in theater — you cannot lean over and inspect an actor's eye from the stalls. Cinema invented it, and it rewires the contract: the audience is no longer watching a person, they are *inside* a person's emotional space. Carl Theodor Dreyer's *The Passion of Joan of Arc* (1928) is built almost entirely of close-ups on Maria Falconetti's face — the relentless intimacy is the film's entire argument. Sergio Leone weaponized the opposite tension: in *Once Upon a Time in the West* (1968) he cuts between vast EWS desert vistas and ECUs of sweating eyes, and the violence of the jump from public-distance to intimate-distance *is* the suspense. Spielberg's rule of thumb — save your tightest, most committed close-up for the single most important emotional beat of the film, so it lands like a punch rather than wallpaper — is sound craft: a tool used constantly stops being a tool.

### Specialized framings

- **Two-shot** — two subjects in one frame. The *relationship* is the subject. The space between them, who is higher, who faces whom, all carry meaning. A balanced two-shot reads as equality; an unbalanced one (one dominant, one small) reads as power imbalance.
- **Insert** — a CU/ECU of an object cut into a scene: a hand turning a key, a text message, a gun on a table. Inserts carry plot information the wider shot can't show, and they control pace (a cut to an insert is a beat of held breath).
- **Master shot** — a single wide take covering the *entire* scene's action, start to finish, with all actors. It is the safety net and the spatial bible: the editor cuts CUs and MSs against it, and it silently teaches the audience where everyone is. In AI filmmaking the master shot is conceptual rather than literal, but the discipline survives — see §5.

→ **AI APPLICATION.** Image and video models default to a *medium-ish, eye-level, centered* framing because that dominates their training data. If you do not specify shot size, you get this bland mean. Name the shot size explicitly and early in the prompt. Models respond to professional vocabulary: "extreme close-up of a weathered eye, iris filling the frame," "wide establishing shot, lone figure small against a brutalist plaza." Veo 3.1's recommended prompt order is **cinematography → subject → action → context → style → ambiance** — i.e. lead with the shot. Be aware models conflate "close-up" with "portrait crop": if you want a *true* ECU (just an eye), say "iris fills the frame, skin texture visible, eyelashes in focus" rather than trusting the label. For inserts, prompt the object in isolation with shallow depth of field ("macro insert shot of a brass key turning in a lock, rest of frame thrown out of focus"). (Models/versions verify — as of mid-2026: Veo 3.1, Kling 3.0, Runway Gen-4.5, Sora 2 Pro.)

---

## 2. Composition: Where Things Go Inside the Rectangle

Composition is the arrangement of visual elements within the frame to guide the eye and create meaning. The eye does not scan a frame evenly; it is pulled by contrast, faces, motion, lines, and learned reading order. Composition is the craft of *predicting and steering* that pull.

### Rule of thirds — and the honest version

Divide the frame into a 3×3 grid with two horizontal and two vertical lines. Place key elements on the lines or at the four intersection points. The horizon goes on the lower third (big sky) or upper third (big foreground), rarely dead center.

The honest version: the rule of thirds is a useful **default that avoids the dead, static feeling of perfect centering**, not a law of beauty. The common claim that it derives from the golden ratio is **false** — thirds (0.333) and the golden ratio (0.382 / 0.618) are simply different numbers, and the rule of thirds was articulated as a painting heuristic (John Thomas Smith, 1797) independently. Its real value is practical: off-center placement creates an implied imbalance the eye finds dynamic, and it leaves room for the subject to look or move *into*. Treat it as training wheels you outgrow, not gospel.

### The golden ratio / phi grid

The golden ratio (φ ≈ 1.618) produces the phi grid: like the thirds grid but with the inner lines pulled closer to center (proportions roughly 1 : 0.618 : 1). The related **Fibonacci spiral** is sometimes overlaid to argue a composition is "naturally harmonious." Be skeptical. There is real evidence humans show mild preference for certain proportions, but the popular claim that φ is a universal hardwired law of beauty is **overstated and largely retrofitted** — analysts can fit a spiral onto almost any competent image after the fact. The practical takeaway: phi placement sits subtly tighter to center than thirds and can feel marginally more "settled." Use it as an alternative default, not a magic key.

### Leading lines

Lines in the image — roads, rivers, architecture, a gaze, a row of columns — pull the eye along them toward (or away from) the subject. Roger Deakins is the modern master: the receding road in *No Country for Old Men*, the corridor geometry throughout *1917*. A leading line that terminates on the subject makes that subject feel inevitable; a line that leads to empty space creates unease or longing.

### Symmetry vs asymmetry

Perfect symmetry reads as order, control, artifice, sometimes the uncanny. **Wes Anderson** built a whole grammar from dead-center one-point-perspective symmetry (*The Grand Budapest Hotel*) — it signals a fastidious, doll-house world under authorial control, and the rare break from it lands hard. Stanley Kubrick used one-point symmetry (*The Shining* corridors) to make ordered spaces feel *wrong*. Asymmetry, by contrast, reads as natural, tense, alive. **Akira Kurosawa** composed in dynamic asymmetry and triangles, distributing figures and motion across the frame so the eye keeps moving (*Seven Samurai*, *Ran*) — his frames feel like living organisms, not arrangements. Neither is "better"; they are opposite statements. Symmetry says *this is composed*; asymmetry says *this is happening*.

### Balance and visual weight

Every element has visual weight: brightness, size, saturation, faces, motion, and sharp focus all add weight. A composition is "balanced" when weights distribute so the frame doesn't feel like it will tip. Crucially, a *small* high-contrast element can balance a *large* dull one — a single lit face balances a wall of shadow (the entire logic of chiaroscuro and film noir). Deliberate *imbalance* is a tool: weight everything to one side and the empty side feels charged with absence.

### Frame within a frame

Use elements in the scene — doorways, windows, mirrors, arches, foreground objects — to create a second frame around the subject. It concentrates attention, adds depth, and carries metaphor: a character framed in a doorway can read as trapped, watched, or separated. *The Searchers* (1956) opens and closes on a doorway framing Ethan against the desert — the frame-within-frame literally states his exile from domestic life.

### Depth layering: foreground / midground / background

A flat frame is dead. Stack visual information in three planes — something near, something mid, something far — and the 2D rectangle reads as 3D space. A foreground element (a branch, a shoulder, a candle) the camera shoots *past* creates immediate depth and a sense of the camera being *in* the world rather than observing it. Gregg Toland's deep-focus work in *Citizen Kane* (1941) kept all three planes sharp simultaneously so the audience could read foreground, midground, and background action at once — composition as storytelling rather than just decoration.

### Negative space

Empty area around the subject. Lots of negative space isolates and diminishes the subject (loneliness, vulnerability, scale) or creates calm and breathing room. *Drive* (2011) and much of Sofia Coppola's work use generous negative space to hold characters in emotional suspension. Negative space is not "wasted" frame — it is active, and it is one of the strongest mood levers you have.

### The headroom / lead room family

Three related rules govern how a subject sits in the frame:

- **Headroom** — the gap between the top of the head and the top of the frame. Too much makes the subject sink and the frame feel empty; too little crops the head and feels claustrophobic. The fix for intensity is *deliberately* tight headroom (or cropping the forehead) in a CU.
- **Lead room / nose room** — when a subject faces or looks to one side, leave space *in front* of the face (on the side they look toward). The eye and the implied gaze need somewhere to go. Frame them looking *out* of the short side instead and the shot feels wrong, trapped, oppressive — a deliberate violation directors use for unease.
- **Look room** is the synonym for lead room applied to a static gaze; **lead room** also covers space in front of a *moving* subject (leave room ahead of a walking figure so they move *into* the frame, not *out* of it).

→ **AI APPLICATION.** Composition is highly promptable but the model will silently default to centered, balanced, single-plane framing unless you fight it. Tactics that work in current image models (Midjourney V7, Nano Banana 2 / Gemini image, Flux):

- **State the composition principle by name**: "rule of thirds composition, subject on left third," "perfectly symmetrical one-point perspective, subject dead center, Wes Anderson style."
- **Force depth explicitly**: name all three planes — "foreground: out-of-focus reeds; midground: a woman on a jetty; background: distant storm clouds." Models do not add depth layers on their own; you must enumerate them.
- **Specify lead/nose room**: "medium close-up, subject looking to the right, generous negative space on the right side of the frame." Without this, models center faces and kill the gaze direction.
- **Frame-within-frame and leading lines** respond to literal description: "shot through a doorway," "a road leading from foreground to the figure at the vanishing point."
- **Negative space**: "minimalist composition, single small figure in the lower-left, vast empty sky," reinforced with `--ar 21:9` or `--ar 2.39:1` so the model has room to leave empty. In Midjourney, parameters go at the end with no punctuation; for composition control prefer describing intersections ("eyes on the upper-third line") over relying on the model to apply a named grid.

A practical truth: image models are *far* better at composition than video models, which is why the dominant 2026 workflow is **compose a still you control, then animate it** (image-to-video) — see §5.

---

## 3. Continuity Grammar: Keeping Multiple Frames Legible

Everything above concerns a single frame. The moment you cut between frames, a second body of rules governs whether the audience can still parse the *space*. These are not stylistic preferences; they are the difference between coherent and disorienting. They are also exactly the rules AI filmmaking breaks by default, because each clip is generated in isolation with no memory of the others.

### The 180-degree rule (the axis of action)

Imagine an invisible line — the **axis of action**, or "the line" — running through the scene along the main direction of action or between two people in conversation. Keep all cameras on **one side** of that line. Do this and screen direction stays consistent: a character on the left stays on the left across cuts, a car moving right keeps moving right, two people in dialogue keep facing each other (A looks frame-right, B looks frame-left). The brain stitches the shots into one coherent space.

**Cross the line** and everything flips: the character jumps to the other side of the frame, the car appears to reverse direction, the two speakers suddenly look the same way and seem to no longer be talking to each other. The audience gets a half-second of subliminal disorientation. The classic football/soccer example: if the broadcast cut to a camera on the opposite touchline, the teams would appear to suddenly attack the wrong goals.

Crossing the line is therefore also a **tool**: a deliberate axis break can signal a psychological rupture, a shift in power, a descent into chaos. Jonathan Demme broke convention in *The Silence of the Lambs* with direct-to-lens looks that put the viewer *on the line*, making conversations feel like interrogations of the audience. Use it on purpose, never by accident.

### The 30-degree rule

When you cut between two shots of the *same* subject, move the camera at least **30 degrees** around it (and ideally change shot size too). Cut from two angles less than 30° apart and the result looks like a small glitch — a **jump cut** — because the framing is too similar to read as a new perspective but too different to read as continuous. The 30° minimum guarantees the new shot reads as a genuinely new viewpoint. (Godard's *Breathless* made deliberate jump cuts a style; that proves the rule by violating it knowingly.)

### Eyeline match

When a character looks off-screen and you cut to what they see, the angle and height of the look must match. If a character looks *down* at something, the cut to the object should be from a high angle (their POV looking down). A mismatched eyeline — character looks up-left, cut to an object framed straight-on at eye level — breaks the spatial illusion. Eyeline match is what makes "she looked at the photograph → [the photograph]" read as a single connected thought.

### Screen direction

The umbrella concept the 180° rule serves. **Screen direction** is the consistent left/right orientation of movement and gaze. A character who exits frame-right should re-enter the next shot frame-left (continuing the same journey). A chase where pursuer and pursued both move screen-right reads as a chase; flip one and they appear to run *at* each other. Directional consistency across an entire sequence — even across a cut to a totally different location — is how the audience knows "this is still the same trip / the same fight / the same conversation."

→ **AI APPLICATION.** This is the hardest discipline in AI filmmaking and the one beginners ignore. Each generated clip knows nothing about the others, so left/right consistency, eyelines, and the axis of action are *yours* to enforce manually. Concrete techniques:

- **Maintain a written axis bible** per scene: "Axis runs east–west. Hero is always camera-LEFT facing RIGHT; antagonist always camera-RIGHT facing LEFT." Bake the direction into *every* shot prompt: "...the hero on the left side of frame, looking screen-right toward the antagonist."
- **Encode movement direction in every clip**: "...walking from left to right across frame." If the next location should continue the journey, prompt "...continues walking left to right." Re-entering subjects: have them exit one side and prompt the next clip to bring them in from the opposite side.
- **Use first-frame / last-frame keyframing** to lock continuity. Veo 3.1 and Kling 3.0 support start-image + end-image generation: provide the end frame of clip A as the start frame of clip B and the spatial layout (who's where, facing where) carries across the cut. This is the single most reliable way to preserve screen direction across separately generated clips.
- **Generate coverage from one reference, not from scratch.** Runway Gen-4.5's reference + "Coverage" workflow generates multiple camera angles (wide, medium, CU) of the *same* composition from one description, holding character, lighting, and spatial relationships — its consistency engine is the closest current tool to a real master-shot-plus-coverage method. Prompt the angles explicitly ("wide from behind, following; then medium of his face looking screen-right") and keep them on one side of your stated axis.
- **For eyeline matches across two clips**, specify the look direction and angle in both: clip A "she looks down and to the left"; clip B (the POV) "high-angle looking down at the photograph on the table." Mismatched height is the most common AI eyeline error — state the camera height in both.
- **Check the cut, not the clip.** A clip can look great alone and still flip the axis against its neighbor. Review pairs of adjacent clips for left/right consistency before committing.

---

## 4. Aspect Ratio and Its Feel

Aspect ratio is the width-to-height proportion of the frame. It is not neutral packaging — the *shape* of the rectangle changes what compositions are possible and how the image feels.

| Ratio | Name | Feel / use |
|---|---|---|
| 1.33:1 (4:3) | Academy / "full frame" | Old TV and pre-1953 cinema. Taller, intimate, "boxed-in"; now used for period, nostalgia, or claustrophobia (*The Lighthouse*, 2019, went even tighter to 1.19:1) |
| 1.85:1 | Standard widescreen | The default theatrical "flat" frame; slightly wider than HD, unobtrusive, naturalistic |
| 1.78:1 (16:9) | HD / TV | The screen you're probably on; the practical default for streaming and YouTube |
| 2.39:1 | Anamorphic "Scope" / CinemaScope | The epic, cinematic feel. Wide horizon, room for two faces at opposite edges, hard to fill — demands deliberate composition. Westerns, sci-fi, prestige drama (*Blade Runner 2049*, *Dune*) |
| 9:16 | Vertical | Phone-native (TikTok, Reels, Shorts). Hostile to landscape; *forces* tight, single-subject, stacked-vertical compositions and faces |

The wider the frame, the more it suits *environment and relationship* (two people separated across a 2.39:1 frame is a whole scene); the taller/narrower the frame, the more it suits *the single figure* and confinement. Directors switch ratios within a film for meaning: *The Grand Budapest Hotel* changes aspect ratio per time period; *Mommy* (2014) snaps from a boxed 1:1 to widescreen at a moment of liberation.

A specific consequence for vertical: 9:16 has almost no horizontal room, so EWS and two-shots barely work and the rule of thirds collapses toward a vertical stack (action zone center, text top/bottom). This is why "shoot horizontal, crop to vertical" usually fails — the original composition wasn't built for the shape.

→ **AI APPLICATION.** Set ratio explicitly and *compose for it*. In Midjourney use `--ar 2.39:1` (or `--ar 21:9` ≈ scope), `--ar 16:9`, `--ar 4:3`, `--ar 9:16`; the parameter goes at the very end with no punctuation. In video models, choose the model's native ratio support — Veo 3.1 outputs native landscape and portrait (and 4K), Kling 3.0 native 4K — rather than generating 16:9 and cropping, which destroys your composition. The big discipline: **generate at the final delivery ratio from the start.** If the deliverable is a vertical reel, prompt 9:16 and compose single-subject, vertically-stacked frames; do not generate a beautiful 2.39:1 shot and crop it to a phone — you will amputate the composition the model built. For dual delivery (16:9 + 9:16), generate twice with ratio-appropriate compositions rather than one master crop.

---

## 5. Putting It Together: The "Shots, Not Scenes" Discipline

The single biggest mindset shift for AI filmmaking is this: **you do not generate scenes, you generate shots.** A novice prompts "a detective interrogates a suspect in a dark room" and gets one undirected, medium, centered clip. A director decomposes that into a shot list — EWS of the room to establish; MS two-shot across the table to set the axis; CU of the detective (on the left, looking screen-right); reverse CU of the suspect (on the right, looking screen-left); insert of a sweating hand; back to CU for the break — and prompts each one with its size, composition, axis position, and movement explicitly stated. This is exactly the master-plus-coverage logic of §1 and §3, ported to a pipeline where the model is your camera operator and you are the director who must specify everything the operator would otherwise know.

The reliable 2026 workflow that respects every principle above:

1. **Design the shot list** (size + composition + axis/screen-direction for each shot) before generating anything.
2. **Compose the key still in an image model** you can control tightly (Midjourney/Nano Banana 2/Flux), because image models obey composition far better than video models.
3. **Animate via image-to-video** (Veo 3.1, Kling 3.0, Runway Gen-4.5), using first/last-frame keyframes to chain shots and preserve screen direction across cuts.
4. **Hold character and space** with a reference image / Runway Coverage so coverage angles stay consistent.
5. **Review adjacent pairs** for axis and eyeline before assembling — the line is broken at the *cut*, not in the clip.

For how these shots are then cut together — pacing, match cuts, the Kuleshov effect — see `10-editing-theory.md`. For how light and lens shape the same frame, see the camera/lighting chapters. For how movement (dolly, crane, handheld) interacts with framing, see the camera-movement chapter. Framing decides *what* the audience sees; the rest of the bible decides how it moves and how it's joined.

---

### Sources

- [Best AI Video Generators 2026 (Veo 3.1, Kling 3.0, Sora 2, Seedance) — AI/ML API](https://aimlapi.com/blog/best-ai-video-generators-2026-veo-3-1-kling-sora-2-seedance-more-compared)
- [AI Video Generation 2026: Sora 2 vs Veo 3.1 vs Kling 3.0 — Lushbinary](https://lushbinary.com/blog/ai-video-generation-sora-veo-kling-seedance-comparison/)
- [Veo 3.1 (First-Last Frame to Video) — fal.ai](https://fal.ai/models/fal-ai/veo3.1/first-last-frame-to-video)
- [Veo 3.1 — Google DeepMind](https://deepmind.google/models/veo/)
- [Kling 3.0 vs Veo 3.1 2026 — veo3ai.io](https://www.veo3ai.io/blog/kling-3-0-vs-veo-3-1-2026)
- [Runway Gen-4: AI Video Generation with World Consistency — Runway Research](https://runwayml.com/research/introducing-runway-gen-4)
- [Runway Gen-4 solves character consistency — VentureBeat](https://venturebeat.com/ai/runways-gen-4-ai-solves-the-character-consistency-challenge-making-ai-filmmaking-actually-useful)
- [Aspect Ratio (--ar) Parameter — Midjourney Docs](https://docs.midjourney.com/hc/en-us/articles/31894244298125-Aspect-Ratio)
- [Midjourney Parameter List — Midjourney Docs](https://docs.midjourney.com/hc/en-us/articles/32859204029709-Parameter-List)
