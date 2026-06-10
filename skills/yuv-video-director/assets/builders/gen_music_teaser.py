"""46.3s TEASER bed: driving kick + bass hits on slams + risers into drops + quiet tension for the
cliffhanger + final swell. Synthesized, royalty-free, deterministic."""
import numpy as np, wave
sr = 44100
D = 46.3
n = int(sr * D)
t = np.arange(n) / sr
rng = np.random.default_rng(12)

def place(buf, sig, at):
    i = int(at*sr); j = min(n, i+len(sig))
    if i < n: buf[i:j] += sig[:j-i]

# --- light Am pad for body ---
pad = np.zeros(n)
for f in [110.0, 220.0, 261.63, 329.63]:
    pad += np.sin(2*np.pi*f*t) + 0.5*np.sin(2*np.pi*(f+0.18)*t)
pad /= np.max(np.abs(pad)); lp = np.zeros(n); a = 0.010
for i in range(1, n): lp[i] = lp[i-1] + a*(pad[i]-lp[i-1])
pad = lp * 0.30

# --- kick every 0.46s, driving 0 -> 34.6, out for cliffhanger, back at 40.8 ---
kick = np.zeros(n)
kl = int(0.16*sr); ke = np.exp(-np.linspace(0, 9, kl))
ks = np.sin(2*np.pi*52*np.arange(kl)/sr * (1+1.6*np.exp(-np.linspace(0,5,kl)))) * ke
tt = 0.0
while tt < D-0.2:
    if tt < 34.4 or tt >= 40.8: place(kick, ks*0.9, tt)
    tt += 0.46

# --- bass hits on the hard cuts ---
hit = np.zeros(n)
hl = int(0.30*sr); he = np.exp(-np.linspace(0, 7, hl))
hs = (np.sin(2*np.pi*40*np.arange(hl)/sr)*0.8 + rng.standard_normal(hl)*0.15) * he
for at in [0.0,2.2,3.3,4.6,6.4,7.1,11.1,11.8,16.1,16.8,22.1,29.4,30.7,32.0,33.3,40.8]:
    place(hit, hs*1.1, at)

# --- risers (1.8s) ending at the drops ---
ris = np.zeros(n)
rl = int(1.8*sr)
ramp = np.linspace(0, 1, rl)**2
noise = rng.standard_normal(rl); lpn = np.zeros(rl); a2 = 0.004
for i in range(1, rl): lpn[i] = lpn[i-1] + a2*(noise[i]-lpn[i-1])
sweep = np.sin(2*np.pi*np.cumsum(np.linspace(180, 720, rl))/sr)
riser = (lpn/(np.max(np.abs(lpn))+1e-9)*0.55 + sweep*0.45) * ramp * 0.55
for end in [6.4, 22.1, 29.4, 40.8]:
    place(ris, riser, max(0, end-1.8))

# --- cliffhanger tension 34.6-40.6: quiet high tremolo + low drone ---
ten = np.zeros(n)
i0, i1 = int(34.6*sr), int(40.6*sr)
seg = np.arange(i1-i0)/sr
trem = (0.6+0.4*np.sin(2*np.pi*5.2*seg))
ten[i0:i1] = (np.sin(2*np.pi*880*seg)*0.05 + np.sin(2*np.pi*55*seg)*0.22) * trem
fade_in = np.linspace(0,1,int(0.4*sr)); ten[i0:i0+len(fade_in)] *= fade_in

# --- final swell 40.8 -> end ---
sw = np.zeros(n)
s0 = int(40.8*sr); ln = n-s0
sramp = np.linspace(0,1,ln)**1.5
sw[s0:] = np.sin(2*np.pi*np.cumsum(np.linspace(140, 300, ln))/sr) * sramp * 0.35

mix = pad + kick + hit + ris + ten + sw
# duck pad during cliffhanger for contrast
duck = np.ones(n); duck[i0:i1] = 0.45
mix *= duck
mix /= (np.max(np.abs(mix)) + 1e-9)
mix[-int(0.45*sr):] *= np.linspace(1, 0, int(0.45*sr))
mix *= 0.7
st = np.stack([mix, mix], axis=1)
pcm = (st*32767).astype(np.int16)
with wave.open("music_teaser.wav", "w") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes(pcm.tobytes())
print("wrote music_teaser.wav", D, "s")
