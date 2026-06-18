# 02 — Physics, Light, Optics, Camera, Materials, Motion

Highest-leverage idea: **AI models learn the statistical look of images, not the physics of light and 3D space.** They have no internal scene geometry, so they fail exactly where a forensic analyst checks — shadow-to-light convergence, reflection vanishing points, consistent specular highlights. Your prompt substitutes *photographic and physical causality* for the model's default "glossy average." Specificity is the constraint that forces a physically plausible solution.

## 1. LIGHT PHYSICS
Rule AI breaks constantly: a point on an object, its shadow, and the light source lie on one straight line — those lines converge at the light. AI scatters that convergence → impossible multi-directional shadows. **Name ONE source, its direction, and the resulting shadow behavior.** Multi-light prompts confuse the model.

**Direction / setup bank:**
- Direction: `light from camera-left, long soft shadows to the right` · `low-angle sun behind subject` · `top-down key` · `45° key`
- Named setups: `Rembrandt lighting (triangle under the eye on the shaded side)` · `butterfly` · `rim light` · `backlight / contre-jour` · `silhouette` · `key + soft fill` · `bounced fill from below`
- Quality: `soft window light` · `overcast diffused, no harsh shadows` · `hard single light, deep chiaroscuro` · `practical lighting (lamps in scene)` · `studio softbox`
- Time/color: `golden hour, warm low rim light` · `blue hour` · `harsh noon overhead, short hard shadows` · `dusk` · `dust/breath catching the light`

Why: naming one source + shadow direction gives a coherent target instead of averaging conflicting cues. "Golden hour rim light" reproduces well (millions of correct examples); "magical/HDR/dramatic" pulls toward stylized renders.

## 2. REFLECTIONS & OPTICS
Same geometric constraint: object-to-reflection lines share a vanishing point, and a reflection must contain *the actual scene*. AI's worst failure zone — mismatched/missing reflections, wrong-direction shadows inside reflections, and eye catchlights lacking crisp directional structure (a giveaway).

**Optics bank:**
- `single sharp catchlight in each eye matching the key light` · `mirror reflects the actual room behind camera` · `wet asphalt with accurate streaked reflections of the neon signs` · `glass with subtle surface glare and depth, not a perfect mirror`
- Tasteful artifacts (sparingly): `slight chromatic aberration on high-contrast edges` · `gentle anamorphic lens flare` · `mild vignetting` · `specular highlights / caustics on rippling water`

Why: telling the model *what the reflection contains* and constraining catchlight count/direction fights decorative, geometry-free reflections. Subtle aberration/vignetting signal a real glass element — flawless optics read as CGI.

## 3. CAMERA / LENS REALISM (the NatGeo look)
Naming a real body + lens + aperture is the strongest single realism lever — the model learned the specific optical signature. Always pair focal length with an f-stop (the aperture tells the model how much blur to apply).

| Focal | Effect to prompt |
|---|---|
| 14–24mm | ultra-wide, expansive, edge distortion |
| 35mm | most natural documentary realism |
| 50mm | closest to human eye |
| 85mm | portrait compression, flattering faces, creamy bokeh |
| 135mm | tight portrait, strong subject separation |
| 200–600mm | wildlife/sports telephoto, heavy background compression |

- Aperture: `f/1.4–f/1.8` blown bokeh · `f/2.8` subject isolation · `f/8` balanced · `f/11–f/16` deep-focus landscape
- Bodies: `Canon EOS R5` · `Sony A1 / A7R V` · `Nikon Z9` · `Hasselblad` (medium format) · `Leica`
- Real lenses: `NIKKOR Z 400mm f/2.8 TC VR S` · `Canon RF 85mm f/1.2` · `Sony FE 70-200mm f/2.8`
- Shutter/ISO/grain: `1/1000s frozen` · `1/30s motion blur` · `ISO 800` · `subtle film grain` · `slight sensor noise`
- Film stocks: `Kodak Portra 400` · `Ektachrome E100` · `Fujifilm Pro 400H` · `Tri-X` · `CineStill 800T`

**NatGeo wildlife template:**
> `Realistic wildlife photograph, [animal + action] in [environment], Nikon Z9 + 400mm f/2.8 at f/4, 1/1000s, ISO 800, golden-hour warm rim light on fur, breath visible in cold air, shallow DoF, crisp focus on the eye, National Geographic editorial color grade`

Why: generic quality tags ("8k, ultra realistic") trigger aesthetic bias → waxy, over-sharpened, flat-lit output. Real gear names invoke physically grounded distributions: compression, DoF falloff, grain that match a real exposure.

## 4. ATMOSPHERE & DEPTH
Flat AI images lack air. Force *layers* and *atmospheric perspective* (distant objects fade cooler/hazier) — the cue the eye uses for scale.
- Layering: `[foreground: grass/rocks/water] · [midground: subject] · [background: distant peaks/horizon], layered depth, strong parallax`
- Atmosphere: `volumetric god rays through gaps` · `morning mist / valley fog` · `heat haze` · `cool blue haze on distant ridges` · `dust glowing in backlight`
- Scale cues: `tiny figure for scale` · `acacia silhouettes against vast sky`

## 5. MATERIAL / TEXTURE PHYSICS
"Texture is revealed by how light interacts with surfaces" — describe the material AND its light behavior + wear. Default failure = over-smoothing → plastic/waxy.
- Skin: `visible pores, fine lines, subtle redness, natural oiliness and tonal variation — nothing airbrushed`
- Fabric: `raw silk with visible slubs and sheen` · `heavy linen, coarse weave, natural creases` · `wool, fuzzy nap, visible knit stitches` · `velvet, directional pile sheen`
- Metal: `mirror-polished chrome, sharp speculars` · `brushed steel, directional grain, fingerprint smudges` · `oxidized copper, green verdigris` · `pitted rusty iron`
- Fur/hair: `individual backlit strands, anisotropic sheen, matted wet clumps`
- Water/wetness: `beaded droplets, specular glints, wet sheen and weight in soaked fabric`
- Foliage/wood: `leaf veins, sun-dappled translucency` · `weathered grain, cracks, dust`
- Universal imperfection: `scratches, dust, fingerprints, worn edges, natural micro-detail`

## 6. MOTION & ENERGY
Match the verbal cue to a real shutter behavior.
- Freeze: `1/2000s, frozen mid-leap, crisp edges, frozen droplets and flying debris, individual dust particles sharp`
- Blur: `1/30s motion blur on the legs, sense of speed`
- Panning: `panning shot, sharp subject, horizontally streaked motion-blurred background`
- Energy: `kicked-up dust trail, splashing water arc, wind-blown mane`

## 7. ANTI-PATTERN LIST (kill these — they trigger aesthetic bias → CGI gloss)
**Avoid:** `8k, 4K, ultra HD, hyperrealistic, photorealistic (as a tag), masterpiece, award-winning, trending on ArtStation, octane render, unreal engine, cinematic, ultra-detailed, stunning, flawless, perfect, ethereal, dreamlike, hyper-saturated, HDR, neon/magical/fantasy lighting`

| Avoid | Use instead |
|---|---|
| flawless | natural |
| perfect skin | realistic skin texture, visible pores |
| cinematic masterpiece | quiet documentary-style portrait |
| beautiful woman in a park | candid, unposed, lived-in scene with [specific detail] |
| 8k / ultra realistic | shot on Canon EOS R5, 35mm, f/2.8 |
| octane render | 35mm film, subtle grain |

**Negative guardrails (where supported):** `no CGI, no 3D render, no game engine, no plastic/waxy skin, no airbrushing, no oversharpening, no oversaturation, no cartoon/illustration`

**Deepest recurring insight:** believability comes from **narrative causality, not descriptor density.** "Flour on her sleeves, morning light through lace curtains" beats ten superlatives because it gives the scene a physical reason to exist. Real-life imperfection + one coherent light + named optics is the whole game.

---
*Sources: AI Video Bootcamp 2026; Artlist (lighting); Aituts (camera prompts); Content Authenticity Initiative & Amped/Forensic Focus & IEEE Xplore (shadow/reflection forensics); Meri CreativAI (the #1 fake mistake); ZSky (textures, landscapes); media.io (wildlife); Photography Life (motion/panning); Miraflow; ZeroSkill; D5 Render (atmospheric perspective). Verified 2024–2026.*
