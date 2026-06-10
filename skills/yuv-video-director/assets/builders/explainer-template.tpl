<!doctype html>
<html lang="he">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js"></script>
    <style>
      @font-face{font-family:"Anton";font-weight:400;src:url("fonts/Anton-Regular.woff2") format("woff2");}
      @font-face{font-family:"Rubik";font-weight:900;src:url("fonts/Rubik-900.woff2") format("woff2");}
      @font-face{font-family:"Rubik";font-weight:700;src:url("fonts/Rubik-700.woff2") format("woff2");}
      :root{--pink:#FF1464;--cyan:#00E5FF;--ink:#0A0A0A;--phx:linear-gradient(100deg,#F9AD45,#F0664E,#DE6092,#FF1464,#8B459A,#7C3AED,#4E7DB7,#00E5FF,#F9AD45);}
      *{margin:0;padding:0;box-sizing:border-box;}
      html,body{width:1920px;height:1080px;overflow:hidden;background:var(--ink);font-family:"Rubik",sans-serif;}
      #net{position:absolute;inset:0;z-index:0;}
      #mvid{position:absolute;inset:0;width:1920px;height:1080px;object-fit:cover;z-index:5;}
      .grad{background:var(--phx);background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;}
      .scene{position:absolute;inset:0;z-index:10;}
      .sc{position:relative;width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:80px 150px;box-sizing:border-box;direction:rtl;}
      .eyebrow{font-family:"JetBrains Mono",monospace;font-size:24px;letter-spacing:6px;color:var(--cyan);direction:ltr;}

      /* S1 hook */
      #s1 .title{font-weight:900;font-size:128px;color:#fff;line-height:1.08;margin-top:26px;text-shadow:0 4px 30px rgba(0,0,0,.6);}
      #s1 .title em{font-style:normal;color:var(--pink);text-shadow:0 0 24px rgba(255,20,100,.55);}
      #s1 .sub{font-weight:700;font-size:42px;color:var(--cyan);margin-top:22px;}
      #s1 .spark{width:200px;height:200px;}

      /* S2 brain */
      #s2 .sc{flex-direction:row;gap:90px;justify-content:center;align-items:center;}
      #s2 .lot{width:560px;height:560px;filter:drop-shadow(0 14px 34px rgba(0,0,0,.7));}
      #s2 .tx{display:flex;flex-direction:column;gap:26px;text-align:right;max-width:760px;}
      #s2 .h{font-weight:900;font-size:96px;line-height:1.05;}
      #s2 .l{font-weight:700;font-size:46px;color:rgba(255,255,255,.92);}
      #s2 .l b{color:var(--cyan);font-weight:900;}

      /* manim captions */
      .mcap{position:absolute;left:0;right:0;bottom:64px;margin:0 auto;width:max-content;max-width:1560px;z-index:20;direction:rtl;
        font-family:"Rubik";font-weight:900;font-size:46px;line-height:1.3;text-align:center;color:#fff;
        background:rgba(8,8,12,.84);border:1px solid rgba(0,229,255,.4);border-right:6px solid var(--pink);
        padding:14px 34px;box-shadow:0 10px 36px rgba(0,0,0,.6);}
      .mcap em{font-style:normal;color:var(--pink);}

      /* S5 results */
      #s5 .h{font-weight:900;font-size:96px;margin-bottom:60px;}
      #s5 .row{display:flex;gap:36px;direction:rtl;}
      #s5 .card{width:420px;padding:46px 30px;background:#101018;border-top:6px solid;box-shadow:0 14px 40px rgba(0,0,0,.5);}
      #s5 .card .t{font-weight:900;font-size:48px;color:#fff;line-height:1.15;}
      #s5 .card .d{font-weight:700;font-size:28px;color:rgba(255,255,255,.7);margin-top:14px;}
      #s5 .orb{position:absolute;left:90px;top:120px;width:300px;height:300px;filter:drop-shadow(0 12px 30px rgba(0,0,0,.7));}

      /* S6 punch */
      #s6 .lot{width:760px;height:522px;filter:drop-shadow(0 14px 36px rgba(0,0,0,.75));}
      #s6 .q1{font-weight:900;font-size:76px;color:#fff;margin-top:8px;}
      #s6 .q2{font-weight:900;font-size:88px;color:var(--pink);text-shadow:0 0 26px rgba(255,20,100,.55);margin-top:10px;}

      /* S7 outro */
      #burst{position:absolute;left:50%;top:38%;width:760px;height:760px;margin-left:-380px;margin-top:-380px;z-index:-1;}
      #s7 .logo{width:190px;filter:drop-shadow(0 0 24px rgba(255,20,100,.5)) drop-shadow(0 0 54px rgba(0,229,255,.3));}
      #s7 .nm{font-weight:900;font-size:104px;color:#fff;margin-top:14px;}
      #s7 .sign{font-family:"Anton";text-transform:uppercase;letter-spacing:0;font-size:66px;margin-top:6px;}
      #s7 .cred{font-weight:700;font-size:32px;color:var(--cyan);margin-top:16px;}
      #s7 .links{font-family:"JetBrains Mono",monospace;font-size:28px;letter-spacing:2px;color:#fff;margin-top:20px;direction:ltr;}
      #s7 .handles{font-family:"JetBrains Mono",monospace;font-size:21px;letter-spacing:2px;color:rgba(255,255,255,.72);margin-top:10px;direction:ltr;}

      #grain{position:absolute;inset:0;z-index:40;opacity:.05;pointer-events:none;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/></filter><rect width='160' height='160' filter='url(%23n)'/></svg>");}
      #vig{position:absolute;inset:0;z-index:41;pointer-events:none;background:radial-gradient(ellipse 82% 82% at 50% 50%,transparent 58%,rgba(0,0,0,.44) 100%);}
      #dip{position:absolute;inset:0;z-index:50;opacity:0;pointer-events:none;background:var(--ink);}
      #fade{position:absolute;inset:0;z-index:60;opacity:0;pointer-events:none;background:var(--ink);}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="@@D@@" data-width="1920" data-height="1080">
      <canvas id="net" width="1920" height="1080"></canvas>
      <audio id="music" class="clip" data-start="0" data-duration="@@D@@" data-track-index="9" data-volume="0.17" src="music.wav"></audio>

      <!-- S1 HOOK -->
      <div id="s1" class="scene clip" data-start="0" data-duration="5.0" data-track-index="1">
        <div class="sc">
          <div id="spark1" class="spark"></div>
          <div class="eyebrow">YUV.AI · EXPLAINER</div>
          <div class="title">איך מכונה <em>לומדת</em> לחשוב?</div>
          <div class="sub">רשתות נוירונים — ההסבר הפשוט</div>
        </div>
      </div>

      <!-- S2 BRAIN -->
      <div id="s2" class="scene clip" data-start="5.0" data-duration="8.0" data-track-index="2">
        <div class="sc">
          <div class="tx">
            <div class="h grad">הכול מתחיל במוח</div>
            <div class="l">בראש שלנו: <b>כ-86 מיליארד</b> נוירונים</div>
            <div class="l">כל למידה = <b>חיבורים שמתחזקים</b></div>
          </div>
          <div id="brainlot" class="lot"></div>
        </div>
      </div>

      <!-- MANIM BODY -->
      <video id="mvid" class="clip" data-start="13.0" data-duration="@@DM@@" data-track-index="0" src="assets/WhatIsNN.mp4" muted playsinline crossorigin="anonymous"></video>
      @@MCAPS_HTML@@

      <!-- S5 RESULTS -->
      <div id="s5" class="scene clip" data-start="@@S5@@" data-duration="8.0" data-track-index="3">
        <div class="sc">
          <div class="h grad">מה זה נותן לנו?</div>
          <div class="row">
            <div class="card" style="border-color:#FF1464"><div class="t">זיהוי תמונות</div><div class="d">רואה — ומבינה מה בתמונה</div></div>
            <div class="card" style="border-color:#00E5FF"><div class="t">תרגום בזמן אמת</div><div class="d">שפה נכנסת, שפה יוצאת</div></div>
            <div class="card" style="border-color:#F9AD45"><div class="t">שיחה טבעית</div><div class="d">מבינה אותך — ועונה</div></div>
          </div>
          <div id="orblot" class="orb"></div>
        </div>
      </div>

      <!-- S6 PUNCH -->
      <div id="s6" class="scene clip" data-start="@@S6@@" data-duration="6.0" data-track-index="4">
        <div class="sc">
          <div id="ghostlot" class="lot"></div>
          <div class="q1">והקסם האמיתי?</div>
          <div class="q2">היא לומדת לזהות גם מה שלא נאמר.</div>
        </div>
      </div>

      <!-- S7 OUTRO -->
      <div id="s7" class="scene clip" data-start="@@S7@@" data-duration="6.0" data-track-index="5">
        <div class="sc">
          <div id="burst"></div>
          <img class="logo" src="assets/logo-phoenix.png" crossorigin="anonymous" alt="" />
          <div class="nm">יובל אבידני</div>
          <div class="sign grad">LET'S FLY HIGH</div>
          <div class="cred">מומחה AI · פינת ה-AI בחדשות 12</div>
          <div class="links">yuv.ai · linktr.ee/yuvai</div>
          <div class="handles">X @yuvalav · IG @yuval_770 · TikTok @yuval.ai · YT @yuv-ai · GitHub @hoodini</div>
        </div>
      </div>

      <div id="grain"></div><div id="vig"></div><div id="dip"></div><div id="fade"></div>
    </div>

    <script>
      const cv=document.getElementById("net"),ctx=cv.getContext("2d");
      function mul(a){return function(){a|=0;a=(a+0x6d2b79f5)|0;let t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
      const rnd=mul(20260609);
      const STOPS=[[249,173,69],[240,102,78],[222,96,146],[124,58,237],[78,125,183],[0,229,255]];
      function col(u){u=Math.max(0,Math.min(0.999,u));const s=u*(STOPS.length-1),i=Math.floor(s),f=s-i,a=STOPS[i],b=STOPS[i+1];return[(a[0]+(b[0]-a[0])*f)|0,(a[1]+(b[1]-a[1])*f)|0,(a[2]+(b[2]-a[2])*f)|0];}
      const Np=64,nodes=[];
      for(let i=0;i<Np;i++){let x,y,u;if(i<22){const a=rnd();x=840-a*640+(rnd()-0.5)*70;y=470-a*300+(rnd()-0.5)*130;u=a*0.26;}else if(i<44){const a=rnd();x=1080+a*640+(rnd()-0.5)*70;y=470-a*300+(rnd()-0.5)*130;u=0.74+a*0.26;}else{const a=rnd();x=960+(rnd()-0.5)*200;y=360+a*440+(rnd()-0.5)*70;u=0.30+a*0.42;}nodes.push({x,y,seed:rnd()*6.2832,u});}
      function drawNet(t){ctx.clearRect(0,0,1920,1080);for(const n of nodes){n.px=n.x+Math.sin(t*0.5+n.seed)*15;n.py=n.y+Math.cos(t*0.4+n.seed)*15;}ctx.lineWidth=1;for(let i=0;i<Np;i++)for(let j=i+1;j<Np;j++){const a=nodes[i],b=nodes[j],d=Math.hypot(a.px-b.px,a.py-b.py);if(d>150)continue;ctx.strokeStyle="rgba(170,195,255,"+(0.17*(1-d/150)).toFixed(3)+")";ctx.beginPath();ctx.moveTo(a.px,a.py);ctx.lineTo(b.px,b.py);ctx.stroke();}for(const n of nodes){const c=col(n.u);ctx.fillStyle="rgb("+c[0]+","+c[1]+","+c[2]+")";ctx.shadowColor=ctx.fillStyle;ctx.shadowBlur=10;ctx.beginPath();ctx.arc(n.px,n.py,2.5,0,6.2832);ctx.fill();}ctx.shadowBlur=0;}
      drawNet(0);

      window.__hfLottie=window.__hfLottie||[];
      // seek-modulo wrapper: sections start past the lottie's own duration, so wrap the
      // adapter's goToAndStop(ms) to loop deterministically instead of clamping at the end
      const L=(id,p)=>{
        const a=lottie.loadAnimation({container:document.getElementById(id),renderer:"svg",loop:true,autoplay:false,path:p});
        const o=a.goToAndStop.bind(a);
        a.goToAndStop=(v,f)=>{const d=a.getDuration(false)*1000;o(f?v:(d>0?v%d:v),f);};
        window.__hfLottie.push(a);
      };
      L("spark1","assets/c-magic.json"); L("brainlot","assets/brain-fire.json"); L("orblot","assets/c-ai.json"); L("ghostlot","assets/ghost-line.json"); L("burst","assets/phoenix-burst.json");

      window.__timelines=window.__timelines||{};
      const tl=gsap.timeline({paused:true});
      const D=@@D@@,proxy={t:0};
      tl.to(proxy,{t:D,duration:D,ease:"none",onUpdate:()=>drawNet(proxy.t)},0);
      tl.to(".grad",{backgroundPositionX:"-200%",duration:D,ease:"none"},0);

      // S1
      tl.from("#spark1",{scale:0.5,opacity:0,duration:0.6,ease:"back.out(1.6)"},0.25);
      tl.from("#s1 .eyebrow",{opacity:0,y:18,duration:0.5,ease:"power2.out"},0.45);
      tl.from("#s1 .title",{opacity:0,y:50,duration:0.8,ease:"power4.out"},0.65);
      tl.from("#s1 .sub",{opacity:0,y:24,duration:0.6,ease:"power2.out"},1.15);
      // S2
      tl.from("#s2 .h",{opacity:0,x:60,duration:0.7,ease:"power3.out"},5.3);
      tl.from("#s2 .l",{opacity:0,x:40,duration:0.6,stagger:0.25,ease:"power2.out"},5.7);
      tl.from("#brainlot",{opacity:0,scale:0.7,duration:0.7,ease:"back.out(1.5)"},5.5);
      // manim captions
      @@MCAPS_JS@@
      // S5
      tl.from("#s5 .h",{opacity:0,y:40,duration:0.6,ease:"power3.out"},@@S5@@+0.25);
      tl.from("#s5 .card",{opacity:0,y:70,duration:0.55,stagger:0.16,ease:"back.out(1.4)"},@@S5@@+0.6);
      tl.from("#orblot",{opacity:0,scale:0.5,duration:0.6,ease:"back.out(1.6)"},@@S5@@+1.0);
      // S6
      tl.from("#ghostlot",{opacity:0,scale:0.72,duration:0.6,ease:"back.out(1.5)"},@@S6@@+0.25);
      tl.from("#s6 .q1",{opacity:0,y:30,duration:0.6,ease:"power3.out"},@@S6@@+0.9);
      tl.from("#s6 .q2",{opacity:0,y:30,duration:0.7,ease:"power3.out"},@@S6@@+1.5);
      // S7
      tl.from("#burst",{scale:0.3,opacity:0,duration:0.8,ease:"power3.out"},@@S7@@+0.15);
      tl.from("#s7 .logo",{scale:0.6,opacity:0,duration:0.7,ease:"back.out(1.6)"},@@S7@@+0.2);
      tl.from("#s7 .nm",{y:34,opacity:0,duration:0.6,ease:"power3.out"},@@S7@@+0.55);
      tl.from("#s7 .sign",{y:24,opacity:0,duration:0.6,ease:"power3.out"},@@S7@@+0.85);
      tl.from("#s7 .cred",{opacity:0,y:16,duration:0.5},@@S7@@+1.15);
      tl.from("#s7 .links",{opacity:0,y:16,duration:0.5},@@S7@@+1.4);
      tl.from("#s7 .handles",{opacity:0,y:14,duration:0.5},@@S7@@+1.65);

      // clean dip transitions at section boundaries
      [13.0,@@S5@@,@@S6@@,@@S7@@].forEach((b)=>{
        tl.to("#dip",{opacity:0.9,duration:0.24,ease:"power2.in",overwrite:"auto"},b-0.26);
        tl.to("#dip",{opacity:0,duration:0.42,ease:"power2.out",overwrite:"auto"},b+0.02);
      });
      tl.to("#fade",{opacity:1,duration:0.6,ease:"power2.in"},D-0.6);
      window.__timelines["main"]=tl;
    </script>
  </body>
</html>
