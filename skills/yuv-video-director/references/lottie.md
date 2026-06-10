# Lottie — branded motion graphics (live, lottie-web)

Use for *designed* brand motion: logo stings, stat reveals, icon pops, the neural pulse. For plain
kinetic text, prefer GSAP.

## The trap (read this)
`diffusionstudio/lottie` (text-to-lottie) previews in **Skottie** (Skia). HyperFrames renders in
**lottie-web**. JSON that's perfect in Skottie can render **blank** in lottie-web (different AE
feature support, group-wrapping rules). **Always screenshot-verify the Lottie in the actual
HyperFrames render — not just the Skottie preview.**

## Authoring a Lottie that renders in lottie-web
- Plain **Bodymovin JSON** (`v, fr, ip, op, w, h, assets:[], layers:[]`).
- Shape layers (`ty:4`) with a group (`ty:"gr"`) → `el`/`sh` + `fl`/`st` + a trailing `tr` transform.
- Animate via the **layer transform** `ks` (scale `s`, opacity `o`) with keyframes carrying `i`/`o`
  bezier handles — lottie-web needs them.
- Colors are normalized RGBA arrays: pink `#FF1464` → `[1, 0.0784, 0.3922, 1]`, cyan `#00E5FF` → `[0, 0.898, 1, 1]`.
- Template: **[../assets/neural-pulse.json](../assets/neural-pulse.json)** (cyan core + expanding pink/cyan rings, loops, renders in lottie-web — verified).

## Wiring into HyperFrames (the contract)
```html
<div id="pulse" style="width:200px;height:200px"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js"></script>
<script>
  window.__hfLottie = window.__hfLottie || [];
  const a = lottie.loadAnimation({
    container: document.getElementById("pulse"),
    renderer: "svg", loop: true, autoplay: false,   // autoplay MUST be false
    path: "assets/neural-pulse.json",                // local asset, not a remote URL
  });
  window.__hfLottie.push(a);                          // the adapter seeks every entry
</script>
```
HyperFrames' lottie adapter seeks each `__hfLottie` entry to composition time via
`goToAndStop(t·1000, false)`. Don't call `.play()`. Keep the container size stable.
For dotLottie (`.lottie`), use `DotLottie` + `setCurrentRawFrameValue`; it must be pushed manually.

## ⚠️ Seek-clamp gotcha (sections later than the lottie's duration)
The adapter seeks to COMPOSITION time — if a section starts at 55s but the lottie's total
duration is 35s, lottie-web clamps to the LAST frame (often an invisible cycle-start pose).
Fix: wrap `goToAndStop` with a deterministic modulo (see the `L()` helper in
[teaser-explainer.md](teaser-explainer.md) — use it in every composition; harmless when not needed).

## Content-synced beats + transparency (the standard)
Lotties must illustrate the SPOKEN content at the exact moment it's said — director-timed beats,
fully transparent (no chip/box; drop-shadow only), persistent+continuous design so any window
reads. Six production-grade content animations + their generator are bundled:
[../assets/gen_content_lotties.py](../assets/gen_content_lotties.py). Verify transparency by
rendering the test grid over an odd-colored background. Full method: [teaser-explainer.md](teaser-explainer.md).
