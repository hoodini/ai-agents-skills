#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
# YUV.AI Skills · One-shot installer for any machine
# Sets up the FULL creative stack:
#   Orchestrator — yuv-pilot (top-of-pyramid router)
#   Design       — yuv-design-system
#   Decks        — yuv-decks
#   Videos       — yuv-viral-video, video-edit, video-to-landing-page,
#                  parallax-landing-page, video-use
#   Video engine — hyperframes, hyperframes-cli, hyperframes-registry,
#                  gsap, website-to-hyperframes
#   AI images    — nano-banana-pro
#   Diagrams     — mermaid-diagrams
# Plus: Python venvs, hyperframes CLI, faster-whisper, system deps
#       (ffmpeg/node/uv), and the shared ElevenLabs API key.
#
# Usage on a fresh machine:
#   curl -sSL https://raw.githubusercontent.com/hoodini/ai-agents-skills/master/install.sh | bash
#
# Or, safer (review the script before running):
#   git clone https://github.com/hoodini/ai-agents-skills /tmp/yuv-skills
#   cd /tmp/yuv-skills && bash install.sh
#
# Idempotent — safe to re-run. Skips what's already installed.
# ─────────────────────────────────────────────────────────────

set -euo pipefail

# ─── colors ──────────────────────────────────────────────────
PINK='\033[38;5;205m'
YELLOW='\033[38;5;226m'
GREEN='\033[32m'
RED='\033[31m'
CYAN='\033[36m'
DIM='\033[2m'
RST='\033[0m'

step()  { printf "\n${PINK}●${RST} ${YELLOW}%s${RST}\n" "$*"; }
ok()    { printf "  ${GREEN}✓${RST} %s\n" "$*"; }
warn()  { printf "  ${YELLOW}⚠${RST} %s\n" "$*"; }
err()   { printf "  ${RED}✗${RST} %s\n" "$*"; }
info()  { printf "  ${DIM}%s${RST}\n" "$*"; }

# ─── intro ───────────────────────────────────────────────────
printf "${PINK}"
cat <<'EOF'
   ╭──────────────────────────────────────────╮
   │   YUV.AI SKILLS · BOOTSTRAP INSTALLER    │
   │   8 skills · Hyperframes · video-use     │
   │   Anton + Rubik · GSAP · ElevenLabs      │
   ╰──────────────────────────────────────────╯
EOF
printf "${RST}\n"

# ─── detect platform ─────────────────────────────────────────
OS="$(uname -s)"
case "$OS" in
  Darwin) PLATFORM="mac" ;;
  Linux)  PLATFORM="linux" ;;
  *)      err "Unsupported OS: $OS — this script supports macOS and Linux."; exit 1 ;;
esac
ok "Platform detected: $PLATFORM"

# ─── system prereqs ──────────────────────────────────────────
step "Checking system prerequisites"

need_cmd() {
  local cmd="$1"
  local install_hint="$2"
  if command -v "$cmd" >/dev/null 2>&1; then
    ok "$cmd present"
    return 0
  else
    warn "$cmd missing — $install_hint"
    return 1
  fi
}

MISSING_REQ=0

# brew on macOS
if [ "$PLATFORM" = "mac" ]; then
  if ! command -v brew >/dev/null 2>&1; then
    err "Homebrew not installed. Install from https://brew.sh and re-run this script."
    exit 1
  fi
  ok "Homebrew present"
fi

# ffmpeg
if ! command -v ffmpeg >/dev/null 2>&1; then
  if [ "$PLATFORM" = "mac" ]; then
    info "Installing ffmpeg via Homebrew…"
    brew install ffmpeg >/dev/null 2>&1 && ok "ffmpeg installed" || { err "ffmpeg install failed"; MISSING_REQ=1; }
  else
    warn "ffmpeg missing — apt install ffmpeg / yum install ffmpeg / etc."; MISSING_REQ=1
  fi
else
  ok "ffmpeg present ($(ffmpeg -version | head -1 | awk '{print $3}'))"
fi

# node
if ! command -v node >/dev/null 2>&1; then
  if [ "$PLATFORM" = "mac" ]; then
    info "Installing Node via Homebrew…"
    brew install node >/dev/null 2>&1 && ok "Node installed" || { err "Node install failed"; MISSING_REQ=1; }
  else
    warn "Node missing — install from https://nodejs.org"; MISSING_REQ=1
  fi
else
  NODE_VER=$(node --version | sed 's/v//' | awk -F. '{print $1}')
  if [ "$NODE_VER" -lt 22 ]; then
    warn "Node $NODE_VER is too old (need ≥ 22). Hyperframes will not run. Upgrade Node and re-run."
    MISSING_REQ=1
  else
    ok "Node v$(node --version | sed 's/v//') present"
  fi
fi

# python3
if ! command -v python3 >/dev/null 2>&1; then
  if [ "$PLATFORM" = "mac" ]; then
    info "Installing python3 via Homebrew…"
    brew install python >/dev/null 2>&1 && ok "python3 installed" || { err "python3 install failed"; MISSING_REQ=1; }
  else
    warn "python3 missing — apt install python3 python3-venv"; MISSING_REQ=1
  fi
else
  ok "python3 present ($(python3 --version | awk '{print $2}'))"
fi

# uv
if ! command -v uv >/dev/null 2>&1; then
  info "Installing uv (Astral package manager)…"
  curl -LsSf https://astral.sh/uv/install.sh | sh >/dev/null 2>&1 && export PATH="$HOME/.local/bin:$PATH"
  if command -v uv >/dev/null 2>&1; then
    ok "uv installed"
  else
    warn "uv install failed — Python venv setup may use pip fallback"
  fi
else
  ok "uv present"
fi

# git / gh / curl (assumed present, but check)
need_cmd git "install via Homebrew or your package manager" || MISSING_REQ=1
need_cmd curl "install via Homebrew or your package manager" || MISSING_REQ=1

if [ "$MISSING_REQ" -eq 1 ]; then
  err "Some prerequisites are missing. Install them and re-run this script."
  exit 1
fi

# ─── ensure dirs ─────────────────────────────────────────────
step "Setting up directories"
mkdir -p "$HOME/.claude/skills"
mkdir -p "$HOME/Developer"
ok "$HOME/.claude/skills"
ok "$HOME/Developer"

# ─── 1. Core creative stack from ai-agents-skills ─────────────
#       (yuv-* skills + video-* skills + nano-banana-pro + parallax-landing-page + mermaid-diagrams)
step "Installing the full YUV creative stack from ai-agents-skills"

CLONE_TMP="$(mktemp -d)/ai-agents-skills"
# Note: yuv-design-system + parallax-landing-page have bundled binary assets — needs full blob fetch (no --filter=blob:none)
git clone --depth 1 --sparse \
  https://github.com/hoodini/ai-agents-skills "$CLONE_TMP" >/dev/null 2>&1
( cd "$CLONE_TMP" && git sparse-checkout set \
    skills/yuv-pilot \
    skills/director \
    skills/yuv-decks \
    skills/yuv-viral-video \
    skills/yuv-design-system \
    skills/video-edit \
    skills/video-to-landing-page \
    skills/parallax-landing-page \
    skills/nano-banana-pro \
    skills/mermaid-diagrams >/dev/null 2>&1 )

for skill in yuv-pilot director yuv-decks yuv-viral-video yuv-design-system video-edit video-to-landing-page parallax-landing-page nano-banana-pro mermaid-diagrams; do
  if [ -d "$HOME/.claude/skills/$skill" ]; then
    info "$skill already exists — refreshing"
    rm -rf "$HOME/.claude/skills/$skill"
  fi
  cp -R "$CLONE_TMP/skills/$skill" "$HOME/.claude/skills/"
  ok "$skill installed at ~/.claude/skills/$skill"
done

rm -rf "$(dirname "$CLONE_TMP")"

# ─── 1a. Cross-tool symlinks: ~/.copilot/skills + ~/.agents/skills ────
#         (GitHub Copilot CLI + Cursor / Aider / Codex CLI discover skills here)
step "Creating cross-tool symlinks for the YUV.AI pyramid"

PYRAMID_SKILLS=(
  yuv-pilot
  director
  yuv-design-system
  yuv-decks
  yuv-viral-video
  video-edit
  parallax-landing-page
  video-to-landing-page
)

for dir in "$HOME/.copilot/skills" "$HOME/.agents/skills"; do
  mkdir -p "$dir"
done

for skill in "${PYRAMID_SKILLS[@]}"; do
  src="$HOME/.claude/skills/$skill"
  [ -d "$src" ] || { warn "$skill not at $src — skipping symlinks"; continue; }
  for link_root in "$HOME/.copilot/skills" "$HOME/.agents/skills"; do
    link="$link_root/$skill"
    if [ -L "$link" ]; then
      ln -sfn "$src" "$link"
    elif [ -e "$link" ]; then
      warn "$link exists and isn't a symlink — leaving alone"
      continue
    else
      ln -s "$src" "$link"
    fi
  done
done
ok "Symlinked $((${#PYRAMID_SKILLS[@]})) pyramid skills into ~/.copilot/skills + ~/.agents/skills"

# ─── 1b. faster-whisper for the video-edit pipeline ──────────
step "Installing faster-whisper (video-edit transcription)"
WHISPER_OK=0
if command -v uv >/dev/null 2>&1; then
  uv pip install --system --quiet faster-whisper >/dev/null 2>&1 && WHISPER_OK=1
fi
if [ "$WHISPER_OK" -eq 0 ]; then
  python3 -m pip install --quiet --user faster-whisper >/dev/null 2>&1 && WHISPER_OK=1
fi
if [ "$WHISPER_OK" -eq 1 ]; then
  ok "faster-whisper installed (CPU int8 ready; large-v3 model auto-downloads on first run)"
else
  warn "faster-whisper install failed — run \`pip install faster-whisper\` manually"
fi

# Python venv for yuv-viral-video
step "Setting up yuv-viral-video Python venv"
cd "$HOME/.claude/skills/yuv-viral-video"
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  ok "venv created"
fi
.venv/bin/pip install --quiet --upgrade pip
.venv/bin/pip install --quiet -r requirements.txt
ok "yuv-viral-video deps installed (pillow, numpy, requests, python-bidi, fontTools, brotli)"
cd - >/dev/null

# ─── 2. video-use (browser-use) ──────────────────────────────
step "Installing video-use (transcription + cuts pipeline)"
VIDEO_USE_DIR="$HOME/Developer/video-use"

if [ -d "$VIDEO_USE_DIR/.git" ]; then
  info "video-use already cloned — pulling latest"
  ( cd "$VIDEO_USE_DIR" && git pull --ff-only >/dev/null 2>&1 ) || true
else
  git clone https://github.com/browser-use/video-use "$VIDEO_USE_DIR" >/dev/null 2>&1
  ok "video-use cloned to $VIDEO_USE_DIR"
fi

# Python deps via uv
if command -v uv >/dev/null 2>&1; then
  ( cd "$VIDEO_USE_DIR" && uv sync >/dev/null 2>&1 )
  ok "video-use deps installed via uv"
else
  ( cd "$VIDEO_USE_DIR" && python3 -m venv .venv && .venv/bin/pip install --quiet -e . )
  ok "video-use deps installed via pip"
fi

# Symlink into ~/.claude/skills/
if [ -L "$HOME/.claude/skills/video-use" ] || [ -e "$HOME/.claude/skills/video-use" ]; then
  rm -rf "$HOME/.claude/skills/video-use"
fi
ln -sfn "$VIDEO_USE_DIR" "$HOME/.claude/skills/video-use"
ok "video-use symlinked to ~/.claude/skills/video-use"

# ─── 3. Hyperframes (heygen-com) — 5 skills ──────────────────
step "Installing Hyperframes + 4 companion skills"

HF_CLONE_TMP="$(mktemp -d)/hyperframes"
git clone --depth 1 --filter=blob:none --sparse \
  https://github.com/heygen-com/hyperframes "$HF_CLONE_TMP" >/dev/null 2>&1
( cd "$HF_CLONE_TMP" && git sparse-checkout set skills >/dev/null 2>&1 )

for skill in hyperframes hyperframes-cli hyperframes-registry gsap website-to-hyperframes; do
  if [ -d "$HOME/.claude/skills/$skill" ]; then
    info "$skill already exists — refreshing"
    rm -rf "$HOME/.claude/skills/$skill"
  fi
  if [ -d "$HF_CLONE_TMP/skills/$skill" ]; then
    cp -R "$HF_CLONE_TMP/skills/$skill" "$HOME/.claude/skills/"
    ok "$skill installed"
  else
    warn "$skill not found in upstream repo — skipping"
  fi
done

rm -rf "$(dirname "$HF_CLONE_TMP")"

# Hyperframes CLI globally
if ! command -v hyperframes >/dev/null 2>&1; then
  step "Installing hyperframes CLI globally"
  npm install -g hyperframes >/dev/null 2>&1 && ok "hyperframes CLI v$(hyperframes --version) installed"
else
  ok "hyperframes CLI present (v$(hyperframes --version))"
fi

# ─── 4. ElevenLabs API key ──────────────────────────────────
step "ElevenLabs API key (shared between video-use and yuv-viral-video)"
ENV_FILE="$VIDEO_USE_DIR/.env"

if [ -f "$ENV_FILE" ] && grep -q "^ELEVENLABS_API_KEY=..*" "$ENV_FILE" 2>/dev/null; then
  ok "API key already configured at $ENV_FILE"
else
  if [ -t 0 ]; then
    info "Get a key at https://elevenlabs.io/app/settings/api-keys"
    printf "  ${YELLOW}Paste your ElevenLabs API key${RST} (or press Enter to skip): "
    read -s ELEVEN_KEY
    echo
    if [ -n "$ELEVEN_KEY" ]; then
      printf 'ELEVENLABS_API_KEY=%s\n' "$ELEVEN_KEY" > "$ENV_FILE"
      chmod 600 "$ENV_FILE"
      ok "key saved to $ENV_FILE"
      # Verify
      if HTTP=$(curl -s -o /dev/null -w '%{http_code}' \
          -H "xi-api-key: $ELEVEN_KEY" \
          https://api.elevenlabs.io/v1/user 2>/dev/null) && [ "$HTTP" = "200" ]; then
        ok "ElevenLabs key verified (200 OK)"
      else
        warn "Key didn't verify (HTTP $HTTP) — double-check the value"
      fi
    else
      warn "Skipped — set later at $ENV_FILE"
    fi
  else
    warn "Non-interactive shell — skipping key prompt. Set later:"
    info "echo 'ELEVENLABS_API_KEY=sk_...' > $ENV_FILE && chmod 600 $ENV_FILE"
  fi
fi

# ─── 5. Final verification ───────────────────────────────────
step "Verifying installation"

INSTALLED_SKILLS=$(ls "$HOME/.claude/skills" | tr '\n' ' ')
ok "Installed skills: $INSTALLED_SKILLS"

ALL_GOOD=1
for skill in yuv-pilot yuv-decks yuv-viral-video yuv-design-system video-edit video-to-landing-page parallax-landing-page nano-banana-pro mermaid-diagrams video-use hyperframes hyperframes-cli hyperframes-registry gsap website-to-hyperframes; do
  if [ -e "$HOME/.claude/skills/$skill" ]; then
    ok "$skill"
  else
    err "$skill missing"
    ALL_GOOD=0
  fi
done

# faster-whisper availability check
if python3 -c "import faster_whisper" >/dev/null 2>&1; then
  ok "faster-whisper Python package available"
else
  warn "faster-whisper not importable — video-edit transcribe will fail. Run: pip install faster-whisper"
fi

# Verify Python environments
if [ -f "$HOME/.claude/skills/yuv-viral-video/.venv/bin/python" ]; then
  ok "yuv-viral-video venv ready"
else
  err "yuv-viral-video venv missing"
  ALL_GOOD=0
fi

if [ -f "$VIDEO_USE_DIR/.venv/bin/python" ]; then
  ok "video-use venv ready"
else
  err "video-use venv missing"
  ALL_GOOD=0
fi

# ─── outro ───────────────────────────────────────────────────
echo
if [ "$ALL_GOOD" -eq 1 ]; then
  printf "${GREEN}"
  cat <<'EOF'
   ╭──────────────────────────────────────────╮
   │   ALL SKILLS INSTALLED · READY TO USE    │
   ╰──────────────────────────────────────────╯
EOF
  printf "${RST}\n"
  echo "  Next steps:"
  echo "    1. ${CYAN}Restart your Claude Code / Codex / Cursor session${RST}"
  echo "       The skills auto-discover at session start."
  echo
  echo "    2. ${CYAN}Test by asking:${RST}"
  echo "       ${DIM}\"edit this short video into a viral short: <path>\"${RST}"
  echo "       ${DIM}\"build me a landing page for [topic]\"${RST}"
  echo
  echo "    3. ${CYAN}Live effects catalog:${RST} https://effects.yuv.ai"
  echo
  echo "    4. ${CYAN}Update later:${RST} just re-run this script — it's idempotent."
else
  printf "${YELLOW}⚠ Some components didn't install cleanly. Check messages above.${RST}\n"
  exit 1
fi
