# Builds cover-studio.html — fully self-contained (fonts + logo inlined as base64).
import base64, sys
sys.stdout.reconfigure(encoding="utf-8")
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()

HTML = r'''<!doctype html><html lang="he"><head><meta charset="UTF-8"/>
<title>YUV.AI Cover Studio</title>
<style>
@font-face{font-family:"AntonX";src:url(data:font/woff2;base64,__ANTON__) format("woff2");}
@font-face{font-family:"RubikX";font-weight:900;src:url(data:font/woff2;base64,__RUBIK__) format("woff2");}
*{margin:0;padding:0;box-sizing:border-box;font-family:system-ui,Segoe UI,sans-serif;}
body{background:#0E0E14;color:#eee;display:flex;min-height:100vh;}
#panel{width:380px;padding:18px;background:#15151E;overflow-y:auto;height:100vh;}
#stage{flex:1;display:flex;align-items:center;justify-content:center;padding:18px;}
canvas{height:92vh;box-shadow:0 20px 80px rgba(0,0,0,.6);}
h1{font-size:18px;color:#FF1464;margin-bottom:4px;} .sub{font-size:11px;color:#888;margin-bottom:14px;}
label{display:block;font-size:11px;color:#9aa;letter-spacing:1px;margin:10px 0 3px;text-transform:uppercase;}
input[type=text],select,textarea{width:100%;padding:7px 9px;background:#0E0E14;border:1px solid #333;color:#eee;border-radius:4px;font-size:13px;}
input[type=range]{width:100%;}
.row{display:flex;gap:8px;} .row>*{flex:1;}
button{width:100%;padding:10px;margin-top:12px;background:linear-gradient(95deg,#FF1464,#7C3AED 60%,#00E5FF);border:0;color:#fff;font-weight:700;border-radius:999px;cursor:pointer;font-size:14px;}
button.ghost{background:#222;border:1px solid #444;}
.tabs{display:flex;gap:6px;margin-bottom:12px;}
.tabs div{flex:1;text-align:center;padding:8px;background:#222;border-radius:6px;cursor:pointer;font-size:12px;font-weight:700;}
.tabs div.on{background:#FF1464;}
.hide{display:none;}
textarea{height:130px;font-size:11px;line-height:1.5;}
small{color:#777;font-size:10px;display:block;margin-top:2px;}
</style></head><body>
<div id="panel">
  <h1>YUV.AI COVER STUDIO</h1><div class="sub">Editorial Poster system · text behind &amp; in front</div>
  <div class="tabs"><div id="tabS" class="on" onclick="tab('S')">STUDIO</div><div id="tabP" onclick="tab('P')">AI PROMPTS</div></div>

  <div id="paneS">
    <label>Preset</label>
    <select id="preset" onchange="applyPreset()">
      <option value="sky">HYPE · Sky (yellow)</option><option value="sunset">HYPE · Sunset (yellow)</option>
      <option value="ink">HYPE · Ink (yellow)</option><option value="cinema">CINEMA · Duotone (white)</option>
    </select>
    <label>Background photo (optional)</label><input type="file" accept="image/*" onchange="loadImg(this,'bg')">
    <label>Subject cutout PNG (transparent)</label><input type="file" accept="image/*" onchange="loadImg(this,'cut')">
    <div class="row"><div><label>Cutout height %</label><input type="range" id="cutH" min="30" max="90" value="55" oninput="draw()"></div>
    <div><label>Cutout X offset</label><input type="range" id="cutX" min="-300" max="300" value="0" oninput="draw()"></div></div>
    <label>Headline line 1</label><input type="text" id="l1" value="STEAL MY" oninput="draw()">
    <label>Headline line 2 (crossed by subject)</label><input type="text" id="l2" value="PROMPTS" oninput="draw()">
    <div class="row">
      <div><label>Color L1</label><select id="c1" onchange="draw()"><option>yellow</option><option>white</option><option>pink</option><option>cyan</option></select></div>
      <div><label>Color L2</label><select id="c2" onchange="draw()"><option>yellow</option><option>white</option><option>pink</option><option>cyan</option></select></div>
    </div>
    <div class="row"><div><label>Y line 1</label><input type="range" id="y1" min="300" max="900" value="470" oninput="draw()"></div>
    <div><label>Y line 2</label><input type="range" id="y2" min="700" max="1400" value="1010" oninput="draw()"></div></div>
    <label>Front word (in front of subject)</label><input type="text" id="lf" value="" oninput="draw()">
    <div class="row"><div><label>Front Y</label><input type="range" id="yf" min="900" max="1500" value="1285" oninput="draw()"></div>
    <div><label>Front size</label><input type="range" id="sf" min="70" max="260" value="150" oninput="draw()"></div></div>
    <label>Ticker words (comma)</label><input type="text" id="ticker" value="ALL DAY,EVERY PLAY,NO LIMITS" oninput="draw()">
    <label>Power stack (comma, empty=off)</label><input type="text" id="stack" value="FOCUS,ENERGY,DISCIPLINE,VICTORY" oninput="draw()">
    <div class="row">
      <div><label>Chip tag</label><input type="text" id="tag" value="AI PROMPTS" oninput="draw()"></div>
      <div><label>Handle</label><input type="text" id="handle" value="@yuval_770 · YUV.AI" oninput="draw()"></div>
    </div>
    <label><input type="checkbox" id="guide" onchange="draw()"> Show 3:4 grid-crop guide</label>
    <button class="ghost" onclick="demo()">Load demo (no photo)</button>
    <button onclick="exportPNG(1920)">⬇ Export 1080×1920 PNG</button>
    <button class="ghost" onclick="exportPNG(1350)">⬇ Export 1080×1350 (grid crop)</button>
  </div>

  <div id="paneP" class="hide">
    <label>Engine</label>
    <select id="eng"><option>Midjourney v7</option><option>Flux / Leonardo</option><option>Nano Banana 2 (best text)</option></select>
    <label>Series</label><select id="pSeries"><option>HYPE</option><option>CINEMA</option></select>
    <label>Subject</label><input type="text" id="pSub" value="a charismatic Israeli tech creator, short dark hair, black t-shirt with a colorful phoenix print">
    <label>Action</label><input type="text" id="pAct" value="leaping mid-air reaching toward the camera">
    <label>Environment</label><input type="text" id="pEnv" value="outdoor rooftop against a vivid blue sky with palm trees">
    <label>Foreground depth prop</label><input type="text" id="pProp" value="a glowing smartphone flying huge in the blurred foreground">
    <div class="row">
      <div><label>Big word 1</label><input type="text" id="pW1" value="STEAL MY"></div>
      <div><label>Big word 2</label><input type="text" id="pW2" value="PROMPTS"></div>
    </div>
    <label>Ticker words</label><input type="text" id="pTick" value="ALL DAY,EVERY PLAY,NO LIMITS">
    <button onclick="genPrompt()">Generate prompt</button>
    <label>Result</label><textarea id="pOut"></textarea>
    <button class="ghost" onclick="navigator.clipboard.writeText(document.getElementById('pOut').value)">Copy</button>
    <small>Pro move: generate the scene WITHOUT text in MJ/Flux, remove bg (hyperframes remove-background), then set the type here in the Studio — pixel-perfect Hebrew/English every time. Nano Banana 2 renders text accurately if you keep it.</small>
  </div>
</div>
<div id="stage"><canvas id="cv" width="1080" height="1920"></canvas></div>
<script>
const ACC={yellow:"#E9FF3D",white:"#FFFFFF",pink:"#FF1464",cyan:"#00E5FF"};
const BGS={sky:["#1557C9","#2E8BE8","#8FD2FF"],sunset:["#2A1860","#B43A8E","#FF8A5C"],ink:["#181826","#0A0A0F","#0A0A0F"]};
const cv=document.getElementById("cv"),X=cv.getContext("2d");
const S={bg:null,cut:null,preset:"sky"};
const logo=new Image();logo.src="data:image/png;base64,__LOGO__";logo.onload=()=>draw();
const $=id=>document.getElementById(id);
const heb=t=>/[֐-׿]/.test(t);
function tab(t){$("paneS").classList.toggle("hide",t!="S");$("paneP").classList.toggle("hide",t!="P");$("tabS").classList.toggle("on",t=="S");$("tabP").classList.toggle("on",t=="P");}
function loadImg(inp,key){const f=inp.files[0];if(!f)return;const img=new Image();img.onload=()=>{S[key]=img;draw();};img.src=URL.createObjectURL(f);}
function applyPreset(){S.preset=$("preset").value;if(S.preset=="cinema"){$("c1").value="white";$("c2").value="white";}else{$("c1").value="yellow";$("c2").value="yellow";}draw();}
function demo(){S.bg=null;S.cut=null;draw();}
function coverFit(img,W,H){const r=Math.max(W/img.width,H/img.height);return[(W-img.width*r)/2,(H-img.height*r)/2,img.width*r,img.height*r];}
function star4(c,x,y,r){c.beginPath();c.moveTo(x,y-r);c.lineTo(x+r*.3,y-r*.3);c.lineTo(x+r,y);c.lineTo(x+r*.3,y+r*.3);c.lineTo(x,y+r);c.lineTo(x-r*.3,y+r*.3);c.lineTo(x-r,y);c.lineTo(x-r*.3,y-r*.3);c.closePath();c.fill();}
function ticker(c,y,words,color){const ws=words.split(",").map(w=>w.trim()).filter(Boolean);if(!ws.length)return;
 c.font="800 27px Arial";c.fillStyle=color;c.textBaseline="middle";let seq=[];for(let r=0;r<6;r++)ws.forEach(w=>seq.push(w));
 let tot=0;seq.forEach(w=>tot+=c.measureText(w.toUpperCase()).width+58);let x=(1080-Math.min(tot,2200))/2;if(x>0)x=-(tot-1080)/2;x=540-tot/2;
 c.save();c.beginPath();c.rect(0,y-26,1080,52);c.clip();c.textAlign="left";
 seq.forEach(w=>{c.fillText(w.toUpperCase().split("").join(String.fromCharCode(8202)),x,y);x+=c.measureText(w.toUpperCase()).width+18;star4(c,x+11,y,9);x+=40;});c.restore();}
function bigLine(c,t,y,color){if(!t)return;const h=heb(t);const fam=h?"900 SZpx RubikX":"400 SZpx AntonX";let s=300;
 c.font=fam.replace("SZ",s);while(c.measureText(t.toUpperCase()).width>1004&&s>60){s-=6;c.font=fam.replace("SZ",s);}
 c.save();c.translate(540,y);c.transform(1,0,Math.tan((h?-6:-8)*Math.PI/180),1,0,0);
 c.fillStyle=color;c.textAlign="center";c.textBaseline="top";c.shadowColor="rgba(0,0,0,.35)";c.shadowBlur=40;c.shadowOffsetY=10;
 if(h)c.direction="rtl";c.fillText(t.toUpperCase(),0,0);c.restore();}
function draw(){
 const W=1080,H=1920,cine=S.preset=="cinema";X.clearRect(0,0,W,H);X.direction="ltr";
 // bg
 if(S.bg){X.save();if(cine){X.filter="saturate(.8) contrast(1.1) brightness(.5) blur(24px)";const[x,y,w,h]=coverFit(S.bg,W,H);X.drawImage(S.bg,x-w*.09,y-h*.09,w*1.18,h*1.18);}else{const[x,y,w,h]=coverFit(S.bg,W,H);X.drawImage(S.bg,x,y,w,h);}X.restore();}
 else{const g=X.createLinearGradient(0,0,0,H);const cs=BGS[cine?"ink":S.preset]||BGS.sky;g.addColorStop(0,cs[0]);g.addColorStop(.45,cs[1]);g.addColorStop(1,cs[2]);X.fillStyle=g;X.fillRect(0,0,W,H);}
 if(cine){X.save();X.globalCompositeOperation="screen";
  let g1=X.createRadialGradient(90,380,0,90,380,900);g1.addColorStop(0,"rgba(255,20,100,.55)");g1.addColorStop(1,"rgba(255,20,100,0)");X.fillStyle=g1;X.fillRect(0,0,W,H);
  let g2=X.createRadialGradient(1020,860,0,1020,860,900);g2.addColorStop(0,"rgba(0,229,255,.5)");g2.addColorStop(1,"rgba(0,229,255,0)");X.fillStyle=g2;X.fillRect(0,0,W,H);X.restore();
  X.fillStyle="rgba(0,0,0,.30)";X.fillRect(0,H-560,W,560);}
 // mid ticker (hype) + headlines (behind cutout)
 if(!cine)ticker(X,parseInt($("y2").value)-58,$("ticker").value,"rgba(255,255,255,.95)");
 bigLine(X,$("l1").value,parseInt($("y1").value),ACC[$("c1").value]);
 bigLine(X,$("l2").value,parseInt($("y2").value),ACC[$("c2").value]);
 // cutout
 if(S.cut){const hgt=H*parseInt($("cutH").value)/100;const w=S.cut.width*(hgt/S.cut.height);
  X.save();X.shadowColor="rgba(0,0,0,.6)";X.shadowBlur=46;X.shadowOffsetY=24;
  X.drawImage(S.cut,540-w/2+parseInt($("cutX").value),H-hgt,w,hgt);X.restore();}
 // front word
 const lf=$("lf").value;if(lf){const h=heb(lf);let s=parseInt($("sf").value);X.save();X.translate(540,parseInt($("yf").value));
  X.transform(1,0,Math.tan((h?-6:-8)*Math.PI/180),1,0,0);X.font=(h?"900 ":"400 ")+s+"px "+(h?"RubikX":"AntonX");
  X.fillStyle=ACC[$("c1").value=="white"?"pink":"white"];X.textAlign="center";X.textBaseline="top";
  X.shadowColor="rgba(0,0,0,.8)";X.shadowBlur=40;if(h)X.direction="rtl";X.fillText(lf.toUpperCase(),0,0);X.restore();X.direction="ltr";}
 // top ticker, stack, chrome
 ticker(X,283,$("ticker").value,"rgba(255,255,255,.92)");
 const st=$("stack").value.trim();if(st){const acc=cine?"#FFFFFF":ACC[$("c1").value];X.font="400 38px AntonX";X.textAlign="right";X.fillStyle=acc;X.textBaseline="top";
  st.split(",").map(w=>w.trim()).forEach((w,i)=>X.fillText(w.toUpperCase(),1016,1452-st.split(",").length*49+i*49));
  X.strokeStyle=acc;X.lineWidth=2;X.fillStyle=acc;
  star4(X,886,1480,14);X.beginPath();X.arc(936,1480,15,0,7);X.stroke();X.beginPath();X.ellipse(936,1480,6.5,15,0,0,7);X.stroke();
  X.beginPath();X.arc(986,1480,15,0,7);X.stroke();X.beginPath();X.arc(986,1480,8,0,7);X.stroke();X.beginPath();X.arc(986,1480,2.5,0,7);X.fill();}
 // chip + phoenix + handle
 X.font="700 29px 'Courier New',monospace";const tg=$("tag").value.toUpperCase();const tw=X.measureText(tg).width;
 X.fillStyle="rgba(8,8,12,.35)";X.strokeStyle="rgba(255,255,255,.9)";X.lineWidth=2;
 roundRect(X,64,372,tw+44,52,26);X.fill();X.stroke();X.fillStyle="#fff";X.textAlign="left";X.textBaseline="middle";X.fillText(tg,86,399);
 if(logo.complete)X.drawImage(logo,1080-64-92,358,92,92);
 X.font="600 26px 'Courier New',monospace";X.fillStyle="rgba(255,255,255,.85)";X.textAlign="center";X.shadowColor="rgba(0,0,0,.8)";X.shadowBlur=10;X.fillText($("handle").value,540,1576);X.shadowBlur=0;
 // vignette
 const v=X.createRadialGradient(540,860,500,540,860,1300);v.addColorStop(0,"rgba(0,0,0,0)");v.addColorStop(1,"rgba(0,0,0,.38)");X.fillStyle=v;X.fillRect(0,0,W,H);
 if($("guide").checked){X.strokeStyle="rgba(255,255,255,.5)";X.setLineDash([14,10]);X.strokeRect(0,285,1080,1350);X.setLineDash([]);}
}
function roundRect(c,x,y,w,h,r){c.beginPath();c.moveTo(x+r,y);c.arcTo(x+w,y,x+w,y+h,r);c.arcTo(x+w,y+h,x,y+h,r);c.arcTo(x,y+h,x,y,r);c.arcTo(x,y,x+w,y,r);c.closePath();}
function exportPNG(h){const guide=$("guide").checked;$("guide").checked=false;draw();
 let out=cv;if(h==1350){out=document.createElement("canvas");out.width=1080;out.height=1350;out.getContext("2d").drawImage(cv,0,285,1080,1350,0,0,1080,1350);}
 out.toBlob(b=>{const a=document.createElement("a");a.href=URL.createObjectURL(b);a.download="yuv-cover-"+($("l2").value||$("l1").value||"x").replace(/\s+/g,"-")+(h==1350?"_4x5":"")+".png";a.click();
 $("guide").checked=guide;draw();});}
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
document.fonts.ready.then(draw);draw();
</script></body></html>'''

html = (HTML.replace("__ANTON__", b64("fonts/Anton-Regular.woff2"))
            .replace("__RUBIK__", b64("fonts/Rubik-900.woff2"))
            .replace("__LOGO__", b64("assets/logo-phoenix.png")))
open("cover-studio.html", "w", encoding="utf-8").write(html)
print("cover-studio.html written:", round(len(html)/1024), "KB")
