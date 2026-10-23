# yuv-viral-video

The **YUV.AI viral-short editor** — a Claude Code / Codex / agent-discoverable skill that turns a raw selfie or screen-recording into a finished short-form video in Yuval Avidani's signature style.

> Drop the path to an `.mp4` / `.mov`, type *"edit this"* (or in Hebrew *"ערוך סרטון"*), and the agent runs the full pipeline: transcribe → cut → grade → glass-cards → karaoke captions → SFX → render to both **9:16 and 16:9**, saved with a `_V<N>` suffix so previous renders are preserved.

---

## What you get

- **Apple-style liquid-glass cards** with real CSS `backdrop-filter` (no PIL pre-bake).
- **Word-by-word karaoke captions**: full sentence visible, inactive words at 45% opacity, active word slammed to 1.0 with a yellow accent + scale pop.
- **Hebrew + English bilingual rendering**: Karantina + Assistant for Hebrew, Anton uppercase for English. Brand-name spelling auto-fixed.
- **MrBeast-paced cuts**: word-snapped boundaries, 30 ms audio fades, no static moments.
- **GSAP motion graphics**: `back.out(1.7)` 3D tilt-pop card entrances, idle floats, scatter exits, marker highlights (sweep / circle / burst / scribble / sketchout).
- **Audio-reactive captions** when the source is music.
- **ElevenLabs SFX kit**: impact, bass-drop, whoosh, riser, ding, glitch, typing — generated on demand.
- **No fabricated content**: every word on every card traces back to something the speaker actually said.
- **Speaker face is never covered**: cards always live on the opposite half of the frame.
- **Always two aspects**: 9:16 (TikTok / Reels / Shorts) and 16:9 (YouTube / LinkedIn / X).
- **Always versioned output**: every render writes a NEW file. Nothing overwrites a final you liked.

---

## You install ONE skill, you're done

This skill **does not stand alone** — it composes two open-source companion skills. **Install all three once, and from then on you can edit any video by typing one sentence.**

| Skill | Source | What it owns |
|---|---|---|
| `yuv-viral-video` | this repo | Editorial style, cards, karaoke colors, SFX kit, archetype layouts, "never cover the face" rules |
| `video-use` | [browser-use/video-use](https://github.com/browser-use/video-use) | Transcription (ElevenLabs Scribe), word-snapped cuts, color grade, ffmpeg correctness |
| `hyperframes` (+ `gsap`, `hyperframes-cli`, `hyperframes-registry`, `website-to-hyperframes`) | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | HTML/CSS/GSAP composition, frame-accurate render to MP4 |

These are all **agent-discoverable skills** — once placed in `~/.claude/skills/` (or your agent's equivalent), Claude Code / Codex / Cursor / Gemini-CLI auto-load them at session start.

---

## Style preferences — automatic

You don't have to repeat your brand on every video request. The skill takes Yuval Avidani's design system, **Phoenix Ink** (the `yuv-design-system` skill, the single source of truth), as its defaults:

### Typography
- **English display / cards / captions:** Anton, UPPERCASE, weight 400, letter-spacing 0 (never negative)
- **Hebrew display / captions:** Karantina 700 (condensed: ~1.25× size)
- **Body / chip / secondary text:** Inter (English) / Assistant (Hebrew)
- **Code / terminal:** JetBrains Mono

### Color palette
- **Stage:** night `#0E0D2A` → `#14123A` (the night sky with soft pink / violet / orange glows)
- **Pink (brand thread):** `#FF2EA0` — glass-card borders, key-moment strips, emphasis words, the CTA
- **Gold (marker / active word):** `#FFD66E` → `#F4B030`
- **Text:** white, secondary `#CFCDEB`

### Banned
- The retired systems: Fly High purple + yellow, neon `#FF1464` + `#00E5FF`, Warm Editorial bone, Rubik for Hebrew
- Blue / navy / slate accents (warm family only)
- 8 px / 12 px "corporate-rounded" radii (use 0, 999px, or 40–56px)
- Default Tailwind palette names
- Multicolor icon sets (Phosphor / Lucide single-stroke only)

### Layout
- Asymmetric over grid-perfect-symmetric
- Two archetypes per video: **screen-share + PIP corner** OR **full-frame selfie** (per-beat decision)
- Cards live on the opposite half of the speaker's face

Full details in `SKILL.md` → "Style preferences" section.

---

## Install (one-time, ~3 minutes)

### 1. Prerequisites

| Tool | macOS | Linux |
|---|---|---|
| ffmpeg ≥ 4 | `brew install ffmpeg` | `apt install ffmpeg` |
| Node ≥ 22 | `brew install node` | `apt install nodejs` |
| Python ≥ 3.10 | usually preinstalled | `apt install python3 python3-venv` |
| `uv` (Python pkg mgr) | `brew install uv` | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Hyperframes CLI | `npm i -g hyperframes` | same |
| Chrome or Chromium | already in `/Applications/` | `apt install chromium` |

### 2. Install the three skills

```bash
# yuv-viral-video (this skill)
mkdir -p ~/.claude/skills
cd /tmp && git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/hoodini/ai-agents-skills.git yuv-clone
cd yuv-clone && git sparse-checkout set skills/yuv-viral-video
cp -R skills/yuv-viral-video ~/.claude/skills/
cd && rm -rf /tmp/yuv-clone

# Python deps for the skill (isolated venv)
cd ~/.claude/skills/yuv-viral-video
python3 -m venv .venv && .venv/bin/pip install -q -r requirements.txt

# video-use
git clone https://github.com/browser-use/video-use ~/Developer/video-use
cd ~/Developer/video-use && uv sync
ln -sfn ~/Developer/video-use ~/.claude/skills/video-use

# hyperframes (5 skills bundled)
cd /tmp && git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/heygen-com/hyperframes.git hf-clone
cd hf-clone && git sparse-checkout set skills
cp -R skills/* ~/.claude/skills/
cd && rm -rf /tmp/hf-clone
```

### 3. ElevenLabs API key (the one piece I can't auto-do)

Both skills read the key from a single shared file:

```bash
mkdir -p ~/Developer/video-use
read -s -p "ElevenLabs API key: " KEY && echo
printf 'ELEVENLABS_API_KEY=%s\n' "$KEY" > ~/Developer/video-use/.env
chmod 600 ~/Developer/video-use/.env

# verify (200 = good, 401 = bad token)
curl -s -o /dev/null -w '%{http_code}\n' \
  -H "xi-api-key: $(sed -n 's/^ELEVENLABS_API_KEY=//p' ~/Developer/video-use/.env)" \
  https://api.elevenlabs.io/v1/user
```

Get a key from https://elevenlabs.io/app/settings/api-keys — Scribe (transcription) and Sound Generation (SFX kit) both go through this single key.

### 4. Restart your agent session

Claude Code / Codex / Cursor scan `~/.claude/skills/` (or equivalent) at session start. Restart and you'll see all 7 skills auto-load:

```
yuv-viral-video, video-use, hyperframes, hyperframes-cli,
hyperframes-registry, gsap, website-to-hyperframes
```

---

## How to use it

### The minimal prompt

> *Edit this: `~/Movies/source.mov`*
>
> *Or in Hebrew: ערוך לי את הסרטון הזה: ~/Movies/source.mov*

The skill takes over: transcribes, picks beats, drafts an EDL, builds the base, composes the visual layer, renders both aspects, and saves to `<videos_dir>/edit/`.

### A directed prompt (using effect IDs from the catalog)

> *Edit this with `style.swiss-pulse`, captions `karaoke.scale-pop` with `marker.circle` on every stat, transition `transition.blur-crossfade`, sfx `whoosh` on every cut and `impact + bass-drop` on the hero number.*

A live visual catalog of every effect, transition, marker, and SFX is published at the project's effects catalog — copyable IDs you can paste into your edit prompt.

### Iterate from feedback

> *V1 looks great except the karaoke is too loud — switch to `karaoke.subtle` and remove `marker.burst`.*

Each render writes a new `_V<N>` file. The skill reuses the cached transcript (Scribe is paid; never re-transcribes) and the cached base, so iterations are fast.

---

## Output structure

```
<videos_dir>/
├── source.mp4                 (original, untouched)
└── edit/
    ├── transcripts/<source>.json     ← cached Scribe output (re-used across iterations)
    ├── edl.json                       ← cut decisions (regenerated per session)
    ├── transcript.json                ← output-timeline word-level (for hyperframes)
    ├── base_9x16_V1.mp4               ← cuts + grade + audio mix
    ├── base_16x9_V1.mp4
    ├── hf/                            ← hyperframes project
    │   ├── DESIGN.md, index.html
    │   ├── base_9x16.mp4, base_16x9.mp4
    │   ├── transcript.json
    │   └── renders/
    ├── final_9x16_V1.mp4              ← deliverable, share this
    ├── final_16x9_V1.mp4
    ├── final_9x16_V2.mp4              ← V2 after feedback
    └── final_16x9_V2.mp4
```

Nothing is ever overwritten. Old versions are kept indefinitely so you can compare or revert.

---

## What it WON'T do

- **Won't fabricate content.** Every card text traces to a real spoken word in the transcript.
- **Won't cover the speaker's face.** Cards live on the opposite half of the frame.
- **Won't horizontally squish the speaker.** PIP source aspect always equals target aspect.
- **Won't ask for creative direction up front.** Your style is preset; the agent executes the first pass and you iterate.
- **Won't render only one aspect.** Always both 9:16 and 16:9.
- **Won't overwrite a previous final.** Always `_V<N+1>` on iteration.
- **Won't use podcast-only audio edits.** This skill is for video. For pure-audio editing, use `video-use` directly.

---

## Companion documentation

- **[`SKILL.md`](./SKILL.md)** — the full editorial bible (3000+ lines: archetypes, hard rules, tooling, common failure modes).
- **[`references/setup.md`](./references/setup.md)** — first-time install playbook.
- **[`assets/fonts/`](./assets/fonts/)** — bundled Anton, Karantina Bold and Assistant Bold / ExtraBold TTFs (Latin + Hebrew), with their OFL licences.
- **[`scripts/`](./scripts/)** — PIL/ffmpeg helpers (fallback path; prefer hyperframes for production).
- **[Effects catalog](https://github.com/hoodini/ai-agents-skills) (visual)** — live HTML catalog of every effect, transition, marker, and SFX with copyable IDs.

---

## Credits

Built on top of:
- [browser-use/video-use](https://github.com/browser-use/video-use) — transcription + cuts (Apache 2.0)
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) — HTML→MP4 rendering (Apache 2.0)
- [GSAP](https://gsap.com) — animation timeline (free since 2024 incl. SplitText)
- [ElevenLabs](https://elevenlabs.io) — Scribe transcription + sound generation

Editorial style, palette, archetype rules, and the YUV.AI signature: Yuval Avidani · [yuv.ai](https://yuv.ai).

License: MIT (this skill). Companion skills retain their upstream licenses.
