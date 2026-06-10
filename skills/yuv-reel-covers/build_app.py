# Builds cover-studio.html v3 — "YUV Cover Studio": liquid-glass UI, one-image AI cutout (in-browser),
# text stretch/skew/behind-front, all social formats, RTL/Hebrew first-class, prompt generator.
import base64, sys
sys.stdout.reconfigure(encoding="utf-8")
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()

HTML = r'''<!doctype html><html lang="en"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>YUV Cover Studio — covers that stop the scroll</title>
<meta property="og:title" content="YUV Cover Studio"/>
<meta property="og:description" content="Poster-grade covers for Reels, TikTok, YouTube, X & LinkedIn — text behind your subject, AI cutout, RTL-first."/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Bebas+Neue&family=Archivo+Black&display=swap" rel="stylesheet">
<style>
@font-face{font-family:"AntonX";src:url(data:font/woff2;base64,__ANTON__) format("woff2");}
@font-face{font-family:"RubikX";font-weight:900;src:url(data:font/woff2;base64,__RUBIK__) format("woff2");}
:root{--pink:#FF1464;--cyan:#00E5FF;--violet:#7C3AED;--yel:#E9FF3D;--glass:rgba(255,255,255,.045);--bord:rgba(255,255,255,.09);}
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:Inter,system-ui,sans-serif;background:#07070C;color:#EDEDF2;min-height:100vh;display:flex;overflow:hidden;}
body::before,body::after{content:"";position:fixed;width:60vw;height:60vw;border-radius:50%;filter:blur(120px);opacity:.16;z-index:0;pointer-events:none;}
body::before{background:var(--pink);top:-20vw;left:-15vw;}
body::after{background:var(--cyan);bottom:-25vw;right:-15vw;}
#side{position:relative;z-index:2;width:392px;height:100vh;overflow-y:auto;padding:20px 18px 40px;
  background:var(--glass);backdrop-filter:blur(28px) saturate(150%);border-right:1px solid var(--bord);}
#side::-webkit-scrollbar{width:6px}#side::-webkit-scrollbar-thumb{background:#2a2a36;border-radius:99px}
#stage{position:relative;z-index:1;flex:1;display:flex;align-items:center;justify-content:center;padding:26px;}
#cv{max-height:92vh;max-width:100%;border-radius:14px;box-shadow:0 30px 90px rgba(0,0,0,.65),0 0 0 1px rgba(255,255,255,.06);}
.brand{display:flex;align-items:center;gap:12px;margin-bottom:4px;}
.brand img{width:42px;filter:drop-shadow(0 0 12px rgba(255,20,100,.5));}
.brand h1{font-size:19px;font-weight:800;background:linear-gradient(95deg,#FF1464,#7C3AED 55%,#00E5FF);-webkit-background-clip:text;background-clip:text;color:transparent;letter-spacing:.5px;}
.sub{font-size:11px;color:#8a8a98;margin:2px 0 14px;}
.tabs{display:flex;background:rgba(255,255,255,.05);border:1px solid var(--bord);border-radius:999px;padding:4px;margin-bottom:16px;}
.tabs div{flex:1;text-align:center;padding:9px;border-radius:999px;cursor:pointer;font-size:12px;font-weight:800;letter-spacing:.6px;color:#aab;transition:.25s;}
.tabs div.on{background:linear-gradient(95deg,var(--pink),var(--violet) 60%,var(--cyan));color:#fff;box-shadow:0 6px 24px rgba(255,20,100,.35);}
.card{background:var(--glass);border:1px solid var(--bord);border-radius:18px;padding:14px;margin-bottom:12px;backdrop-filter:blur(20px);}
.card h3{font-size:10.5px;letter-spacing:2.2px;color:#9fa3b8;margin-bottom:10px;display:flex;align-items:center;gap:8px;text-transform:uppercase;}
.card h3::before{content:"";width:7px;height:7px;border-radius:99px;background:linear-gradient(95deg,var(--pink),var(--cyan));box-shadow:0 0 10px var(--pink);}
label{display:block;font-size:10.5px;color:#9aa0b4;margin:9px 0 4px;letter-spacing:.4px;}
input[type=text]{width:100%;padding:9px 12px;background:rgba(0,0,0,.35);border:1px solid var(--bord);color:#fff;border-radius:12px;font-size:13.5px;outline:none;transition:.2s;}
input[type=text]:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,229,255,.12);}
select{width:100%;padding:9px 12px;background:rgba(0,0,0,.35);border:1px solid var(--bord);color:#fff;border-radius:12px;font-size:13px;}
input[type=range]{-webkit-appearance:none;width:100%;height:5px;border-radius:99px;background:linear-gradient(90deg,var(--pink),var(--cyan));outline:none;}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:17px;height:17px;border-radius:50%;background:#fff;border:3px solid var(--pink);box-shadow:0 2px 10px rgba(0,0,0,.5);cursor:pointer;}
.row{display:flex;gap:10px;}.row>*{flex:1;min-width:0;}
.fmt{display:flex;flex-wrap:wrap;gap:6px;}
.fmt div{padding:7px 11px;border-radius:999px;background:rgba(255,255,255,.05);border:1px solid var(--bord);font-size:10.5px;font-weight:700;cursor:pointer;color:#bbc;transition:.2s;letter-spacing:.3px;}
.fmt div.on{background:linear-gradient(95deg,var(--pink),var(--violet));color:#fff;border-color:transparent;box-shadow:0 4px 18px rgba(255,20,100,.4);}
.sw{display:flex;gap:8px;margin-top:2px;}
.sw div{width:26px;height:26px;border-radius:50%;cursor:pointer;border:2px solid transparent;transition:.15s;}
.sw div.on{border-color:#fff;transform:scale(1.18);box-shadow:0 0 14px currentColor;}
.toggle{display:flex;align-items:center;justify-content:space-between;font-size:12.5px;color:#cdd;padding:7px 0;}
.tg{width:40px;height:22px;border-radius:99px;background:rgba(255,255,255,.12);position:relative;cursor:pointer;transition:.25s;flex:none;}
.tg::after{content:"";position:absolute;width:16px;height:16px;border-radius:50%;background:#fff;top:3px;left:3px;transition:.25s;}
.tg.on{background:linear-gradient(95deg,var(--pink),var(--cyan));}
.tg.on::after{left:21px;}
.btn{width:100%;padding:13px;margin-top:10px;border:0;border-radius:999px;cursor:pointer;font-size:14px;font-weight:800;letter-spacing:.4px;color:#fff;
  background:linear-gradient(95deg,var(--pink),var(--violet) 55%,var(--cyan));box-shadow:0 10px 32px rgba(255,20,100,.4);transition:.2s;}
.btn:hover{transform:translateY(-2px);box-shadow:0 14px 40px rgba(255,20,100,.55);}
.btn.ghost{background:rgba(255,255,255,.07);border:1px solid var(--bord);box-shadow:none;color:#dde;}
.btn.magic{background:linear-gradient(95deg,#E9FF3D,#00E5FF);color:#07111a;}
.up{border:1.5px dashed rgba(255,255,255,.22);border-radius:16px;padding:16px;text-align:center;font-size:12px;color:#9aa;cursor:pointer;transition:.2s;}
.up:hover{border-color:var(--cyan);color:#fff;background:rgba(0,229,255,.05);}
.up b{color:#fff;}
#status{font-size:11px;color:var(--yel);min-height:15px;margin-top:6px;text-align:center;}
textarea{width:100%;height:150px;padding:10px;background:rgba(0,0,0,.35);border:1px solid var(--bord);color:#dde;border-radius:12px;font-size:11px;line-height:1.55;}
small{color:#778;font-size:10px;display:block;margin-top:4px;line-height:1.5;}
.hide{display:none!important;}
</style></head><body>
<div id="side">
  <div class="brand"><img src="data:image/png;base64,__LOGO__"/><div><h1>YUV COVER STUDIO</h1><div class="sub">poster-grade covers · text behind you · RTL first</div></div></div>
  <div class="tabs"><div id="tabS" class="on" onclick="tab('S')">STUDIO</div><div id="tabP" onclick="tab('P')">AI PROMPTS</div></div>

  <div id="paneS">
    <div class="card"><h3>Format</h3><div class="fmt" id="fmt"></div></div>

    <div class="card"><h3>Your image</h3>
      <div class="up" onclick="document.getElementById('file').click()"><b>Upload one photo</b><br>we'll handle the layers &amp; masking</div>
      <input type="file" id="file" accept="image/*" class="hide" onchange="onPhoto(this)">
      <button class="btn magic" id="magicBtn" onclick="magic()" disabled>✂ Magic Cutout (AI, in-browser)</button>
      <div id="status"></div>
      <div class="toggle">Photo as background <div class="tg on" id="tgBG" onclick="tog(this);draw()"></div></div>
      <div class="row"><div><label>Subject size</label><input type="range" id="cutH" min="25" max="100" value="58" oninput="draw()"></div>
      <div><label>Subject ⟷</label><input type="range" id="cutX" min="-40" max="40" value="0" oninput="draw()"></div></div>
      <label>Backdrop (when photo bg is off)</label>
      <select id="bgsel" onchange="draw()"><option value="sky">Vivid Sky</option><option value="sunset">Sunset</option><option value="ink">Rich Black</option><option value="cinema">Cinema duotone (pink/cyan)</option></select>
      <small>Advanced: <a href="#" style="color:#7cf" onclick="document.getElementById('cutfile').click();return false">upload a ready cutout PNG</a></small>
      <input type="file" id="cutfile" accept="image/png" class="hide" onchange="loadCut(this)">
    </div>

    <div class="card"><h3>Headline</h3>
      <input type="text" id="l1" value="STEAL MY" oninput="draw()" placeholder="Line 1 — English or עברית">
      <div class="row" style="margin-top:8px"><div class="sw" id="sw1"></div>
        <div class="toggle" style="flex:none;gap:8px">behind <div class="tg on" id="bh1" onclick="tog(this);draw()"></div></div></div>
      <input type="text" id="l2" value="PROMPTS" oninput="draw()" placeholder="Line 2" style="margin-top:10px">
      <div class="row" style="margin-top:8px"><div class="sw" id="sw2"></div>
        <div class="toggle" style="flex:none;gap:8px">behind <div class="tg on" id="bh2" onclick="tog(this);draw()"></div></div></div>
      <div class="row"><div><label>Size</label><input type="range" id="hs" min="40" max="130" value="100" oninput="draw()"></div>
      <div><label>Stretch ↕ (taller letters)</label><input type="range" id="stretch" min="100" max="230" value="138" oninput="draw()"></div></div>
      <div class="row"><div><label>Slant</label><input type="range" id="skew" min="-14" max="6" value="-8" oninput="draw()"></div>
      <div><label>Font</label><select id="fontsel" onchange="draw()"><option value="auto">Auto (Anton/Rubik)</option><option value="Bebas Neue">Bebas Neue</option><option value="Archivo Black">Archivo Black</option></select></div></div>
      <div class="row"><div><label>Line 1 ↕</label><input type="range" id="y1" min="8" max="60" value="23" oninput="draw()"></div>
      <div><label>Line 2 ↕</label><input type="range" id="y2" min="30" max="85" value="52" oninput="draw()"></div></div>
      <label>Punch word (always in front)</label><input type="text" id="lf" value="" oninput="draw()" placeholder="e.g. עכשיו / NOW">
      <div class="row"><div><label>Punch ↕</label><input type="range" id="yf" min="40" max="92" value="67" oninput="draw()"></div>
      <div><label>Punch size</label><input type="range" id="sf" min="40" max="200" value="120" oninput="draw()"></div></div>
    </div>

    <div class="card"><h3>Poster extras</h3>
      <div class="toggle">Ticker strips (ALL DAY ✦ …) <div class="tg on" id="tgTick" onclick="tog(this);draw()"></div></div>
      <input type="text" id="ticker" value="ALL DAY,EVERY PLAY,NO LIMITS" oninput="draw()">
      <div class="toggle">Power stack + icons <div class="tg on" id="tgStack" onclick="tog(this);draw()"></div></div>
      <input type="text" id="stack" value="FOCUS,ENERGY,DISCIPLINE,VICTORY" oninput="draw()">
      <div class="toggle">Brand chip + phoenix + handle <div class="tg on" id="tgBrand" onclick="tog(this);draw()"></div></div>
      <div class="row"><div><input type="text" id="tag" value="AI PROMPTS" oninput="draw()"></div>
      <div><input type="text" id="handle" value="@yuval_770 · YUV.AI" oninput="draw()"></div></div>
      <div class="toggle">Safe-zone guide <div class="tg" id="tgGuide" onclick="tog(this);draw()"></div></div>
    </div>

    <button class="btn" onclick="exportPNG()">⬇ Export PNG</button>
    <button class="btn ghost" onclick="demo()">✨ Load demo</button>
  </div>

  <div id="paneP" class="hide">
    <div class="card"><h3>Prompt generator</h3>
      <label>Engine</label><select id="eng"><option>Midjourney v7</option><option>Flux / Leonardo</option><option>Nano Banana 2 (best text)</option></select>
      <label>Series</label><select id="pSeries"><option>HYPE</option><option>CINEMA</option></select>
      <label>Subject</label><input type="text" id="pSub" value="a charismatic Israeli tech creator, short dark hair, black t-shirt with a colorful phoenix print">
      <label>Action</label><input type="text" id="pAct" value="leaping mid-air reaching toward the camera">
      <label>Environment</label><input type="text" id="pEnv" value="outdoor rooftop against a vivid blue sky with palm trees">
      <label>Depth prop (crosses the frame, blurred)</label><input type="text" id="pProp" value="a glowing smartphone flying huge in the blurred foreground">
      <div class="row"><div><label>Word 1</label><input type="text" id="pW1" value="STEAL MY"></div>
      <div><label>Word 2</label><input type="text" id="pW2" value="PROMPTS"></div></div>
      <label>Ticker</label><input type="text" id="pTick" value="ALL DAY,EVERY PLAY,NO LIMITS">
      <button class="btn" onclick="genPrompt()">Generate</button>
      <textarea id="pOut"></textarea>
      <button class="btn ghost" onclick="navigator.clipboard.writeText(document.getElementById('pOut').value)">Copy</button>
      <small>Pro flow: generate the scene WITHOUT text → upload here → Magic Cutout → type the headline (Hebrew works perfectly). AI photo drama + pixel-perfect type.</small>
    </div>
  </div>
</div>
<div id="stage"><canvas id="cv"></canvas></div>

<script>
const ACC={yellow:"#E9FF3D",white:"#FFFFFF",pink:"#FF1464",cyan:"#00E5FF"};
const FMTS=[["REEL / TIKTOK",1080,1920,"reel"],["POST 4:5",1080,1350,""],["SQUARE",1080,1080,""],["YT THUMB",1280,720,""],["YT BANNER",2560,1440,"yt"],["X HEADER",1500,500,""],["LINKEDIN",1584,396,""],["FB COVER",820,312,""]];
const BGS={sky:["#1557C9","#2E8BE8","#8FD2FF"],sunset:["#2A1860","#B43A8E","#FF8A5C"],ink:["#181826","#0A0A0F","#0A0A0F"],cinema:["#181826","#0A0A0F","#0A0A0F"]};
const cv=document.getElementById("cv"),X=cv.getContext("2d");
const S={bg:null,bgBlob:null,cut:null,fi:0,c1:"yellow",c2:"yellow"};
const logo=new Image();logo.src="data:image/png;base64,__LOGO__";logo.onload=()=>draw();
const $=id=>document.getElementById(id);
const heb=t=>/[֐-׿]/.test(t);
const on=el=>el.classList.contains("on");
function tog(el){el.classList.toggle("on");}
function tab(t){$("paneS").classList.toggle("hide",t!="S");$("paneP").classList.toggle("hide",t!="P");$("tabS").classList.toggle("on",t=="S");$("tabP").classList.toggle("on",t=="P");}
// format pills
const fmtBox=$("fmt");FMTS.forEach((f,i)=>{const d=document.createElement("div");d.textContent=f[0];if(i==0)d.classList.add("on");
 d.onclick=()=>{S.fi=i;[...fmtBox.children].forEach(c=>c.classList.remove("on"));d.classList.add("on");setSize();draw();};fmtBox.appendChild(d);});
function setSize(){const f=FMTS[S.fi];cv.width=f[1];cv.height=f[2];}
// color swatches
function swatches(boxId,key){const b=$(boxId);Object.entries(ACC).forEach(([k,v],i)=>{const d=document.createElement("div");d.style.background=v;d.style.color=v;
 if((key=="c1"&&k=="yellow")||(key=="c2"&&k=="yellow"))d.classList.add("on");
 d.onclick=()=>{S[key]=k;[...b.children].forEach(c=>c.classList.remove("on"));d.classList.add("on");draw();};b.appendChild(d);});}
swatches("sw1","c1");swatches("sw2","c2");
function onPhoto(inp){const f=inp.files[0];if(!f)return;S.bgBlob=f;const img=new Image();
 img.onload=()=>{S.bg=img;S.cut=null;$("magicBtn").disabled=false;$("status").textContent="Photo loaded — hit Magic Cutout ✂";draw();};
 img.src=URL.createObjectURL(f);}
function loadCut(inp){const f=inp.files[0];if(!f)return;const img=new Image();img.onload=()=>{S.cut=img;draw();};img.src=URL.createObjectURL(f);}
async function magic(){
 if(!S.bgBlob)return;$("magicBtn").disabled=true;
 try{
  $("status").textContent="Loading AI model… first time ≈30-60s";
  const mod=await import("https://cdn.jsdelivr.net/npm/@imgly/background-removal@1.5.5/+esm");
  const out=await mod.removeBackground(S.bgBlob,{progress:(k,c,t)=>{$("status").textContent="AI cutout: "+Math.round(c/Math.max(t,1)*100)+"%";}});
  const img=new Image();img.onload=()=>{S.cut=img;$("status").textContent="Cutout ready ✓ — your text now lives behind you";draw();};
  img.src=URL.createObjectURL(out);
 }catch(e){$("status").textContent="AI cutout failed ("+e.message+") — use Advanced upload";console.error(e);}
 $("magicBtn").disabled=false;}
function demo(){S.bg=null;S.cut=null;S.bgBlob=null;const img=new Image();
 img.onload=()=>{S.cut=img;draw();};img.onerror=()=>draw();img.src="assets/yuval-cutout.png";draw();}
function coverFit(img,W,H){const r=Math.max(W/img.width,H/img.height);return[(W-img.width*r)/2,(H-img.height*r)/2,img.width*r,img.height*r];}
function star4(c,x,y,r){c.beginPath();c.moveTo(x,y-r);c.lineTo(x+r*.3,y-r*.3);c.lineTo(x+r,y);c.lineTo(x+r*.3,y+r*.3);c.lineTo(x,y+r);c.lineTo(x-r*.3,y+r*.3);c.lineTo(x-r,y);c.lineTo(x-r*.3,y-r*.3);c.closePath();c.fill();}
function famFor(t){const f=$("fontsel").value;if(f!="auto")return[`"${f}"`,400];return heb(t)?["RubikX",900]:["AntonX",400];}
function bigLine(c,t,yPct,color,behind){if(!t)return;const W=cv.width,H=cv.height;
 const[fam,wt]=famFor(t);const st=parseInt($("stretch").value)/100;const sk=parseInt($("skew").value);
 let s=Math.round(H*0.22*parseInt($("hs").value)/100/st*1.6);
 c.font=wt+" "+s+"px "+fam;const up=t.toUpperCase();
 while(c.measureText(up).width>W-Math.round(W*.07)&&s>24){s-=4;c.font=wt+" "+s+"px "+fam;}
 c.save();c.translate(W/2,H*yPct/100);c.scale(1,st);c.transform(1,0,Math.tan(sk*Math.PI/180),1,0,0);
 c.fillStyle=color;c.textAlign="center";c.textBaseline="top";
 c.shadowColor="rgba(0,0,0,.35)";c.shadowBlur=Math.round(H*.02);c.shadowOffsetY=Math.round(H*.005);
 if(heb(t))c.direction="rtl";c.fillText(up,0,0);c.restore();c.direction="ltr";}
function ticker(c,y,color){const W=cv.width;const ws=$("ticker").value.split(",").map(w=>w.trim()).filter(Boolean);if(!ws.length)return;
 const fs=Math.max(14,Math.round(W*0.025));c.font="800 "+fs+"px Inter, Arial";c.fillStyle=color;c.textBaseline="middle";
 let seq=[];for(let r=0;r<8;r++)ws.forEach(w=>seq.push(w));
 let tot=0;seq.forEach(w=>tot+=c.measureText(w.toUpperCase()).width+fs*2);
 let x=W/2-tot/2;c.save();c.beginPath();c.rect(0,y-fs,W,fs*2);c.clip();c.textAlign="left";
 seq.forEach(w=>{c.fillText(w.toUpperCase(),x,y);x+=c.measureText(w.toUpperCase()).width+fs*.6;star4(c,x+fs*.35,y,fs*.33);x+=fs*1.4;});c.restore();}
function draw(){
 const W=cv.width,H=cv.height;const cine=$("bgsel").value=="cinema";const usePhotoBG=on($("tgBG"))&&S.bg;
 X.clearRect(0,0,W,H);X.direction="ltr";
 // BG
 if(usePhotoBG){X.save();if(cine){X.filter="saturate(.8) contrast(1.1) brightness(.5) blur("+Math.round(W*.022)+"px)";const[x,y,w,h]=coverFit(S.bg,W,H);X.drawImage(S.bg,x-w*.09,y-h*.09,w*1.18,h*1.18);}
  else{const[x,y,w,h]=coverFit(S.bg,W,H);X.drawImage(S.bg,x,y,w,h);}X.restore();}
 else{const g=X.createLinearGradient(0,0,0,H);const cs=BGS[$("bgsel").value];g.addColorStop(0,cs[0]);g.addColorStop(.45,cs[1]);g.addColorStop(1,cs[2]);X.fillStyle=g;X.fillRect(0,0,W,H);}
 if(cine){X.save();X.globalCompositeOperation="screen";
  let g1=X.createRadialGradient(W*.08,H*.2,0,W*.08,H*.2,H*.55);g1.addColorStop(0,"rgba(255,20,100,.55)");g1.addColorStop(1,"rgba(255,20,100,0)");X.fillStyle=g1;X.fillRect(0,0,W,H);
  let g2=X.createRadialGradient(W*.95,H*.45,0,W*.95,H*.45,H*.55);g2.addColorStop(0,"rgba(0,229,255,.5)");g2.addColorStop(1,"rgba(0,229,255,0)");X.fillStyle=g2;X.fillRect(0,0,W,H);X.restore();
  X.fillStyle="rgba(0,0,0,.3)";X.fillRect(0,H*.72,W,H*.28);}
 // BEHIND text
 if(on($("tgTick"))&&!cine)ticker(X,H*parseInt($("y2").value)/100-H*.03,"rgba(255,255,255,.95)");
 if(on($("bh1")))bigLine(X,$("l1").value,parseInt($("y1").value),ACC[S.c1],true);
 if(on($("bh2")))bigLine(X,$("l2").value,parseInt($("y2").value),ACC[S.c2],true);
 // SUBJECT
 if(S.cut){const hgt=H*parseInt($("cutH").value)/100;const w=S.cut.width*(hgt/S.cut.height);
  X.save();X.shadowColor="rgba(0,0,0,.6)";X.shadowBlur=Math.round(H*.025);X.shadowOffsetY=Math.round(H*.012);
  X.drawImage(S.cut,W/2-w/2+W*parseInt($("cutX").value)/100,H-hgt,w,hgt);X.restore();}
 // FRONT text
 if(!on($("bh1")))bigLine(X,$("l1").value,parseInt($("y1").value),ACC[S.c1],false);
 if(!on($("bh2")))bigLine(X,$("l2").value,parseInt($("y2").value),ACC[S.c2],false);
 const lf=$("lf").value;
 if(lf){const[fam,wt]=famFor(lf);const sk=parseInt($("skew").value);let s=Math.round(H*parseInt($("sf").value)/1000);s=Math.max(24,s);
  X.save();X.translate(W/2,H*parseInt($("yf").value)/100);X.transform(1,0,Math.tan(sk*Math.PI/180),1,0,0);
  X.font=wt+" "+s+"px "+fam;X.fillStyle=S.c1=="white"?ACC.pink:"#FFFFFF";X.textAlign="center";X.textBaseline="top";
  X.shadowColor="rgba(0,0,0,.8)";X.shadowBlur=Math.round(H*.02);if(heb(lf))X.direction="rtl";X.fillText(lf.toUpperCase(),0,0);X.restore();X.direction="ltr";}
 // chrome
 if(on($("tgTick")))ticker(X,Math.max(H*.155,40),"rgba(255,255,255,.92)");
 if(on($("tgStack"))&&$("stack").value.trim()){const acc=cine?"#FFFFFF":ACC[S.c1];const fs=Math.round(H*.021+10);
  X.font="400 "+fs+"px AntonX";X.textAlign="right";X.fillStyle=acc;X.textBaseline="top";
  const words=$("stack").value.split(",").map(w=>w.trim());const baseY=H*.76 - words.length*fs*1.28;
  words.forEach((w,i)=>X.fillText(w.toUpperCase(),W-Math.round(W*.06),baseY+i*fs*1.28));
  const iy=H*.76+fs*.4,ir=fs*.42;X.strokeStyle=acc;X.lineWidth=2;X.fillStyle=acc;
  star4(X,W-Math.round(W*.06)-ir*5.4,iy,ir);
  X.beginPath();X.arc(W-Math.round(W*.06)-ir*3.2,iy,ir,0,7);X.stroke();X.beginPath();X.ellipse(W-Math.round(W*.06)-ir*3.2,iy,ir*.45,ir,0,0,7);X.stroke();
  X.beginPath();X.arc(W-Math.round(W*.06)-ir,iy,ir,0,7);X.stroke();X.beginPath();X.arc(W-Math.round(W*.06)-ir,iy,ir*.5,0,7);X.stroke();X.beginPath();X.arc(W-Math.round(W*.06)-ir,iy,ir*.16,0,7);X.fill();}
 if(on($("tgBrand"))){const fs=Math.round(H*.014+8);X.font="700 "+fs+"px 'Courier New',monospace";
  const tg=$("tag").value.toUpperCase();const tw=X.measureText(tg).width;const cy=Math.max(H*.19,76);
  X.fillStyle="rgba(8,8,12,.35)";X.strokeStyle="rgba(255,255,255,.9)";X.lineWidth=2;
  rr(X,Math.round(W*.06),cy,tw+fs*1.6,fs*1.9,fs);X.fill();X.stroke();
  X.fillStyle="#fff";X.textAlign="left";X.textBaseline="middle";X.fillText(tg,Math.round(W*.06)+fs*.8,cy+fs*.95);
  const lw=Math.round(H*.05+26);if(logo.complete)X.drawImage(logo,W-Math.round(W*.06)-lw,cy-fs*.3,lw,lw);
  X.font="600 "+Math.round(fs*.95)+"px 'Courier New',monospace";X.fillStyle="rgba(255,255,255,.85)";X.textAlign="center";
  X.shadowColor="rgba(0,0,0,.8)";X.shadowBlur=10;X.fillText($("handle").value,W/2,H-Math.max(H*.045,22));X.shadowBlur=0;}
 // vignette + guide
 const v=X.createRadialGradient(W/2,H*.45,H*.3,W/2,H*.45,H*.78);v.addColorStop(0,"rgba(0,0,0,0)");v.addColorStop(1,"rgba(0,0,0,.36)");X.fillStyle=v;X.fillRect(0,0,W,H);
 if(on($("tgGuide"))){X.strokeStyle="rgba(255,255,255,.55)";X.setLineDash([14,10]);
  const g=FMTS[S.fi][3];
  if(g=="reel")X.strokeRect(0,(H-1350*H/1920)/2,W,1350*H/1920);
  if(g=="yt")X.strokeRect((W-1546)/2,(H-423)/2,1546,423);
  X.setLineDash([]);}
}
function rr(c,x,y,w,h,r){c.beginPath();c.moveTo(x+r,y);c.arcTo(x+w,y,x+w,y+h,r);c.arcTo(x+w,y+h,x,y+h,r);c.arcTo(x,y+h,x,y,r);c.arcTo(x,y,x+w,y,r);c.closePath();}
function exportPNG(){const g=on($("tgGuide"));if(g)tog($("tgGuide"));draw();
 cv.toBlob(b=>{const a=document.createElement("a");a.href=URL.createObjectURL(b);
  a.download="yuv-cover-"+FMTS[S.fi][0].split(" ")[0].toLowerCase()+"-"+($("l2").value||$("l1").value||"x").replace(/\s+/g,"-")+".png";a.click();
  if(g)tog($("tgGuide"));draw();});}
function genPrompt(){
 const e=$("eng").value,sr=$("pSeries").value,sub=$("pSub").value,act=$("pAct").value,env=$("pEnv").value,prop=$("pProp").value;
 const w1=$("pW1").value.toUpperCase(),w2=$("pW2").value.toUpperCase();
 const tick=$("pTick").value.split(",").map(s=>s.trim().toUpperCase()).join(" ✦ ");
 let core;
 if(sr=="HYPE")core=`ultra low-angle full-body action shot of ${sub}, ${act}, larger-than-life sports-editorial campaign poster, ${env}, vivid saturated colors, crisp rim light, premium ad-campaign retouching, ${prop} crossing the frame with motion blur for depth of field, GIANT condensed italic sans-serif typography in neon yellow: "${w1}" across the upper area and "${w2}" across the lower third, the subject's body and limbs overlapping the huge letters so the text reads both behind and in front of the figure, small repeated ticker caption "${tick}" in bold white spaced capitals, tiny thin line icons (four-point star, globe, target) in the bottom right corner, magazine poster composition, shot on medium format, hyper-detailed`;
 else core=`dramatic cinematic portrait of ${sub}, ${act}, ${env}, split lighting with hot pink light from the left and electric cyan light from the right, duotone color grade, crushed blacks, moody fog, symmetrical composition, GIANT condensed white sans-serif typography: "${w1}" at the top and "${w2}" across the middle, the words partially hidden BEHIND the subject's head so the figure overlaps the letters, minimal, premium film-poster look, 35mm cinematic still, hyper-detailed`;
 let out;
 if(e.startsWith("Midjourney"))out=core+" --ar 4:5 --style raw --v 7";
 else if(e.startsWith("Flux"))out="typographic poster, accurate legible text rendering. "+core+". 4:5 portrait";
 else out="Create a 4:5 portrait poster image. Render ALL text EXACTLY as written, correct spelling. "+core+". Keep the headline letters razor-sharp and perfectly legible.";
 $("pOut").value=out;}
setSize();document.fonts.ready.then(draw);draw();
</script></body></html>'''

html = (HTML.replace("__ANTON__", b64("fonts/Anton-Regular.woff2"))
            .replace("__RUBIK__", b64("fonts/Rubik-900.woff2"))
            .replace("__LOGO__", b64("assets/logo-phoenix.png")))
open("cover-studio.html", "w", encoding="utf-8").write(html)
print("cover-studio.html v3:", round(len(html)/1024), "KB")
