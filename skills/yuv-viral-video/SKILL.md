---
name: yuv-viral-video
description: Edit any selfie or screen-share footage into a viral short-form video in YUV.AI's signature style — Apple-style liquid-glass cards (real CSS backdrop-filter), dark-mode polish, MrBeast-paced cuts, video-title karaoke captions, premium GSAP motion graphics, no fake content, never covering the speaker's face. Look and fonts come from yuv-design-system (Phoenix Ink): Hebrew in Karantina + Assistant, English in Anton uppercase. Always renders BOTH 9:16 and 16:9 and always saves with _V<N> suffix for backups. Trigger when the user drops a path to an .mp4/.mov/.mkv and says "edit this", "make it viral", "turn this into a short", or any Hebrew equivalent (ערוך סרטון, סרטון ויראלי, להפוך לוויראלי, ריל, שורט). The pipeline is the COMBINATION of two skills: video-use (transcription + word-snapped cuts + base extraction) and hyperframes (HTML/CSS/GSAP visual composition + render). Do NOT use for podcast-only audio edits.
---

# Yuv-Viral-Video

The signature YUV.AI viral-short pipeline. **Two skills working together**:

- **`video-use`** — transcribes the source via ElevenLabs Scribe, picks word-snapped cuts, extracts and concats segments into a `base.mp4`. This is the cuts + base layout layer.
- **`hyperframes`** — takes the base as a background video and adds the visual composition layer in HTML/CSS/GSAP: liquid-glass cards with real `backdrop-filter`, GSAP motion graphics with `back.out` springy easing, word-by-word karaoke captions, scene transitions, and renders to MP4 via Chromium.

**You MUST use both.** Do not invent your own PIL-based cards, do not pre-bake blur into PNGs, do not write your own ffmpeg compositor. The hyperframes skill exists specifically to do the visual layer at Hollywood quality.

## Companion skills (read these BEFORE you start)

Both companion skills are installed locally and auto-discovered by Claude Code at session start. **You MUST load and apply their guidelines** — this skill is the *editorial* layer on top of them, not a replacement.

| Skill | Path | Owns |
|---|---|---|
| `video-use` | `~/.claude/skills/video-use/SKILL.md` (symlink → `~/Developer/video-use`) | Transcription (ElevenLabs Scribe), word-snapped cuts, color grade, ffmpeg-correctness (per-segment extract → `-c copy` concat, 30 ms audio fades, `setpts=PTS-STARTPTS+T/TB` overlays, output-timeline SRT offsets, transcript caching). Read its **"Hard Rules (production correctness — non-negotiable)"** section before authoring `edl.json`. Helpers live at `~/Developer/video-use/helpers/` and are invoked as `python helpers/<name>.py`. |
| `hyperframes` | `~/.claude/skills/hyperframes/SKILL.md` | HTML-as-source-of-truth video compositions, `data-*` timing attributes, CSS-driven appearance, frame-accurate library-clock animation (GSAP, Lottie, Motion One). Read its companion docs `house-style.md`, `data-in-motion.md`, `patterns.md`, `visual-styles.md` before writing the composition `index.html`. |
| `hyperframes-cli` | `~/.claude/skills/hyperframes-cli/SKILL.md` | The `hyperframes init / lint / preview / render / transcribe / tts` commands. CLI is also installed globally (`hyperframes` on `$PATH`) so `npx` is optional. |
| `gsap` | `~/.claude/skills/gsap/SKILL.md` | The full GSAP animation vocabulary. The `back.out(1.7)` springy easing rule in this document is one applied pattern; reach for gsap's full toolkit when the material calls for it. |
| `website-to-hyperframes` | `~/.claude/skills/website-to-hyperframes/SKILL.md` | One-shot: scrape a URL → hyperframes composition. Useful when the source has on-screen UI worth re-staging. |

### Precedence (when this document conflicts with a companion skill)

- **Production correctness (cuts, encoding, ffmpeg flags, ffmpeg filter ordering, transcript handling) → companion skill wins.** If `video-use` says "subtitles applied LAST in the filter chain after every overlay" and this document is silent or different, do what `video-use` says. Same for hyperframes API conventions, `data-*` attributes, frame-adapter patterns.
- **Editorial style (fonts, glass cards, "never cover the face", `_V<N>` versioning, archetype layout decisions, MrBeast pacing, no-fabricated-content rule) → this document wins.** Companion skills are deliberately style-agnostic; the YUV.AI house style lives here.
- **Strategy confirmation:** `video-use` Hard Rule 11 says "confirm the plan in plain English before executing." For viral shorts in YUV.AI style this is **deliberately suspended** — the style is fully captured in this document's Hard Rules, so the agent should execute the first pass and iterate from feedback rather than blocking on creative-direction questions. (For non-viral video-use sessions, follow the companion skill's rule.)
- **Cut-edge padding:** `video-use` allows 30–200 ms; this document picks 50 ms head / 80 ms tail as the YUV.AI default within that range. Both are correct; the narrower value is a style choice.

### Shared configuration

Both skills read `ELEVENLABS_API_KEY` from `~/Developer/video-use/.env`. Set it once and both skills work. Do not duplicate the key in this skill's directory.

## Save location

**Default:** `~/Documents/yuv-projects/videos/<slug>/` — always save viral video projects here so renders are findable. The `<slug>` is short, derived from the topic or source filename.

```bash
mkdir -p ~/Documents/yuv-projects/videos
cd ~/Documents/yuv-projects/videos
# Initialize the project here.
hyperframes init <slug> --video <source.mp4> --non-interactive
cd <slug>
```

Final renders land at `~/Documents/yuv-projects/videos/<slug>/renders/final_*_V<N>.mp4` (both 9:16 and 16:9). Tell the user where the videos live at the end of every render.

---

## Style preferences (from `yuv-design-system`, Phoenix Ink v3)

This skill is the **video instantiation** of Yuval Avidani's brand system. **`yuv-design-system` is the only source of colours, fonts, logos and motion rules**; the tables below are a summary of it for this pipeline. If they ever differ, yuv-design-system wins. They override any companion-skill defaults that conflict.

### Typography

| Role | English | Hebrew | Rule |
|---|---|---|---|
| Display / cards / karaoke captions | **Anton** (uppercase, weight 400, letter-spacing `0` — never negative) | **Karantina 700** (condensed: size it ~1.25× what you'd give Assistant) | Always uppercase for English, never title case. |
| Body / glass-card body copy / chip text | **Inter** (400 / 500 / 600 / 700) | **Assistant** (500 / 700 / 800) | Use only when the card has secondary body copy beneath the display title. Line-height 1.4 inside cards. |
| Numbers / counters / stats | **Anton** | **Karantina 700** | Treat numbers as display text, never body. |
| Code / mono (terminal cards, paths) | **JetBrains Mono** | — | For typewriter-style code reveals. |

**Hebrew direction:** `dir="rtl"` on every Hebrew caption container. Use `python-bidi`'s `get_display()` only in PIL fallback paths; CSS handles RTL natively. Logical CSS properties (`margin-inline-*`, `padding-inline-*`) preferred over physical (`margin-left`).

**Banned:** Rubik, Heebo and Suez One (retired), serif fonts as defaults, system-ui stack, Anton on Hebrew text (renders as hollow X — Anton is Latin-only).

### Color palette (Phoenix Ink, inside the MP4)

| Role | Value | Use |
|---|---|---|
| Stage / dark BG | night `#0E0D2A` → `#14123A` (the night sky: `#0A0922 → #15133C` with soft pink / violet / orange glows) | Layout-B backgrounds, letterbox fill, end card |
| Text | `#FFFFFF`, secondary `#CFCDEB` | Captions, card text |
| Brand thread | pink `#FF2EA0` (on night text: `#FF8FCC`) | Glass-card border accents, key-moment strip stroke, emphasis words, the CTA pill |
| Marker / active word | gold `#FFD66E` (marker block: `linear-gradient(180deg,#FFD66E,#F4B030)` with ink `#1C1A4B` text) | Active karaoke word, one key word per card |
| Tiny accents | violet `#8B6CFF`, cyan `#5DE4E9`, orange `#FF8F3A` | Glows and small marks only |

**Banned in any rendered output:**

- Every retired system listed at the top of yuv-design-system: Fly High purple `#5E17EB` + yellow `#FFEC00`, neon `#FF1464` + `#00E5FF`, Liquid Glass magenta + `#16D6E8`, Warm Editorial bone/cream.
- Pure black stages (`#000`, `#0A0A0A`, `#0c0e16`) — use night.
- Default Tailwind palette names (`slate-*`, `zinc-*`, `gray-*`, `emerald-*`, `cyan-*`, `indigo-*`, `violet-*`, `rose-*`).
- Multicolor icon sets — Phosphor or Lucide single-stroke only.

### Layout & motion defaults

- **Border radius:** glass cards use `36–56px` (signature soft-rounded). Pill CTAs `999px`. Never the 8/12px corporate-rounded middle ground.
- **Shadows:** pink-tinted on light surfaces (`0 18px 40px rgba(255,46,160,.07)`), deep night on dark ones (`0 26px 60px rgba(14,13,42,.45)`); never the default blue-black `rgba(0,0,0,.1)`.
- **Whitespace:** generous. Cards never fill more than 60% of the frame's free zone.
- **Asymmetry over grid-perfect.** Offset cards. Overlap. One element breaking the grid.
- **Grain:** 1–2% noise on any preview / catalog page (not inside the rendered MP4 — would compress to mush).
- **Animation library:** GSAP (always). `back.out(1.7)` for card entrances, `power3.out` for SplitText reveals, `expo.out` for slam beats, `sine.inOut` for idle floats.

### Inheritance rule

If you are building any auxiliary surface (a preview page, a catalog, a dashboard, a render-status UI), apply `yuv-design-system` in full: night hero / paper and cloud sections, pink accent, gold marker, its components, the real phoenix and wordmark, the canonical links. It is the canonical source of truth for all Yuval-brand visuals.

If you are rendering the MP4 itself, apply the table above. Same brand, two delivery surfaces. Every shareable video ends on the phoenix + wordmark + links (yuv-design-system §8–§9).

## The live effects catalog (use this as the menu)

Yuval maintains a public, live, scrollable visual catalog of every effect, transition, marker, card, theme, and SFX this skill can apply to a video:

**👉 https://effects.yuv.ai**

When commissioning an edit, Yuval (or anyone he sends the catalog to) clicks any effect's chip — the chip copies a stable identifier like `captions.karaoke.scale-pop` to the clipboard. He pastes those IDs into the prompt:

> *"edit this with `style.swiss-pulse`, captions `karaoke.scale-pop`, `marker.circle` on stats, transition `blur-crossfade`, sfx `whoosh` on every cut, sfx `impact` on hero word."*

**You must respect every effect ID** the user pastes. The catalog page is the single source of truth — every ID maps to a documented effect with verified behaviour. If the user names an ID you don't recognize, fetch the catalog (https://effects.yuv.ai) and find its definition rather than improvising.

The catalog also contains a **prompt library** (effects.yuv.ai #prompts) with 8 production-ready full-edit prompts (product launch / explainer / live-code / flow walkthrough / hot-take / tutorial / founder pitch / Hebrew talking-head). When the user references "the prompt for X scenario," route there.

## Bilingual rendering — Hebrew + English in the same video

Many edits will mix Hebrew narration with English brand tokens (Claude, GitHub, hyperframes, etc.). The skill must:

1. **Per-glyph font routing** — Anton handles Latin, Karantina handles Hebrew. The single `font-family: 'Anton', 'Karantina', sans-serif` declaration on every display container does this automatically (body text: `'Inter', 'Assistant', sans-serif`). Never apply Anton to a Hebrew character (it renders as a hollow X — Anton is Latin-only).

2. **RTL containers** — every Hebrew caption line gets `dir="rtl"` on its container. English brand tokens stay LTR within the same line via the browser's bidirectional algorithm — no manual reordering needed.

3. **Brand-name spelling in Hebrew** — Yuval's preferred Hebrew transliterations:
   - "Claude" → **"קלוד"** (not "קלאוד")
   - "Hyperframes" → keep English ("Hyperframes")
   - "GitHub" → keep English ("GitHub")
   - When Scribe transcribes a brand name with the wrong Hebrew spelling, fix it in the post-transcription pass before generating the karaoke layer.

4. **Companion catalog has bilingual EN/HE everywhere** — the live catalog flips entire UI to Hebrew on toggle (see effects.yuv.ai). The same `data-lang` toggle pattern applies to any auxiliary surface this skill produces (preview pages, render-status UIs, etc.).

## Lessons baked from production iterations

The video pipeline itself is governed by the Hard Rules below — but any HTML/CSS surface this skill produces (preview page, render dashboard, catalog) must respect yuv-design-system §2 and §5:

- **Bilingual = toggle, not side-by-side**
- **Mobile = hamburger nav under ~940px**
- **One display headline per section**
- **`document.title` is part of language toggle**
- **IntersectionObserver for any catalog with >8 demos**
- **Build comprehensive on first pass — don't iterate on scope**
- **`Claude-in-Chrome` for SPAs, `WebFetch` only for static HTML**
- **Verify content from real source pages, never invent**

## When to consult this skill

Any time the user drops a video file and asks for an edit. Even a one-line ask like *"take this and edit it: <path>"* should trigger the full flow below. Don't ask for creative direction up front — the user's style is captured in the **Hard Rules** below; just execute and iterate from feedback.

## Three things to internalize before touching anything

**1. NEVER invent content.** Every word on every card must trace to something the speaker actually said in the transcript. No fake currency placeholders ("$$$"), no fake percentages ("100% understood"), no invented CTAs ("link in bio") if no link was promised. The user will catch fabricated content instantly and trust collapses fast. When in doubt, copy the literal Hebrew quote into the card. Same rule applies to Hebrew transliteration of brand names — for example, when a brand is "Claude", the proper Hebrew transliteration is "קלוד" (not "קלאוד"); use the brand owner's preferred spelling, not whatever Scribe heard.

**2. NEVER cover the speaker's face.** Position cards in the *opposite* half of the frame from the face, or use a top/bottom banner that sits above/below the face zone. For a full-frame selfie, the safe zones are y=0–400 (top banner) and y>1500 (bottom). For screen-share footage where the speaker is in a corner PIP, cards live anywhere in the screen-content area.

**3. NEVER non-uniformly scale the speaker.** Source PIP aspect must equal target PIP aspect. If you scale a 470×460 source crop into a 920×580 box, the speaker comes out horizontally squished and the user will reject the output. Pick target dims that match source aspect, or use `force_original_aspect_ratio=decrease` + center-pad.

Everything else in this document is a worked example or a tooling detail. The three above are non-negotiable.

## The pipeline (high-level)

```
source.mp4
   ↓  video-use: transcribe (ElevenLabs Scribe — word-level + diarized + audio events)
transcripts/<source>.json
   ↓  pick word-snapped beats → edl.json (ranges with start/end, layout per range, motion per beat)
   ↓  video-use: build base.mp4 per aspect (per-segment extract + grade + 30ms fades + concat)
base_<aspect>_V<N>.mp4   (one per aspect — 9:16 and 16:9)
   ↓  generate output-timeline transcript.json (word-level, output-timeline timestamps, brand-name spelling fixed)
transcript.json
   ↓  hyperframes init <project>     (creates index.html scaffold + DESIGN.md slot)
   ↓  hyperframes: build composition.html
   :   <video> bg + glass cards (CSS backdrop-filter) + karaoke caption layer + GSAP timeline
   ↓  hyperframes lint           (validates the composition)
   ↓  hyperframes render          (Chromium captures every frame, mux to MP4)
final_<aspect>_V<N>.mp4
```

## Hard Rules (the editor's bill of rights)

These are correctness rules. Deviation produces silent failures or angry users.

1. **Hebrew display = Karantina 700, Hebrew body = Assistant. English = Anton uppercase.** Never mix. Never substitute. The fonts are bundled in `assets/fonts/` (Karantina-Bold, Assistant-Bold/ExtraBold, Anton) because download URLs change. In hyperframes CSS, declare `font-family: Karantina` (weight 700) for Hebrew display, `Assistant` for Hebrew body and `Anton` for English; the compiler embeds them automatically.
2. **Real CSS backdrop-filter for glass.** `backdrop-filter: blur(40px) saturate(160%)` on the card body. Do NOT pre-bake blur into a PNG. Do NOT use semi-transparent fills as a stand-in for blur — they look flat.
3. **3D-tilt entrance for cards.** GSAP entrance: `scale 0.85 → 1.0`, `rotationY -12deg → 0`, `y +60 → 0` with `ease: "back.out(1.7)"` and `transformPerspective: 900`. No flat fade-ins.
4. **Word-by-word karaoke synced to the transcript.** Active word: `scale 1.0` + accent color. Past/future words: `scale 1.0` at 55% opacity. Per-word `gsap.fromTo(scale 1.5 → 1.0, ease "back.out(2)", duration 0.16)` on activation.
5. **Subtitles applied LAST.** The karaoke layer has the highest z-index. No card should overlap it.
6. **Per-segment extract → `-c copy` concat.** The video-use skill enforces this; mirror it. Single-pass filtergraphs cause double-encode of every segment.
7. **30 ms audio fades at every segment boundary.** `afade=t=in:st=0:d=0.03,afade=t=out:st={dur-0.03}:d=0.03`. Without this, audible pops at every cut.
8. **Word-boundary snapping with 50 ms head / 80 ms tail padding.** Cut edges come from `word.start` / `word.end` in the Scribe transcript.
9. **Cache transcripts.** Never re-transcribe the same source. Scribe costs money.
10. **All Hebrew text in any rendering pass must be RTL-correct.** In CSS, set `dir="rtl"` on the container; libass handles RTL natively. In any PIL fallback path, use `python-bidi`'s `get_display()`.
11. **Even pixel dimensions.** ffmpeg's `yuv420p` chroma subsampling requires even W and H. Odd dims silently round, which then breaks `alphamerge` ("Input frame sizes do not match").
12. **Aspect preservation on the speaker PIP.** Match source crop aspect to target PIP aspect.
13. **NEVER make up content.** Audit every string against the transcript before render.
14. **Save every render with `_V<N>.mp4` suffix.** Each iteration writes a NEW versioned file. Never overwrite a previous final — the user keeps backups by version.
15. **All session outputs in `<videos_dir>/edit/`.** Never write inside the skill directory.

## Layout decisions (the most important call you make)

The first decision after transcribing is **what the source footage actually is**. There are two archetypes:

### Archetype 1 — "Screen-share with speaker PIP corner"

Source: 16:9 with a screen recording (browser, app, dashboard) filling most of the frame, and the speaker's webcam in a small corner PIP. **The screen content IS the visual story.** Hide it and the user gets angry.

| Output | Top zone (screen content) | Bottom / corner zone (speaker PIP) | Card real estate |
|--------|---------------------------|------------------------------------|------------------|
| 9:16 | Top 2/3 — crop center column of source, scale to 1080×1280 | Bottom 1/3 — crop the source PIP region (e.g. 470×460), scale to a target with **matching aspect** (e.g. 600×588), apply rounded mask 50px+ | Hyperframes glass cards float in top 2/3 over the screen content; key-moment strip floats just above PIP |
| 16:9 | Full frame — scale source 2560×1440 to 1920×1080 | The PIP is naturally in source bottom-right; overlay a rounded-corner mask on that exact region | Cards on left half, key-strip across bottom |

### Archetype 2 — "Full-frame selfie"

Source: vertical or horizontal with the speaker filling the frame. There's no "screen" beyond the speaker themselves. **The speaker IS the content** — keep them prominent.

| Output | Speaker placement (per-beat) | Card real estate |
|--------|------------------------------|------------------|
| 9:16 | **Layout A (emotional beats — HOOK / PROBLEM / WOW / CTA)**: full-frame center-vertical crop. **Layout B (explanatory beats)**: speaker shrunk to a top-right rounded PIP (e.g. 480×640), dark gradient BG fills rest. Source crop for the PIP must include the speaker's full head — start `y` at ~80px in the source, NOT 200px+ (that cuts the forehead). | Layout B: glass cards fill the bottom 2/3 |
| 16:9 | Letterbox: scale source vertically to fit height, blurred (`gblur sigma=22`) zoomed copy fills the side bars, crisp speaker centered on top | Cards on left half over the blurred BG |

If the source is HYBRID (some beats are full speaker, others screen-share), pick the archetype per beat. Set `"layout": "A"` or `"layout": "B"` per range in `edl.json`.

## Apple-style liquid-glass cards (the hyperframes layer)

**The card style is non-negotiable.** Build it in HTML/CSS, not PIL.

```css
.card {
  position: absolute;
  border-radius: 56px;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(40px) saturate(160%);
  -webkit-backdrop-filter: blur(40px) saturate(160%);
  border: 1.5px solid rgba(255, 255, 255, 0.18);
  box-shadow:
    0 26px 60px rgba(14, 13, 42, 0.5),
    inset 0 2px 0 rgba(255, 255, 255, 0.18);
  padding: 60px 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 24px;
  transform-origin: center;
  will-change: transform, opacity;
}
.card.dark {
  background: rgba(20, 18, 58, 0.62);
}
```

```js
// Entrance — 3D tilt-pop with overshoot
gsap.set(".card", { opacity: 0, scale: 0.85, y: 60, rotationY: -12, transformPerspective: 900 });
tl.to(sel, { opacity: 1, scale: 1.0, y: 0, rotationY: 0, duration: 0.55, ease: "back.out(1.7)" }, beat.s + 0.05);
// Subtle idle float — keeps the card alive
tl.to(sel, { y: -8, duration: 0.9, ease: "sine.inOut", yoyo: true, repeat: 1 }, beat.s + 0.6);
// Exit
tl.to(sel, { opacity: 0, scale: 0.95, y: -30, duration: 0.30, ease: "power2.in" }, beat.e - 0.30);
tl.set(sel, { visibility: "hidden" }, beat.e);
```

**Inside the card**, stagger the children so the card "fills" itself with content rather than appearing all at once:

```js
tl.from(`${sel} .chip`, { y: 30, opacity: 0, scale: 0.9,
  duration: 0.4, ease: "back.out(1.6)", stagger: 0.10 }, beat.s + 0.40);
```

## Karaoke (video-title style)

Group transcript words into chunks of 3 (or break on >0.5s pauses). Each chunk becomes one `.cap-group` div. Within the chunk, each word is a `<span class="cap-word">` (or `.cap-word.en` for English brand tokens, `.cap-word.accent` for emphasis Hebrew).

CSS:

```css
.cap-word {
  font: 700 135px Karantina;           /* ~1.25× the old 108px: Karantina is condensed */
  color: rgba(255, 255, 255, 0.55);    /* dim future/past */
  text-shadow: 0 8px 18px rgba(14,13,42,.85), 0 0 28px rgba(14,13,42,.7);
  -webkit-text-stroke: 4px #0E0D2A;
  transform-origin: center bottom;
}
.cap-word.en { font: 400 124px Anton; letter-spacing: 0; color: rgba(255, 214, 110, 0.6); }
.cap-word.active { color: #FFFFFF; }
.cap-word.en.active { color: #FFD66E; }
.cap-word.accent.active { color: #FF8FCC; text-shadow: 0 0 20px rgba(255,46,160,.55); }
```

GSAP per-word:

```js
tl.fromTo(wordSel,
  { scale: 1.5, opacity: 0 },
  { scale: 1.0, opacity: 1, duration: 0.16, ease: "back.out(2)" },
  word.start);
tl.call(() => document.querySelector(wordSel).classList.add("active"), [], word.start + 0.02);
```

Group entrance/exit per `cap-group`:

```js
tl.fromTo(groupSel,
  { opacity: 0, visibility: "visible", scale: 0.85, y: 30 },
  { opacity: 1, scale: 1, y: 0, duration: 0.25, ease: "back.out(1.6)" },
  group.start);
tl.to(groupSel, { opacity: 0, scale: 0.95, y: -20, duration: 0.2, ease: "power2.in" }, group.end - 0.20);
tl.set(groupSel, { visibility: "hidden" }, group.end);
```

**English brand tokens stay English.** The detection regex `^[A-Za-z][A-Za-z0-9\-']*$` routes English/brand words to the EN style (Anton, uppercase). Hebrew flows through libass+FriBidi for RTL or via `dir="rtl"` in CSS.

## Per-segment dynamic motion

Every segment baked-in motion. Subtle MrBeast-style amounts.

| Kind | Effect | Typical amount |
|------|--------|----------------|
| `push_in` | Slow zoom in | 0.04–0.07 |
| `pull_out` | Slow zoom out (revealing) | 0.05–0.07 |
| `snap_in` | Cubic ease-out punch zoom | 0.05–0.10 |
| `dolly_l` / `dolly_r` | Held zoom + horizontal drift | 0.04 |
| `hold` | No motion (use sparingly) | – |

Keep amounts subtle. Anything ≥0.10 outside of WOW-class beats reads as "too much zoom".

## Bottom key-moment strips

A small glass strip across the bottom summarising the current beat in 1–4 words. Hebrew on the right (RTL), English on the left (Anton uppercase), pink border. Appears only on key beats — not every beat.

```css
.km-strip {
  position: absolute;
  left: 40px; right: 40px;
  bottom: 30px;
  height: 110px;
  border-radius: 30px;
  background: rgba(20, 18, 58, 0.62);
  backdrop-filter: blur(30px);
  border: 1.5px solid rgba(255, 46, 160, 0.55);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  z-index: 70;
}
```

## SFX library

Generated via ElevenLabs sound-generation API. Standard kit:

- `impact.mp3` — HOOK punch + WOW slam
- `bass_drop.mp3` — layered with impact for the boom
- `whoosh.mp3` — every cut transition
- `riser.mp3` — building into a punchline
- `ding.mp3` — UI pop on card reveals + per-bar dings on chart entrance
- `glitch.mp3` — short transition glitch
- `typing.mp3` — under any terminal/coding card

Mix in the video-use base layer (not in hyperframes) so the audio is committed before the visual composition reads it.

## Versioning

**Every render writes a NEW file.** Find the highest existing `final_<aspect>_V<N>.mp4` and increment. The composite scripts split `BASE_VERSION` (read from) and `OUT_VERSION` (write to) so the base can be reused across multiple final iterations.

## Common failure modes (and the fixes)

- **"Input frame sizes do not match (X vs Y)"** → odd target dimension. Round to even pixels for both W and H.
- **Hebrew letters render reversed** → in CSS, set `dir="rtl"` on the container. In PIL fallbacks, wrap with `bidi.get_display()`.
- **Hebrew avatar letter renders as hollow X** → using Anton font for a Hebrew character. Anton is Latin-only. Switch to Karantina (display) or Assistant (body) for any text containing Hebrew.
- **`Filter 'split' has output 0 unconnected`** → declared a split but didn't consume one of its outputs. Check labels match.
- **Speaker looks horizontally squished** → non-uniform scale on the PIP source crop. Match target aspect to source aspect.
- **Speaker forehead/hair cut off in PIP** → source crop `y` started too low. For a 2560×1440 source where the speaker fills the frame, start `y ≈ 80`, not 200+.
- **`subtitles=` filter fails on Windows** → unescaped colon in the path. Escape with `\:`.
- **`-shortest` ignored** → `-loop 1` on a PNG creates an infinite stream. Add `-t <dur>` to constrain the looped input.
- **`-t` doesn't limit source duration** → `-t` is an *input option* and must come BEFORE the `-i` it applies to.
- **Hyperframes "sparse keyframes" warning** → re-encode the base with `-g 30 -keyint_min 30` for smooth seek. `ffmpeg -i in.mp4 -c:v libx264 -r 30 -g 30 -keyint_min 30 -movflags +faststart -c:a copy out.mp4`.

## File layout (per project)

```
<videos_dir>/edit/
├── transcripts/<source>.json          (cached Scribe output)
├── edl.json                           (cut decisions, layout per range, motion per beat)
├── transcript.json                    (output-timeline word-level, generated for hyperframes)
├── base_<aspect>_V<N>.mp4              (video-use cuts + base layout, audio mixed)
├── hf/                                 (hyperframes project)
│   ├── DESIGN.md                       (visual identity — colors, fonts, motion rules)
│   ├── index.html                      (the composition)
│   ├── base_9x16.mp4 / base_16x9.mp4   (copied from parent edit/)
│   ├── transcript.json                 (copied from parent edit/)
│   └── renders/                        (hyperframes output)
└── final_<aspect>_V<N>.mp4              (copied from hf/renders/, with version bumped)
```

## Setup

See `references/setup.md` for: ffmpeg, ElevenLabs API key, hyperframes CLI (`npx hyperframes`), python-bidi, fonts. The `video-use` skill is a hard prerequisite — install that first.

## Scripts (this skill)

These scripts handle the video-use side (cuts + base extraction). The hyperframes side is authored as HTML/CSS/JS per project — no fixed scripts there because every project has its own beats and content.

- `scripts/apple_glass.py` — `apple_glass_card()`, `make_glass_mask()`, `make_dark_bg()`, `rtl()`, `COLORS`, layout constants. Used as a PIL fallback only — prefer hyperframes for production cards.
- `scripts/build_screen_share.py` — base build for Archetype 1 (screen-share + corner PIP)
- `scripts/build_selfie.py` — base build for Archetype 2 (full-frame speaker)
- `scripts/make_karaoke.py` — output-timeline ASS karaoke (used as a PIL fallback or for ffmpeg-direct paths)
- `scripts/make_sfx.py` — ElevenLabs SFX batch generator
- `scripts/composite_screen_share.py` / `scripts/composite_selfie.py` — full ffmpeg filter_complex paths (legacy, prefer hyperframes)
- `scripts/make_layout_assets.py` — pre-render dark-mode BG + speaker masks

## The unbreakable promise

If the user drops a video and asks for an edit, the output:

1. Shows the screen content if it's a screen-share (NEVER hide it under dark BG).
2. Shows the speaker prominently if it's a selfie (NEVER shrink to tiny corner).
3. Has every card text traceable to a real spoken word in the transcript.
4. Renders both 9:16 AND 16:9.
5. Saves with `_V<N>` so the previous version is preserved.
6. Uses Karantina + Assistant for Hebrew, Anton uppercase for English, and Phoenix Ink colours. Always.
7. Never covers the speaker's face.
8. Uses **hyperframes** for the visual composition (real CSS backdrop-filter, GSAP springy easing, Hollywood-grade animation).

Get those right and you've delivered. Anything else is polish.
