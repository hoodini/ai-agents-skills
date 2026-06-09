/*
 * YUV.AI neural-net phoenix field — deterministic, SEEKABLE canvas background.
 * Drive it from a GSAP proxy so HyperFrames renders it frame-accurately:
 *
 *   const proxy = { t: 0 };
 *   tl.to(proxy, { t: DURATION, ease: "none", onUpdate: () => drawNet(proxy.t) }, 0);
 *   drawNet(0);  // initial frame
 *
 * Warm-left / cool-right gradient = the phoenix (amber wing -> pink/violet body -> cyan wing).
 * No Date.now()/Math.random() — seeded mulberry32 — so the same t always yields the same frame.
 * Requires a <canvas id="net" width="1920" height="1080"> on the page.
 */
const cv = document.getElementById("net"), ctx = cv.getContext("2d");

function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const rnd = mulberry32(20260609);
const STOPS = [[249,173,69],[240,102,78],[222,96,146],[124,58,237],[78,125,183],[0,229,255]];
function col(u) {
  u = Math.max(0, Math.min(0.999, u));
  const s = u * (STOPS.length - 1), i = Math.floor(s), f = s - i, a = STOPS[i], b = STOPS[i + 1];
  return [(a[0]+(b[0]-a[0])*f)|0, (a[1]+(b[1]-a[1])*f)|0, (a[2]+(b[2]-a[2])*f)|0];
}
const N = 74, nodes = [];
for (let i = 0; i < N; i++) {
  let x, y, u;
  if (i < 25) { const a = rnd(); x = 840 - a*640 + (rnd()-0.5)*70; y = 470 - a*300 + (rnd()-0.5)*130; u = a*0.26; }          // warm left wing
  else if (i < 50) { const a = rnd(); x = 1080 + a*640 + (rnd()-0.5)*70; y = 470 - a*300 + (rnd()-0.5)*130; u = 0.74 + a*0.26; } // cool right wing
  else { const a = rnd(); x = 960 + (rnd()-0.5)*200; y = 360 + a*440 + (rnd()-0.5)*70; u = 0.30 + a*0.42; }                       // body + tail
  nodes.push({ x, y, seed: rnd()*6.2832, u });
}
function drawNet(t) {
  ctx.clearRect(0, 0, 1920, 1080);
  for (const n of nodes) { n.px = n.x + Math.sin(t*0.5 + n.seed)*16; n.py = n.y + Math.cos(t*0.4 + n.seed)*16; }
  ctx.lineWidth = 1;
  for (let i = 0; i < N; i++) for (let j = i + 1; j < N; j++) {
    const a = nodes[i], b = nodes[j], d = Math.hypot(a.px-b.px, a.py-b.py);
    if (d > 158) continue;
    ctx.strokeStyle = "rgba(170,195,255," + (0.20*(1 - d/158)).toFixed(3) + ")";
    ctx.beginPath(); ctx.moveTo(a.px, a.py); ctx.lineTo(b.px, b.py); ctx.stroke();
  }
  for (const n of nodes) {
    const c = col(n.u);
    ctx.fillStyle = "rgb(" + c[0] + "," + c[1] + "," + c[2] + ")";
    ctx.shadowColor = ctx.fillStyle; ctx.shadowBlur = 12;
    ctx.beginPath(); ctx.arc(n.px, n.py, 3, 0, 6.2832); ctx.fill();
  }
  ctx.shadowBlur = 0;
}
