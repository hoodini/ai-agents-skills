<!doctype html>
<html lang="he">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js"></script>
    <style>
      @font-face{font-family:"Anton";font-weight:400;src:url("fonts/Anton-Regular.woff2") format("woff2");}
      @font-face{font-family:"Rubik";font-weight:900;src:url("fonts/Rubik-900.woff2") format("woff2");}
      @font-face{font-family:"Rubik";font-weight:700;src:url("fonts/Rubik-700.woff2") format("woff2");}
      :root{--pink:#FF1464;--cyan:#00E5FF;--ink:#0A0A0A;--phx:linear-gradient(100deg,#F9AD45,#F0664E,#DE6092,#FF1464,#8B459A,#7C3AED,#4E7DB7,#00E5FF,#F9AD45);}
      *{margin:0;padding:0;box-sizing:border-box;}
      html,body{width:1080px;height:1920px;overflow:hidden;background:var(--ink);font-family:"Inter",sans-serif;}
      #bg{position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 80% 55% at 50% 42%,#161622,#0A0A0F 70%);}
      #mvid{position:absolute;left:0;top:656px;width:1080px;height:607px;object-fit:cover;z-index:5;box-shadow:0 0 0 2px rgba(0,229,255,.35),0 18px 60px rgba(0,0,0,.6);}
      .grad{background:var(--phx);background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;}
      .display{font-family:"Anton";text-transform:uppercase;letter-spacing:0;line-height:0.92;}

      #nsuper{position:absolute;left:0;right:0;top:150px;z-index:18;display:flex;flex-direction:column;align-items:center;gap:6px;}
      #nsuper img{width:120px;filter:drop-shadow(0 0 14px rgba(255,20,100,.45));}
      #nsuper .nm{direction:rtl;font-family:"Rubik";font-weight:900;font-size:80px;color:#fff;line-height:1;margin-top:8px;}
      #nsuper .ti{direction:rtl;font-family:"Rubik";font-weight:700;font-size:34px;color:var(--cyan);}
      #acc{width:460px;height:74px;}

      .illu{position:absolute;z-index:18;filter:drop-shadow(0 14px 34px rgba(0,0,0,.8));}
      .illu-lot{width:100%;height:100%;}
      .illu-lab{position:absolute;left:-80px;right:-80px;top:100%;margin-top:10px;direction:rtl;font-family:"Rubik";font-weight:700;font-size:32px;color:#fff;text-align:center;text-shadow:0 2px 14px rgba(0,0,0,.95),0 0 22px rgba(0,229,255,.35);white-space:nowrap;}

      .cap{position:absolute;left:0;right:0;bottom:380px;margin:0 auto;width:max-content;max-width:980px;z-index:20;direction:rtl;
        font-family:"Rubik",sans-serif;font-weight:900;font-size:56px;line-height:1.3;text-align:center;
        background:rgba(8,8,12,.88);border:1px solid rgba(0,229,255,.4);border-right:7px solid var(--pink);
        padding:18px 34px;box-shadow:0 10px 40px rgba(0,0,0,.6);}
      .cap span{color:rgba(255,255,255,.5);}

      #ec{position:absolute;inset:0;z-index:30;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;}
      #burst{position:absolute;left:50%;top:40%;width:760px;height:760px;margin-left:-380px;margin-top:-380px;z-index:-1;}
      #ec .logo{width:240px;filter:drop-shadow(0 0 26px rgba(255,20,100,.5)) drop-shadow(0 0 60px rgba(0,229,255,.3));}
      #ec .nm{direction:rtl;font-family:"Rubik";font-weight:900;font-size:118px;color:#fff;margin-top:16px;}
      #ec .sign{font-size:88px;margin-top:6px;}
      #ec .cred{direction:rtl;font-family:"Rubik";font-weight:700;font-size:38px;color:var(--cyan);margin-top:18px;}
      #ec .links{font-family:"JetBrains Mono";font-size:34px;letter-spacing:2px;color:#fff;margin-top:22px;}
      #ec .handles{font-family:"JetBrains Mono";font-size:24px;letter-spacing:1px;color:rgba(255,255,255,.72);margin-top:16px;line-height:1.7;}

      #grain{position:absolute;inset:0;z-index:40;opacity:.05;pointer-events:none;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/></filter><rect width='160' height='160' filter='url(%23n)'/></svg>");}
      #vig{position:absolute;inset:0;z-index:41;pointer-events:none;background:radial-gradient(ellipse 95% 80% at 50% 50%,transparent 55%,rgba(0,0,0,.5) 100%);}
      #dip{position:absolute;inset:0;z-index:50;opacity:0;pointer-events:none;background:var(--ink);}
      #fade{position:absolute;inset:0;z-index:60;opacity:0;pointer-events:none;background:var(--ink);}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="31.3" data-width="1080" data-height="1920">
      <div id="bg"></div>
      <video id="mvid" class="clip" data-start="0" data-duration="26.3" data-media-start="124.3" data-track-index="0" src="source.mp4" muted playsinline crossorigin="anonymous"></video>
      <audio id="news-audio" class="clip" data-start="0" data-duration="26.3" data-media-start="124.3" data-track-index="2" data-volume="1" src="source.mp4"></audio>
      <audio id="music" class="clip" data-start="0" data-duration="31.3" data-track-index="9" data-volume="0.15" src="music.wav"></audio>

      <div id="nsuper" class="clip" data-start="1.0" data-duration="5.4" data-track-index="15">
        <img src="assets/logo-phoenix.png" crossorigin="anonymous" alt="" />
        <div class="nm">יובל אבידני</div>
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
        <div class="links">yuv.ai · linktr.ee/yuvai</div>
        <div class="handles">X @yuvalav · IG @yuval_770 · TikTok @yuval.ai<br>YT @yuv-ai · GitHub @hoodini</div>
      </div>

      <div id="grain"></div><div id="vig"></div><div id="dip"></div><div id="fade"></div>
    </div>

    <script>
      window.__hfLottie=window.__hfLottie||[];
      const L=(id,p)=>window.__hfLottie.push(lottie.loadAnimation({container:document.getElementById(id),renderer:"svg",loop:true,autoplay:false,path:p}));
      L("acc","assets/name-accent.json"); L("burst","assets/phoenix-burst.json");

      window.__timelines=window.__timelines||{};
      const tl=gsap.timeline({paused:true});
      const D=31.3;
      tl.to("#ec .grad",{backgroundPositionX:"-200%",duration:6,ease:"none"},26);
      tl.from("#mvid",{opacity:0,scale:0.94,duration:0.5,ease:"power2.out"},0.0);
      tl.from("#nsuper img",{scale:0.6,opacity:0,duration:0.6,ease:"back.out(1.6)"},1.1);
      tl.from("#nsuper .nm",{y:24,opacity:0,duration:0.5,ease:"power3.out"},1.35);
      tl.from("#nsuper .ti",{y:18,opacity:0,duration:0.45,ease:"power2.out"},1.6);
      tl.to("#nsuper",{opacity:0,duration:0.5,ease:"power1.in"},5.6);
      @@ILLU_JS@@

      @@CAPS_JS@@

      tl.to("#dip",{opacity:0.92,duration:0.28,ease:"power2.in"},26.0);
      tl.to("#dip",{opacity:0,duration:0.5,ease:"power2.out"},26.45);
      tl.from("#burst",{scale:0.3,opacity:0,duration:0.8,ease:"power3.out"},26.4);
      tl.from("#ec .logo",{scale:0.6,opacity:0,duration:0.7,ease:"back.out(1.6)"},26.45);
      tl.from("#ec .nm",{y:36,opacity:0,duration:0.6,ease:"power3.out"},26.8);
      tl.from("#ec .sign",{y:24,opacity:0,duration:0.6,ease:"power3.out"},27.1);
      tl.from("#ec .cred",{opacity:0,y:18,duration:0.5},27.4);
      tl.from("#ec .links",{opacity:0,y:18,duration:0.5},27.65);
      tl.from("#ec .handles",{opacity:0,y:16,duration:0.5},27.9);
      tl.to("#fade",{opacity:1,duration:0.55,ease:"power2.in"},D-0.55);
      window.__timelines["main"]=tl;
    </script>
  </body>
</html>
