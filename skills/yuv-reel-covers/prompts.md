# AI-Image Prompt Formulas — Editorial Poster covers (reverse-engineered)

Derived from 12 Midjourney describes of the reference posters + visual analysis. The Cover Studio
app generates these automatically (AI PROMPTS tab); these are the master formulas + worked examples.

## MASTER — HYPE (sports-editorial, the SHELLY look)
```
ultra low-angle full-body action shot of {SUBJECT}, {ACTION}, larger-than-life sports-editorial
campaign poster, {ENVIRONMENT}, vivid saturated colors, crisp rim light, premium ad-campaign
retouching, {DEPTH PROP} crossing the frame with motion blur for depth of field, GIANT condensed
italic sans-serif typography in neon yellow: "{WORD1}" across the upper area and "{WORD2}" across
the lower third, the subject's body and limbs overlapping the huge letters so the text reads both
behind and in front of the figure, small repeated ticker caption "{T1} ✦ {T2} ✦ {T3}" in bold white
spaced capitals, tiny thin line icons (four-point star, globe, target) in the bottom right corner,
magazine poster composition, shot on medium format, hyper-detailed --ar 4:5 --style raw --v 7
```

## MASTER — CINEMA (the Joker look, Neon-Phoenix grade)
```
dramatic cinematic portrait of {SUBJECT}, {ACTION}, {ENVIRONMENT}, split lighting with hot pink
light from the left and electric cyan light from the right, duotone color grade, crushed blacks,
moody fog, symmetrical composition, GIANT condensed white sans-serif typography: "{WORD1}" at the
top and "{WORD2}" across the middle, the words partially hidden BEHIND the subject's head so the
figure overlaps the letters, minimal, premium film-poster look, 35mm cinematic still,
hyper-detailed --ar 4:5 --style raw --v 7
```

Per-engine tweaks:
- **Flux / Leonardo:** drop the MJ flags; prefix `typographic poster, accurate legible text rendering.`
- **Nano Banana 2 (best text fidelity — use Yuval's nano-banana-2 skill):** prefix
  `Create a 4:5 portrait poster image. Render ALL text EXACTLY as written, correct spelling.` and
  keep headline words short. NB2 can also take Yuval's photo as a reference input for likeness.
- **Hebrew headlines:** image models butcher Hebrew — generate the SCENE without text
  (remove the typography sentence), then run `hyperframes remove-background` on the result and set
  the type in Cover Studio. Pixel-perfect Hebrew every time. This is the pro workflow.

## Worked examples (Yuval's content)
1. HYPE / Claude Desktop launch:
   SUBJECT: "a charismatic Israeli tech creator, short dark hair, black t-shirt with a colorful
   phoenix print" · ACTION: "leaping mid-air reaching toward the camera" · ENVIRONMENT: "rooftop
   against a vivid blue sky with palm trees" · DEPTH PROP: "a glowing laptop flying huge in the
   blurred foreground" · WORDS: "STEAL MY" / "PROMPTS" · TICKER: ALL DAY ✦ EVERY PLAY ✦ NO LIMITS
2. HYPE / cheetah collab: SUBJECT: "a smiling tech creator standing beside a real cheetah" ·
   ENVIRONMENT: "golden savanna safari light" · DEPTH PROP: "tall grass blades blurred in the
   foreground" · WORDS: "BORN TO" / "RUN".
3. CINEMA / tutorial series: SUBJECT: "an intense tech creator looking straight into camera" ·
   ENVIRONMENT: "dark studio with haze" · WORDS: "CLAUDE" / "CODE".

## The hybrid pipeline (the one that always wins)
AI image (scene only, no text) → `npx hyperframes remove-background scene.png -o cutout.png` →
open **cover-studio.html** → load scene as BG + cutout as subject → type the headline (any
language) → Export PNG. You get the AI-photo drama with guaranteed-perfect typography.
