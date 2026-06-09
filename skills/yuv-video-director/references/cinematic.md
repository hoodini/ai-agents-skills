# Cinematic teaser — psychological / cliffhanger / FOMO

When the brief is "Netflix teaser", "award-winning trailer", "psychological", "cliffhanger", "FOMO"
— pacing is **dynamic**, not just fast. The power is in **contrast**: tension → drop → rush → hold.

## The arc (worked example — the shipped 40s cinematic teaser)
```
0–4s   COLD OPEN   near-black, heavy vignette, the field DIM (~0.3 gain).
                   One slow statement at a time, fade-up: "Every brand has a look."
                   "None of them were built to move." (echoes the frame.md design.md→camera idea)
4–6s   GLIMPSES    3 fast DARK flashes (code · "NEURONS" · palette) w/ glitch stabs — "something's coming"
6–10s  BUILD       "What if one agent…" / "…could build the whole thing?" tension rising
10–12s HOLD        "W A T C H ." letter-spacing expands; the field starts to IGNITE (gain ramps 0.3→1)
12s    THE DROP    big chromatic flash → the REAL logo scales in + the text-to-lottie BURST blooms
                   + "YUV.AI" rainbow. The payoff. (FRAME.md "Neural-Net Phoenix Cover")
17–26s PROOF RUSH  fast slams: HYPERFRAMES · MANIM · (Manim clip beat) · LOTTIE · FRAME.MD  (FOMO)
26–31s CLIFFHANGER slow again: "An agent made this teaser." / "So can yours." (yours = pink-glow)
31–40s END CARD    logo + "LET'S FLY HIGH" + the full LINK SET + CTA pill → fade
```
Build → rest → **drop** → rush → **hold** → card. The drop only hits because the open was restrained.

## Techniques that sell "cinematic"
- **Heavy vignette** (`radial-gradient … rgba(0,0,0,.72)`) + **film grain** overlay throughout.
- **Field-ignite envelope** — the neural-net field `gain(t)` stays low (~0.3) until the drop, then ramps to 1. Darkness first makes the bloom land.
- **One idea on screen at a time** in the slow sections; **dramatic holds** (1–2s) on a single line.
- **The drop = chromatic flash + logo scale-in + the Lottie burst** firing together on one frame.
- **Statement reveals**: fade-up + slight `y` + (optional) blur-to-sharp; elegant, unhurried.

## Non-negotiable brand must-haves (every YUV.AI video)
1. **A real, featured Lottie** — generate one (don't ship a token pulse). Use the bundled
   [../assets/lottie-burst-generator.py](../assets/lottie-burst-generator.py) → a looping phoenix
   burst, or author another. This is the "text-to-lottie" requirement — verify it in lottie-web.
2. **The actual phoenix logo** — [../assets/logo-phoenix.png](../assets/logo-phoenix.png) at the reveal + end card (not just the CSS field).
3. **The link end-card** — logo + "LET'S FLY HIGH" + the full link set + a CTA. See [brand-kit.md](brand-kit.md).
4. **Grounded in FRAME.md** — its treatments (cover/statement/closing), lead/counter, glow-in-moderation, the neural-net field + phoenix.
