"""
YUV.AI — "What is a neural network?" — nearly-wordless visual explainer.
Three chapters: single neuron -> layered network -> training (loss descent).

Test:  py -m manim render -ql --fps 15 manim/what_is_nn.py WhatIsNN
Final: py -m manim render -qh --fps 30 manim/what_is_nn.py WhatIsNN
Output: media/videos/what_is_nn/1080p30/WhatIsNN.mp4
"""
from manim import *
import numpy as np

INK      = "#0A0A0A"
PINK     = "#FF1464"
CYAN     = "#00E5FF"
WHITEISH = "#F5F5F7"
AMBER    = "#F9AD45"
# phoenix gradient stops, warm -> cool
PHX = ["#F9AD45", "#F0664E", "#DE6092", "#7C3AED", "#4E7DB7", "#00E5FF"]


def phx(u):
    u = max(0.0, min(0.999, u))
    return PHX[int(u * len(PHX))]


config.background_color = INK


class WhatIsNN(Scene):
    def construct(self):
        Text.set_default(font="Segoe UI")
        self._mark("chapter1-neuron")
        self.chapter_neuron()
        self._mark("chapter2-network")
        self.chapter_network()
        self._mark("chapter3-training")
        self.chapter_training()
        self._mark("end")

    def _mark(self, name):
        try:
            print(f"[CHAPTER] {name} @ {self.renderer.time:.2f}s")
        except Exception:
            pass

    # ------------------------------------------------------------------
    # Chapter 1 — a single artificial neuron (~13s)
    # ------------------------------------------------------------------
    def chapter_neuron(self):
        title = Text("A R T I F I C I A L   N E U R O N",
                     font_size=26, color=WHITEISH, weight=BOLD)
        title.to_edge(UP, buff=0.6)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.9)
        self.wait(0.5)

        C = np.array([-0.4, 0.0, 0.0])  # neuron center
        in_pos = [np.array([-4.8, 1.7, 0.0]),
                  np.array([-4.8, 0.0, 0.0]),
                  np.array([-4.8, -1.7, 0.0])]
        in_glows = VGroup(*[Dot(p, radius=0.18, color=CYAN, fill_opacity=0.22,
                                stroke_width=0) for p in in_pos])
        in_dots = VGroup(*[Dot(p, radius=0.09, color=CYAN) for p in in_pos])
        x_labels = VGroup(*[
            Text(f"x{i + 1}", font_size=24, color=CYAN).next_to(d, LEFT, buff=0.28)
            for i, d in enumerate(in_dots)
        ])

        # weights = visibly different stroke widths
        widths = [2.0, 6.0, 3.5]
        lines = VGroup()
        for p, w in zip(in_pos, widths):
            v = C - p
            u = v / np.linalg.norm(v)
            lines.add(Line(p + u * 0.16, C - u * 0.56,
                           stroke_width=w, color=WHITEISH, stroke_opacity=0.55))
        w_labels = VGroup()
        for i, l in enumerate(lines):
            mid = (l.get_start() + l.get_end()) / 2
            d = l.get_end() - l.get_start()
            n = np.array([-d[1], d[0], 0.0])
            n = n / np.linalg.norm(n)
            if n[1] < 0:
                n = -n
            w_labels.add(Text(f"w{i + 1}", font_size=20, color=AMBER)
                         .move_to(mid + n * 0.34))

        n_glow = Dot(C, radius=0.85, color=PINK, fill_opacity=0.13, stroke_width=0)
        neuron = Circle(radius=0.5, color=WHITEISH, stroke_width=3.5,
                        fill_color=PINK, fill_opacity=0.10).move_to(C)
        sum_lbl = Text("sum", font_size=20, color=WHITEISH).move_to(C)

        for grp, z in [(lines, 0), (in_glows, 1), (n_glow, 1), (in_dots, 2),
                       (neuron, 2), (x_labels, 3), (w_labels, 3),
                       (sum_lbl, 3), (title, 3)]:
            grp.set_z_index(z)

        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in in_dots], lag_ratio=0.15),
            FadeIn(in_glows),
            LaggedStart(*[FadeIn(l, shift=RIGHT * 0.15) for l in x_labels],
                        lag_ratio=0.15),
            run_time=1.1,
        )
        self.play(
            LaggedStart(*[Create(l) for l in lines], lag_ratio=0.2),
            LaggedStart(*[FadeIn(w) for w in w_labels], lag_ratio=0.2),
            run_time=1.2,
        )
        self.play(GrowFromCenter(n_glow), GrowFromCenter(neuron),
                  FadeIn(sum_lbl), run_time=0.9)
        self.wait(0.7)

        # two rounds of pulses traveling the weighted lines into the neuron
        for round_idx in range(2):
            pulses = VGroup()
            for l in lines:
                p = VGroup(
                    Dot(radius=0.13, color=CYAN, fill_opacity=0.35, stroke_width=0),
                    Dot(radius=0.065, color=WHITEISH),
                ).move_to(l.get_start())
                p.set_z_index(4)
                pulses.add(p)
            self.add(pulses)
            self.play(
                LaggedStart(*[MoveAlongPath(p, l) for p, l in zip(pulses, lines)],
                            lag_ratio=0.22),
                run_time=1.7,
            )
            # arrival -> neuron flash (scale 1 -> 1.25 -> 1, WHITEISH -> PINK -> WHITEISH)
            self.play(
                FadeOut(pulses),
                neuron.animate.scale(1.25).set_stroke(color=PINK),
                n_glow.animate.scale(1.25).set_fill(opacity=0.30),
                run_time=0.3,
            )
            self.play(
                neuron.animate.scale(0.8).set_stroke(color=WHITEISH),
                n_glow.animate.scale(0.8).set_fill(opacity=0.13),
                run_time=0.3,
            )
            if round_idx == 0:
                self.wait(0.6)

        # output arrow + traveling output pulse
        a_start = C + RIGHT * 0.62
        a_end = C + RIGHT * 3.4
        arrow = Arrow(a_start, a_end, buff=0, color=PINK, stroke_width=5,
                      max_tip_length_to_length_ratio=0.10)
        out_lbl = Text("out", font_size=22, color=PINK).next_to(a_end, UP, buff=0.25)
        arrow.set_z_index(0)
        out_lbl.set_z_index(3)
        self.play(GrowArrow(arrow), FadeIn(out_lbl, shift=LEFT * 0.15), run_time=0.7)

        out_pulse = VGroup(
            Dot(radius=0.13, color=PINK, fill_opacity=0.35, stroke_width=0),
            Dot(radius=0.065, color=WHITEISH),
        ).move_to(a_start)
        out_pulse.set_z_index(4)
        self.add(out_pulse)
        self.play(out_pulse.animate.move_to(a_end), run_time=0.8)
        self.play(FadeOut(out_pulse), run_time=0.25)
        self.play(FadeOut(title), run_time=0.5)
        self.wait(0.5)

        self.ch1_group = VGroup(in_glows, in_dots, x_labels, lines, w_labels,
                                n_glow, neuron, sum_lbl, arrow, out_lbl)

    # ------------------------------------------------------------------
    # Chapter 2 — many neurons become a network (~10s)
    # ------------------------------------------------------------------
    def chapter_network(self):
        self.play(FadeOut(self.ch1_group, scale=0.25), run_time=0.9)

        layers = [4, 6, 6, 2]
        x0, x1, span_y = -3.6, 3.6, 4.2
        glows, dots = VGroup(), VGroup()
        layer_dots, positions = [], []
        for li, n in enumerate(layers):
            x = x0 + li * (x1 - x0) / (len(layers) - 1)
            col_dots, col_pos = VGroup(), []
            for k in range(n):
                y = (k - (n - 1) / 2) * (span_y / max(n - 1, 1))
                p = [x, y, 0]
                c = phx(li / (len(layers) - 1))
                glows.add(Dot(p, radius=0.16, color=c, fill_opacity=0.22,
                              stroke_width=0))
                d = Dot(p, radius=0.08, color=c)
                dots.add(d)
                col_dots.add(d)
                col_pos.append(p)
            layer_dots.append(col_dots)
            positions.append(col_pos)

        edge_layers, edges = [], VGroup()
        for li in range(len(layers) - 1):
            grp = VGroup()
            for a in positions[li]:
                for b in positions[li + 1]:
                    e = Line(a, b, stroke_width=1.0, color=CYAN, stroke_opacity=0.18)
                    grp.add(e)
                    edges.add(e)
            edge_layers.append(grp)

        edges.set_z_index(0)
        glows.set_z_index(1)
        dots.set_z_index(2)

        self.play(
            Create(edges, lag_ratio=0.002),
            FadeIn(glows),
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.04),
            run_time=2.6,
        )
        self.wait(0.5)

        # two forward-pass waves: layer-by-layer cascade
        for wave in range(2):
            self.play(*[d.animate.scale(1.4) for d in layer_dots[0]], run_time=0.2)
            self.play(*[d.animate.scale(1 / 1.4) for d in layer_dots[0]], run_time=0.2)
            for li in range(len(layers) - 1):
                self.play(
                    *[e.animate.set_stroke(opacity=0.8, width=2.4)
                      for e in edge_layers[li]],
                    run_time=0.3,
                )
                self.play(
                    *[e.animate.set_stroke(opacity=0.18, width=1.0)
                      for e in edge_layers[li]],
                    *[d.animate.scale(1.45) for d in layer_dots[li + 1]],
                    run_time=0.26,
                )
                self.play(*[d.animate.scale(1 / 1.45) for d in layer_dots[li + 1]],
                          run_time=0.2)
            if wave == 0:
                self.wait(0.35)
        self.wait(0.7)

        self.net_dots = dots
        self.net_glows = glows
        self.net_edges = edges

    # ------------------------------------------------------------------
    # Chapter 3 — training: loss goes down, weights settle (~11s)
    # ------------------------------------------------------------------
    def chapter_training(self):
        dots, glows, edges = self.net_dots, self.net_glows, self.net_edges

        loss_lbl = Text("LOSS", font_size=22, color=WHITEISH, weight=BOLD)
        loss_lbl.move_to([-6.0, 3.25, 0])
        loss_num = DecimalNumber(2.40, num_decimal_places=2, mob_class=Text,
                                 font_size=34, color=PINK)
        loss_num.next_to(loss_lbl, RIGHT, buff=0.3)
        loss_lbl.set_z_index(3)
        loss_num.set_z_index(3)
        self.play(FadeIn(loss_lbl), FadeIn(loss_num), run_time=0.5)

        # three gradient-descent steps: deterministic edge flicker, loss drops
        for step, target in enumerate([1.52, 0.78, 0.31]):
            anims = []
            for idx, e in enumerate(edges):
                w = 0.6 + ((idx * 7 + step * 13) % 11) / 11 * 2.4
                op = 0.10 + ((idx * 5 + step * 3) % 9) / 9 * 0.55
                anims.append(e.animate.set_stroke(width=w, opacity=op))
            self.play(
                LaggedStart(*anims, lag_ratio=0.002),
                ChangeDecimalToValue(loss_num, target),
                run_time=1.35,
            )
            self.wait(0.3)

        # converged: edges settle to calm uniform opacity
        self.play(*[e.animate.set_stroke(width=1.3, opacity=0.32) for e in edges],
                  run_time=0.9)
        self.wait(0.4)

        # one slow golden glow pulse over the whole network, then hold
        self.play(
            *[d.animate.set_color(AMBER) for d in dots],
            *[g.animate.set_color(AMBER) for g in glows],
            *[e.animate.set_stroke(color=AMBER) for e in edges],
            rate_func=there_and_back,
            run_time=2.4,
        )
        self.wait(1.6)
        # no fade out — the editor handles the transition
