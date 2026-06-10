"""72s cinematic bed for the NN explainer: Am pad + soft pulse, lift at the punch, swell into outro."""
import numpy as np, wave
sr = 44100
D = 72.0
n = int(sr * D)
t = np.arange(n) / sr

def adsr(att, rel, level=1.0):
    env = np.ones(n) * level
    a = int(att*sr); r = int(rel*sr)
    env[:a] = np.linspace(0, level, a)
    env[-r:] = np.linspace(level, 0, r)
    return env

pad = np.zeros(n)
for f in [110.0, 164.81, 220.0, 261.63, 329.63]:
    for det in (-0.15, 0.15):
        pad += np.sin(2*np.pi*(f+det)*t)
    pad += 0.25*np.sin(2*np.pi*2*f*t)
pad /= np.max(np.abs(pad))
trem = 0.85 + 0.15*np.sin(2*np.pi*0.1*t)
pad *= trem
lp = np.zeros(n); a = 0.012
for i in range(1, n): lp[i] = lp[i-1] + a*(pad[i]-lp[i-1])
pad = lp * adsr(3.0, 2.5, 0.5)

pulse = np.zeros(n)
step = int(0.5*sr)
env = np.exp(-np.linspace(0, 8, int(0.22*sr)))
blip = np.sin(2*np.pi*58*np.arange(len(env))/sr) * env
for k in range(0, n-len(blip), step):
    pulse[k:k+len(blip)] += blip
pulse *= 0.2

# gentle lift at the punch section (last 14-8s) + swell into outro (last 6s)
swell = np.zeros(n)
s0 = int((D-6.0)*sr); ln = n - s0
ns = np.random.default_rng(7).standard_normal(ln)
lp2 = np.zeros(ln); a2 = 0.002
for i in range(1, ln): lp2[i] = lp2[i-1] + a2*(ns[i]-lp2[i-1])
ramp = np.linspace(0, 1, ln)**2
sweep = np.sin(2*np.pi*np.cumsum(np.linspace(120, 320, ln))/sr)
swell[s0:] = (lp2/(np.max(np.abs(lp2))+1e-9)*0.6 + sweep*0.4) * ramp * 0.5

mix = pad*0.6 + pulse*0.5 + swell*0.7
mix /= (np.max(np.abs(mix)) + 1e-9)
mix *= 0.6
st = np.stack([mix, mix], axis=1)
pcm = (st*32767).astype(np.int16)
with wave.open("music.wav", "w") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes(pcm.tobytes())
print("wrote music.wav", D, "s")
