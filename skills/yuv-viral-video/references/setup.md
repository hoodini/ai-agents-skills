# Setup — yuv-viral-video

This skill builds on top of the **video-use** skill (cuts, transcription, motion). Install that first via `~/Developer/video-use/install.md`. The pieces below are the additional dependencies this skill needs on top of video-use.

## Prerequisites

| Tool | Why | Install |
|------|-----|---------|
| `ffmpeg` ≥ 4.x | Everything | `brew install ffmpeg` (macOS) / Windows: `winget install ffmpeg` / Linux: `apt install ffmpeg` |
| Python ≥ 3.10 with PIL/numpy/requests | Card rendering, ASS generation | `uv pip install pillow numpy requests` |
| `python-bidi` | Hebrew RTL reordering for PIL | `uv pip install python-bidi` |
| `fontTools` | Make static Assistant weights from the variable font (only when refreshing fonts) | `uv pip install fonttools` |
| ElevenLabs API key | Scribe transcription + sound generation | https://elevenlabs.io/app/settings/api-keys → write to `~/Developer/video-use/.env` |
| Anton, Karantina, Assistant TTF | Fonts (English Anton; Hebrew Karantina display + Assistant body) | Bundled in `assets/fonts/` — copy them into `<edit>/fonts/` |

## Bundled fonts

The skill ships these because download URLs change and CDN paths break. Fonts follow `yuv-design-system` §2 (Phoenix Ink):

```
assets/fonts/Anton-Regular.ttf        — Anton (display, English)
assets/fonts/Karantina-Bold.ttf       — Karantina 700 (Hebrew display, karaoke, numbers; Latin included)
assets/fonts/Assistant-ExtraBold.ttf  — Assistant 800 (Hebrew card text)
assets/fonts/Assistant-Bold.ttf       — Assistant 700 (Hebrew labels)
assets/fonts/OFL-*.txt                — licences
```

The scripts read fonts from `<edit>/fonts/`, so copy them there once per machine:

```bash
mkdir -p <edit>/fonts && cp <skill>/assets/fonts/*.ttf <edit>/fonts/
```

For the ASS / libass karaoke path, point ffmpeg at the same folder: `subtitles=karaoke.ass:fontsdir=<edit>/fonts`.

If they get corrupted, re-fetch from the Google Fonts repo:

```bash
curl -sL https://raw.githubusercontent.com/google/fonts/main/ofl/karantina/Karantina-Bold.ttf -o assets/fonts/Karantina-Bold.ttf
curl -sL "https://raw.githubusercontent.com/google/fonts/main/ofl/assistant/Assistant%5Bwght%5D.ttf" -o /tmp/Assistant.ttf
python -c "
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
for w, n in [(700, 'Bold'), (800, 'ExtraBold')]:
    instancer.instantiateVariableFont(TTFont('/tmp/Assistant.ttf'), {'wght': w}, updateFontNames=True).save(f'assets/fonts/Assistant-{n}.ttf')
"
```

## ElevenLabs API key

Write to `~/Developer/video-use/.env`:

```
ELEVENLABS_API_KEY=sk_...
```

This skill reads from that file directly (via `make_sfx.py`) so the key only lives in one place across both skills.

Quick sanity check:
```bash
curl -s -o /dev/null -w '%{http_code}\n' \
  -H "xi-api-key: $(sed -n 's/^ELEVENLABS_API_KEY=//p' ~/Developer/video-use/.env)" \
  https://api.elevenlabs.io/v1/user
# 200 = good, 401 = bad token
```

## One-time pre-render: layout assets

The dark-mode background and speaker masks are static — generate them once per project:

```bash
python scripts/make_layout_assets.py  # writes layout_assets/bg_*.png, speaker_mask_*.png
```

Re-run only if you change SPEAKER_9X16 / SPEAKER_16X9 dims in `apple_glass.py`.

## Per-project workflow

```bash
cd <videos_dir>/edit/
# 1. Transcribe (uses video-use skill)
python ~/Developer/video-use/helpers/transcribe.py <source.mp4> --edit-dir .
python ~/Developer/video-use/helpers/pack_transcripts.py --edit-dir .

# 2. Author edl.json (cuts, layout per range, motion per beat) by hand from the packed transcripts

# 3. Generate SFX (one-time per project)
python <skill>/scripts/make_sfx.py    # generates sfx/*.mp3 via ElevenLabs

# 4. Pick archetype:
#    Screen-share + speaker PIP corner → build_screen_share.py
#    Full-frame selfie speaker         → build_selfie.py
python <skill>/scripts/build_<archetype>.py

# 5. Render cards + anims
python <skill>/scripts/make_cards_<archetype>.py
python <skill>/scripts/make_anims.py     # only if METRICS / AUTO beats present

# 6. Karaoke
python <skill>/scripts/make_karaoke.py

# 7. Composite
python <skill>/scripts/composite_<archetype>.py
```

Each composite increments `OUT_VERSION` so finals are saved as `final_9x16_V<N>.mp4`. Bump `OUT_VERSION` before re-rendering to keep backups.

## Dependencies summary

```
# requirements.txt
pillow>=10
numpy>=1.24
requests>=2.30
python-bidi>=0.6
fonttools>=4.50
librosa>=0.10        # only used by video-use, kept for completeness
matplotlib>=3.7      # ditto
```
