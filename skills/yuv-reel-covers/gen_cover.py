# YUV.AI cover generator v2 — Editorial Poster system (reverse-engineered SHELLY/cinema DNA).
# Templates: editorial (giant skewed type front/behind + tickers + stack) · cinema (duotone split-light)
#            behind / stack (v1 legacy).
# Examples:
#   py gen_cover.py editorial --bg sky --cutout assets/yuval-cutout.png --back "STEAL MY|PROMPTS" `
#      --ticker "ALL DAY,EVERY PLAY,NO LIMITS" --stack "FOCUS,ENERGY,DISCIPLINE,VICTORY" --tag AI --out ex1
#   py gen_cover.py cinema --bg-img assets/yuval.png --cutout assets/yuval-cutout.png --back "CLAUDE|CODE" --tag "FILM SCHOOL" --out ex3
import argparse, subprocess, os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

ACC = {"yellow": "#E9FF3D", "white": "#FFFFFF", "pink": "#FF1464", "cyan": "#00E5FF"}
BGS = {
    "sky":    "linear-gradient(180deg,#1557C9 0%,#2E8BE8 42%,#8FD2FF 100%)",
    "sunset": "linear-gradient(180deg,#2A1860 0%,#B43A8E 55%,#FF8A5C 100%)",
    "ink":    "radial-gradient(ellipse 90% 60% at 50% 38%,#181826,#0A0A0F 75%)",
}
p = argparse.ArgumentParser()
p.add_argument("template", choices=["editorial", "cinema", "behind", "stack"])
p.add_argument("--bg", choices=list(BGS), default="sky")
p.add_argument("--bg-img", default="", help="photo background (cover-fit); overrides --bg")
p.add_argument("--cutout", default="", help="background-removed subject PNG")
p.add_argument("--img", default="assets/yuval-cutout.png")  # legacy templates
p.add_argument("--back", required=True, help="headline; '|' splits line1|line2")
p.add_argument("--c1", choices=list(ACC), default="yellow")
p.add_argument("--c2", choices=list(ACC), default="yellow")
p.add_argument("--front", default="")
p.add_argument("--cfront", choices=list(ACC), default="white")
p.add_argument("--sub", default="")
p.add_argument("--accent-back", type=int, default=-1)
p.add_argument("--accent-front", type=int, default=-2)
p.add_argument("--color", choices=["pink", "cyan", "amber"], default="pink")  # legacy
p.add_argument("--ticker", default="BUILD,SHIP,FLY HIGH", help="comma list -> joined with stars")
p.add_argument("--stack", default="", help="comma list, bottom-right power words")
p.add_argument("--tag", default="YUV.AI")
p.add_argument("--y1", type=int, default=470); p.add_argument("--y2", type=int, default=1010)
p.add_argument("--front-top", type=int, default=1285)
p.add_argument("--cut-h", type=int, default=1260, help="cutout height px")
p.add_argument("--size-back", type=int, default=0); p.add_argument("--size-front", type=int, default=150)
p.add_argument("--out", required=True)
a = p.parse_args()

HEB = re.compile(r"[֐-׿]")
def disp_font(t): return ("Rubik", 900, -6) if HEB.search(t) else ("Anton", 400, -8)
STAR = '<svg viewBox="0 0 24 24" style="width:.62em;height:.62em;margin:0 14px;vertical-align:middle"><path d="M12 0 L14.5 9.5 L24 12 L14.5 14.5 L12 24 L9.5 14.5 L0 12 L9.5 9.5 Z" fill="currentColor"/></svg>'
def ticker_html(items, reps=3):
    seg = STAR.join(f"<span>{w.strip()}</span>" for w in items.split(","))
    return STAR.join([seg] * reps)

lines = a.back.split("|")
L1, L2 = lines[0], (lines[1] if len(lines) > 1 else "")
f1, w1, sk1 = disp_font(L1); f2, w2, sk2 = disp_font(L2 or L1)

ICONS = '''<svg viewBox="0 0 24 24"><path d="M12 1 L14 10 L23 12 L14 14 L12 23 L10 14 L1 12 L10 10 Z" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>
<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="1.4"/><ellipse cx="12" cy="12" rx="4.5" ry="10" fill="none" stroke="currentColor" stroke-width="1.2"/><line x1="2" y1="12" x2="22" y2="12" stroke="currentColor" stroke-width="1.2"/></svg>
<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="1.4"/><circle cx="12" cy="12" r="5.5" fill="none" stroke="currentColor" stroke-width="1.2"/><circle cx="12" cy="12" r="1.6" fill="currentColor"/></svg>'''

if a.template in ("editorial", "cinema"):
    cine = a.template == "cinema"
    accent = ACC["white"] if cine else ACC[a.c1]
    bg_css = f"background:{BGS[a.bg]};" if not a.bg_img else ""
    bg_img_html = f'<img class="bgimg" src="{a.bg_img}"/>' if a.bg_img else ""
    duo = '''<div class="duoA"></div><div class="duoB"></div><div class="duoD"></div>''' if cine else ""
    cut_html = f'<img id="cut" class="cut" src="{a.cutout}"/>' if a.cutout else ""
    stack_html = ""
    if a.stack:
        words = "".join(f"<div>{w.strip()}</div>" for w in a.stack.split(","))
        stack_html = f'<div class="stack">{words}<div class="icons">{ICONS}</div></div>'
    front_html = f'<div id="lf" class="lf">{a.front}</div>' if a.front else ""
    mid_t = "" if cine else f'<div class="tick mid">{ticker_html(a.ticker)}</div>'
    top_t = f'<div class="tick top">{ticker_html(a.ticker)}</div>'
    ff, fw, fsk = disp_font(a.front or "A")
    body = f'''
      {bg_img_html}{duo}
      {mid_t}
      <div id="l1" class="hl" style="top:{a.y1}px;color:{ACC[a.c1] if not cine else '#FFFFFF'};font-family:'{f1}';font-weight:{w1};transform:skewX({sk1}deg)">{L1}</div>
      {f'<div id="l2" class="hl" style="top:{a.y2}px;color:{ACC[a.c2] if not cine else "#FFFFFF"};font-family:{f2!r};font-weight:{w2};transform:skewX({sk2}deg)">{L2}</div>' if L2 else ''}
      {cut_html}
      {front_html}
      {top_t}
      {stack_html}'''
    css = f'''
      #root{{{bg_css}}}
      .bgimg{{position:absolute;inset:0;width:1080px;height:1920px;object-fit:cover;z-index:0;{'filter:saturate(.8) contrast(1.1) brightness(.5) blur(24px);transform:scale(1.18);' if cine else ''}}}
      .duoA{{position:absolute;inset:0;z-index:1;background:radial-gradient(ellipse 70% 60% at 8% 20%,rgba(255,20,100,.55),transparent 60%);mix-blend-mode:screen;}}
      .duoB{{position:absolute;inset:0;z-index:1;background:radial-gradient(ellipse 70% 60% at 95% 45%,rgba(0,229,255,.5),transparent 60%);mix-blend-mode:screen;}}
      .duoD{{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(0,0,0,.25),transparent 30%,transparent 60%,rgba(0,0,0,.55));}}
      .hl{{position:absolute;left:38px;right:38px;z-index:2;text-align:center;text-transform:uppercase;line-height:.92;
        font-size:300px;letter-spacing:-0.01em;white-space:nowrap;text-shadow:0 10px 50px rgba(0,0,0,.35);}}
      .cut{{position:absolute;left:50%;transform:translateX(-50%);bottom:0;height:{a.cut_h}px;z-index:3;
        filter:drop-shadow(0 0 30px rgba(0,0,0,.55)) drop-shadow(0 26px 60px rgba(0,0,0,.7));}}
      .lf{{position:absolute;left:30px;right:30px;top:{a.front_top}px;z-index:4;text-align:center;text-transform:uppercase;
        font-family:'{ff}';font-weight:{fw};transform:skewX({fsk}deg);font-size:{a.size_front}px;color:{ACC[a.cfront]};
        white-space:nowrap;text-shadow:0 8px 40px rgba(0,0,0,.8);}}
      .tick{{position:absolute;left:0;right:0;z-index:5;text-align:center;font-family:"Inter",Arial,sans-serif;font-weight:800;
        font-size:27px;letter-spacing:4px;white-space:nowrap;overflow:hidden;color:{'rgba(255,255,255,.92)' if not cine else 'rgba(255,255,255,.85)'};}}
      .tick.top{{top:283px;}}
      .tick.mid{{top:{a.y2-58}px;z-index:2;color:rgba(255,255,255,.95);}}
      .stack{{position:absolute;right:64px;bottom:330px;z-index:5;text-align:right;font-family:'Anton';
        font-size:38px;letter-spacing:1px;line-height:1.28;color:{accent};text-transform:uppercase;}}
      .stack .icons{{display:flex;gap:14px;justify-content:flex-end;margin-top:16px;}}
      .stack .icons svg{{width:40px;height:40px;color:{accent};}}'''
    fit_js = '''
      // auto-fit headline + front to width (re-run after fonts load — Hebrew Rubik loads async)
      const fit = () => { for (const id of ["l1","l2","lf"]) {
        const el = document.getElementById(id); if (!el) continue;
        el.style.fontSize = "300px";
        let s = 300;
        while (el.scrollWidth > 1004 && s > 60) { s -= 6; el.style.fontSize = s + "px"; }
      } };
      fit(); document.fonts.ready.then(fit);'''
else:
    # ---- v1 legacy templates (behind / stack) ----
    G = {"pink": "255,20,100", "cyan": "0,229,255", "amber": "249,173,69"}[a.color]
    C = {"pink": "#FF1464", "cyan": "#00E5FF", "amber": "#F9AD45"}[a.color]
    def accent_words(text, idx):
        ws = text.split()
        if idx == -2: return f'<span class="acc">{text}</span>'
        return " ".join(f'<span class="acc">{w}</span>' if i == idx else w for i, w in enumerate(ws))
    def autosize(t):
        m = max(len(w) for w in t.split());  return 290 if m <= 4 else 245 if m <= 6 else 195 if m <= 8 else 160
    sb = a.size_back or autosize(a.back.replace("|", " "))
    if a.template == "behind":
        body = f'''<div class="back-text">{accent_words(a.back, a.accent_back)}</div>
      <img class="cut0" src="{a.img}"/>
      <div class="front-text">{accent_words(a.front, a.accent_front)}</div>'''
        css = f'''.back-text{{position:absolute;left:40px;right:40px;top:430px;z-index:2;direction:rtl;text-align:center;font-family:"Rubik";font-weight:900;font-size:{sb}px;line-height:1.04;color:#fff;}}
      .cut0{{position:absolute;left:50%;transform:translateX(-50%);bottom:0;height:1250px;z-index:3;filter:drop-shadow(0 0 34px rgba({G},.42));}}
      .front-text{{position:absolute;left:30px;right:30px;top:{a.front_top}px;z-index:4;direction:rtl;text-align:center;font-family:"Rubik";font-weight:900;font-size:{a.size_front}px;color:#fff;text-shadow:0 8px 40px rgba(0,0,0,.9),0 0 50px rgba({G},.35);}}
      .acc{{color:{C};text-shadow:0 0 34px rgba({G},.55);}}
      #root{{background:{BGS['ink']};}}'''
    else:
        body = f'''<div class="stk"><div class="big">{accent_words(a.back, a.accent_back)}</div>{f'<div class="sb">{a.sub}</div>' if a.sub else ''}</div>'''
        css = f'''.stk{{position:absolute;inset:0;z-index:3;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:34px;text-align:center;}}
      .big{{font-family:"Anton","Rubik";text-transform:uppercase;font-size:{sb}px;line-height:.98;color:#fff;direction:rtl;}}
      .sb{{font-family:"Rubik";font-weight:900;font-size:96px;color:{C};text-shadow:0 0 30px rgba({G},.5);direction:rtl;}}
      .acc{{color:{C};text-shadow:0 0 34px rgba({G},.55);}}
      #root{{background:{BGS['ink']};}}'''
    fit_js = ""

html = f'''<!doctype html><html><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
@font-face{{font-family:"Anton";src:url("fonts/Anton-Regular.woff2") format("woff2");}}
@font-face{{font-family:"Rubik";font-weight:900;src:url("fonts/Rubik-900.woff2") format("woff2");}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#0A0A0A;}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;}}
.chip{{position:absolute;top:372px;left:64px;z-index:6;font-family:"JetBrains Mono",monospace;font-size:29px;letter-spacing:4px;
  color:#fff;border:2px solid rgba(255,255,255,.9);padding:10px 22px;border-radius:999px;background:rgba(8,8,12,.35);}}
.phx{{position:absolute;top:358px;right:64px;width:92px;z-index:6;filter:drop-shadow(0 2px 14px rgba(0,0,0,.6));}}
.handle{{position:absolute;left:0;right:0;top:1560px;z-index:6;text-align:center;font-family:"JetBrains Mono",monospace;
  font-size:26px;letter-spacing:3px;color:rgba(255,255,255,.85);text-shadow:0 2px 10px rgba(0,0,0,.8);}}
.vig{{position:absolute;inset:0;z-index:5;pointer-events:none;background:radial-gradient(ellipse 95% 80% at 50% 45%,transparent 55%,rgba(0,0,0,.38) 100%);}}
.grain{{position:absolute;inset:0;z-index:7;opacity:.05;pointer-events:none;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/></filter><rect width='160' height='160' filter='url(%23n)'/></svg>");}}
{css}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="0.2" data-width="1080" data-height="1920">
  {body}
  <div class="vig"></div>
  <div class="chip">{a.tag}</div>
  <img class="phx" src="assets/logo-phoenix.png"/>
  <div class="handle">@yuval_770 · YUV.AI</div>
  <div class="grain"></div>
</div>
<script>
{fit_js}
window.__timelines=window.__timelines||{{}};window.__timelines["main"]=gsap.timeline({{paused:true}});
</script></body></html>'''

open("index.html", "w", encoding="utf-8").write(html)
print(f"index.html written ({a.template})")
os.makedirs("out", exist_ok=True)
subprocess.run(["npx", "--yes", "hyperframes@latest", "render", "--fps", "30", "--output", "out/_tmp.mp4"],
               shell=True, check=True, capture_output=True)
subprocess.run(["ffmpeg", "-y", "-i", "out/_tmp.mp4", "-frames:v", "1", f"out/{a.out}.png"],
               shell=True, check=True, capture_output=True)
os.remove("out/_tmp.mp4")
print(f"COVER -> out/{a.out}.png")



