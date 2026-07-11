<p align="center">
  <img src="https://img.shields.io/badge/AI-Agent%20Skills-blueviolet?style=for-the-badge&logo=robot&logoColor=white" alt="AI Agent Skills"/>
  <img src="https://img.shields.io/badge/GitHub-Star-yellow?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Star"/>
  <img src="https://img.shields.io/badge/AWS-GenAI%20Superstar-orange?style=for-the-badge&logo=amazonaws&logoColor=white" alt="AWS GenAI Superstar"/>
</p>

<p align="center">
  <img src="hero-skills.jpg" alt="AI Agent Skills Hero"/>
</p>

<h1 align="center">🧠 Agent Skills Repository</h1>

<p align="center">
  <strong>Created by <a href="https://yuv.ai">Yuval Avidani</a></strong> · <em>AI Builder, Speaker, 2× GitHub Star, AWS GenAI Superstar, AI commentator on Channel 12 News (Israel)</em><br/>
  <a href="https://yuv.ai">yuv.ai</a> · <a href="https://linktr.ee/yuvai">all links</a> · <a href="https://x.com/yuvalav">@yuvalav</a> · <a href="https://instagram.com/yuval_770">@yuval_770</a> · <a href="https://youtube.com/@yuv-ai">YouTube</a> · <a href="https://github.com/hoodini">GitHub</a>
</p>

---

## ⚡ Install the full creative stack in one command

```bash
curl -sSL https://raw.githubusercontent.com/hoodini/ai-agents-skills/master/install.sh | bash
```

Installs **16 skills** as one package: **director** (award-winning film + AI-production Bible, story-first workflow) · **yuv-pilot** (top-of-pyramid orchestrator) · **yuv-design-system** (brand) · **yuv-decks** (cinematic presentations) · **yuv-viral-video** (short-form) · **video-edit** · **video-to-landing-page** · **parallax-landing-page** · **hyperframes** + 4 companions · **nano-banana-pro** (AI images) · **mermaid-diagrams**. Plus ffmpeg / Node / Python / faster-whisper / hyperframes CLI / Python venvs / cross-tool symlinks to ~/.copilot/skills + ~/.agents/skills. Works on macOS, Linux, Windows (Git Bash/WSL).

After install, restart your agent and just type what you want:

```
"make a deck about <topic> for <audience>"
"build a stunning parallax landing page from this video: <path>"
"edit this video into a viral short: <path>"
```

The right skill auto-fires. Projects save to **`~/Documents/yuv-projects/{decks,landings,videos}/<slug>/`** so they're always findable.

> 🌐 **Live examples:** [yuv.ai](https://yuv.ai) · [effects.yuv.ai](https://effects.yuv.ai) (HyperFrames effects catalog) · [examples/parasites/](examples/parasites/) (three parallax landings: GitHub Desktop, Marcus the lion, Hope the cheetah)

---

## 🪜 The YUV.AI skills pyramid

The YUV.AI creative stack is a **three-tier pyramid**. You don't have to remember which skill does what — say what you want, the orchestrator routes.

```
                  ┌─────────────────────┐
                  │     yuv-pilot       │   ← top: intent → route
                  │  (orchestrator)     │
                  └──────────┬──────────┘
                             │
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
   ┌─────────┐        ┌─────────────┐      ┌──────────────┐
   │yuv-decks│        │ yuv-design- │      │  yuv-viral-  │
   │         │        │   system    │      │    video     │
   │ talks · │        │             │      │              │
   │ slides ·│        │ palette ·   │      │ short MP4s · │
   │ keynotes│        │ typography ·│      │ Reels · TikTok│
   │         │        │ 3 modes ·   │      │ MrBeast-paced │
   │         │        │ assets      │      │ editorial    │
   └─────────┘        └─────────────┘      └──────────────┘
   ┌─────────────┐    ┌─────────────────┐  ┌──────────────────┐
   │ video-edit  │    │ parallax-       │  │ video-to-        │
   │             │    │ landing-page    │  │ landing-page     │
   │ captioned · │    │                 │  │                  │
   │ Hebrew+EN · │    │ scroll-scrub ·  │  │ Apple-style ·    │
   │ transcript- │    │ video frames ·  │  │ sticky hero ·    │
   │ review flow │    │ github/lion/hope│  │ frames + sections│
   └─────────────┘    └─────────────────┘  └──────────────────┘
                             │
                             ▼ (the middle tier uses these)
   open-slide · hyperframes · gsap · nano-banana-pro · video-use ·
   slide-authoring · mermaid-diagrams · hyperframes-cli · website-to-hyperframes

                  Brand DNA — universal Fly High throughline:
                  flight metaphors · HUD + dials · phoenix mark ·
                  "Let's Fly High" watermark · Anton + JetBrains Mono
                  (palette is the chapter, motifs are the brand)
```

### How to invoke

| Say | What fires |
|---|---|
| `"build me a deck about <topic> for <audience>"` | `yuv-decks` (lead) + `yuv-design-system` in **Decks mode** + `open-slide` scaffolding |
| `"build a landing page for me / my brand"` | `yuv-design-system` in **Neon mode** + `gsap` for motion |
| `"turn this video into a landing page"` *(5–15s clip)* | `parallax-landing-page` — scroll-scrub cinematic landing |
| `"turn this video into a landing page"` *(longer, with sections)* | `video-to-landing-page` — Apple-style sticky-hero |
| `"edit this video / add captions"` | `video-edit` — transcript-review-before-render workflow |
| `"make it viral / YUV.AI short"` | `yuv-viral-video` — opinionated MrBeast-paced pipeline |
| `"launch my new course / cross-channel campaign"` | `yuv-pilot` — orchestrates a build order across multiple skills |
| `"what should I build for my brand"` *(strategic, no specific deliverable)* | `yuv-pilot` — surfaces options |
| `"build me a snake game"` *(no YUV.AI signal)* | **Whole pyramid stays out** — picks whatever palette fits |
| `"build me a YUV.AI snake game"` *(explicit brand signal)* | `yuv-design-system` in **Neon mode** + Three.js or Canvas |

### Three palette modes (only when applied)

| Mode | When | Palette |
|---|---|---|
| **Neon** *(default for YUV.AI web/app/game/dashboard/social)* | Anything that's not a slide deck | Hot pink `#FF1464` + neon cyan `#00E5FF` + white or rich black |
| **Decks** *(Fly High)* | Presentations, slides, keynotes only | Purple `#5E17EB` + yellow `#FFEC00` + grey `#F1F2F2` |
| **Warm Editorial** | Hope, Marcus, bigcats.ai, practical.yuv.ai | Pink + yellow + bone |

The pyramid auto-applies **only** when YUV.AI brand context is signaled (`my brand`, `for me`, `YUV.AI`, etc.). Generic requests stay outside the system — Claude / Copilot / Cursor pick whatever fits the project.

---

## 🆕 NEW: cinematic-scrub-landing — golden landing page template

Drop in a hero video + logo + product photo. Get back a **premium cinematic landing page** with mouse-driven video scrubbing and a 5-beat narrative arc.

<p align="center">
  <img src="skills/cinematic-scrub-landing/assets/01-hero-mouse-scrub.png" alt="Mouse-scrub hero" width="640"/>
</p>

The hero video lives fixed across the whole page — moving the mouse left-right scrubs the timeline so the subject responds to the cursor. Below it, **four fully-opaque sections each carry their own brand identity** (bright primary-accent recipe / cream nostalgia album / dark contemplative pricing / red action finale) and walk the viewer through *longing → joy → nostalgia → contemplation → action*. Works for **any language** (RTL or LTR) and **any subject** — food, tech, animals, fashion, services, SaaS, wildlife, music, books, real estate.

<p align="center">
  <img src="skills/cinematic-scrub-landing/assets/02-yellow-recipe.png" alt="Bright primary section" width="220"/>
  <img src="skills/cinematic-scrub-landing/assets/03-cream-album.png" alt="Cream album section" width="220"/>
  <img src="skills/cinematic-scrub-landing/assets/04-dark-pricing.png" alt="Dark pricing section" width="220"/>
  <img src="skills/cinematic-scrub-landing/assets/05-red-cta.png" alt="Red CTA finale" width="220"/>
</p>

**What's baked in (every rule hard-won from a real production build):**

- **All-keyframes ffmpeg re-encode** (`-g 1 -keyint_min 1`) so mouse-scrub is buttery, not stuttery
- **The z-index trap** documented as hard rule #1 (outer wrapper has NO bg class, or the video disappears)
- **Per-section opaque identities** — no monotone scrim through every section
- **Language-aware typography trinity** (Hebrew Rubik+Assistant+Suez One / English Anton+Inter+Caveat / Arabic Cairo+Tajawal+Reem Kufi / Japanese Noto Sans JP / etc.)
- **RTL/LTR mirroring** — hero panel side, cursor cue side, scroll-to-top position, arrow direction
- **Six reusable visual primitives** — polaroid, stamp, ribbon, highlight-circle, ghost-text, motif SVGs
- **Real product photography wins over generated gradients** — the skill always finds prominent placement for `PRODUCT_IMAGE`
- **Clickable scroll-spy navbar** + scroll-to-top button + favicon set from the logo
- **12-step verification gate** before reporting done

Reference implementation: <https://github.com/hoodini/bamba> (Israeli RTL site for the snack "במבה" — the original build this skill was distilled from).

🔗 **[View cinematic-scrub-landing →](skills/cinematic-scrub-landing/SKILL.md)**

Pairs with `parallax-landing-page` (scroll-scrub frames, page never moves) and `video-to-landing-page` (Apple-style sticky hero with sections below) — pick `cinematic-scrub-landing` when the hero should respond to the **cursor** and the page below should **tell a story**.

---

## 🆕 NEW: yuv-design-system — single source of truth for visuals

Yuval Avidani's canonical design system, now public. **Replaces** the prior `yuv-design` skill (which only covered the Warm Editorial pink/yellow/bone family). Encodes:

- **Two palette modes** — **Fly High** (purple `#5E17EB` + yellow `#FFEC00` + grey, the default for keynotes / dashboards / dev-facing UIs) and **Warm Editorial** (pink + yellow + bone, only for the Hope / bigcats / practical.yuv.ai brand family)
- **Mandatory typography** — Anton + Inter for English, Rubik + Assistant for Hebrew, letter-spacing 0 by default
- **Signature components** — `PurpleBar`, `YellowUnderline`, `FlightHUD`, `CompassDial`, `CounterUp`, `HeroBg`
- **Brand assets bundled** — 4 phoenix logos + studio portrait, with a 4-step asset-retrieval fallback chain for any machine
- **Canonical link set + bio** — auto-included on any footer / about / credits block
- **Lessons-learned reference** — 15 hardened production patterns (bilingual toggle, mobile hamburger threshold, Anton letter-spacing rules, yellow-span `line-height ≥ 1.0`, IntersectionObserver for GSAP catalogs, GH Pages cert nudge, …)
- **Pre-flight checklist** — 14 mandatory checks before any visual ships

🔗 **[View yuv-design-system →](skills/yuv-design-system/SKILL.md)**

Pairs with `yuv-decks` (cinematic presentation builder), `yuv-viral-video` (short-form video), and `hyperframes` (capture web → MP4). Project brand wins when explicitly specified; otherwise this skill fills the vacuum.

---

## 🆕 NEW: yuv-decks — opinionated cinematic deck builder

Builds open-slide presentation decks in Yuval Avidani's signature style: 4-act narrative arc (Boarding → Ascent → Cruise → Descent), Yuval voice (plain-language, no jargon, ≤8–12 word bullets, define every name), the flight-themed `JourneyBar` unifying every slide, reusable `UseCase` / `CaseStudy` / `LessonsGrid` templates, and an automatic orchestration of nano-banana cinematic hero images + Hyperframes video moments + Mermaid technical diagrams.

Inherits all palette/typography/components from `yuv-design-system` and locks the **Decks mode** (Fly High purple/yellow/grey — the dedicated palette for slides). For talks whose central metaphor IS literal flight, opt into the `cinematic-flight` mode (sky-blue + hot pink) — same arc and JourneyBar, different palette. Never falls through to Neon (web/app palette).

🔗 **[View yuv-decks →](skills/yuv-decks/SKILL.md)**

Reference implementation: <https://github.com/hoodini/build-agents-that-ship> (the NICE pre-hackathon "Build Agents That Ship" deck, May 2026).

---

## 🆕 NEW: Parallax Landing Page Skill

Turn any short video (5–15s) into a **cinematic scroll-driven landing page** where the
user's scroll gesture *scrubs the frames in place* — the page itself never scrolls. A single
locked viewport with five dramatic text scenes that crossfade in/out as the frame index
advances, an Anton + Caveat typography contract, off-white #f5f1ea (never pure white), a
vignette + film-grain overlay, a loader that preloads every frame, and a final scene that
holds the CTAs (no separate end section). Built on the proven `parasites/` reference repo
(GitHub Desktop / Marcus the white lion / Hope the cheetah landings).

🔗 **[View the Parallax Landing Page Skill →](skills/parallax-landing-page/SKILL.md)**

**What's inside:**
- `scripts/extract_frames.py` — ffprobe + ffmpeg `-q:v 2` extraction with auto-computed `scrollBudget` (≈26 px per frame, clamped to `[2500, 8000]`)
- `assets/parallax.js` — virtual-scroll controller: wheel/touch/keyboard intercepted, document never moves, RAF-driven lerp (0.22) for buttery frame scrubbing
- `assets/style.css` — locked-body landing page CSS (`body.scrub-page`), 5-scene grid, vignette + grain, Anton/Caveat/Inter font stack
- `assets/landing-page-template.html` — full template with `{{placeholders}}` for slug, scenes, CTAs
- `assets/hub-template.html` — 3-up showcase grid template for multi-landing projects
- `references/copy-guide.md` — the five-beat arc (Hook → Origin → Stakes → Moment → Resolution) with three real cinematic examples
- `references/showcase-integration.md` — exact edits to grow an existing hub (card + nav + chain CTA)

**One-shot:** point the script at a video, capture the JSON, fill in the template, serve with `python -m http.server`.

```bash
python skills/parallax-landing-page/scripts/extract_frames.py demo.mp4 ./out/demo
```

🎬 **See it live:** the three landing pages built with this skill ship in
[`examples/parasites/`](examples/parasites/) — GitHub Desktop, Marcus the white lion,
and Hope the cheetah. After cloning:

```bash
cd examples/parasites && python -m http.server 8000
# open http://localhost:8000/
```

> Note: distinct from `video-to-landing-page` (which uses an evenly-spaced
> scroll-listener approach). This skill is the "Apple AirPods Pro" variant — every frame,
> locked body, dramatic typography, narrative beats.

---

## 🆕 NEW: Video-Edit Skill (with Interactive Transcript Editor)

A complete captioned-video pipeline that **pauses for human transcript approval** before the
long final render — the support mechanism that makes captions perfect (especially Hebrew).
Transcribes any video with `faster-whisper` (defaults to `large-v3`), applies a configurable
corrections dictionary, opens an **interactive browser editor** with video preview, per-line
inline editing, dictionary apply, find/replace and **optional in-browser LLM suggestions via
WebLLM** (Qwen2.5-3B / Llama-3.2-3B over WebGPU — runs entirely offline once cached). On
approval, redistributes word timings and generates a HyperFrames composition with
liquid-glass caption pills, drifting blob background, liquid morph wipes, and optional
behind-subject text via background removal. Supports English, Hebrew and any
Whisper-supported language.

🔗 **[View the Video-Edit Skill →](skills/video-edit/SKILL.md)**

**What's inside:**
- `transcribe.py` — faster-whisper CPU/CUDA with safe fallback
- `make_review.py` + `apply_review.py` — emit & ingest a `transcript_review.txt` round-trip
- `transcript-editor/index.html` — self-contained webapp (RTL-aware, autosaves to localStorage)
- `gen_body.py` — generator for editorial + matrix liquid-glass caption sub-composition
- `host-template.html` + `liquid-blobs.html` + EN/HE parallax-outro templates
- `corrections-hebrew.md` — curated dictionary of common Hebrew Whisper mishears

---

## 🆕 NEW: Video-to-Landing-Page Skill

Drop a video, get a cinematic **scroll-driven landing page** — Apple-style sticky hero where
scrolling progresses the visible frame through the video. Extracts evenly-spaced frames via
ffmpeg, builds a self-contained `index.html` with a `requestAnimationFrame`-driven scroll
listener, and includes headline / sections / CTA below. Respects the `yuv-design-system` typography
(Anton + Inter for English, Rubik + Assistant for Hebrew) and Fly High purple palette by default.

🔗 **[View the Video-to-Landing-Page Skill →](skills/video-to-landing-page/SKILL.md)**

**One command from video to deployable page:**

```bash
python skills/video-to-landing-page/references/extract-frames.py demo.mp4 ./landing-demo --build-html
```

Then customise `__HEADLINE__`, `__TAGLINE__`, `__CTA_TEXT__` in the generated `index.html`
and drop the folder on Vercel / Netlify / Cloudflare Pages.

---

## 🚀 NEW: Yuv-Viral-Video Skill

**Just added!** The complete signature-style video editor that turns raw selfie or screen-share footage into a viral short-form video the way YUV.AI ships them — Apple-style liquid-glass cards with real backdrop blur, dark-mode polish, MrBeast-paced cuts, video-title karaoke captions, content-relevant motion graphics, no fake content, **never covering the speaker's face**, always rendering BOTH 9:16 and 16:9, always saving with `_V<N>` backup suffix. Hebrew is rendered in Rubik Black (with proper RTL via `python-bidi`), English in Anton uppercase. Encodes every painful lesson from real edits as a hard rule the next render automatically respects.

🔗 **[View the Yuv-Viral-Video Skill →](skills/yuv-viral-video/SKILL.md)**

**What it does:**
- Apple-style frosted glass cards: rounded corners + `gblur sigma=24` backdrop + `alphamerge` masks so the blur stops cleanly at the rounded shape (no rectangular leak past the corners)
- Auto-routes the layout per archetype: screen-share footage shows the screen content (top 2/3) with rounded speaker PIP at bottom 1/3; full-frame selfie shows the speaker prominently with cards in the safe top-banner zone (face never covered)
- Per-segment dynamic motion (push-in / pull-out / snap-in / dolly / shake) baked into the extract chain with subtle MrBeast-style amounts
- Real animated diagrams: bar chart (uses actual category names from transcript, never fake numbers), flow diagram with glowing brand-color nodes connected by animated dashed arrows
- Word-by-word video-title karaoke: scale-pop entrance with `\fscx150\fscy150\t(0,140,\fscx100\fscy100)`, accent words get yellow + rotation jitter, English brand tokens auto-route to Anton uppercase
- Bottom key-moment glass strips that summarise the current beat in 1-4 words (Hebrew right + English left + yellow accent stripe)
- ElevenLabs SFX kit (impact, bass_drop, whoosh, riser, ding, glitch, typing) mixed at the right output times via `adelay`
- Two-pass loudnorm to -14 LUFS / -1 dBTP / LRA 11 (TikTok / Reels / YouTube standard)
- **Versioning**: every render writes a NEW `final_*_V<N>.mp4` — previous versions are never overwritten
- **Truth contract**: every word on every card is auditable against the actual transcript. No "$$$" placeholders, no "100% הבנה" if the speaker didn't say it, no "לינק בביו" if no link was promised

---

## 🆕 NEW: Meta Ads Skill

**Just added!** A battle-tested skill for pulling, analyzing, and managing Meta ad performance (Facebook, Instagram, Messenger, Click-to-WhatsApp, Threads) via the Marketing API. No guesswork, no generic dashboards — the scripts auto-discover your accounts, decode status codes and currency units, handle rate limits and async insights jobs, and guard write actions behind explicit confirmations.

🔗 **[View the Meta Ads Skill →](skills/meta-ads/SKILL.md)**

**What it does:**
- Pulls ad-level, ad-set-level, campaign-level, and account-level insights with full breakdowns (platform, placement, age, gender, country, device)
- Auto-discovers every ad account your token can see, ranked by last-30-day spend — so you never paste the wrong `act_` ID
- Handles both auth paths out of the box: System User tokens (never expire, BM-owned accounts) and long-lived user tokens (60-day, sees personal Instagram-boost accounts)
- Ships a token-exchange script for the short→60-day swap — no more fumbling through Graph Explorer docs
- Creative fatigue detection, anomaly detection vs. prior period, CTWA-aware analysis playbooks
- Write actions (pause, budget update, duplicate) gated behind explicit confirmation with impact summaries and rollback patterns
- Baked-in troubleshooting for every failure mode we hit the hard way: sandbox proxy blocks, 37-month data wall, DELETED-status error 1815001, minor-unit currency bugs, IG boosts invisible to SU tokens, and more

---

## 🆕 NEW: Google Workspace CLI Skill

**Just added!** A comprehensive skill that teaches AI agents to use the `gws` CLI — one command-line tool for **all** of Google Workspace: Drive, Gmail, Calendar, Sheets, Docs, Slides, Chat, Tasks, Admin, Meet, Forms, Keep, and more. Your agent can now manage your entire Google Workspace without custom tooling.

🔗 **[View the Google Workspace CLI Skill →](skills/google-workspace-cli/SKILL.md)**

**What it does:**
- Enables AI agents to interact with every Google Workspace API via `gws` CLI commands
- Covers Drive, Gmail, Calendar, Sheets, Docs, Slides, Chat, Tasks, Meet, Forms, Admin, Keep, Apps Script, and more
- Includes 100+ ready-to-use command examples with real JSON payloads
- MCP server integration for Claude Desktop, VS Code, Gemini CLI, and other MCP clients
- Multiple auth workflows: interactive, headless/CI, service accounts, and multi-account support
- Built on Google's Discovery Service — automatically picks up new API endpoints

---

## 🧠 Honest Agent Skill

A universal skill that configures ALL your AI coding agents to be honest, objective, and non-sycophantic. Run it once, and every agent (Claude Code, GitHub Copilot, Cursor, Windsurf, etc.) will stop telling you what you want to hear and start giving you honest, direct feedback.

🔗 **[View the Honest Agent Skill →](skills/honest-agent/SKILL.md)**

**What it does:**
- Configures honest, objective communication across 7 verified AI coding agents
- One-time setup that updates all your agent instruction files
- Supports both project-level and global configuration
- Works with Claude Code, Copilot, Cursor, Windsurf, Cline, Aider, and Continue.dev

---

<p align="center">
  <strong>A curated collection of AI agent skills for enhanced coding assistance</strong>
</p>

<p align="center">
  <em>Supercharge your AI coding agents with specialized knowledge and production-ready patterns</em>
</p>

<p align="center">
  <a href="#-available-skills">Skills</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

## 👋 About Yuval Avidani

<table>
<tr>
<td width="180" valign="top">
<a href="https://yuv.ai"><img src="https://github.com/hoodini.png?size=180" width="180" alt="Yuval Avidani"/></a>
</td>
<td valign="top">

### **Yuval Avidani** — *AI Builder & Speaker · Founder of YUV.AI*

**🏆 2× GitHub Star** · **🌟 AWS Gen AI Superstar** · **📺 AI commentator on Channel 12 News (Israel)** · **🎤 Enterprise AI Trainer**

> Founder of **YUV.AI** — leading Hebrew-speaking AI educator and technical innovator. Builds, teaches, and ships AI that actually works. Open-source maintainer of 110+ projects spanning AI agents, video pipelines, design systems, and developer tools.

**Hebrew bio:** *יובל אבידני — מגיש פינת AI בחדשות 12, GitHub Star כפול, AWS Gen AI Superstar, מייסד YUV.AI. בונה, מלמד, ומשגר AI שעובד.*

</td>
</tr>
</table>

### 🔗 Find me everywhere

<p>
  <a href="https://yuv.ai"><img src="https://img.shields.io/badge/yuv.ai-website-5E17EB?style=for-the-badge&logo=safari&logoColor=FFEC00" /></a>
  <a href="https://linktr.ee/yuvai"><img src="https://img.shields.io/badge/Linktree-all_links-39E09B?style=for-the-badge&logo=linktree&logoColor=white" /></a>
  <a href="https://x.com/yuvalav"><img src="https://img.shields.io/badge/X-@yuvalav-000000?style=for-the-badge&logo=x&logoColor=white" /></a>
  <a href="https://instagram.com/yuval_770"><img src="https://img.shields.io/badge/Instagram-@yuval__770-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
  <a href="https://www.tiktok.com/@yuval.ai"><img src="https://img.shields.io/badge/TikTok-@yuval.ai-000000?style=for-the-badge&logo=tiktok&logoColor=white" /></a>
  <a href="https://youtube.com/@yuv-ai"><img src="https://img.shields.io/badge/YouTube-@yuv--ai-FF0000?style=for-the-badge&logo=youtube&logoColor=white" /></a>
  <a href="https://github.com/hoodini"><img src="https://img.shields.io/badge/GitHub-@hoodini-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/yuval-avidani-87081474/"><img src="https://img.shields.io/badge/LinkedIn-Yuval_Avidani-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://facebook.com/yuval.avidani"><img src="https://img.shields.io/badge/Facebook-Yuval_Avidani-1877F2?style=for-the-badge&logo=facebook&logoColor=white" /></a>
</p>

### 💼 Work with me

- **🎓 Practical Claude Desktop course** → <https://practical.yuv.ai>
- **🚀 Enterprise AI training & speaking** → DM on [LinkedIn](https://www.linkedin.com/in/yuval-avidani-87081474/) or [@yuvalav](https://x.com/yuvalav)
- **🤝 Built something with this stack?** Tag [@yuvalav](https://x.com/yuvalav) on X or DM [@yuval_770](https://instagram.com/yuval_770) on Instagram — I'll feature the best work
- **⭐ Star this repo** if it saves you time — helps other builders find it

---

## ✨ What Are Agent Skills?

Agent skills are **specialized knowledge modules** that enhance AI coding agents with domain-specific expertise. They provide:

- 🎯 **Focused Knowledge** — Only what the AI doesn't already know
- 📝 **Production-Ready Code** — Working examples, not abstract concepts  
- ⚡ **Quick Activation** — Trigger keywords for instant context
- 🔄 **Reusable Patterns** — Copy once, use everywhere

---

## �️ Understanding Agent Skills (Open Standard)

### What is SKILL.md?

**SKILL.md** is a simple, open format for giving AI agents new capabilities and expertise. It's an open standard that works across multiple AI coding agents and platforms.

> **Agent Skills** are folders of instructions, scripts, and resources that your AI agent can discover and use to perform tasks more accurately and efficiently.

### Why Use Agent Skills?

**For You (Developer)**:
- 📚 **Learn Faster** — Pre-built knowledge from experts in your domain
- 🎯 **Better Results** — Agents have context to work more accurately
- ♻️ **Reuse Everywhere** — Same skill works across Copilot, Claude Code, Cursor, Windsurf, and more
- 🔐 **Version Control** — Skills are part of your repository, tracked in git

**For Your Team**:
- 📖 **Capture Knowledge** — Document processes and best practices
- 🚀 **Share Skills** — Distribute expertise across projects
- 🏢 **Enterprise Use** — Centralize organizational knowledge

**For AI Agents**:
- 🧠 **Domain Expertise** — Perform specialized tasks reliably
- 🔧 **New Capabilities** — Enable new workflows and automations
- 🎓 **Context** — Access procedures, scripts, and examples on demand

### What Can You Do With Agent Skills?

Agent skills enable AI agents to:
- **Domain Expertise**: Package specialized knowledge (legal review, data analysis, deployment procedures)
- **New Capabilities**: Create presentations, build MCP servers, analyze datasets, debug failures
- **Repeatable Workflows**: Turn multi-step tasks into consistent, auditable processes
- **Interoperability**: Reuse skills across different compatible agent products

---

## 📚 How Agent Skills Work (Step-by-Step for Beginners)

### Step 1: Understanding the File Structure

Each skill is a simple folder with a `SKILL.md` file inside:

```
your-project/
├── .github/skills/          # GitHub Copilot project skills location
│   └── my-skill-name/
│       ├── SKILL.md         # Main skill file (required)
│       ├── script.js        # Optional: supporting scripts
│       └── examples.md      # Optional: more examples
├── .claude/skills/          # Claude Code project skills location
│   └── my-skill-name/
│       └── SKILL.md
└── ~/.copilot/skills/       # Personal skills (available across all projects)
    └── my-skill-name/
        └── SKILL.md
```

### Step 2: Understanding SKILL.md Format

Every `SKILL.md` file has two parts:

**YAML Frontmatter** (metadata):
```yaml
---
name: my-skill-name           # Unique identifier (lowercase, hyphens for spaces)
description: What this skill  # When should the agent use this skill?
license: MIT                  # Optional: license information
---
```

**Markdown Body** (instructions):
The rest of the file contains instructions and examples for the AI agent.

### Step 3: A Real Example

Here's what a simple `SKILL.md` looks like:

```markdown
---
name: github-actions-debugging
description: Guide for debugging failing GitHub Actions workflows. Use this when asked to debug CI/CD failures or workflow issues.
---

# Debugging GitHub Actions Workflows

When debugging a failing workflow:

1. **Check the job logs** - Look for error messages and stack traces
2. **Review recent changes** - What changed since the last successful run?
3. **Test locally** - Reproduce the issue in your local environment
4. **Fix and validate** - Make changes and verify they work

## Common Issues and Solutions

### Issue: Workflow fails with "Command not found"
**Solution**: Install the required tool in your workflow step

### Issue: Permission denied when running scripts
**Solution**: Add `chmod +x script.sh` before running the script
```

### Step 4: Agent Discovers and Uses Your Skill

When you ask your AI agent to do something:

```
"Debug why our GitHub Actions workflow is failing"
```

The agent will:
1. ✅ **Recognize** that you're asking about GitHub Actions
2. ✅ **Find** the `github-actions-debugging` skill in your project
3. ✅ **Load** the `SKILL.md` file into its context
4. ✅ **Follow** the instructions to help you debug

### Step 5: Supported Locations

**Project Skills** (specific to one repository):
- `your-repo/.github/skills/` — For GitHub Copilot
- `your-repo/.claude/skills/` — For Claude Code

**Personal Skills** (available across all projects on your machine):
- `~/.copilot/skills/` — For GitHub Copilot (Copilot CLI and VS Code)
- `~/.claude/skills/` — For Claude Code

**Organization/Enterprise Skills** (coming soon):
- Enterprise-level skills support is in development

---

## 🤝 Supported AI Agents

Agent Skills work with these AI coding agents:

| Agent | Support | Location |
|:------|:--------|:---------|
| **GitHub Copilot** | ✅ Full Support | `.github/skills/` or `~/.copilot/skills/` |
| **Claude Code** | ✅ Full Support | `.claude/skills/` or `~/.claude/skills/` |
| **Cursor** | ✅ Full Support | `.cursor/rules/` |
| **Windsurf** | ✅ Full Support | `.windsurf/rules/` |
| **VS Code Insiders** | ✅ Full Support | Agent mode with skills |
| **VS Code (Stable)** | ⏳ Coming Soon | Support coming in future release |

---

## 📦 Available Skills

| Skill | Description | Keywords |
|:------|:------------|:---------|
| **[aws-harness](skills/aws-harness/SKILL.md)** 🆕 | Build a new agent AND deploy it easily on AWS, or wrap + ship an agent you already have, via the Bedrock AgentCore harness - CLI (create/dev/deploy/invoke) plus SDK-wrap and FastAPI/Docker/ECR paths, every import verified | `agent harness`, `AWS harness`, `AgentCore`, `agentcore create`, `agentcore deploy`, `deploy agent on AWS`, `bring your own agent` |
| **[director](skills/director/SKILL.md)** 🆕 | Award-winning director's brain — a 28-chapter film + AI-production Bible (~108k words) wrapped in a gated, interrogation-first workflow that locks the IDEA and SCRIPT before generating a single pixel, then plans shots/camera/light/sound, then generates. Honest neuroscience (no dopamine-as-pleasure myths), current AI image/video model selection, character-consistency SOP, first/last-frame keyframing | `director`, `video`, `film`, `teaser`, `trailer`, `storyboard`, `script`, `screenwriting`, `documentary`, `סרטון`, `טיזר`, `תסריט`, `סטוריבורד` |
| **[yuv-design-system](skills/yuv-design-system/SKILL.md)** 🆕 | Yuv's canonical visual brand — Fly High purple (default) + Warm Editorial pink, Anton/Inter + Rubik/Assistant, signature components, brand assets, canonical bio/links, 15 hardened production patterns | `design system`, `brand`, `Fly High`, `Warm Editorial`, `Anton`, `Rubik`, `PurpleBar`, `YellowUnderline`, `FlightHUD`, `yuv.ai` |
| **[yuv-decks](skills/yuv-decks/SKILL.md)** 🆕 | Open-slide cinematic deck builder — 4-act narrative arc, Yuval voice, JourneyBar, reusable templates, automatic nano-banana + Hyperframes orchestration | `deck`, `presentation`, `slides`, `talk`, `keynote`, `open-slide`, `cinematic deck`, `מצגת`, `שקפים` |
| **[yuv-viral-video](skills/yuv-viral-video/SKILL.md)** | Short-form video editor — liquid-glass cards, dark-mode, MrBeast-paced cuts, karaoke captions, ALWAYS 9:16 + 16:9, never covers the speaker's face | `viral video`, `reel`, `short`, `selfie edit`, `liquid glass`, `karaoke captions`, `ויראלי`, `ריל` |
| **[parallax-landing-page](skills/parallax-landing-page/SKILL.md)** 🆕 | Cinematic scroll-scrub landing page from a short video — locked body, virtual scroll, 5 crossfading scenes, Anton + Caveat typography | `parallax landing`, `scroll-scrub`, `frame-by-frame`, `Anton`, `Caveat`, `locked hero`, `virtual scroll`, `video to landing page` |
| **[video-edit](skills/video-edit/SKILL.md)** 🆕 | Captioned-video pipeline with interactive transcript editor + WebLLM suggestions before render | `video edit`, `captions`, `transcribe`, `Hebrew`, `WebLLM`, `liquid-glass captions`, `HyperFrames` |
| **[video-to-landing-page](skills/video-to-landing-page/SKILL.md)** 🆕 | Apple-style scroll-driven landing page from any video — frames scrub on scroll | `landing page from video`, `scroll-frame`, `Apple scroll`, `scrub on scroll` |
| **[meta-ads](skills/meta-ads/SKILL.md)** 🆕 | Meta Marketing API — Facebook, Instagram, CTWA ad insights, fatigue analysis, write actions | `Meta ads`, `Facebook ads`, `Instagram ads`, `Marketing API`, `ROAS`, `CPA`, `CTR`, `CTWA`, `creative fatigue` |
| **[google-workspace-cli](skills/google-workspace-cli/SKILL.md)** 🆕 | Google Workspace CLI (`gws`) — Drive, Gmail, Calendar, Sheets, Docs, Chat & more | `gws`, `Google Workspace`, `Google Drive`, `Gmail`, `Google Calendar`, `Google Sheets`, `MCP` |
| **[copilot-sdk](skills/copilot-sdk/SKILL.md)** | GitHub Copilot SDK for building agentic applications | `Copilot SDK`, `GitHub SDK`, `agentic app`, `embed Copilot` |
| **[honest-agent](skills/honest-agent/SKILL.md)** 🆕 | Configure all AI agents for honest, objective feedback | `honest agent`, `no sycophancy`, `objective`, `contradict me` |
| **[aws-strands](skills/aws-strands/SKILL.md)** | The agent framework (the "brain") - write agent logic, tools & multi-agent systems; deploy via aws-harness | `Strands`, `agent framework`, `agents as tools`, `Swarm`, `Graph`, `BedrockModel` |
| **[aws-account-management](skills/aws-account-management/SKILL.md)** | AWS Organizations, IAM, billing & multi-account | `AWS Organizations`, `IAM`, `SCPs`, `Cost Explorer` |
| **[langchain](skills/langchain/SKILL.md)** | LangChain/LangGraph pipelines and agent workflows | `LangChain`, `LangGraph`, `RAG`, `LCEL` |
| **[vercel](skills/vercel/SKILL.md)** | Vercel deployment, serverless, and edge functions | `Vercel`, `serverless`, `edge function` |
| **[railway](skills/railway/SKILL.md)** | Railway platform deployment and configuration | `Railway`, `deploy container` |
| **[cloudflare](skills/cloudflare/SKILL.md)** | Cloudflare Workers, Pages, D1, R2, KV & AI | `Cloudflare`, `Workers`, `D1`, `R2`, `edge computing` |
| **[figma](skills/figma/SKILL.md)** | Figma API, component code generation & design tokens | `Figma API`, `design tokens`, `Figma to code` |
| **[fal-ai](skills/fal-ai/SKILL.md)** | Serverless AI image/video generation with fal.ai | `fal.ai`, `Flux`, `SDXL`, `AI image generation` |
| **[mongodb](skills/mongodb/SKILL.md)** | MongoDB & Mongoose queries, aggregation pipelines | `MongoDB`, `Mongoose`, `aggregation`, `NoSQL` |
| **[bun](skills/bun/SKILL.md)** | Bun JavaScript runtime, bundler & test runner | `Bun`, `bun.sh`, `JavaScript runtime` |
| **[owasp-security](skills/owasp-security/SKILL.md)** | OWASP Top 10 security vulnerabilities & prevention | `OWASP`, `security`, `XSS`, `SQL injection`, `CSRF` |
| **[shabbat-times](skills/shabbat-times/SKILL.md)** | Jewish calendar data and Shabbat times integration | `Shabbat times`, `Hebcal`, `Zmanim` |
| **[copilot-docs](skills/copilot-docs/SKILL.md)** | GitHub Copilot custom instructions reference | `copilot-instructions.md` |
| **[nano-banana-pro](skills/nano-banana-pro/SKILL.md)** | Google Gemini 3 Pro Image generation | `Nano Banana Pro`, `Gemini 3 Pro Image` |
| **[github-trending](skills/github-trending/SKILL.md)** | GitHub trending repositories scraping | `GitHub trending`, `trending repos` |
| **[ux-design-systems](skills/ux-design-systems/SKILL.md)** | Design systems and component libraries | `design system`, `design tokens`, `theming` |
| **[web-accessibility](skills/web-accessibility/SKILL.md)** | WCAG compliance and accessibility patterns | `accessibility`, `a11y`, `WCAG`, `ARIA` |
| **[mobile-responsiveness](skills/mobile-responsiveness/SKILL.md)** | Responsive design and mobile-first patterns | `responsive`, `mobile-first`, `breakpoints` |
| **[analytics-metrics](skills/analytics-metrics/SKILL.md)** | Data visualization and analytics dashboards | `analytics`, `dashboard`, `charts`, `KPI` |
| **[mermaid-diagrams](skills/mermaid-diagrams/SKILL.md)** | Mermaid diagram syntax for visualizations | `Mermaid`, `flowchart`, `sequence diagram` |
| **[local-llm-router](skills/local-llm-router/SKILL.md)** | Route queries to local LLMs in air-gapped networks with Serena MCP | `local LLM`, `Ollama`, `LM Studio`, `air-gapped`, `Serena`, `model routing` |
| **[x-twitter-scraper](skills/x-twitter-scraper/SKILL.md)** | X/Twitter data extraction — tweet search, user lookup, followers, media, monitoring | `Twitter`, `X`, `scraper`, `OSINT`, `tweets`, `followers` |

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yuval-avidani/ai-agents-skills.git
```

### 2. Copy Skills to Your Project

Choose your AI coding agent and follow the instructions below.

---

## 💻 Setup Guide: Using Skills in Your Agent (For Beginners)

This guide walks you through setting up Agent Skills in your favorite coding agent, step by step.

### 🎯 Prerequisites

Before you start, you need:
- A coding agent installed (Copilot, Claude Code, Cursor, or Windsurf)
- A project folder on your computer
- Basic familiarity with command line or your agent's UI

### 📍 Step-by-Step Setup

#### **Option 1: GitHub Copilot** (Most Popular)

<details>
<summary><strong>🟢 Setup GitHub Copilot with Skills</strong></summary>

**For Project Skills** (specific to one repository):

1. **In your project folder**, create the skills directory:
   ```bash
   mkdir -p .github/skills
   ```

2. **Copy the skills you want** from this repository:
   ```bash
   # Copy a single skill
   cp -r skills/vercel .github/skills/
   
   # Or copy all skills
   cp -r skills/* .github/skills/
   ```

3. **Or manually create a skill**:
   ```
   your-project/
   └── .github/
       └── skills/
           └── my-custom-skill/
               └── SKILL.md
   ```

4. **Open your project in VS Code** and start using Copilot Agent
5. **Ask Copilot a question** related to your skill, and it will automatically load it!

**For Personal Skills** (available across all your projects):

1. **Find your home directory** (`~` or `C:\Users\YourUsername`)

2. **Create personal skills folder**:
   ```bash
   mkdir -p ~/.copilot/skills
   ```

3. **Copy skills there**:
   ```bash
   cp -r skills/vercel ~/.copilot/skills/
   ```

4. **Now all your projects** can use these skills automatically!

**Verify it's working:**
- Open Copilot Agent
- Ask about something covered in your skill (e.g., "How do I deploy to Vercel?")
- Copilot will use the skill to help you

</details>

---

#### **Option 2: Claude Code**

<details>
<summary><strong>🟣 Setup Claude Code with Skills</strong></summary>

**For Project Skills**:

1. **In your project folder**, create the skills directory:
   ```bash
   mkdir -p .claude/skills
   ```

2. **Copy the skills you want**:
   ```bash
   # Single skill
   cp -r skills/langchain .claude/skills/
   
   # All skills
   cp -r skills/* .claude/skills/
   ```

3. **Open your project in Claude Code**
4. **Chat with Claude** about tasks covered in your skills - it will automatically use them!

**For Personal Skills** (available everywhere):

1. **Create personal skills folder**:
   ```bash
   mkdir -p ~/.claude/skills
   ```

2. **Copy skills there**:
   ```bash
   cp -r skills/aws-harness ~/.claude/skills/
   ```

**Verify it's working:**
- Open Claude Code in your project
- Ask about something in your skill
- Claude will reference and use the skill

</details>

---

#### **Option 3: Cursor**

<details>
<summary><strong>🔵 Setup Cursor with Skills</strong></summary>

**For Project Rules**:

1. **In your project folder**:
   ```bash
   mkdir -p .cursor/rules
   ```

2. **Copy SKILL.md files** (rename them as rules):
   ```bash
   # Copy a skill as a rule file
   cp skills/figma/SKILL.md .cursor/rules/figma.md
   
   # Or copy multiple
   cp skills/*/SKILL.md .cursor/rules/
   ```

3. **In Cursor Settings**, configure which rules to use:
   - Settings → Rules → Add project rules
   - Point to `.cursor/rules/` folder

4. **Start using Cursor** - it will apply these rules to your context automatically

</details>

---

#### **Option 4: Windsurf**

<details>
<summary><strong>🟡 Setup Windsurf with Skills</strong></summary>

**For Project Rules**:

1. **In your project folder**:
   ```bash
   mkdir -p .windsurf/rules
   ```

2. **Copy skills as rules**:
   ```bash
   # Copy specific skills
   cp skills/vercel/SKILL.md .windsurf/rules/vercel.md
   
   # Or copy all skills
   cp skills/*/SKILL.md .windsurf/rules/
   ```

3. **Windsurf automatically** discovers rules in `.windsurf/rules/`
4. **Start building** - Windsurf will use these rules contextually

</details>

---

### 🎓 What Happens After Setup?

Once you've set up your skills:

1. **Agent Detects Skills**: Your AI agent scans the skill directories
2. **Agent Reads SKILL.md**: It reads the name and description from frontmatter
3. **Agent Activates on Relevance**: When you ask a question matching the description, the agent loads the skill
4. **Agent Follows Instructions**: Your agent now has the context to help you accurately

### 💡 Example: Using a Vercel Skill

**You have this SKILL.md**:
```yaml
---
name: vercel-deployment
description: Deploying applications to Vercel. Use this when asked about deploying, hosting, or managing Vercel projects.
---
```

**You ask your agent**:
> "Help me deploy my React app to Vercel"

**Agent automatically**:
- ✅ Finds `vercel-deployment` skill
- ✅ Loads SKILL.md into context
- ✅ Follows the deployment instructions
- ✅ Helps you deploy successfully!

### 🐛 Troubleshooting

| Problem | Solution |
|:--------|:---------|
| Agent not using skill | Restart your agent, or make sure folder path is correct |
| Skill file not found | Verify `SKILL.md` is in the right folder and named exactly "SKILL.md" |
| Agent using wrong skill | Make sure skill descriptions are descriptive enough to match your request |

---

## 💻 Usage (Advanced)

---

## 📐 Skill Format

Each skill follows a consistent structure:

```markdown
---
name: skill-name
description: Brief description with trigger keywords
---

# Skill Title

Quick start and core patterns...
```

### 🎯 Key Principles

| Principle | Description |
|:----------|:------------|
| **Concise is key** | Only include what the AI doesn't already know |
| **Progressive disclosure** | Start with quick start, then advanced patterns |
| **Concrete examples** | Working code over abstract descriptions |
| **Trigger keywords** | Include words that activate the skill |

---

## 📁 Repository Structure

```
ai-agents-skills/
├── 📄 README.md
├── 📁 skills/
│   ├── 📁 meta-ads/              # 🆕 NEW!
│   │   ├── 📄 SKILL.md
│   │   ├── 📄 requirements.txt
│   │   ├── 📁 assets/
│   │   │   └── 📄 env.template
│   │   ├── 📁 references/
│   │   │   ├── 📄 setup.md
│   │   │   ├── 📄 insights-fields.md
│   │   │   ├── 📄 analysis-playbooks.md
│   │   │   ├── 📄 write-actions.md
│   │   │   └── 📄 troubleshooting.md
│   │   └── 📁 scripts/
│   │       ├── 📄 meta_client.py
│   │       ├── 📄 auth_check.py
│   │       ├── 📄 exchange_token.py
│   │       ├── 📄 list_accounts.py
│   │       ├── 📄 list_campaigns.py
│   │       ├── 📄 fetch_insights.py
│   │       ├── 📄 creative_fatigue.py
│   │       ├── 📄 anomaly_detect.py
│   │       ├── 📄 pause_ad.py
│   │       ├── 📄 update_budget.py
│   │       └── 📄 duplicate_ad.py
│   ├── 📁 google-workspace-cli/ # 🆕 NEW!
│   │   └── 📄 SKILL.md
│   ├── 📁 copilot-sdk/
│   │   └── 📄 SKILL.md
│   ├── 📁 honest-agent/
│   │   └── 📄 SKILL.md
│   ├── 📁 aws-harness/      # 🆕 NEW!
│   │   └── 📄 SKILL.md
│   ├── 📁 aws-strands/
│   │   └── 📄 SKILL.md
│   ├── 📁 aws-account-management/
│   │   └── 📄 SKILL.md
│   ├── 📁 langchain/
│   │   └── 📄 SKILL.md
│   ├── 📁 vercel/
│   │   └── 📄 SKILL.md
│   ├── 📁 railway/
│   │   └── 📄 SKILL.md
│   ├── 📁 cloudflare/
│   │   └── 📄 SKILL.md
│   ├── 📁 figma/
│   │   └── 📄 SKILL.md
│   ├── 📁 fal-ai/
│   │   └── 📄 SKILL.md
│   ├── 📁 mongodb/
│   │   └── 📄 SKILL.md
│   ├── 📁 bun/
│   │   └── 📄 SKILL.md
│   ├── 📁 owasp-security/
│   │   └── 📄 SKILL.md
│   ├── 📁 shabbat-times/
│   │   └── 📄 SKILL.md
│   ├── 📁 copilot-docs/
│   │   └── 📄 SKILL.md
│   ├── 📁 nano-banana-pro/
│   │   └── 📄 SKILL.md
│   ├── 📁 github-trending/
│   │   └── 📄 SKILL.md
│   ├── 📁 ux-design-systems/
│   │   └── 📄 SKILL.md
│   ├── 📁 web-accessibility/
│   │   └── 📄 SKILL.md
│   ├── 📁 mobile-responsiveness/
│   │   └── 📄 SKILL.md
│   ├── 📁 analytics-metrics/
│   │   └── 📄 SKILL.md
│   ├── 📁 mermaid-diagrams/
│   │   └── 📄 SKILL.md
│   ├── 📁 local-llm-router/
│   │   ├── 📄 SKILL.md
│   │   └── 📁 references/
│   │       └── 📄 model-matrix.md
│   └── 📁 x-twitter-scraper/
│       └── 📄 SKILL.md
└── 📁 templates/
    └── 📁 skill-template/
        └── 📄 SKILL.md
```

---

## 🤝 Contributing

We welcome contributions! Here's how to add a new skill:

1. **Fork** this repository
2. **Create** a new skill in `skills/your-skill-name/SKILL.md`
3. **Follow** the [skill template](templates/skill-template/SKILL.md)
4. **Submit** a pull request

### Contribution Guidelines

- ✅ Include practical, production-ready code examples
- ✅ Add trigger keywords in the description
- ✅ Test all code snippets before submitting
- ✅ Keep explanations concise but complete
- ❌ Don't include basic concepts the AI already knows
- ❌ Don't use placeholder code or TODOs

---

## 🌟 Star History

If you find this repository useful, please consider giving it a ⭐!

---

## 📄 License

MIT License — Feel free to use, modify, and distribute.

---

<p align="center">
  <a href="https://yuv.ai"><img src="https://img.shields.io/badge/yuv.ai-5E17EB?style=flat-square&logo=safari&logoColor=FFEC00" /></a>
  <a href="https://linktr.ee/yuvai"><img src="https://img.shields.io/badge/Linktree-39E09B?style=flat-square&logo=linktree&logoColor=white" /></a>
  <a href="https://x.com/yuvalav"><img src="https://img.shields.io/badge/X-@yuvalav-000000?style=flat-square&logo=x&logoColor=white" /></a>
  <a href="https://instagram.com/yuval_770"><img src="https://img.shields.io/badge/IG-@yuval__770-E4405F?style=flat-square&logo=instagram&logoColor=white" /></a>
  <a href="https://www.tiktok.com/@yuval.ai"><img src="https://img.shields.io/badge/TikTok-@yuval.ai-000000?style=flat-square&logo=tiktok&logoColor=white" /></a>
  <a href="https://youtube.com/@yuv-ai"><img src="https://img.shields.io/badge/YouTube-@yuv--ai-FF0000?style=flat-square&logo=youtube&logoColor=white" /></a>
  <a href="https://github.com/hoodini"><img src="https://img.shields.io/badge/GitHub-@hoodini-181717?style=flat-square&logo=github&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/yuval-avidani-87081474/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" /></a>
  <a href="https://facebook.com/yuval.avidani"><img src="https://img.shields.io/badge/Facebook-1877F2?style=flat-square&logo=facebook&logoColor=white" /></a>
</p>

<p align="center">
  <strong>Made with ❤️ by <a href="https://yuv.ai">Yuval Avidani</a> · YUV.AI</strong><br/>
  <em>Building AI agents that ship · Let's Fly High 🚀</em>
</p>

<p align="center">
  <a href="https://github.com/hoodini/ai-agents-skills">
    <img src="https://img.shields.io/github/stars/hoodini/ai-agents-skills?style=social" alt="Star this repo"/>
  </a>
  <a href="https://github.com/hoodini">
    <img src="https://img.shields.io/badge/Follow-@hoodini-181717?style=social&logo=github" alt="Follow on GitHub"/>
  </a>
</p>
