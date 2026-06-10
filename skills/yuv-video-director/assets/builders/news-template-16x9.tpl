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
      html,body{width:1920px;height:1080px;overflow:hidden;background:var(--ink);font-family:"Inter",sans-serif;}
      #net{position:absolute;inset:0;z-index:0;}
      #mvid{position:absolute;inset:0;width:1920px;height:1080px;object-fit:cover;z-index:5;}
      .grad{background:var(--phx);background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;}
      .display{font-family:"Anton";text-transform:uppercase;letter-spacing:0;line-height:0.9;}

      /* broadcast name-super (top-left, personal brand) */
      #nsuper{position:absolute;left:60px;top:120px;z-index:18;display:flex;flex-direction:column;gap:6px;}
      #nsuper .row{display:flex;align-items:center;gap:16px;}
      #nsuper img{width:64px;filter:drop-shadow(0 0 10px rgba(255,20,100,.4));}
      #nsuper .nm{direction:rtl;font-family:"Rubik";font-weight:900;font-size:58px;color:#fff;line-height:1;text-shadow:0 2px 18px rgba(0,0,0,.7);}
      #nsuper .ti{direction:rtl;font-family:"Rubik";font-weight:700;font-size:27px;color:var(--cyan);text-shadow:0 2px 14px rgba(0,0,0,.8);}
      #acc{width:380px;height:62px;margin-top:-4px;}

      /* karaoke captions — centered via margin (no transform), 2-line safe, lower */
      .cap{position:absolute;left:0;right:0;bottom:38px;margin:0 auto;width:max-content;max-width:1480px;z-index:20;direction:rtl;
        font-family:"Rubik",sans-serif;font-weight:900;font-size:46px;line-height:1.28;text-align:center;
        background:rgba(8,8,12,.86);border:1px solid rgba(0,229,255,.4);border-right:6px solid var(--pink);
        padding:13px 32px;box-shadow:0 10px 34px rgba(0,0,0,.6);}
      .cap span{color:rgba(255,255,255,.5);}

      /* director-timed TRANSPARENT lottie overlays — float directly on the footage */
      .illu{position:absolute;z-index:18;filter:drop-shadow(0 12px 30px rgba(0,0,0,.78));}
      .illu-lot{width:100%;height:100%;}
      .illu-lab{position:absolute;left:-70px;right:-70px;top:100%;margin-top:8px;direction:rtl;font-family:"Rubik";font-weight:700;font-size:25px;color:#fff;text-align:center;text-shadow:0 2px 12px rgba(0,0,0,.95),0 0 20px rgba(0,229,255,.35);white-space:nowrap;}

      /* outro */
      #ec{position:absolute;inset:0;z-index:30;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}
      #burst{position:absolute;left:50%;top:40%;width:760px;height:760px;margin-left:-380px;margin-top:-380px;z-index:-1;}
      #ec .logo{width:180px;filter:drop-shadow(0 0 22px rgba(255,20,100,.5)) drop-shadow(0 0 50px rgba(0,229,255,.3));}
      #ec .nm{direction:rtl;font-family:"Rubik";font-weight:900;font-size:96px;color:#fff;margin-top:14px;}
      #ec .sign{font-size:64px;margin-top:4px;}
      #ec .cred{direction:rtl;font-family:"Rubik";font-weight:700;font-size:30px;color:var(--cyan);margin-top:14px;}
      #ec .links{font-family:"JetBrains Mono";font-size:27px;letter-spacing:2px;color:#fff;margin-top:18px;}
      #ec .handles{font-family:"JetBrains Mono";font-size:21px;letter-spacing:2px;color:rgba(255,255,255,.72);margin-top:10px;}

      #grain{position:absolute;inset:0;z-index:40;opacity:.05;pointer-events:none;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/></filter><rect width='160' height='160' filter='url(%23n)'/></svg>");}
      #vig{position:absolute;inset:0;z-index:41;pointer-events:none;background:radial-gradient(ellipse 82% 82% at 50% 50%,transparent 60%,rgba(0,0,0,.42) 100%);}
      #dip{position:absolute;inset:0;z-index:50;opacity:0;pointer-events:none;background:var(--ink);}
      #fade{position:absolute;inset:0;z-index:60;opacity:0;pointer-events:none;background:var(--ink);}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="31.3" data-width="1920" data-height="1080">
      <canvas id="net" width="1920" height="1080"></canvas>

      <video id="mvid" class="clip" data-start="0" data-duration="26.3" data-media-start="124.3" data-track-index="0" src="source.mp4" muted playsinline crossorigin="anonymous"></video>
      <audio id="news-audio" class="clip" data-start="0" data-duration="26.3" data-media-start="124.3" data-track-index="2" data-volume="1" src="source.mp4"></audio>
      <audio id="music" class="clip" data-start="0" data-duration="31.3" data-track-index="9" data-volume="0.15" src="music.wav"></audio>

      <div id="nsuper" class="clip" data-start="1.0" data-duration="5.4" data-track-index="15">
        <div class="row"><img src="assets/logo-phoenix.png" crossorigin="anonymous" alt="" /><div class="nm">יובל אבידני</div></div>
        <div class="ti">מומחה AI · פינת ה-AI בחדשות 12</div>
        <div id="acc"></div>
      </div>

      @@ILLU_HTML@@

      @@CAPS_HTML@@

      <div id="ec" class="clip" data-start="26.3" data-duration="5.0" data-track-index="4">
        <div id="burst"></div>
        <img class="logo" src="assets/logo-phoenix.png" crossorigin="anonymous" alt="" />
        <div class="nm">יובל אבידני</div>
        <div class="sign display grad">LET'S FLY HIGH</div>
        <div class="cred">מומחה AI · פינת ה-AI בחדשות 12</div>
        <div class="links">yuv.ai&nbsp;&nbsp;·&nbsp;&nbsp;linktr.ee/yuvai</div>
        <div class="handles">X @yuvalav&nbsp;·&nbsp;IG @yuval_770&nbsp;·&nbsp;TikTok @yuval.ai&nbsp;·&nbsp;YT @yuv-ai&nbsp;·&nbsp;GitHub @hoodini</div>
      </div>

      <div id="grain"></div><div id="vig"></div><div id="dip"></div><div id="fade"></div>
    </div>

    <script>
      const cv=document.getElementById("net"),ctx=cv.getContext("2d");
      function mul(a){return function(){a|=0;a=(a+0x6d2b79f5)|0;let t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
      const rnd=mul(20260609);
      const STOPS=[[249,173,69],[240,102,78],[222,96,146],[124,58,237],[78,125,183],[0,229,255]];
      function col(u){u=Math.max(0,Math.min(0.999,u));const s=u*(STOPS.length-1),i=Math.floor(s),f=s-i,a=STOPS[i],b=STOPS[i+1];return[(a[0]+(b[0]-a[0])*f)|0,(a[1]+(b[1]-a[1])*f)|0,(a[2]+(b[2]-a[2])*f)|0];}
      const Np=60,nodes=[];
      for(let i=0;i<Np;i++){let x,y,u;if(i<20){const a=rnd();x=840-a*640+(rnd()-0.5)*70;y=470-a*300+(rnd()-0.5)*130;u=a*0.26;}else if(i<40){const a=rnd();x=1080+a*640+(rnd()-0.5)*70;y=470-a*300+(rnd()-0.5)*130;u=0.74+a*0.26;}else{const a=rnd();x=960+(rnd()-0.5)*200;y=360+a*440+(rnd()-0.5)*70;u=0.30+a*0.42;}nodes.push({x,y,seed:rnd()*6.2832,u});}
      function net(t,g){ctx.clearRect(0,0,1920,1080);for(const n of nodes){n.px=n.x+Math.sin(t*0.5+n.seed)*15;n.py=n.y+Math.cos(t*0.4+n.seed)*15;}ctx.lineWidth=1;for(let i=0;i<Np;i++)for(let j=i+1;j<Np;j++){const a=nodes[i],b=nodes[j],d=Math.hypot(a.px-b.px,a.py-b.py);if(d>150)continue;ctx.strokeStyle="rgba(170,195,255,"+(0.16*(1-d/150)*g).toFixed(3)+")";ctx.beginPath();ctx.moveTo(a.px,a.py);ctx.lineTo(b.px,b.py);ctx.stroke();}for(const n of nodes){const c=col(n.u);ctx.globalAlpha=g;ctx.fillStyle="rgb("+c[0]+","+c[1]+","+c[2]+")";ctx.shadowColor=ctx.fillStyle;ctx.shadowBlur=10;ctx.beginPath();ctx.arc(n.px,n.py,2.4,0,6.2832);ctx.fill();}ctx.globalAlpha=1;ctx.shadowBlur=0;}
      net(0,1);

      window.__hfLottie=window.__hfLottie||[];
      const L=(id,p)=>window.__hfLottie.push(lottie.loadAnimation({container:document.getElementById(id),renderer:"svg",loop:true,autoplay:false,path:p}));
      L("acc","assets/name-accent.json"); L("burst","assets/phoenix-burst.json");

      window.__timelines=window.__timelines||{};
      const tl=gsap.timeline({paused:true});
      const D=31.3,proxy={t:0};
      // field: hidden under footage, ignites for the outro
      tl.to(proxy,{t:D,duration:D,ease:"none",onUpdate:()=>{const g=proxy.t<25.8?0:Math.min(1,(proxy.t-25.8)/1.2);net(proxy.t,g);}},0);
      tl.to("#ec .grad",{backgroundPositionX:"-200%",duration:6,ease:"none"},26);

      // name-super in + out (broadcast lower-third)
      tl.from("#nsuper .row",{x:-40,opacity:0,duration:0.6,ease:"power3.out"},1.1);
      tl.from("#nsuper .ti",{x:-30,opacity:0,duration:0.5,ease:"power2.out"},1.35);
      tl.to("#nsuper",{opacity:0,duration:0.5,ease:"power1.in"},5.6);
      // concept illustrations (fire in sync with the spoken terms)
      @@ILLU_JS@@

      // captions (karaoke)
      @@CAPS_JS@@

      // clean dip-to-ink transition footage -> outro
      tl.to("#dip",{opacity:0.92,duration:0.28,ease:"power2.in"},26.0);
      tl.to("#dip",{opacity:0,duration:0.5,ease:"power2.out"},26.45);

      // outro
      tl.from("#burst",{scale:0.3,opacity:0,duration:0.8,ease:"power3.out"},26.4);
      tl.from("#ec .logo",{scale:0.6,opacity:0,duration:0.7,ease:"back.out(1.6)"},26.45);
      tl.from("#ec .nm",{y:30,opacity:0,duration:0.6,ease:"power3.out"},26.8);
      tl.from("#ec .sign",{y:24,opacity:0,duration:0.6,ease:"power3.out"},27.1);
      tl.from("#ec .cred",{opacity:0,y:16,duration:0.5},27.4);
      tl.from("#ec .links",{opacity:0,y:16,duration:0.5},27.65);
      tl.from("#ec .handles",{opacity:0,y:14,duration:0.5},27.9);

      tl.to("#fade",{opacity:1,duration:0.55,ease:"power2.in"},D-0.55);
      window.__timelines["main"]=tl;
    </script>
  </body>
</html>
