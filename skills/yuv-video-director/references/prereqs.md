# Prerequisites & environment (check first; degrade gracefully)

| Need | Check | Notes |
|---|---|---|
| Node 22+ | `node --version` | HyperFrames CLI (`npx hyperframes`) |
| FFmpeg | `ffmpeg -version` | encode/probe |
| Python 3.11+ **with pip** | `py -m pip --version` | Manim + captions |
| ManimCE | `py -m manim --version` | `py -m pip install manim` if missing |
| Headless Chrome | `npx hyperframes doctor` | downloaded on first render/validate |

## Windows gotchas (this machine)
- **`python` on PATH is Hermes' venv → NO pip.** Use the **`py` launcher** (defaults to real
  `C:\Python313`). Always `py -m pip ...`, `py -m manim ...`.
- The PowerShell shell **resets to `C:\` each call** — `Set-Location <project>` inside every command.
- The sandbox **blocks `Remove-Item` on `C:\`-relative paths** — use absolute paths or just don't remove.
- Anton (and most display fonts) are **not auto-resolved** by the HyperFrames renderer — download the
  **latin** woff2 and declare `@font-face`. Inter + JetBrains Mono auto-resolve.

## Graceful degradation
- **No Manim / no pip** → skip math beats (route to GSAP/Three.js) or offer to install; don't fail the whole video.
- **No LaTeX** → fine; author Manim with `Text()`/`MarkupText`, never `Tex`/`MathTex`.
- **Offline** → fonts/Lottie/Manim assets must be local (no Google Fonts `<link>`, no remote Lottie `path`).
