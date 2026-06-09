---
version: alpha
name: YUV.AI Neon Phoenix — Frame (video / frame layer)
description: >
  Video-first frame spec for the YUV.AI brand. The unit is the frame (1920×1080), not the
  slide-in-a-deck. Atoms are sacred — the neon two-canvas system (rich-black OR white, never
  grey), hot pink + electric cyan in a lead/counter relationship, Anton uppercase tracked +
  Inter body + JetBrains Mono readouts, glow in moderation, zero radius save circles/pills.
  The signature environment is the neural-net phoenix: a field of glowing graph nodes joined
  by faint edges, seeded along a phoenix silhouette, rainbow-graded amber→pink→violet→cyan.
  Rainbow lives in the phoenix mark + the neural-net field ONLY; UI gradients stay pink→cyan.
unit: the frame — 1920×1080 primary; 9:16 and 1:1 documented
principle: atoms are sacred · composition is free · numbers come from the script

colors:
  pink:       "#FF1464"   # primary thread — CTAs, hero spans, "current" accents
  pink-hot:   "#FF0080"   # high-energy variant — glow shadows, hover
  cyan:       "#00E5FF"   # electric secondary — data points, focus, links
  cyan-edge:  "#00FFFF"   # max-neon, small surfaces only
  white:      "#FFFFFF"   # canvas (light) / text on ink
  ink:        "#0A0A0A"   # canvas (dark), the neon ground
  charcoal:   "#1A1A1A"   # raised panel on ink, secondary text on white
  line-pink:  "rgba(255,20,100,0.18)"
  line-cyan:  "rgba(0,229,255,0.22)"
  # phoenix gradient stops — neural-net field + phoenix mark ONLY (not UI)
  phx-amber:  "#F9AD45"
  phx-coral:  "#F0664E"
  phx-magenta:"#DE6092"
  phx-violet: "#6744A4"
  phx-blue:   "#4E7DB7"

typography:
  # — reading ramp (Inter) —
  body:          { fontFamily: "Inter", cqw: 1.05, weight: 400, lineHeight: 1.6 }
  body-light:    { fontFamily: "Inter", cqw: 1.5,  weight: 300, lineHeight: 1.5, note: "pull-quote / support voice" }
  section-label: { fontFamily: "Inter", px: 13, weight: 700, tracking: "4px", upper: true }
  item-label:    { fontFamily: "Inter", px: 12, weight: 700, tracking: "3px", upper: true }
  readout:       { fontFamily: "JetBrains Mono", px: 14, weight: 500, tracking: "2px", upper: true, note: "HUD / instrument values" }
  # — display / hero ramp (Anton, uppercase, tracked 0 default) —
  card-title:    { fontFamily: "Anton", cqw: 1.9, lineHeight: 1.05, tracking: "0", upper: true }
  bar-title:     { fontFamily: "Anton", cqw: 2.3, lineHeight: 1.0,  tracking: "0", upper: true }
  column-title:  { fontFamily: "Anton", cqw: 3.6, lineHeight: 1.0,  tracking: "0", upper: true }
  section-headline:{ fontFamily: "Anton", cqw: 4.4, lineHeight: 1.0, tracking: "0", upper: true }
  stat-numeral:  { fontFamily: "Anton", cqw: 5.5, lineHeight: 1.0,  tracking: "0", upper: true }
  hero-title:    { fontFamily: "Anton", cqw: 7.5, lineHeight: 0.92, tracking: "0", upper: true }
  jumbo-feature: { fontFamily: "Anton", cqw: 10.0, lineHeight: 0.95, tracking: "0", upper: true, note: "only <=180px-equiv may go -0.01em" }

spacing:
  pad-x: "5cqw"
  pad-y: "4.5cqw"
  gap-grid: "1.8cqw"
  card-pad: "2cqw"

components:
  neural-net-field:
    ground: "{colors.ink}"
    nodes: "glowing dots, 2.5–4px, colored along the phoenix gradient, box-shadow bloom"
    edges: "1px lines, opacity fades with distance (rgba white ~0.18 max), no edge > ~160px"
    placement: "seed node positions along a phoenix silhouette path; subtle deterministic drift"
    seekable: "MUST be clock-driven (GSAP proxy onUpdate / hf-seek), never Date.now()/rAF wall-clock"
    description: "THE signature environment. The brand, alive. Rainbow lives here + in the phoenix mark."
  region-split:
    layout: "two solid surfaces meeting at a hard edge; ink|white or ink|charcoal; ratios 40/60, 50/50, 38/62"
    rounded: "0"
    description: "Layout device. Canvas is white OR ink — NEVER a grey middle."
  card:
    backgroundColor: "{colors.ink} (on ink ground) or {colors.white} (on light)"
    border: "1px {colors.line-pink} or {colors.line-cyan}; lead card adds 4px pink/cyan LEFT or TOP stripe"
    rounded: "0"
    shadow: "none (glow on hover/hero only)"
    typography: "{typography.card-title} + {typography.body}"
    description: "Flat. The single coloured stripe is the only chrome."
  glow:
    text: "text-shadow: 0 0 16px rgba(255,20,100,.65), 0 0 32px rgba(255,20,100,.35) (pink) / cyan variant"
    box: "0 0 24px rgba(255,20,100,.5) on hero CTA"
    rule: "EITHER text-shadow OR box-shadow per element, never both. Hero + primary CTA + 1–2 accents only."
  accent-line:
    backgroundColor: "{colors.pink}"
    size: "4cqw × 0.22cqw"
    rounded: "0"
    description: "Sub-headline rule; or a pink→cyan gradient progress bar (the ONLY UI gradient)."
  hud-strip:
    backgroundColor: "rgba(10,10,10,0.85)"
    typography: "{typography.readout}; phase tag in cyan box, values in pink"
    description: "Fly High throughline — phase (CLIMB/CRUISE/DESCENT) + readouts + flight number."
  phoenix-mark:
    description: "The neural-net phoenix logo. Rainbow-graded. Bottom-right watermark ~120–180px, or hero centerpiece."
  cta:
    backgroundColor: "{colors.pink} (fill) or transparent + 2px {colors.cyan} (outline)"
    rounded: "999px"
    description: "Pill — the only non-zero radius. Anton uppercase, glow in moderation."
---

# YUV.AI Neon Phoenix — Frame (video / frame layer)

## Overview

YUV.AI at frame scale is a **neon command deck**: a rich-black ground alive with the
**neural-net phoenix** — glowing graph nodes joined by faint edges, seeded along a phoenix
silhouette, graded amber → pink → violet → cyan. Over that environment, composition is built
from **hard region splits** (ink ↔ white ↔ charcoal) and **Anton uppercase** headlines, with
**hot pink** and **electric cyan** in a strict **lead/counter** relationship — one leads each
frame, the other accents. Glow is the atmosphere; it fires on the hero and the primary CTA, not
on everything.

The voice: **Anton** — tall condensed caps, uppercase, `letter-spacing: 0` (Anton is already
condensed; never negative except a hair at jumbo) — carries every headline, stat, and title;
**Inter** carries body and labels; **JetBrains Mono** carries instrument readouts. Anton
declares; Inter explains; Mono measures.

**Key characteristics at frame scale:**
- **Neon two-canvas** — `{colors.ink}` OR `{colors.white}`, **never grey.** Pick one per frame.
- **Neural-net phoenix** as the living environment + the brand mark (the rainbow lives here).
- **Lead / counter** — pink leads OR cyan leads; never both at full strength on one frame.
- **Anton uppercase + Inter + Mono.** Headlines ink-on-white / white-on-ink / pink-with-glow.
- **Glow in moderation** — hero + primary CTA + 1–2 accents. Strip-mall neon is failure.
- **Flat** — zero shadow, radius only on circles (nodes, nav) and pills (CTAs).
- **Fly High throughline** — flight metaphors, HUD strips, phoenix mark, "LET'S FLY HIGH" watermark.

### Frame Craft Bar
Three eyeball tests gate every frame:
- **Squint** — one element dominates at **3–6×** its neighbor: the `hero-title`/`jumbo-feature`, a `stat-numeral`, or the phoenix mark. Never two rival headlines.
- **Silence** — frames read **40–55% empty** (the neural-net field fills negative space, not more text); the **catalog is the one dense exception.**
- **Restraint** — pink **or** cyan leads; rainbow ONLY in the phoenix/neural-net field; glow on hero + CTA only.
- **Reference** — aim at a **neon mission-control HUD / Tron title card** (glowing graph on black, condensed caps as architecture); failure looks like a **soft drop-shadowed SaaS card deck**.

## The Frame

- **Primary:** 1920×1080 (16:9). Display sizes authored in **`cqw`** (`px ÷ 1920 × 100 = cqw`).
- **Vertical:** 1080×1920 (9:16). **Square:** 1080×1080 (1:1).
- **Safe area:** `5cqw` (pad-x). The neural-net field bleeds full-frame behind everything.

**The container law.** Every frame ground sets `container-type: size`; frame-relative units are
`cqw`/`cqh` against it — **never `vw`.** In a fixed-1920 HyperFrames composition you may author
in px directly (`cqw × 19.2 = px`); keep the ratios.

## Colors

Two canvases: rich-black `{colors.ink}` (default — the neon ground) or `{colors.white}` (light
marketing / about). Never `#F1F2F2` grey (that's Decks mode), never `#FAFAF7` (Warm Editorial).
Pink and cyan in **lead/counter**: if pink leads a frame, cyan appears only on small high-
attention marks (a focus ring, one data point), and vice-versa. **The only UI gradient is
pink → cyan** (progress bars, underlines, small surfaces). **Rainbow (amber→pink→violet→cyan)
is reserved for the phoenix mark and the neural-net field — never a UI wash.** Headlines: white
on ink, ink on white, or pink-with-glow. Never grey headlines (grey is body/meta).

## Typography

Two ramps. The **reading ramp** (Inter body 1.05cqw, body-light 1.5cqw, labels/Mono in px)
carries copy, eyebrows, and readouts; the **display ramp** (Anton, `card-title` 1.9cqw →
`jumbo-feature` 10cqw) carries every headline and stat.

- **Legibility floor:** any load-bearing line ≥ **1.4cqw** (~27px); px labels are chrome only.
- **Fit-to-measure:** ≤3 words → `hero-title`/`jumbo-feature`; 4–6 → `section-headline`; 7+ → `column-title`. Cap the block ≤ 78cqw.
- **Anton is uppercase, `letter-spacing: 0`** (never negative; a hair `-0.01em` only at jumbo ≥180px-equiv). **Inter labels uppercase, 3–4px tracked. Mono readouts 2px tracked.** No italic, no sentence-case Anton.

## Depth & Surface

Flat, with hard edges and neon glow as the only "depth":
- **Hard region boundaries** — primary structural device.
- **Accent borders** — 4px pink/cyan left (lead cards), 4px top (catalog cards).
- **Glow** — moderated bloom on hero text, primary CTA, phoenix mark.
- **Neural-net field** — the living texture behind content (never a literal depth/shadow).

**Ceiling:** no box-shadow as elevation, no rounded rectangle, no rainbow UI wash, no grey canvas.

## Shapes

- **0 radius** on every rectangle — regions, cards, panels, accent lines, HUD.
- **999px** on pills (CTAs) only. **50%** on circles — neural-net nodes, nav dots.

## Components

- **neural-net-field** — the signature environment + brand mark (rainbow lives here).
- **region-split** — the layout device; ink ↔ white ↔ charcoal at a hard edge.
- **card** (4px pink/cyan stripe, flat) / **cta** (pill) / **accent-line** (pink, or pink→cyan progress).
- **glow** — moderated bloom. **hud-strip** — the Fly High instrument throughline. **phoenix-mark** — watermark or hero.

## Frame Treatments

> Recipe per plate: ground · composes · focal · chrome · accent · silence · density.
> Lean centered where the move allows; vary anchor; one idea per frame.

### 1 · Neural-Net Phoenix Cover  (identity · move: living field · centered)
**Ground** full `{colors.ink}` with the **neural-net-field** alive behind. **Composes**
neural-net-field, hero-title, section-label, hud-strip, phoenix-mark. **Focal** the `hero-title`
(2 lines) centered, line two in `{colors.pink}` with glow; the phoenix mark forms / hovers behind.
**Chrome** a cyan `section-label` eyebrow above; a HUD strip along the bottom. **Accent** pink leads,
cyan eyebrow counters. **Silence** the field fills the negative space; ~50% type-empty. **Density** sparse.

### 2 · Feature Stat  (anchor · move: scale + glow · left)
**Ground** `{colors.ink}`, field dimmed. **Composes** stat-numeral/jumbo-feature, section-label,
body-light. **Focal** a `stat-numeral` or 2-line headline, pink-with-glow OR white, left-anchored.
**Chrome** an Inter `section-label` eyebrow; an optional Inter-300 support line ≤44cqw. **Accent**
pink lead, one cyan mark. **Silence** ~45% empty. **Density** sparse.

### 3 · Statement  (voice · move: panel split · giant type)
**Ground** 40/60 split — `{colors.charcoal}` panel + `{colors.ink}` field. **Composes** region-split,
section-headline, accent-line. **Focal** a 2–3 line statement in white, one key word pink-with-glow.
**Chrome** a pink `accent-line` above; small Mono attribution. **Accent** pink line + pink word.
**Density** sparse.

### 4 · Three-Column Catalog  (the pieces · move: density — the dense frame · centered head)
**Ground** `{colors.ink}`, `pad-x`. **Composes** section-headline, 3–4× card. **Focal** a centered
`section-headline` over cards (4px pink/cyan top stripe, Anton title, Inter body, one Mono tag).
**Accent** alternating pink/cyan stripes; glow off (cards are calm). **Silence** tight — the density
exception. **Density** dense-exception.

### 5 · Pipeline Timeline  (process · move: horizontal rail · left→right)
**Ground** `{colors.ink}`, `pad-x`. **Composes** section-headline, a pink→cyan rail with cyan nodes
(ink halos) + Anton stage labels. **Focal** the rail with 4–5 stages. **Accent** the pink→cyan
gradient rail (the sanctioned UI gradient). **Density** standard.

### 6 · Closing Plate  (closer · move: phoenix + sign-off · centered)
**Ground** `{colors.ink}`, neural-net-field re-igniting. **Composes** phoenix-mark, hero-title,
accent-line, section-label, hud-strip. **Focal** the phoenix mark + "LET'S FLY HIGH" sign-off,
centered, pink-with-glow. **Chrome** website + socials in Mono; HUD reads LANDED. **Accent** pink lead.
**Silence** ~55% empty; field carries it. **Density** sparse. *(Only the final frame may fade out.)*

## Composition Rules

### Do
- Keep the canvas **ink OR white**, never grey; let the **neural-net field** fill negative space.
- Pick **one lead** (pink or cyan) per frame; the other only accents.
- Set every Anton element **uppercase, `letter-spacing: 0`**; Inter labels uppercase 3–4px; Mono 2px.
- Reserve **rainbow** for the phoenix mark + neural-net field; keep UI gradients **pink→cyan**.
- Fire **glow** on the hero + primary CTA + 1–2 accents only.
- Carry one **Fly High throughline** per video — HUD strip, phoenix mark, "let's fly high", flight copy.

### Don't
- Don't use a grey canvas, a fourth surface, a drop-shadow elevation, or a rounded rectangle.
- Don't run pink AND cyan both at full strength on one frame.
- Don't spill rainbow into UI fills/washes (phoenix + field only).
- Don't glow every element (strip-mall neon). Don't set Anton sentence-case or negative-tracked.
- Don't drop a load-bearing line below 1.4cqw.

## Aspect-Ratio Behavior

| Treatment | 16:9 | 9:16 | 1:1 |
|---|---|---|---|
| Phoenix Cover | hero centered, field full | hero lower, phoenix top | centered |
| Feature Stat | figure left, support right | figure top, support below | centered |
| Statement | 40/60 panel+field | stacked panel over field | stacked |
| Catalog | head over 3–4-up | head top, cards stacked | head top, 2×2 |
| Pipeline | horizontal rail | vertical rail | compact rail |
| Closing | phoenix centered, HUD base | phoenix top, sign-off below | centered |

Hold `5cqw` on the short edge; re-step display per ratio so no line drops below 1.4cqw.

## Numerals & Claims (hard rule)

Never invent figures, stats, dates, or counts. Render slots as `— figure —`, `{metric}`, `N×`.
Real numerals appear only when the script supplies them. Node-graph counts are decorative.

## Pre-Render Self-Audit

- **Canvas** — ink OR white, never grey; neural-net field present where the ground is ink.
- **Squint** — one focal per frame dominates 3–6×; never two rival headlines.
- **Lead** — pink or cyan leads; the other only accents; rainbow only in phoenix/field.
- **Type** — Anton uppercase `ls:0`, fit-to-measure, ≥1.4cqw floor; Inter/Mono labels tracked.
- **Glow** — hero + CTA + 1–2 accents only; never every element; never text-shadow AND box-shadow on one element.
- **Depth** — 0 elevation shadow, 0 rounded rectangle; pills + circles only.
- **Throughline** — one Fly High motif present (HUD / phoenix / flight copy / "let's fly high").
- **Fabrication** — every numeral traces to the script, else placeholder.

## Known Gaps

- **Motion is composition-adjacent here** — this frame spec defines look + layout; HyperFrames GSAP
  timelines carry timing/transitions. The neural-net field MUST be seekable (clock-driven), never wall-clock.
- **Anton + Inter + JetBrains Mono** via Google Fonts (HyperFrames embeds them). Hebrew swaps Anton→Rubik, Inter→Assistant.
- **9:16 / 1:1 are guidance**, not pixel-locked; verify the 1.4cqw legibility floor per ratio.
- The neural-net field, glow, and pink→cyan gradients are CSS/canvas-only; the phoenix mark art is the one external asset.
