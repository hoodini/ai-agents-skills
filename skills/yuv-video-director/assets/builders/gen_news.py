# Personal-brand cut builder: 2-line karaoke captions + DIRECTOR-TIMED transparent Lottie beats.
# Usage: py gen_news.py [maxchars] [foot_start] [layout: h|v]
import json, sys
sys.stdout.reconfigure(encoding="utf-8")

MAXCHARS = int(sys.argv[1]) if len(sys.argv) > 1 else 46
FOOT_START = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
LAYOUT = sys.argv[3] if len(sys.argv) > 3 else "h"

FIX = [
    ("מומחי היי שלנו","מומחה ה-AI שלנו"),("ברוך בורי הקלוד","ברוך בורא ה-Claude"),
    ("עסקת מסקנות","הסקת מסקנות"),("ונטיח","וננתח"),("טבוני","תבוני"),
    ("פויקט","פרויקט"),("מעולדת","ימי הולדת"),("האיי-איי","ה-AI"),
]
def fix(t):
    for a,b in FIX: t=t.replace(a,b)
    return t

CUT_START, CUT_END = 124.3, 150.6
PUNCH = ("לא","נאמר","שורות","בין","תבוני","קלוד")

# ---- DIRECTOR BEATS: (start, end, lottie, label, style_16x9, style_9x16) ----
# Timed to the spoken content of the cut (offsets from CUT_START):
#  0.2-4.2  "קיצור ותמצות"          -> WhatsApp chatter collapses into a summary
#  4.2-9.9  "פענוח, לפלח... תבוני"   -> decode beam scanning text (RTL)
#  9.9-12.7 "הדבר הקסום"             -> magic sparkles
# 12.7-16.0 "בני אדם רואים בטקסט"     -> reading eye over text
# 16.0-21.3 "מה שלא נאמר/בין השורות"  -> THE hero: hidden line materializes between lines
# 21.4-24.7 "ה-AI טוב בלחלץ"          -> orb extracts the hidden gem
BEATS = [
    (0.25, 4.15, "wa-collapse.json", "קיצור ותמצות",
     "right:80px;top:128px;width:430px;height:430px",
     "left:0;right:0;margin:0 auto;top:160px;width:470px;height:470px"),
    (4.35, 9.75, "decode-beam.json", "פענוח",
     "right:80px;top:140px;width:430px;height:430px",
     "left:0;right:0;margin:0 auto;top:172px;width:460px;height:460px"),
    (9.95, 12.55, "c-magic.json", "הקסם",
     "right:112px;top:128px;width:390px;height:390px",
     "left:0;right:0;margin:0 auto;top:184px;width:430px;height:430px"),
    (12.8, 15.9, "eye-read.json", "מה שכתוב — בני אדם",
     "right:86px;top:138px;width:420px;height:420px",
     "left:0;right:0;margin:0 auto;top:178px;width:450px;height:450px"),
    (16.05, 21.2, "ghost-line.json", "מה שלא נאמר · בין השורות",
     "right:56px;top:132px;width:560px;height:385px",
     "left:0;right:0;margin:0 auto;top:208px;width:600px;height:413px"),
    (21.4, 24.7, "orb-extract.json", "ה-AI מחלץ",
     "right:90px;top:128px;width:430px;height:430px",
     "left:0;right:0;margin:0 auto;top:172px;width:460px;height:460px"),
]

data = json.load(open("transcript.json", encoding="utf-8"))

# ---- captions: pack words into <=MAXCHARS chunks, karaoke per word ----
chunks = []
for s in data["segments"]:
    if not (CUT_START <= s["start"] < CUT_END): continue
    words = fix(s["text"]).strip().split()
    if not words: continue
    cs = FOOT_START + (s["start"]-CUT_START); ce = FOOT_START + (min(s["end"],CUT_END)-CUT_START)
    cd = max(0.8, ce-cs)
    groups, cur, cl = [], [], 0
    for w in words:
        add = len(w)+(1 if cur else 0)
        if cur and cl+add>MAXCHARS: groups.append(cur); cur=[w]; cl=len(w)
        else: cur.append(w); cl+=add
    if cur: groups.append(cur)
    tot = sum(sum(len(w) for w in g) for g in groups) or 1; acc=0
    for g in groups:
        gl=sum(len(w) for w in g); gstart=round(cs+(acc/tot)*cd,2); gdur=max(0.7,round((gl/tot)*cd,2))
        chunks.append((g,gstart,gdur)); acc+=gl

caps_html, caps_js = [], []
for i,(words,cs,cd) in enumerate(chunks):
    total=sum(len(w) for w in words) or 1; spans=[]; acc=0
    for j,w in enumerate(words):
        spans.append(f'<span id="c{i}w{j}">{w}</span>')
        wt=round(cs+(acc/total)*cd*0.82,2)
        pink=any(p in w for p in PUNCH); c="#FF1464" if pink else "#FFFFFF"
        sh="0 0 16px rgba(255,20,100,.6)" if pink else "0 0 10px rgba(255,255,255,.22)"
        caps_js.append(f'tl.set("#c{i}w{j}",{{color:"{c}",textShadow:"{sh}"}},{wt});'); acc+=len(w)
    caps_html.append(f'<div id="cap{i}" class="cap clip" data-start="{cs}" data-duration="{cd}" data-track-index="{20+i}">{" ".join(spans)}</div>')
    caps_js.append(f'tl.from("#cap{i}",{{yPercent:30,opacity:0,duration:0.26,ease:"power2.out",overwrite:"auto"}},{cs});')

# ---- director beats -> transparent floating lottie overlays ----
illu_html, illu_js = [], []
for n,(b0,b1,lot,lab,sh,sv) in enumerate(BEATS):
    st = sh if LAYOUT=="h" else sv
    dur = round(b1-b0,2)
    illu_html.append(f'<div id="bt{n}" class="illu clip" data-start="{b0}" data-duration="{dur}" data-track-index="{60+n}" style="{st}"><div class="illu-lot" id="bt{n}lot"></div><div class="illu-lab">{lab}</div></div>')
    illu_js.append(
        f'L("bt{n}lot","assets/{lot}");'
        f'tl.from("#bt{n}",{{scale:0.7,opacity:0,duration:0.45,ease:"back.out(1.6)",overwrite:"auto"}},{b0});'
        f'tl.to("#bt{n}",{{opacity:0,y:-14,duration:0.3,ease:"power1.in",overwrite:"auto"}},{round(b0+dur-0.32,2)});')

print(f"{len(chunks)} captions (<= {MAXCHARS} chars), {len(BEATS)} director beats, layout {LAYOUT}")

html = (open("template.tpl",encoding="utf-8").read()
        .replace("@@CAPS_HTML@@","\n      ".join(caps_html))
        .replace("@@CAPS_JS@@","\n      ".join(caps_js))
        .replace("@@ILLU_HTML@@","\n      ".join(illu_html))
        .replace("@@ILLU_JS@@","\n      ".join(illu_js)))
open("index.html","w",encoding="utf-8").write(html)
print("wrote index.html")
