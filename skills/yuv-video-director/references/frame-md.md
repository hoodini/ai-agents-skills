# frame.md — the design layer for video

`design.md` describes a brand for the **web** (scroll, hover, small text, chrome). None of that
exists in a 16:9 frame. **`frame.md`** is the same brand atoms re-expressed for the camera:
type scale for 1920×1080, dwell, motion personality, safe margins — so the agent composes without
guessing. It's a `DESIGN.md` superset; **atoms stay sacred, composition stays free, numbers come
from the script.**

## How HyperFrames consumes it
Read a design spec in precedence order: **`frame.md` → `design.md` → `DESIGN.md`** (check both
casings; `frame.md` wins). Bind its palette/typography onto `:root`; use its **exact** hex/fonts —
never invent. After authoring, verify every hex in the HTML is in the spec and every font matches.

## The YUV.AI frame
Use the bundled **[../assets/FRAME.md](../assets/FRAME.md)** — YUV.AI Neon Phoenix:
- canvas **rich-black `#0A0A0A`** (default) or **white** — never grey
- **pink `#FF1464`** + **cyan `#00E5FF`** in a **lead/counter** relationship (one leads per frame)
- **rainbow** (amber→pink→violet→cyan) **only** in the phoenix mark + the neural-net field — never a UI wash; UI gradients are **pink→cyan**
- **Anton** uppercase (`letter-spacing:0`) + **Inter** body + **JetBrains Mono** readouts
- glow in moderation (hero + primary CTA + 1–2 accents)
- a **Fly High throughline** per video: HUD strip, phoenix mark, "LET'S FLY HIGH", flight copy

The full spec carries six **Frame Treatments** (cover, feature stat, statement, catalog, pipeline,
closing) and a pre-render self-audit. Format = YAML frontmatter (colors / typography ramp in `cqw`
/ components) + markdown. In a fixed-1920 composition, author px directly (`cqw × 19.2 = px`).

## Adapting another frame.md pack (e.g. HeyGen's gallery)
HeyGen ships frame packs (Coral, Capsule, Cartesian…) at hyperframes.dev/design. To rebrand one to
YUV.AI: keep its **structure** (frontmatter keys, treatments, the container-type:size law, the
"numerals come from the script" rule) and **swap the atoms** — colors → Neon tokens, Bebas/serif →
Anton, add the neural-net field + glow + lead/counter rules. The bundled FRAME.md was built this way.
