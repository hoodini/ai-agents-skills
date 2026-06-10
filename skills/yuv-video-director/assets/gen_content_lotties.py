"""gen_content_lotties.py — six CONTENT Lotties for the news edit (lottie-web verified pattern).
wa-collapse / decode-beam / eye-read / ghost-line (HERO 640x440) / orb-extract / brain-fire.
v3 philosophy: every icon fully drawn + persistent; continuous looping accent motion;
any random 3s window shows a complete attractive image in motion. Transparent background."""
import json, math, os
FR = 30
PINK  = [1,0.078,0.392,1]; CYAN = [0,0.898,1,1]; WHITE = [1,1,1,1]
AMBER = [0.976,0.678,0.27,1]; VIOLET = [0.486,0.227,0.929,1]
WA_L  = [0.145,0.827,0.4,1]; WA_D = [0.07,0.55,0.31,1]
GREEN = [0.23,0.86,0.43,1]; SLATE = [0.08,0.10,0.16,1]
FACET = [1,0.85,0.58,1]
EO={"x":[0.4],"y":[0]}; EI={"x":[0.6],"y":[1]}
EO2={"x":[0.4,0.4],"y":[0,0]}; EI2={"x":[0.6,0.6],"y":[1,1]}

def loop(cyc,c,n,op):
    out=[]
    for k in range(n):
        b=k*c
        for kf in cyc:
            d={"t":b+kf["t"],"s":kf["s"]}
            if "i" in kf: d["i"]=kf["i"]; d["o"]=kf["o"]
            out.append(d)
    out.append({"t":op,"s":cyc[0]["s"]}); return {"a":1,"k":out}
def K(t,s):  return {"t":t,"s":s,"i":EI2,"o":EO2}     # multi-dim kf
def K1(t,s): return {"t":t,"s":s,"i":EI,"o":EO}       # 1-dim kf
def F(t,s):  return {"t":t,"s":s}                      # final (no easing)
def tr(p=(0,0),s=(100,100),r=0,o=100): return {"ty":"tr","p":{"a":0,"k":list(p)},"a":{"a":0,"k":[0,0]},"s":{"a":0,"k":list(s)},"r":{"a":0,"k":r},"o":{"a":0,"k":o}}
def rc(p,s,rad): return {"ty":"rc","p":{"a":0,"k":list(p)},"s":{"a":0,"k":list(s)},"r":{"a":0,"k":rad}}
def elp(p,s): return {"ty":"el","p":{"a":0,"k":list(p)},"s":{"a":0,"k":list(s)}}
def shp(v,closed=True): return {"ty":"sh","ks":{"a":0,"k":{"c":closed,"v":[list(p) for p in v],"i":[[0,0]]*len(v),"o":[[0,0]]*len(v)}}}
def sshp(v,k=0.18,closed=True,ks=None):
    n=len(v); ii=[]; oo=[]
    for idx in range(n):
        p=v[(idx-1)%n]; q=v[(idx+1)%n]; kk=(ks[idx] if ks else k)
        tx=(q[0]-p[0])*kk; ty=(q[1]-p[1])*kk
        oo.append([tx,ty]); ii.append([-tx,-ty])
    return {"ty":"sh","ks":{"a":0,"k":{"c":closed,"v":[list(p) for p in v],"i":ii,"o":oo}}}
def fl(c,o=100): return {"ty":"fl","c":{"a":0,"k":c},"o":{"a":0,"k":o}}
def stk(c,w,o=100): return {"ty":"st","c":{"a":0,"k":c},"o":{"a":0,"k":o},"w":{"a":0,"k":w},"lc":2,"lj":2}
def grp(it,nm="g"): return {"ty":"gr","nm":nm,"it":it+[tr()]}
def L(nm,shapes,ks,op): return {"ty":4,"nm":nm,"ip":0,"op":op,"st":0,"ao":0,"ks":{"o":ks.get("o",{"a":0,"k":100}),"r":ks.get("r",{"a":0,"k":0}),"p":ks["p"],"a":ks.get("a",{"a":0,"k":[0,0,0]}),"s":ks.get("s",{"a":0,"k":[100,100,100]})},"shapes":shapes}
def glow(col,r,o): return grp([elp([0,0],[r*2.4,r*2.4]),fl(col,o*0.16),elp([0,0],[r*1.6,r*1.6]),fl(col,o*0.30),elp([0,0],[r,r]),fl(col,o*0.6)],"glow")
def star(sz): return shp([[0,-sz],[sz*0.24,-sz*0.24],[sz,0],[sz*0.24,sz*0.24],[0,sz],[-sz*0.24,sz*0.24],[-sz,0],[-sz*0.24,-sz*0.24]],True)
def save(name,layers,op,w=512,h=512):
    os.makedirs("assets",exist_ok=True)
    json.dump({"v":"5.7.4","fr":FR,"ip":0,"op":op,"w":w,"h":h,"assets":[],"layers":layers},open("assets/"+name,"w"),separators=(",",":"))
    print(name,"OK",len(layers),"layers")

# ============================================================ 1) WA-COLLAPSE
# 4 WhatsApp bubbles bob, then sequentially shrink + fly down into a persistent
# summary card; card pops on each landing; green check strokes in; cycle repeats.
C,N=132,9; OP=C*N; lay=[]
BUB=[(150,64,184,'L'),(352,124,196,'R'),(160,184,200,'L'),(350,244,176,'R')]
DEP=[30,48,66,84]; FL=16; LAND=[d+FL for d in DEP]; CARD=(256,388)

def bubble_shapes(w,side):
    col = WA_D if side=='L' else WA_L
    sgn = -1 if side=='L' else 1
    tail = shp([[sgn*(w/2-6),12],[sgn*(w/2+16),26],[sgn*(w/2-6),30]],True)
    off = 6 if side=='L' else -6
    return [grp([rc([off,-9],[w-52,11],5.5),fl(WHITE,92)],"s1"),
            grp([rc([off*2.3,9],[w-84,11],5.5),fl(WHITE,78)],"s2"),
            grp([tail,fl(col)],"tail"),
            grp([rc([0,0],[w,56],16),fl(col)],"bg"),
            grp([elp([0,0],[w+26,84]),fl(col,16)],"glow")]

# check badge at card corner (TOP layer)
chk = shp([[-12,1],[-4,10],[14,-9]],False)
tm_e = loop([K1(0,[0]),K1(102,[0]),K1(116,[100]),F(C-1,[100])],C,N,OP)
chk_g = {"ty":"gr","nm":"chk","it":[chk,{"ty":"tm","s":{"a":0,"k":0},"e":tm_e,"o":{"a":0,"k":0},"m":1},stk(GREEN,8),tr()]}
lay.append(L("check",[chk_g,grp([elp([0,0],[46,46]),fl(SLATE)],"badge"),grp([elp([0,0],[72,72]),fl(GREEN,22)],"glo")],
    {"p":{"a":0,"k":[398,312,0]},
     "o":loop([K1(0,[0]),K1(101,[0]),K1(105,[100]),K1(124,[100]),K1(129,[0]),F(C-1,[0])],C,N,OP),
     "s":loop([K(0,[0,0,100]),K(101,[0,0,100]),K(107,[118,118,100]),K(112,[100,100,100]),F(C-1,[100,100,100])],C,N,OP)},OP))

for i,(cx,cy,w,side) in enumerate(BUB):
    d=DEP[i]; si=i*4
    kp=[K(0,[cx,cy,0])]; t=10; up=True
    while t<d-4:
        kp.append(K(t,[cx,cy-5 if up else cy,0])); up=not up; t+=10
    kp+=[K(d,[cx,cy,0]),K(d+FL,[CARD[0],CARD[1]-28,0]),F(C-1,[CARD[0],CARD[1]-28,0])]
    ks_=[K(0,[0,0,100])]
    if si>0: ks_.append(K(si,[0,0,100]))
    ks_+=[K(si+8,[114,114,100]),K(si+13,[100,100,100]),K(d,[100,100,100]),K(d+FL,[14,14,100]),F(C-1,[14,14,100])]
    ko=[K1(0,[100] if si==0 else [0])]
    if si>0: ko+=[K1(si,[0]),K1(si+5,[100])]
    ko+=[K1(d+FL-5,[100]),K1(d+FL,[0]),F(C-1,[0])]
    lay.append(L("bub%d"%i,bubble_shapes(w,side),
        {"p":loop(kp,C,N,OP),"s":loop(ks_,C,N,OP),"o":loop(ko,C,N,OP)},OP))

card_s=[K(0,[100,100,100])]
for l in LAND: card_s+=[K(l-2,[100,100,100]),K(l+3,[107,107,100]),K(l+8,[100,100,100])]
card_s.append(F(C-1,[100,100,100]))
lay.append(L("card",[grp([rc([0,-56],[246,24],12),fl(PINK)],"hdr"),
                     grp([rc([0,-12],[246,14],7),fl(WHITE,90)],"l1"),
                     grp([rc([-27,18],[192,14],7),fl(WHITE,70)],"l2"),
                     grp([rc([0,0],[304,170],18),stk(CYAN,5)],"str"),
                     grp([rc([0,0],[304,170],18),fl(SLATE)],"bg"),
                     grp([elp([0,0],[400,260]),fl(CYAN,9)],"glo")],
    {"p":{"a":0,"k":[CARD[0],CARD[1],0]},"s":loop(card_s,C,N,OP)},OP))
save("wa-collapse.json",lay,OP)

# ============================================================ 2) DECODE-BEAM
# 4 dim right-aligned strips; cyan beam sweeps R->L; strips light as it crosses;
# strip 2 flips PINK and stays lit until next sweep; 3 dots drift up the beam.
C,N=90,13; OP=C*N; lay=[]
STR=[(150,280),(215,330),(280,240),(345,300)]; RIGHT=420
# dots on top
for (dx,y0,y1) in [(-10,396,196),(8,344,158),(0,300,130)]:
    lay.append(L("dot",[grp([elp([0,0],[12,12]),fl(CYAN,95)],"d"),grp([elp([0,0],[26,26]),fl(CYAN,30)],"g")],
        {"p":loop([K(0,[452+dx,y0,0]),K(82,[60+dx,y1,0]),F(C-1,[60+dx,y1,0])],C,N,OP),
         "o":loop([K1(0,[0]),K1(10,[85]),K1(70,[85]),K1(82,[0]),F(C-1,[0])],C,N,OP)},OP))
lay.append(L("beam",[grp([rc([0,0],[3,378],1.5),fl(WHITE,85)],"wc"),
                     grp([rc([0,0],[8,378],4),fl(CYAN)],"core"),
                     grp([rc([0,0],[38,366],12),fl(CYAN,20)],"mid"),
                     grp([rc([0,0],[78,366],18),fl(CYAN,10)],"out"),
                     grp([elp([0,0],[130,420]),fl(CYAN,8)],"halo")],
    {"p":loop([K(0,[452,250,0]),K(82,[60,250,0]),F(C-1,[60,250,0])],C,N,OP),
     "o":loop([K1(0,[0]),K1(4,[100]),K1(78,[100]),K1(84,[0]),F(C-1,[0])],C,N,OP)},OP))
LITO=[ [K1(0,[0]),K1(7,[0]),K1(65,[100]),K1(71,[100]),K1(80,[0]),F(C-1,[0])],
       [K1(0,[100]),K1(8,[100]),K1(13,[0]),K1(18,[0]),K1(76,[100]),F(C-1,[100])],
       [K1(0,[0]),K1(7,[0]),K1(57,[100]),K1(63,[100]),K1(73,[0]),F(C-1,[0])],
       [K1(0,[0]),K1(7,[0]),K1(70,[100]),K1(75,[100]),K1(84,[0]),F(C-1,[0])] ]
for i,(y,w) in enumerate(STR):
    cx=RIGHT-w/2; col = PINK if i==1 else WHITE
    g=[grp([rc([0,0],[w,18],9),fl(col)],"lit")]
    if i==1: g.insert(0,grp([rc([0,0],[w+18,32],16),fl(PINK,20)],"pglo"))
    lay.append(L("lit%d"%i,g,{"p":{"a":0,"k":[cx,y,0]},"o":loop(LITO[i],C,N,OP)},OP))
for (y,w) in STR:
    lay.append(L("dim",[grp([rc([0,0],[w,18],9),fl(WHITE,35)],"d")],{"p":{"a":0,"k":[RIGHT-w/2,y,0]}},OP))
save("decode-beam.json",lay,OP)

# ============================================================ 3) EYE-READ
# Almond eye above 3 white strips; iris sweeps R->L twice/cycle (Hebrew);
# pink underline glides under strips matching the gaze; one quick blink/cycle.
C,N=120,10; OP=C*N; lay=[]
EC=(256,168)
irisp=loop([K(0,[300,168,0]),K(44,[212,168,0]),K(52,[300,168,0]),K(96,[212,168,0]),K(108,[300,168,0]),F(C-1,[300,168,0])],C,N,OP)
blink=loop([K(0,[100,100,100]),K(68,[100,100,100]),K(73,[100,8,100]),K(78,[100,100,100]),F(C-1,[100,100,100])],C,N,OP)
lay.append(L("pupil",[grp([elp([-10,-10],[11,11]),fl(WHITE,90)],"hl"),grp([elp([0,0],[26,26]),fl(SLATE)],"pu")],
    {"p":irisp,"s":blink},OP))
lay.append(L("iris",[grp([elp([0,0],[56,56]),fl(CYAN)],"ir"),grp([elp([0,0],[86,86]),fl(CYAN,25)],"ig")],
    {"p":irisp,"s":blink},OP))
eye_path={"ty":"sh","ks":{"a":0,"k":{"c":True,"v":[[-102,0],[0,-60],[102,0],[0,60]],
    "i":[[0,0],[-58,0],[0,0],[58,0]],"o":[[0,0],[58,0],[0,0],[-58,0]]}}}
lay.append(L("eo",[{"ty":"gr","nm":"eye","it":[eye_path,fl(CYAN,6),stk(CYAN,7),tr()]},
                   grp([elp([0,0],[236,148]),fl(CYAN,8)],"glo")],
    {"p":{"a":0,"k":[EC[0],EC[1],0]},"s":blink},OP))
lay.append(L("under",[grp([rc([0,0],[96,9],4.5),fl(PINK)],"u"),grp([rc([0,0],[126,24],12),fl(PINK,20)],"ug")],
    {"p":loop([K(0,[368,338,0]),K(44,[144,338,0]),K(46,[144,338,0]),K(51,[368,382,0]),K(96,[194,382,0]),K(98,[194,382,0]),K(103,[368,338,0]),F(C-1,[368,338,0])],C,N,OP),
     "o":loop([K1(0,[100]),K1(44,[100]),K1(47,[0]),K1(50,[0]),K1(54,[100]),K1(96,[100]),K1(99,[0]),K1(102,[0]),K1(106,[100]),F(C-1,[100])],C,N,OP)},OP))
for (y,w) in [(320,320),(364,270),(408,296)]:
    lay.append(L("ln",[grp([rc([0,0],[w,16],8),fl(WHITE)],"l")],{"p":{"a":0,"k":[416-w/2,y,0]}},OP))
save("eye-read.json",lay,OP)

# ============================================================ 4) GHOST-LINE (HERO 640x440)
# Two solid white strips; 6 pink dashes fly into the gap (back-ease), connect
# into one glowing line; ring pulse on completion; shimmer hold; scatter; repeat.
C,N=150,8; OP=C*N; lay=[]
GW,GH=640,440; LY=220
TX=[143,214,285,356,427,498]
DSH=[(-90,192,0),(-90,250,6),(-90,206,12),(730,252,3),(730,190,9),(730,242,15)]
# sparkles (top)
for j,(sx,sy) in enumerate([(205,202),(330,240),(442,206)]):
    lay.append(L("sp",[grp([star(10),fl(WHITE)],"s")],
        {"p":{"a":0,"k":[sx,sy,0]},
         "o":loop([K1(0,[0]),K1(44+j*22,[0]),K1(52+j*22,[95]),K1(64+j*22,[0]),F(C-1,[0])],C,N,OP),
         "s":loop([K(0,[40,40,100]),K(44+j*22,[40,40,100]),K(54+j*22,[120,120,100]),K(64+j*22,[40,40,100]),F(C-1,[40,40,100])],C,N,OP)},OP))
lay.append(L("ring1",[grp([elp([0,0],[300,140]),stk(PINK,5)],"r")],
    {"p":{"a":0,"k":[320,LY,0]},
     "s":loop([K(0,[10,10,100]),K(34,[10,10,100]),K(60,[160,160,100]),F(C-1,[160,160,100])],C,N,OP),
     "o":loop([K1(0,[0]),K1(33,[0]),K1(35,[92]),K1(60,[0]),F(C-1,[0])],C,N,OP)},OP))
lay.append(L("ring2",[grp([elp([0,0],[260,120]),stk(CYAN,3)],"r")],
    {"p":{"a":0,"k":[320,LY,0]},
     "s":loop([K(0,[8,8,100]),K(41,[8,8,100]),K(67,[150,150,100]),F(C-1,[150,150,100])],C,N,OP),
     "o":loop([K1(0,[0]),K1(40,[0]),K1(42,[80]),K1(67,[0]),F(C-1,[0])],C,N,OP)},OP))
lay.append(L("core",[grp([rc([0,-1],[420,5],2.5),fl(WHITE,85)],"w"),grp([rc([0,0],[428,14],7),fl(PINK)],"p")],
    {"p":{"a":0,"k":[320,LY,0]},
     "o":loop([K1(0,[0]),K1(32,[0]),K1(36,[100]),K1(50,[84]),K1(64,[100]),K1(78,[84]),K1(92,[100]),K1(106,[84]),K1(116,[100]),K1(122,[0]),F(C-1,[0])],C,N,OP)},OP))
for i,(sx,sy,st) in enumerate(DSH):
    tx=TX[i]; left = sx<0
    ox = tx+18 if left else tx-18
    sx2 = -130 if left else 770; sy2 = sy+(15 if i%2 else -15)
    kp=[K(0,[sx,sy,0])]
    if st>0: kp.append(K(st,[sx,sy,0]))
    kp+=[K(st+14,[ox,LY,0]),K(st+20,[tx,LY,0]),K(120+i*2,[tx,LY,0]),K(136+i*2,[sx2,sy2,0]),F(C-1,[sx2,sy2,0])]
    lay.append(L("dash%d"%i,[grp([rc([0,0],[72,13],6.5),fl(PINK)],"d"),grp([rc([0,0],[80,22],11),fl(PINK,16)],"dg")],
        {"p":loop(kp,C,N,OP),
         "o":loop([K1(0,[100]),K1(132+i*2,[100]),K1(140+i*2,[0]),F(C-1,[0])],C,N,OP)},OP))
lay.append(L("lglow",[grp([elp([0,0],[440,30]),fl(PINK,30)],"g1"),grp([elp([0,0],[480,64]),fl(PINK,16)],"g2"),grp([elp([0,0],[540,116]),fl(PINK,9)],"g3")],
    {"p":{"a":0,"k":[320,LY,0]},
     "o":loop([K1(0,[0]),K1(30,[0]),K1(38,[95]),K1(52,[70]),K1(66,[100]),K1(80,[72]),K1(94,[100]),K1(108,[75]),K1(116,[95]),K1(124,[0]),F(C-1,[0])],C,N,OP)},OP))
for y in (80,360):
    lay.append(L("strip",[grp([rc([0,0],[470,26],13),fl(WHITE)],"s")],{"p":{"a":0,"k":[320,y,0]}},OP))
save("ghost-line.json",lay,OP,GW,GH)

# ============================================================ 5) ORB-EXTRACT
# 5x3 dim dot grid; pink orb bobs above; amber gem rises along an arc into the
# orb (faint cyan beam while traveling); orb pulses + sparkle on absorb; respawn.
C,N=110,11; OP=C*N; lay=[]
lay.append(L("spark",[grp([star(16),fl(WHITE)],"s")],
    {"p":{"a":0,"k":[304,106,0]},
     "o":loop([K1(0,[0]),K1(56,[0]),K1(61,[100]),K1(74,[0]),F(C-1,[0])],C,N,OP),
     "s":loop([K(0,[20,20,100]),K(56,[20,20,100]),K(66,[135,135,100]),K(74,[30,30,100]),F(C-1,[20,20,100])],C,N,OP),
     "r":loop([K1(0,[0]),F(C-1,[45])],C,N,OP)},OP))
lay.append(L("flash",[grp([elp([0,0],[90,90]),fl(WHITE,55)],"w"),grp([elp([0,0],[150,150]),fl(PINK,40)],"p")],
    {"p":{"a":0,"k":[256,140,0]},
     "o":loop([K1(0,[0]),K1(54,[0]),K1(60,[80]),K1(72,[0]),F(C-1,[0])],C,N,OP)},OP))
lay.append(L("orb",[grp([elp([0,0],[46,46]),fl(WHITE)],"core"),glow(PINK,44,100)],
    {"p":loop([K(0,[256,140,0]),K(28,[256,131,0]),K(56,[256,140,0]),K(84,[256,133,0]),F(C-1,[256,140,0])],C,N,OP),
     "s":loop([K(0,[100,100,100]),K(26,[106,106,100]),K(50,[100,100,100]),K(60,[128,128,100]),K(74,[100,100,100]),K(92,[105,105,100]),F(C-1,[100,100,100])],C,N,OP)},OP))
lay.append(L("gem",[grp([shp([[0,-23],[14,-2],[0,16],[-14,-2]]),fl(FACET)],"facet"),
                    grp([shp([[0,-32],[24,0],[0,34],[-24,0]]),fl(AMBER)],"gem"),
                    glow(AMBER,30,70)],
    {"p":loop([K(0,[256,372,0]),K(6,[256,366,0]),K(12,[256,372,0]),K(30,[290,298,0]),K(46,[272,210,0]),K(56,[257,150,0]),K(60,[257,148,0]),K(64,[256,372,0]),K(82,[256,372,0]),K(94,[256,366,0]),F(C-1,[256,372,0])],C,N,OP),
     "s":loop([K(0,[100,100,100]),K(30,[108,108,100]),K(56,[96,96,100]),K(76,[10,10,100]),K(84,[116,116,100]),K(90,[100,100,100]),K(100,[106,106,100]),F(C-1,[100,100,100])],C,N,OP),
     "o":loop([K1(0,[100]),K1(50,[100]),K1(58,[0]),K1(78,[0]),K1(84,[100]),F(C-1,[100])],C,N,OP)},OP))
lay.append(L("beam",[{"ty":"gr","nm":"b","it":[shp([[247,176],[265,176],[300,372],[212,372]]),fl(CYAN),tr()]}],
    {"p":{"a":0,"k":[0,0,0]},
     "o":loop([K1(0,[0]),K1(12,[0]),K1(18,[20]),K1(50,[20]),K1(58,[0]),F(C-1,[0])],C,N,OP)},OP))
for r in range(3):
    for cc in range(5):
        idx=r*5+cc; ks={"p":{"a":0,"k":[176+cc*40,336+r*34,0]}}
        if idx%4==1:
            tA=(idx*9)%76
            ks["o"]=loop([K1(0,[38]),K1(tA,[38]),K1(tA+10,[72]),K1(tA+20,[38]),F(C-1,[38])],C,N,OP)
        else:
            ks["o"]={"a":0,"k":38}
        lay.append(L("dot",[grp([elp([0,0],[13,13]),fl(WHITE)],"d")],ks,OP))
save("orb-extract.json",lay,OP)

# ============================================================ 6) BRAIN-FIRE
# Side-view brain silhouette (smooth closed path: bumpy top, flatter back, stem
# notch bottom-rear, frontal curve) + 7 phoenix nodes firing in cascade + 5 links.
C,N=104,12; OP=C*N; lay=[]
# cerebrum outline (bumpy top, frontal curve, flatter back) — cerebellum + stem are
# separate overlapping shapes (classic brain-icon geometry, reads instantly).
BV=[(114,224),(122,172),(152,134),(196,118),(228,134),(268,112),(304,134),(344,126),
    (378,162),(392,212),(378,246),(344,256),(308,278),(250,292),(180,288),(134,262)]
KS=[0.16]*16
KS[4]=0.10; KS[6]=0.10  # crisp gyri dips
NP=[(162,244,PINK),(200,178,AMBER),(246,238,WHITE),(266,158,CYAN),(312,192,VIOLET),(354,228,PINK),(282,258,CYAN)]
EDG=[(0,1),(1,2),(2,3),(3,4),(4,5)]
for i,(x,y,col) in enumerate(NP):
    fi=8+i*6
    s_=[K(0,[86,86,100]),K(fi,[86,86,100]),K(fi+7,[136,136,100]),K(fi+18,[88,88,100]),
        K(62+i*4,[88,88,100]),K(69+i*4,[100,100,100]),K(76+i*4,[86,86,100]),F(C-1,[86,86,100])]
    o_=[K1(0,[70]),K1(fi,[70]),K1(fi+7,[100]),K1(fi+18,[70]),F(C-1,[70])]
    lay.append(L("n%d"%i,[grp([elp([0,0],[20,20]),fl(col)],"core"),grp([elp([0,0],[48,48]),fl(col,22)],"glo")],
        {"p":{"a":0,"k":[x,y,0]},"s":loop(s_,C,N,OP),"o":loop(o_,C,N,OP)},OP))
for (a,b) in EDG:
    pa=NP[a][:2]; pb=NP[b][:2]; colb=NP[b][2]; tb=8+a*6+3
    lay.append(L("lb",[{"ty":"gr","nm":"hot","it":[shp([pa,pb],False),stk(colb,5),tr()]}],
        {"p":{"a":0,"k":[0,0,0]},
         "o":loop([K1(0,[0]),K1(tb,[0]),K1(tb+7,[90]),K1(tb+20,[0]),F(C-1,[0])],C,N,OP)},OP))
for (a,b) in EDG:
    lay.append(L("lbase",[{"ty":"gr","nm":"ln","it":[shp([NP[a][:2],NP[b][:2]],False),stk(WHITE,4,30),tr()]}],
        {"p":{"a":0,"k":[0,0,0]}},OP))
stem={"ty":"gr","nm":"stem","it":[rc([0,0],[22,48],11),fl(CYAN,8),stk(CYAN,4.5),
    {"ty":"tr","p":{"a":0,"k":[298,304]},"a":{"a":0,"k":[0,0]},"s":{"a":0,"k":[100,100]},"r":{"a":0,"k":-24},"o":{"a":0,"k":100}}]}
cereb={"ty":"gr","nm":"cereb","it":[elp([342,272],[58,40]),fl(CYAN,8),stk(CYAN,4.5),tr()]}
lay.append(L("brain",[{"ty":"gr","nm":"br","it":[sshp(BV,ks=KS),fl(CYAN,6),stk(CYAN,6),tr()]},
                      cereb,stem,
                      grp([elp([253,218],[340,270]),fl(CYAN,7)],"glo")],
    {"p":{"a":0,"k":[253,218,0]},"a":{"a":0,"k":[253,218,0]},
     "s":loop([K(0,[100,100,100]),K(52,[102,102,100]),F(C-1,[100,100,100])],C,N,OP)},OP))
save("brain-fire.json",lay,OP)
print("ALL SIX DONE")
