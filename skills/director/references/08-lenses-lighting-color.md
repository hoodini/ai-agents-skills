# Lenses, Lighting & Color

Three systems decide what an image *feels* like before a single word of dialogue lands: the **lens** (how space and faces are shaped by optics), the **light** (where it comes from, how hard it is, what color), and the **grade** (the final color relationship laid over everything). Story, blocking, and editing live in other chapters (see `06-shots-framing-composition.md`, `10-editing-theory.md`); this chapter is about the photochemical and optical layer — "the look" — and how to reproduce it when your "camera" is a diffusion model.

The throughline: **none of these are decoration.** A lens choice is a psychological claim about distance. A lighting ratio is a moral claim about how much we're allowed to see. A palette is a thesis about what the film is about. Get them arbitrary and the image reads as "footage." Get them deliberate and aligned, and the image reads as *authored* — which, for AI work, is the entire game, because the default output of every model is competent, generic, and dead.

---

## Part 1 — Lenses & Optics

### Focal length: the single most under-understood control

**Focal length** is the distance (in millimeters) from the lens's optical center to the sensor when focused at infinity. Practically, it sets the **angle of view** (how much of the world fits in frame) and, far more importantly, it dictates the **camera-to-subject distance** you must adopt to fill the frame with a given subject — and *that distance* is what actually distorts or flatters a face.

This is the deep point most beginners miss: **a lens does not "distort" a face. Proximity does.** A 24mm lens looks "wide and warped" on a portrait only because to fill the frame with a head at 24mm you have to get the camera ~30cm from the nose, and at that range the nose is meaningfully closer to the lens than the ears, so it balloons. Shoot the same face at 24mm from across a room and it's undistorted (just tiny in frame). The focal length forces the distance; the distance does the perceptual work.

| Class | Range (full-frame) | Forces you to stand… | Effect on a face | Effect on space | Emotional read |
|---|---|---|---|---|---|
| Ultra-wide | 14–24mm | Very close | Nose/forehead bulge, "fisheye" feel | Deep, exaggerated, walls splay | Disorientation, intimacy-as-intrusion, comedy, scale |
| Wide | 28–35mm | Close | Slight enlargement of near features | Roomy, environment-forward | Naturalistic, "you are there," vérité |
| Normal | ~40–58mm | Conversational | Neutral, true proportions | Matches lived spatial sense | Honest, transparent, classical |
| Short tele / portrait | 85–135mm | Several meters back | Flattering, flattened, features compressed | Background pulled forward, isolated | Beauty, longing, observation |
| Long tele | 200mm+ | Far away | Very flat, "pancake" face | Extreme compression, planes stack | Voyeurism, surveillance, fate, separation |

**Lens compression** is the headline consequence of going long. A telephoto doesn't magnify the background relative to reality the way people think — what it does is let you stand far back, and at long distances the *relative* size difference between near and far objects shrinks (a person 5m away vs. a building 50m away looks almost the same scale when both are far from you). The result: backgrounds appear huge and pressed up against the subject. The canonical demonstration is *The Graduate* (1967): Dustin Hoffman runs toward the church on a long lens, and the famous shot makes him appear to sprint without getting closer — the compression collapses the depth he's covering. Sergio Leone's standoffs in *The Good, the Bad and the Ugly* use long lenses to stack faces into flat, fated planes. Conversely, wide-angle exaggeration: the corridor sequences in *The Shining*, the dread-inducing close wides on faces in *Requiem for a Dream*, or Terry Gilliam's whole career — bulging, anxious, the world too close.

> **The "50mm ≈ human eye" claim — what's actually true.** It's a useful rule of thumb that is half-myth. The human eye's *sharp foveal* field is narrow (roughly equivalent to a long lens), while our *full peripheral* field is enormous (wider than any normal lens). So neither end matches. What 50mm on full-frame *does* match reasonably well is **perspective and magnification at typical viewing**: a 50mm image printed and held at normal distance produces the same relative object sizes and depth relationships your brain expects from being in the room. The "normal" range is really ~40–58mm and the eye-match is about *spatial proportion*, not angle of view. Don't repeat "50mm sees what you see" as gospel; the accurate version is "50mm renders perspective the way an unhurried observer perceives it." Note also that focal-length character is **sensor-size dependent** — these numbers are for full-frame (≈36mm wide sensor); a 50mm on a smaller sensor crops to a tighter, more telephoto-feeling image, which is why "35mm-equivalent" exists as a normalizing language.

#### → AI APPLICATION
Modern video models respond to focal-length vocabulary directly. The Veo prompting convention is to lead with cinematography, then subject: a single sentence like *"50mm natural lens, eye-level medium shot of a tired detective…"* The shorthand the models reliably parse: `24mm wide`, `35mm natural`, `50mm portrait`, `85mm telephoto isolation`, `100mm macro`. Crucially, **also state the distortion you want, not just the number**, because the model learned "85mm" from captioned stills of varying quality: pair it with the *effect* — `"85mm telephoto, compressed background, flattened facial features, subject isolated from environment"` — so you steer both the metadata token and the visual outcome. For wide exaggeration, say `"24mm wide-angle, exaggerated perspective, foreground looms, walls splay outward."` Encode focal length the same way across every shot of a character to keep their face-shape consistent — switching from a 35mm to an 85mm between two cuts of the same person can change their apparent face width enough to break continuity, the optical equivalent of a wardrobe error.

---

### Aperture, depth of field, and the storytelling of focus

**Aperture** is the size of the lens opening, written as an **f-number** (f/1.4, f/8, f/16). Counterintuitively, *smaller f-number = larger opening = more light = shallower depth of field.* (The f-number is focal length ÷ aperture diameter, a ratio, which is why the math runs backwards from intuition.)

**Depth of field (DOF)** is the range of distance that appears acceptably sharp. The trade is the core expressive lever:

- **Shallow DOF** (f/1.4–f/2.8, or long lens, or close subject) → a thin sliver of sharpness, everything else melts. This **directs the eye absolutely**, isolates the subject, and signals subjectivity and intimacy. It's the modern "cinematic" default, sometimes to a fault — a wall of bokeh can be a substitute for actual composition.
- **Deep focus** (f/8–f/16, wide lens, lots of light) → foreground and background both sharp, the viewer's eye is *free to roam* and must be guided by staging instead. This is harder and more democratic.

The textbook case is **deep focus in *Citizen Kane* (1941)**, shot by Gregg Toland. In the scene where young Charles plays in the snow outside while his fate is decided by adults at a desk inside, *all three planes are sharp* — the boy in the far window, the mother mid-frame, the banker foreground. The technique (wide lenses, brutal lighting levels, sometimes optical trickery and split-diopters) lets the staging do the storytelling: the audience watches the child being signed away in the same crisp instant. André Bazin made deep focus a moral argument — it respects the viewer's freedom to choose where to look, versus shallow focus which decides *for* you. Contrast *Saving Private Ryan*'s shallow, jittery subjectivity, or any Sofia Coppola film where shallow focus = a character sealed inside her own interiority.

**Bokeh** is the *aesthetic quality* of the out-of-focus blur, not merely the amount. It's shaped by the iris (number/curve of aperture blades): rounded blades give creamy circular highlights; straight blades give polygonal "nonagon" balls. Vintage and specialty glass produce swirly (Petzval), soap-bubble, or "cat's-eye" bokeh toward the frame edges. This is texture and personality, and it's a thing AI models render as a learned vibe rather than from physics.

#### → AI APPLICATION
State the look in two registers — the **f-stop token** and the **plain-language consequence**. For shallow: `"shot at f/1.4, shallow depth of field, creamy bokeh, background dissolves into soft light, only the eyes are tack-sharp."` For deep focus: `"deep focus, f/11, foreground midground and background all sharp, Citizen Kane-style staging across planes."` Veo and Kling both honor `"shallow depth with creamy bokeh"` vs. `"deep focus, everything sharp"` as discrete instructions. Two caveats: (1) deep focus is *harder* to get from diffusion models — their training data skews toward shallow "pretty" stock and phone-portrait-mode bokeh, so you may need to over-specify and reject several generations; (2) bokeh *shape* can be steered (`"hexagonal bokeh"`, `"circular creamy bokeh"`, `"swirly vintage bokeh"`) but is unreliable — treat it as a flavor request, not a guarantee. For consistency across separately generated shots, freeze the aperture phrase as a reusable token in your prompt template so the blur character doesn't lurch between cuts.

---

### Anamorphic: the "scope" feel

A standard **spherical** lens projects the world onto the sensor in normal proportions. An **anamorphic** lens squeezes a wide (≈2.39:1) field horizontally onto the sensor, and you de-squeeze in post. This was invented to get widescreen onto 4-perf 35mm film, but it left a set of *artifacts* that became beloved signatures:

- **Oval/elliptical bokeh** — out-of-focus highlights stretch into vertical ellipses, especially off-center.
- **Horizontal lens flares** — that blue-streak flare slashing across the frame (J.J. Abrams' *Star Trek* turned it into a meme; *Blade Runner 2049* uses it with restraint and intent).
- **The 2.39:1 frame itself** — the "epic," letterboxed scope shape.
- **Subtle barrel and focus "breathing"**, plus distinctive face-rendering at the edges.

The cumulative effect reads as **"big movie."** Audiences can't name it, but they feel the prestige. Roger Deakins, Hoyte van Hoytema (*Interstellar*, *Oppenheimer* mixed large-format), and Denis Villeneuve's collaborators lean on anamorphic character constantly.

#### → AI APPLICATION
You can't put glass in a model, so you summon the *artifacts*. The reliable phrase stack: `"anamorphic 2.39:1, horizontal blue lens flares from light sources, oval bokeh, slight barrel distortion, cinematic widescreen film look."` Set the output aspect to 2.39:1 (or render 16:9 and crop in post if the model won't go wide). Be honest: models reproduce the *flares and oval bokeh* convincingly because those are heavily represented in training stills, but true edge-of-frame anamorphic geometry is approximate. For a coherent film, decide spherical-vs-anamorphic *once* and bake it into every shot's prompt — mixing a clean spherical shot into an anamorphic sequence is jarring in the same way a continuity error is.

---

## Part 2 — Lighting

### Three-point lighting, built from nothing

Forget the diagram for a second and reason from the problem. You have a face. A single light from one side gives you a hard bright cheek and a black cheek — dramatic, but often too much. To control the *contrast* and the *shape*, classical practice uses three instruments, each solving one problem:

1. **Key light** — the main, dominant source. It establishes the direction and the basic exposure. Everything else is defined *relative to the key*. Where you put the key is the single most consequential lighting decision (see direction, below).
2. **Fill light** — a softer, dimmer source on the *opposite* side of the key. Its only job is to lift the shadow side so we can see detail in it. *More fill = flatter, friendlier, lower contrast. Less fill = more shadow, more mystery, more menace.*
3. **Back light** (a.k.a. rim or hair light) — placed behind/above the subject, aimed at the back of the head and shoulders. It draws a bright edge that **separates the subject from the background**, giving the 2D image a sense of depth. Without it, dark hair melts into a dark wall.

**Key-to-fill ratio** is the numeric soul of mood. If the key delivers 4× the light of the fill, that's a **4:1 ratio** (≈2 stops difference) — punchy, dramatic. A **2:1** ratio is gentle and flattering (sitcom, romance, corporate). An **8:1 or higher** is harsh, hard-boiled, noir. A **1:1** is flat and clinical (or comedic). When people say a scene "looks like a sitcom" vs. "looks like prestige drama," they are very often describing the fill ratio without knowing it.

### High-key vs. low-key

These terms get misused constantly, so define precisely:

- **High-key**: low contrast, abundant fill, few hard shadows, bright overall. Reads as safe, upbeat, open, exposed (musicals, comedies, most commercials, *Barbie*'s plastic brightness, Apple keynotes).
- **Low-key**: high contrast, dominant shadow, hard pools of light in darkness. Reads as tense, secretive, dangerous, interior (*The Godfather*, film noir, *Joker*, most horror).

"Key" here refers to the *overall tonal scale*, not the key light. High-key ≠ "the key light is bright."

### Hard vs. soft light — and why size is everything

The hardness of a light depends almost entirely on the **apparent size of the source relative to the subject**, not its brightness.

- **Hard light**: small source (bare bulb, the noon sun, a spotlight). Sharp-edged, dark, defined shadows. Reveals texture (every pore, every wrinkle). Dramatic, aggressive, unflattering-but-truthful. Noir lives here.
- **Soft light**: large source (an overcast sky, a big diffused softbox, light bounced off a wall). Gradual shadow edges, wraps around the face, hides skin texture. Flattering, gentle, "beauty" light.

The sun is *physically* huge but *apparently* tiny because it's so far — hence hard, hard shadows at noon. Put a diffusion silk between it and the actor and you've enlarged the apparent source: soft. This size-relationship is the one lighting fact that explains the most cases.

### Direction of light — a vocabulary of meaning

Where the key sits relative to the face is a semiotic system:

| Direction | What it does | Connotation | Example |
|---|---|---|---|
| **Front / flat** | Fills out shadows, erases shape | Open, innocent, flat, "newscast" | Beauty ads, glamour |
| **Side (45°)** | Carves form, one cheek lit | Balanced drama, dimensional | Most narrative film |
| **Back / rim** | Edge glow, face may go dark | Mystery, holiness, silhouette | Doorway reveals, halos |
| **Top** | Eye-sockets shadowed, cheekbones harsh | Oppression, interrogation, the divine-or-doomed | *The Godfather* — Gordon Willis kept Brando's eyes in shadow under top light |
| **Underlight** | Reverses natural shadow logic | Monstrous, uncanny, "campfire ghost story" | Horror, villains |

**Rembrandt lighting** is a specific, beloved 45°-and-slightly-above key that leaves a small inverted triangle of light on the shadow-side cheek (under the eye). It's named for the painter, gives instant dimensional "portrait" gravity, and is the default flattering-yet-serious key.

**Chiaroscuro** (Italian, "light-dark") is the broader fine-art principle of bold light/dark contrast to model form and drama — Caravaggio in paint, *The Third Man* and noir in film. Low-key lighting is chiaroscuro applied to cinema.

### Motivated lighting and practicals

**Motivated lighting** means the (carefully constructed, often huge) movie lights are made to *appear* as if they come from a source the audience can believe — a window, a lamp, a fire, the moon. The craft is hiding the artifice behind a plausible in-world reason. A **practical** is a light *visible in the shot itself* — a table lamp, a neon sign, a candle, a phone screen — that also (or only) lights the scene. *Blade Runner 2049*, *Euphoria*, and almost all of Roger Deakins' interiors are master classes in motivated, practical-driven light. The opposite — unmotivated light with no believable source — is what makes amateur footage feel "lit" in a bad way.

### Color temperature (Kelvin)

Light has a color, measured on the **Kelvin (K)** scale (counterintuitively, *lower K = warmer/oranger*, *higher K = cooler/bluer* — the opposite of the "warm/cool" feeling):

| Source | ~Kelvin | Look |
|---|---|---|
| Candle / firelight | 1800K | Deep orange |
| Tungsten bulb | 3200K | Warm amber |
| Golden hour sun | 3500K | Honeyed |
| Noon daylight | 5600K | Neutral white |
| Overcast / shade | 6500–7500K | Cool blue |
| Deep blue hour / moonlight (cinematic convention) | 8000K+ | Cold blue |

The camera's **white balance** decides which color is rendered as "neutral white"; everything off that point takes on a cast. Setting white balance to tungsten (3200K) while shooting daylight makes the whole frame go cold blue — the classic "night/cold" look. The interplay of a warm practical against a cool ambient (orange lamp, blue dusk window) is one of the most pleasing and most-used contrasts in modern cinematography.

### Golden hour, blue hour, magic hour

- **Golden hour**: the ~hour after sunrise / before sunset. Sun is low, raking, warm, soft (long path through atmosphere). Long shadows, glowing rim light, forgiving on skin. Terrence Malick (*Days of Heaven*, *The Tree of Life*) built a whole aesthetic on it.
- **Blue hour**: the ~20–40 min of twilight *after* the sun is down, when the sky is deep saturated blue and there's still soft skylight but no direct sun. Even, melancholy, "between worlds."
- **Magic hour** is the umbrella term filmmakers use for these brief, gorgeous, *fleeting* windows — "hour" is a flattering lie; you get minutes, which is why these shots are precious and hard.

#### → AI APPLICATION (Lighting)
Lighting is where AI prompting pays the highest dividends, because the model has seen millions of lit images and responds to craft vocabulary precisely. Specify lighting in four slots the way a gaffer thinks: **quality + direction + source + temperature + atmosphere.**

- Three-point intent: `"Rembrandt key from camera-left 45° above, soft fill, strong rim/back light separating subject from dark background, 4:1 contrast ratio."`
- Mood by tonal scale: `"low-key chiaroscuro lighting, deep shadows, single hard practical lamp, noir"` vs. `"high-key, soft even light, bright airy, minimal shadows."`
- Hard/soft: `"hard direct sunlight, sharp-edged shadows"` vs. `"large softbox, soft wraparound light, no harsh shadows."`
- Temperature contrast (the money move): `"warm 3200K practical tungsten lamp foreground against cool 7000K blue window light, mixed color temperature."`
- Time-of-day: `"golden hour, low warm raking sun, long shadows, glowing rim light"` / `"blue hour, deep blue twilight, soft ambient skylight, no direct sun."`

Two honest limits: (1) AI does not simulate real light transport — it pattern-matches the *appearance* of a lighting setup, so a physically incoherent prompt (key and fill from impossible angles) may still render plausibly or may produce uncanny double-shadows; verify the shadow logic in outputs. (2) For multi-shot consistency, **the direction of the key must be stated identically every time** — if shot A is keyed camera-left and shot B drifts to camera-right on the same character in the same room, the audience feels the room "flip" even if they can't articulate why. Lock a "lighting bible" string per location and reuse it verbatim.

---

## Part 3 — Color

### Color theory for emotion — the honest version

Colors carry associations, but be skeptical of the pop-psychology "red = anger, blue = calm" listicle. The associations are **real but contextual and culturally variable**, and their power in film comes less from any single hue's "meaning" than from **relationships, saturation, and patterned repetition**. A few reliable, defensible principles:

- **Warm hues (red/orange/yellow) advance; cool hues (blue/green) recede.** This is a perceptual fact (chromostereopsis + atmospheric association) and it's a compositional tool: a warm subject pops off a cool background.
- **Saturation and contrast carry more reliable emotional weight than hue.** A desaturated palette reads bleak/serious/past (*Saving Private Ryan*, *The Road*) regardless of which colors remain; high saturation reads heightened, hyperreal, or candy-bright (*Amélie*'s reds and greens, *Speed Racer*).
- **Meaning is built by repetition and rule, not by a universal dictionary.** Red means whatever the film *teaches* it to mean. In *The Sixth Sense*, red is deliberately scrubbed from the palette except where the supernatural intrudes — the film *trains* you. *Schindler's List*'s red coat works because the rest is monochrome.

So: don't write "blue is sad" in your notes. Write "*this film* uses cold desaturated cyan for the institutional world and warm amber only inside the home, so the two times we see amber outdoors land as hope." That's how color actually does work.

### Complementary palettes and the teal-and-orange epidemic

**Complementary colors** sit opposite on the color wheel (red/green, blue/orange, yellow/purple). Pairing them maximizes contrast and "pop" — the eye loves the tension. The single most exploited pair in modern cinema is **blue-teal shadows + orange highlights**, because human **skin tones are orange**, so pushing shadows/backgrounds teal makes actors leap off the frame with minimum effort.

It's everywhere — Michael Bay, the Marvel house grade, countless thrillers — precisely *because* it's a cheap, reliable win, which is exactly why it's become a cliché and a tell of lazy grading. Use it knowingly: it's not "wrong," it's *overused*, and an audience's eye is now slightly numb to it. The deeper craft move is a **considered, atypical palette** — *Mad Max: Fury Road* (hyper-orange day / hyper-teal night, but pushed to operatic extremes intentionally, with director George Miller and colorist Eric Whipp making it a *statement* rather than a default), *Her* (warm reds and corals, deliberately avoiding tech-blue to make the future feel tender), *Amélie* (saturated red/green/gold).

### Color as character and theme; the color script

A film can assign a color to a character or an idea and track it across the runtime. *Vertigo* uses green for the spectral Madeleine and red for Scottie's obsession. *The Matrix* greens the simulation and blues/cools the real world. *Joker* tracks Arthur's descent through a sickly green.

**The color script** is a Pixar-popularized pre-production artifact (pioneered there in *Toy Story* / *A Bug's Life* era and made famous as a discipline): a sequence of small, low-detail color paintings — one per beat/sequence — that maps the *emotional temperature of the entire film as a color journey* before any final frame exists. *Inside Out*'s color script is the canonical example: each emotional location and memory state has a designed palette, and the arc of the film is legible purely as a strip of color swatches. The discipline forces you to plan color *relationally across time*, not shot-by-shot — which is exactly the discipline AI filmmaking most needs.

### LUTs and grading basics

- **Color correction** = the technical pass: balance exposure, fix white balance, match shots to a neutral, consistent baseline. *Boring but mandatory.*
- **Color grading** = the creative pass: impose the *look* (the teal-orange, the bleach-bypass, the warm nostalgia) on top of corrected footage.
- A **LUT (Look-Up Table)** is a file (commonly `.cube`) that maps every input color to an output color — a portable "recipe" for a look. Two kinds matter: **technical LUTs** (convert log/flat camera footage to standard Rec.709 display) and **creative/look LUTs** (apply a stylized grade). A LUT is a *starting point*, not a finished grade — pros apply a LUT then adjust under it.
- **Node-based grading** (DaVinci Resolve) lets you stack operations — correct on one node, apply the LUT on another, add a vignette/power-window on a third — so the look is editable and consistent.

### Continuity of color across a sequence

A scene shot over hours (sun moving, clouds) or across many AI generations will *not* match by default. The grade's job is to make a sequence feel like it happened in one continuous reality: matched skin tones, matched black levels, matched white point, a shared overall cast. The eye is extremely sensitive to a face that's slightly pinker in one cut and greener in the next — it reads as "wrong" even when the viewer can't say why. This is the single biggest tell that separates assembled-clips from a *film*, and it is the central problem of AI filmmaking, where every shot is born from a different roll of dice.

#### → AI APPLICATION (Color)
Color is the discipline where AI work most needs a *plan imposed from outside the model*, because each generation is independently sampled and will drift. Two layers:

**1. Lock the palette at the prompt layer (so frames are born close).**
- Build a **color script before generating** — literally a list of hex codes or named palettes per sequence, the Pixar discipline applied to prompts. e.g. *Act 1 = cold institutional cyan #1B3A4B + bone #E8E2D0; Act 3 = warm amber #C8772E + deep teal #14333A.*
- Some image models accept explicit color steering: **Flux / Flux 2** support hex color steering (state the brand/scene color and it usually lands), and Midjourney's `--sref` (style reference) and a fixed seed/style code propagate a palette across a whole asset set. Nano Banana 2 / Pro is strong at character + look consistency across generations and at rendering an *intended* palette from a reference image. *(Model capabilities as of mid-2026 — verify current versions.)*
- Phrase it concretely: `"color palette: teal shadows (#14333A), warm amber key light (#C8772E), desaturated overall, muted background, cinematic grade."` Reuse this **identical palette string** in every shot's prompt — this is the prompt-side analog of a master grade.
- Feed a **reference frame/style image** (image-to-image, `--sref`, or Nano Banana's multi-reference) so the model has a concrete color target instead of re-rolling the palette each time.

**2. Conform everything in the grade (because the prompt won't be enough).**
Treat every AI clip like raw footage from a sloppy multi-camera shoot — *because that's exactly what it is.* In DaVinci Resolve:
- First **color-correct each shot to a neutral baseline** (match white point, black level, skin tone) — AI clips arrive with wildly inconsistent casts.
- Then apply **one creative LUT / one grade node tree across the whole sequence** so a single look sits over everything. This is what actually buys continuity; the prompt only gets you close.
- Use Resolve's **shot-match / AI color-match** to pull all clips toward a chosen hero shot, then refine by hand. AI LUT generators export `.cube` files Resolve imports directly, useful as a fast consistent base.
- Keep a **vignette / film-grain / slight halation node at the end** of the chain, applied globally — uniform grain and a unifying vignette do enormous work hiding the fact that twelve shots came from twelve independent generations (grain realism is covered deeper in the cinematic-ai-video skill; here the point is *apply it once, globally, last*).

The mental model: **prompt-side palette discipline minimizes the drift; a single global grade erases the rest.** Skip either and your film looks like a playlist of clips. Do both and separately-generated frames read as one photographed world.

---

## Putting the three pillars together

Lens, light, and color are not independent — they compound into a single legible "look," and great cinematographers think in the whole. *Blade Runner 2049*: long-ish lenses and anamorphic flares (optics) + hard, motivated, color-saturated practicals against fog (light) + a bold restricted palette that shifts per location, amber Las Vegas vs. cold gray LA (color). Strip any one pillar out and the world collapses. For AI work the lesson is procedural: **decide all three up front, encode them as fixed strings, and impose color continuity in post.** The model gives you competent pixels; the *look* is the part you author — through which lens vocabulary you lock, which lighting bible you reuse, and which palette you refuse to let drift.

See also: `06-shots-framing-composition.md` (how staging substitutes for shallow focus in deep-focus shots), `06-shots-framing-composition.md` (where the eye goes), and `10-editing-theory.md` (matching look across cuts).

---

### Sources
- Veo cinematic / lens & lighting prompting conventions: [Google Cloud — Ultimate prompting guide for Veo 3.1](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1), [Veo3 cinematic prompts guide](https://www.veo3ai.io/blog/veo-3-cinematic-prompts-guide-2026), [Skywork — Veo 3.1 lighting & camera tricks](https://skywork.ai/blog/ai-video/veo-3-1-lighting-and-camera-prompt-tricks/)
- AI video model landscape & camera control (Veo / Kling / Runway / Sora status): [TeamDay — Best AI Video Models 2026](https://www.teamday.ai/blog/best-ai-video-models-2026), [Lushbinary — Sora 2 vs Veo 3.1 vs Kling 3.0](https://lushbinary.com/blog/ai-video-generation-sora-veo-kling-seedance-comparison/)
- AI image color/consistency (Midjourney --sref/--cref, Flux hex steering, Nano Banana 2): [TeamDay — Best AI Image Models 2026](https://www.teamday.ai/blog/best-ai-image-models-2026), [invideo — Nano Banana Pro vs GPT-Image vs Midjourney](https://invideo.io/blog/best-ai-image-model-comparison/)
- LUTs / grading consistency across shots in DaVinci Resolve: [No Film School — Color grade with AI](https://nofilmschool.com/color-grade-with-ai), [Blackmagic — DaVinci Resolve Color](https://www.blackmagicdesign.com/products/davinciresolve/color), [color.io — AI Color Match](https://www.color.io/ai-color-match)
