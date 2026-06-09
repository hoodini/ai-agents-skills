"""Generate a looping 'phoenix-burst' Bodymovin Lottie (radiating rainbow rays + rings).
Loops every CYCLE frames across OP frames so HyperFrames' goToAndStop(t*1000) shows a live
burst at any composition time. Renders in lottie-web (verified). Full phoenix palette."""
import json, math

W = H = 400
CX = CY = 200
FR = 30
CYCLE = 60          # 2s per burst
CYCLES = 22
OP = CYCLE * CYCLES  # 1320 frames ≈ 44s, covers any comp time

# phoenix palette stops as normalized RGBA
PHX = [
    (0xF9,0xAD,0x45),(0xF7,0x88,0x44),(0xF0,0x66,0x4E),(0xDE,0x60,0x92),
    (0xFF,0x14,0x64),(0x8B,0x45,0x9A),(0x7C,0x3A,0xED),(0x4E,0x7D,0xB7),(0x00,0xE5,0xFF),
]
def rgba(c): return [round(c[0]/255,4), round(c[1]/255,4), round(c[2]/255,4), 1]

EO = {"x":[0.33],"y":[0]}; EI = {"x":[0.5],"y":[1]}      # 1-dim ease
EO2 = {"x":[0.33,0.33],"y":[0,0]}; EI2 = {"x":[0.5,0.5],"y":[1,1]}  # 2-dim

def kf_scale_y(start_peak):
    """scaleY pulses 6 -> 100 each cycle, X constant 100."""
    k = []
    for c in range(CYCLES):
        b = c*CYCLE
        k.append({"t":b,    "s":[100,6],   "i":EI2,"o":EO2})
        k.append({"t":b+34, "s":[100,100], "i":EI2,"o":EO2})
        k.append({"t":b+CYCLE-1,"s":[100,100],"i":EI2,"o":EO2})
    k.append({"t":OP,"s":[100,6]})
    return {"a":1,"k":k}

def kf_opacity():
    k = []
    for c in range(CYCLES):
        b = c*CYCLE
        k.append({"t":b,    "s":[0],   "i":EI,"o":EO})
        k.append({"t":b+6,  "s":[100], "i":EI,"o":EO})
        k.append({"t":b+48, "s":[0],   "i":EI,"o":EO})
    k.append({"t":OP,"s":[0]})
    return {"a":1,"k":k}

def kf_ring_scale():
    k = []
    for c in range(CYCLES):
        b = c*CYCLE
        k.append({"t":b,    "s":[12,12],  "i":EI2,"o":EO2})
        k.append({"t":b+52, "s":[260,260],"i":EI2,"o":EO2})
        k.append({"t":b+CYCLE-1,"s":[260,260],"i":EI2,"o":EO2})
    k.append({"t":OP,"s":[12,12]})
    return {"a":1,"k":k}

def kf_ring_opacity():
    k = []
    for c in range(CYCLES):
        b = c*CYCLE
        k.append({"t":b,    "s":[0],  "i":EI,"o":EO})
        k.append({"t":b+8,  "s":[85], "i":EI,"o":EO})
        k.append({"t":b+52, "s":[0],  "i":EI,"o":EO})
    k.append({"t":OP,"s":[0]})
    return {"a":1,"k":k}

layers = []
ind = 1
RAYS = 18
for i in range(RAYS):
    ang = i * (360.0/RAYS)
    c = PHX[i % len(PHX)]
    layers.append({
        "ddd":0,"ind":ind,"ty":4,"nm":f"ray{i}","sr":1,
        "ks":{"o":kf_opacity(),"r":{"a":0,"k":ang},"p":{"a":0,"k":[CX,CY,0]},
              "a":{"a":0,"k":[0,0,0]},"s":kf_scale_y(34)},
        "ao":0,
        "shapes":[{"ty":"gr","nm":"g","it":[
            {"ty":"rc","nm":"r","d":1,"p":{"a":0,"k":[0,-78]},"s":{"a":0,"k":[7,150]},"r":{"a":0,"k":0}},
            {"ty":"fl","nm":"f","c":{"a":0,"k":rgba(c)},"o":{"a":0,"k":100}},
            {"ty":"tr","p":{"a":0,"k":[0,0]},"a":{"a":0,"k":[0,0]},"s":{"a":0,"k":[100,100]},"r":{"a":0,"k":0},"o":{"a":0,"k":100}}
        ]}],
        "ip":0,"op":OP,"st":0,"bm":0
    })
    ind += 1

# 3 expanding rings, staggered, alternating pink/cyan/amber
ring_cols = [(0xFF,0x14,0x64),(0x00,0xE5,0xFF),(0xF9,0xAD,0x45)]
for r in range(3):
    c = ring_cols[r]
    op_kf = kf_ring_opacity()
    sc_kf = kf_ring_scale()
    # stagger by shifting times
    shift = r*14
    for kf in op_kf["k"]: kf["t"] = min(OP, kf["t"]+shift)
    for kf in sc_kf["k"]: kf["t"] = min(OP, kf["t"]+shift)
    layers.append({
        "ddd":0,"ind":ind,"ty":4,"nm":f"ring{r}","sr":1,
        "ks":{"o":op_kf,"r":{"a":0,"k":0},"p":{"a":0,"k":[CX,CY,0]},
              "a":{"a":0,"k":[0,0,0]},"s":sc_kf},
        "ao":0,
        "shapes":[{"ty":"gr","nm":"g","it":[
            {"ty":"el","nm":"e","p":{"a":0,"k":[0,0]},"s":{"a":0,"k":[60,60]}},
            {"ty":"st","nm":"s","c":{"a":0,"k":rgba(c)},"o":{"a":0,"k":100},"w":{"a":0,"k":5},"lc":2,"lj":1},
            {"ty":"tr","p":{"a":0,"k":[0,0]},"a":{"a":0,"k":[0,0]},"s":{"a":0,"k":[100,100]},"r":{"a":0,"k":0},"o":{"a":0,"k":100}}
        ]}],
        "ip":0,"op":OP,"st":0,"bm":0
    })
    ind += 1

doc = {"v":"5.7.4","fr":FR,"ip":0,"op":OP,"w":W,"h":H,"nm":"phoenix-burst","ddd":0,"assets":[],"layers":layers}
with open(r"assets\phoenix-burst.json","w") as f:
    json.dump(doc, f, separators=(",",":"))
print("wrote assets/phoenix-burst.json :", len(layers), "layers, op", OP)
