#!/bin/sh
# Install skills from this repo into a Grok Bot skill library.
#
#   sh scripts/install-grok-bot.sh --skill meta-ads [--skill other] [--dest <dir>]
#   sh scripts/install-grok-bot.sh --all [--dest <dir>]
#
# Copies skills/<slug>/ to <dir>/<slug>/, replacing any existing copy, so a rerun updates in place.
# <dir> defaults to $HOME/agent-data/workflows, the library every Grok Bot on the account reads.
# Run it on the bot's own computer (ask the bot to run it, or use its terminal). Afterwards the
# skills show under Settings > Plugins > Yours and in the "/" menu of a conversation.
# Python skills also need their requirements (installed below when a requirements.txt exists).
# Exit 0 on success, 1 when nothing was installed, 2 on a usage error.
set -eu

usage() {
  echo "usage: sh scripts/install-grok-bot.sh (--skill <slug>)... | --all [--dest <dir>]" >&2
  exit 2
}

dest="${HOME:-}/agent-data/workflows"
skills=""
all=0
while [ $# -gt 0 ]; do
  case "$1" in
    --skill) [ $# -ge 2 ] || usage; skills="$skills $2"; shift 2 ;;
    --all) all=1; shift ;;
    --dest) [ $# -ge 2 ] || usage; dest="$2"; shift 2 ;;
    *) usage ;;
  esac
done
[ -n "$dest" ] || usage
[ "$all" -eq 1 ] || [ -n "$skills" ] || usage

root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
if [ "$all" -eq 1 ]; then
  skills=$(for f in skills/*/SKILL.md; do s=${f%/SKILL.md}; echo "${s##*/}"; done)
fi

mkdir -p "$dest"
count=0
for slug in $skills; do
  if [ ! -f "skills/$slug/SKILL.md" ]; then
    echo "skip $slug: no skills/$slug/SKILL.md" >&2
    continue
  fi
  rm -rf "${dest:?}/$slug"
  cp -R "skills/$slug" "$dest/$slug"
  find "$dest/$slug" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
  if [ -f "skills/$slug/requirements.txt" ] && command -v python3 >/dev/null 2>&1; then
    python3 -m pip install --user --quiet -r "skills/$slug/requirements.txt" 2>/dev/null \
      || python3 -m pip install --user --quiet --break-system-packages -r "skills/$slug/requirements.txt" \
      || echo "warning: could not install Python requirements for $slug" >&2
  fi
  echo "installed $slug"
  count=$((count + 1))
done
if [ "$count" -eq 0 ]; then
  echo "install-grok-bot.sh: nothing installed" >&2
  exit 1
fi
echo "$count skill(s) installed to $dest"
