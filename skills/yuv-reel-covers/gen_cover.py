# YUV.AI Instagram Reel cover generator — Neon Phoenix brand, unified grid system.
# Usage:
#   py gen_cover.py behind --img assets/yuval-cutout.png --back "קלוד דסקטופ" --front "משנה הכל!" \
#       --accent-back 1 --color pink --tag "CLAUDE · AI" --out claude-desktop
#   py gen_cover.py stack --back "CLAUDE CODE" --sub "המדריך המלא" --color cyan --tag DEV --out claude-code
# Canvas 1080x1920; ALL key content inside the 3:4 grid-crop safe zone (y 285..1635).
import argparse, subprocess, os, sys
sys.stdout.reconfigure(encoding="utf-8")

COLORS = {"pink": "#FF1464", "cyan": "#00E5FF", "amber": "#F9AD45"}
GLOW = {"pink": "255,20,100", "cyan": "0,229,255", "amber": "249,173,69"}

p = argparse.ArgumentParser()
p.add_argument("template", choices=["behind", "stack"])
p.add_argument("--img", default="assets/yuval-cutout.png")
p.add_argument("--back", required=True, help="big text (behind subject / main stack)")
p.add_argument("--front", default="", help="text IN FRONT of the subject (behind template)")
p.add_argument("--sub", default="", help="subtitle (stack template)")
p.add_argument("--accent-back", type=int, default=-1, help="word index in BACK to color (-1=none)")
p.add_argument("--accent-front", type=int, default=-2, help="word index in FRONT to color (-2=all)")
p.add_argument("--color", choices=list(COLORS), default="pink")
p.add_argument("--tag", default="YUV.AI")
p.add_argument("--size-back", type=int, default=0, help="px; 0=auto")
p.add_argument("--size-front", type=int, default=150)
p.add_argument("--front-top", type=int, default=1285, help="y of the front text (chest level)")
p.add_argument("--out", required=True)
a = p.parse_args()

C = COLORS[a.color]; G = GLOW[a.color]

def accent(text, idx, cls="acc"):
    words = text.split()
    if idx == -2:  # all accented
        return f'<span class="{cls}">{text}</span>'
    return " ".join(f'<span class="{cls}">{w}</span>' if i == idx else w for i, w in enumerate(words))

def autosize(text):
    longest = max(len(w) for w in text.split())
    if longest <= 4: return 290
    if longest <= 6: return 245
    if longest <= 8: return 195
    return 160

size_back = a.size_back or autosize(a.back)

if a.template == "behind":
    body = f'''
      <div class="back-text">{accent(a.back, a.accent_back)}</div>
      <img class="cutout" src="{a.img}" />
      <div class="front-text">{accent(a.front, a.accent_front)}</div>'''
    extra_css = f'''
      .back-text{{position:absolute;left:40px;right:40px;top:430px;z-index:2;direction:rtl;text-align:center;
        font-family:"Rubik";font-weight:900;font-size:{size_back}px;line-height:1.04;color:#fff;}}
      .cutout{{position:absolute;left:50%;transform:translateX(-50%);bottom:0;height:1250px;z-index:3;
        filter:drop-shadow(0 0 34px rgba({G},.42)) drop-shadow(0 24px 60px rgba(0,0,0,.8));}}
      .front-text{{position:absolute;left:30px;right:30px;top:{a.front_top}px;z-index:4;direction:rtl;text-align:center;
        font-family:"Rubik";font-weight:900;font-size:{a.size_front}px;line-height:1.05;color:#fff;
        text-shadow:0 8px 40px rgba(0,0,0,.9),0 0 50px rgba({G},.35);}}'''
else:  # stack
    body = f'''
      <div class="stack">
        <div class="big">{accent(a.back, a.accent_back)}</div>
        {f'<div class="sub">{a.sub}</div>' if a.sub else ''}
      </div>'''
    extra_css = f'''
      .stack{{position:absolute;left:40px;right:40px;top:0;bottom:0;z-index:3;display:flex;flex-direction:column;
        justify-content:center;align-items:center;text-align:center;gap:34px;}}
      .big{{font-family:"Anton","Rubik";font-weight:900;text-transform:uppercase;font-size:{size_back}px;
        line-height:0.98;color:#fff;direction:rtl;}}
      .sub{{font-family:"Rubik";font-weight:900;font-size:96px;color:{C};direction:rtl;
        text-shadow:0 0 30px rgba({G},.5);}}'''

html = f'''<!doctype html><html lang="he"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<style>
@font-face{{font-family:"Anton";src:url("fonts/Anton-Regular.woff2") format("woff2");}}
@font-face{{font-family:"Rubik";font-weight:900;src:url("fonts/Rubik-900.woff2") format("woff2");}}
@font-face{{font-family:"Rubik";font-weight:700;src:url("fonts/Rubik-700.woff2") format("woff2");}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#0A0A0A;}}
#net{{position:absolute;inset:0;z-index:0;opacity:.55;}}
.vig{{position:absolute;inset:0;z-index:1;background:radial-gradient(ellipse 90% 70% at 50% 46%,transparent 40%,rgba(0,0,0,.6) 100%);}}
.acc{{color:{C};text-shadow:0 0 34px rgba({G},.55);}}
.chip{{position:absolute;top:330px;left:64px;z-index:5;font-family:"JetBrains Mono",monospace;font-size:30px;
  letter-spacing:4px;color:{C};border:2px solid {C};padding:10px 22px;border-radius:999px;background:rgba(8,8,12,.55);}}
.phx{{position:absolute;top:316px;right:64px;width:92px;z-index:5;filter:drop-shadow(0 0 16px rgba({G},.45));}}
.handle{{position:absolute;left:0;right:0;top:1556px;z-index:5;text-align:center;font-family:"JetBrains Mono",monospace;
  font-size:27px;letter-spacing:3px;color:rgba(255,255,255,.78);}}
{extra_css}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="0.2" data-width="1080" data-height="1920">
  <canvas id="net" width="1080" height="1920"></canvas>
  <div class="vig"></div>
  <div class="chip">{a.tag}</div>
  <img class="phx" src="assets/logo-phoenix.png"/>
  {body}
  <div class="handle">@yuval_770 · YUV.AI</div>
</div>
<script>
const cv=document.getElementById("net"),ctx=cv.getContext("2d");
function mul(s){{return function(){{s|=0;s=(s+0x6d2b79f5)|0;let t=Math.imul(s^(s>>>15),1|s);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;}};}}
const rnd=mul(20260610);
const ST=[[249,173,69],[240,102,78],[222,96,146],[124,58,237],[78,125,183],[0,229,255]];
function col(u){{u=Math.max(0,Math.min(0.999,u));const s=u*(ST.length-1),i=Math.floor(s),f=s-i,x=ST[i],y=ST[i+1];return[(x[0]+(y[0]-x[0])*f)|0,(x[1]+(y[1]-x[1])*f)|0,(x[2]+(y[2]-x[2])*f)|0];}}
const N=46,ns=[];
for(let i=0;i<N;i++){{const u=rnd();ns.push({{x:rnd()*1080,y:200+rnd()*1500,u:u}});}}
ctx.lineWidth=1;
for(let i=0;i<N;i++)for(let j=i+1;j<N;j++){{const A=ns[i],B=ns[j],d=Math.hypot(A.x-B.x,A.y-B.y);if(d>200)continue;
ctx.strokeStyle="rgba(170,195,255,"+(0.14*(1-d/200)).toFixed(3)+")";ctx.beginPath();ctx.moveTo(A.x,A.y);ctx.lineTo(B.x,B.y);ctx.stroke();}}
for(const m of ns){{const c=col(m.u);ctx.fillStyle="rgb("+c[0]+","+c[1]+","+c[2]+")";ctx.shadowColor=ctx.fillStyle;ctx.shadowBlur=10;
ctx.beginPath();ctx.arc(m.x,m.y,2.6,0,6.2832);ctx.fill();}}
ctx.shadowBlur=0;
window.__timelines=window.__timelines||{{}};window.__timelines["main"]=gsap.timeline({{paused:true}});
</script></body></html>'''

open("index.html", "w", encoding="utf-8").write(html)
print(f"index.html written ({a.template}, back size {size_back}px)")
subprocess.run(["npx", "--yes", "hyperframes@latest", "render", "--fps", "30",
                "--output", "out/_tmp.mp4"], shell=True, check=True, capture_output=True)
os.makedirs("out", exist_ok=True)
subprocess.run(["ffmpeg", "-y", "-i", "out/_tmp.mp4", "-frames:v", "1", f"out/{a.out}.png"],
               shell=True, check=True, capture_output=True)
os.remove("out/_tmp.mp4")
print(f"COVER -> out/{a.out}.png")
