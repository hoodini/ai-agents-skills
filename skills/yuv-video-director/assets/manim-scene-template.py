"""
YUV.AI — "How a neural network learns vs. the human brain"
ManimCE scene, neon neural-net (logo) styling on rich black.
Render: py -m manim render -qh --fps 30 manim/neural_brain.py NeuralBrain
"""
from manim import *
import math

INK   = "#0A0A0A"
PINK  = "#FF1464"
CYAN  = "#00E5FF"
WHITEISH = "#F5F5F7"
DIM   = "#8A8A93"
# phoenix gradient stops, warm -> cool (matches the logo)
PHX = ["#F9AD45", "#F0664E", "#DE6092", "#7C3AED", "#4E7DB7", "#00E5FF"]

def phx(u):
    u = max(0.0, min(0.999, u))
    return PHX[int(u * (len(PHX)))]

config.background_color = INK


class NeuralBrain(Scene):
    def construct(self):
        Text.set_default(font="Segoe UI")
        self.title_card()
        ann, ann_edges, ann_label = self.build_ann()
        brain, brain_edges, brain_label = self.build_brain()

        for grp, z in [(ann_edges, 0), (ann[1], 1), (ann[2], 2), (ann_label, 3),
                       (brain_edges, 0), (brain[0], 1), (brain[1], 2), (brain_label, 3)]:
            grp.set_z_index(z)

        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in ann[2]], lag_ratio=0.04),
            FadeIn(ann[1]),
            Create(ann_edges), FadeIn(ann_label, shift=UP*0.3),
            run_time=1.6,
        )
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in brain[1]], lag_ratio=0.05),
            FadeIn(brain[0]),
            Create(brain_edges), FadeIn(brain_label, shift=UP*0.3),
            run_time=1.6,
        )
        self.wait(0.4)

        self.train_ann(ann_edges)
        self.learn_brain(brain, brain_edges)
        self.freeze_vs_adapt(ann_edges)

        # clear the two networks, keep a thin memory of them
        self.play(
            *[FadeOut(m) for m in [ann_edges, brain_edges, ann_label, brain_label]],
            *[FadeOut(d) for d in ann[2]], *[FadeOut(g) for g in ann[1]],
            *[FadeOut(d) for d in brain[1]], *[FadeOut(g) for g in brain[0]],
            FadeOut(self.note),
            run_time=0.8,
        )
        self.params_panel()
        self.closing()

    # ---------------------------------------------------------------
    def title_card(self):
        t1 = Text("HOW A NEURAL NETWORK LEARNS", font_size=46, color=WHITEISH, weight=BOLD)
        t2 = Text("vs. the human brain", font_size=30, color=CYAN)
        g = VGroup(t1, t2).arrange(DOWN, buff=0.25).move_to(ORIGIN)
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, shift=UP*0.2), run_time=0.6)
        self.wait(0.6)
        self.play(g.animate.scale(0.46).to_edge(UP, buff=0.35), run_time=0.8)
        self.heading = g

    # ---------------------------------------------------------------
    def build_ann(self):
        layers = [4, 6, 6, 3]
        x0, span_x, span_y = -4.6, 3.0, 3.2
        glows, dots, positions = VGroup(), VGroup(), []
        for li, n in enumerate(layers):
            x = x0 + li * (span_x / (len(layers) - 1))
            col_pos = []
            for k in range(n):
                y = (k - (n - 1) / 2) * (span_y / max(n - 1, 1))
                p = [x, y, 0]
                u = li / (len(layers) - 1)
                c = phx(u)
                glows.add(Dot(p, radius=0.17, color=c, fill_opacity=0.22, stroke_width=0))
                dots.add(Dot(p, radius=0.07, color=c))
                col_pos.append(p)
            positions.append(col_pos)
        edges = VGroup()
        for li in range(len(layers) - 1):
            for a in positions[li]:
                for b in positions[li + 1]:
                    edges.add(Line(a, b, stroke_width=1.0, color=CYAN, stroke_opacity=0.18))
        label = Text("ARTIFICIAL NEURAL NETWORK", font_size=22, color=PINK, weight=BOLD)
        label.next_to([x0 + span_x / 2, 0, 0], DOWN, buff=2.0).set_y(-3.45).set_x(x0 + span_x/2)
        return (positions, glows, dots), edges, label

    def build_brain(self):
        cx, cy = 4.2, 0.0
        # neurons placed in a two-lobe brain-ish cloud (deterministic)
        pts = []
        seeds = [
            (-1.0, 1.1), (-0.2, 1.4), (0.7, 1.2), (1.3, 0.6),
            (-1.4, 0.3), (-0.6, 0.5), (0.2, 0.7), (1.0, 0.2),
            (-1.2, -0.5), (-0.4, -0.3), (0.4, -0.1), (1.2, -0.6),
            (-0.9, -1.1), (-0.1, -1.3), (0.8, -1.0), (0.1, 0.1),
        ]
        for (dx, dy) in seeds:
            pts.append([cx + dx * 1.25, cy + dy * 1.7, 0])
        glows, dots = VGroup(), VGroup()
        for p in pts:
            glows.add(Dot(p, radius=0.16, color=PINK, fill_opacity=0.20, stroke_width=0))
            dots.add(Dot(p, radius=0.07, color="#FF7AB6"))
        # organic connections (curved-ish via straight lines to nearest few)
        edges = VGroup()
        for i, a in enumerate(pts):
            d = sorted(range(len(pts)), key=lambda j: (pts[j][0]-a[0])**2 + (pts[j][1]-a[1])**2)
            for j in d[1:4]:
                if j > i:
                    edges.add(Line(a, pts[j], stroke_width=1.2, color="#FF7AB6", stroke_opacity=0.22))
        label = Text("THE HUMAN BRAIN", font_size=22, color=CYAN, weight=BOLD)
        label.set_x(cx).set_y(-3.45)
        self.brain_pts = pts
        return (glows, dots), edges, label

    # ---------------------------------------------------------------
    def train_ann(self, edges):
        note = Text("Training updates the WEIGHTS & BIASES — millions of them",
                    font_size=26, color=WHITEISH).set_y(-2.55)
        self.note = note
        self.play(FadeIn(note, shift=UP*0.2), run_time=0.6)
        # loss readout
        loss = ValueTracker(2.40)
        loss_lbl = Text("LOSS", font_size=18, color=DIM).set_x(-4.6).set_y(2.7)
        loss_num = always_redraw(lambda: Text(f"{loss.get_value():.2f}", font_size=30, color=PINK)
                                 .next_to(loss_lbl, RIGHT, buff=0.25))
        self.play(FadeIn(loss_lbl), FadeIn(loss_num), run_time=0.4)
        # three "epochs": edges flicker stroke width/opacity (gradient descent)
        for step in range(3):
            anims = []
            for idx, e in enumerate(edges):
                w = 0.6 + ((idx * 7 + step * 13) % 11) / 11 * 2.6
                op = 0.12 + ((idx * 5 + step * 3) % 9) / 9 * 0.55
                anims.append(e.animate.set_stroke(width=w, opacity=op))
            self.play(LaggedStart(*anims, lag_ratio=0.002),
                      loss.animate.set_value(2.40 - (step + 1) * 0.72),
                      run_time=0.9)
        self.play(FadeOut(loss_lbl), FadeOut(loss_num), run_time=0.4)
        self.loss_objs = VGroup(loss_lbl, loss_num)

    def learn_brain(self, brain, edges):
        new_note = Text("In the brain, learning IS the wiring — connections strengthen & form",
                        font_size=26, color=WHITEISH).set_y(-2.55)
        self.play(FadeOut(self.note), FadeIn(new_note), run_time=0.5)
        self.note = new_note
        pts = self.brain_pts
        # strengthen existing
        self.play(*[e.animate.set_stroke(width=3.0, opacity=0.75) for e in edges[:8]], run_time=0.9)
        # grow NEW synapses
        new_edges = VGroup(
            Line(pts[1], pts[8], stroke_width=2.6, color=CYAN, stroke_opacity=0.7),
            Line(pts[3], pts[11], stroke_width=2.6, color=CYAN, stroke_opacity=0.7),
            Line(pts[5], pts[14], stroke_width=2.6, color=CYAN, stroke_opacity=0.7),
            Line(pts[0], pts[6], stroke_width=2.6, color="#FF7AB6", stroke_opacity=0.7),
        )
        self.play(LaggedStart(*[Create(e) for e in new_edges], lag_ratio=0.2), run_time=1.2)
        self.brain_new = new_edges
        know = Text("knowledge lives in the structure itself", font_size=22, color=CYAN).set_x(4.2).set_y(2.7)
        self.play(FadeIn(know, shift=UP*0.2), run_time=0.6)
        self.wait(0.4)
        self.play(FadeOut(know), run_time=0.4)

    def freeze_vs_adapt(self, ann_edges):
        new_note = Text("Training ends → the network FREEZES.  The brain never stops.",
                        font_size=27, color=WHITEISH).set_y(-2.55)
        self.play(FadeOut(self.note), FadeIn(new_note), run_time=0.5)
        self.note = new_note
        frozen = Text("FROZEN", font_size=24, color=CYAN, weight=BOLD).set_x(-3.1).set_y(2.7)
        box = SurroundingRectangle(frozen, color=CYAN, buff=0.18)
        self.play(*[e.animate.set_stroke(opacity=0.10) for e in ann_edges],
                  Create(box), FadeIn(frozen), run_time=0.8)
        self.freeze_objs = VGroup(frozen, box)
        self.add(self.brain_new)
        self.wait(0.5)
        self.play(FadeOut(self.freeze_objs),
                  *[FadeOut(e) for e in self.brain_new], run_time=0.5)

    # ---------------------------------------------------------------
    def params_panel(self):
        head = Text("PARAMETERS = the weights & biases the model stores", font_size=30,
                    color=WHITEISH, weight=BOLD).set_y(2.7)
        self.play(FadeIn(head, shift=UP*0.2), run_time=0.7)

        rows = [("7B", "14 GB", 0.32), ("70B", "140 GB", 0.66), ("175B", "350 GB", 0.92)]
        y0 = 1.1
        groups = VGroup()
        for i, (p, gb, frac) in enumerate(rows):
            y = y0 - i * 1.15
            pnum = Text(p, font_size=40, color=PINK, weight=BOLD).set_x(-5.2).set_y(y)
            arrow = Text("→", font_size=34, color=DIM).set_x(-3.9).set_y(y)
            size = Text(gb, font_size=30, color=CYAN).set_x(-2.7).set_y(y)
            track = Rectangle(width=5.0, height=0.34, color="#23232B",
                              fill_color="#16161C", fill_opacity=1, stroke_width=1).set_x(2.0).set_y(y)
            bar = Rectangle(width=5.0*frac, height=0.34, fill_opacity=1, stroke_width=0)
            bar.set_color_by_gradient(PINK, CYAN)
            bar.set_x(2.0 - 5.0/2 + (5.0*frac)/2).set_y(y)
            groups.add(VGroup(pnum, arrow, size, track, bar))
        self.play(LaggedStart(*[FadeIn(g[:4]) for g in groups], lag_ratio=0.15), run_time=1.0)
        self.play(LaggedStart(*[GrowFromEdge(g[4], LEFT) for g in groups], lag_ratio=0.18), run_time=1.2)

        # consequences
        cons = VGroup(
            Text("↑ accuracy", font_size=26, color=CYAN),
            Text("↑ knowledge", font_size=26, color=CYAN),
            Text("↓ hallucinations", font_size=26, color=PINK),
            Text("↑ cost & size", font_size=26, color=DIM),
        ).arrange(RIGHT, buff=0.7).set_y(-2.7)
        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.2) for c in cons], lag_ratio=0.15), run_time=1.0)
        self.wait(1.0)
        self.play(FadeOut(head), FadeOut(groups), FadeOut(cons), run_time=0.7)

    def closing(self):
        l1 = Text("Both learn by reshaping connections.", font_size=38, color=WHITEISH, weight=BOLD)
        l2 = Text("One freezes when training ends — the other never stops.",
                  font_size=30, color=CYAN)
        g = VGroup(l1, l2).arrange(DOWN, buff=0.35).move_to(ORIGIN)
        self.play(Write(l1), run_time=1.1)
        self.play(FadeIn(l2, shift=UP*0.2), run_time=0.8)
        self.wait(1.4)
        self.play(FadeOut(g), FadeOut(self.heading), run_time=0.8)
        self.wait(0.3)
