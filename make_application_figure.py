#!/usr/bin/env python3
"""Application-landscape schematic for the Project 3 report (refined).

Core conclusion: each paradigm fits the workload class that matches its
data-movement cost -- Von Neumann for control-intensive / general-purpose work,
Processing-in-Memory for data-movement-bound work (AI inference, graph/DB).

Design goals: restrained Nature-style palette, hairline strokes, generous
whitespace, direct labels, an accurate ReRAM-crossbar motif (not gimmicky
symbols), panel letters a/b. Backend: matplotlib (exclusive). Vector PDF + SVG.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from matplotlib.lines import Line2D

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 8,
})

# --- restrained palette: ink + two desaturated accents + one muted cost cue ---
INK     = "#22303c"   # near-black slate for text and rules
SUBINK  = "#5d6b76"   # secondary gray for captions
VN      = "#3f6079"   # desaturated slate-blue  (Von Neumann)
VN_FILL = "#eef2f5"
PIM     = "#5f7d68"   # desaturated sage-green   (PIM)
PIM_FILL= "#eef2ec"
COST    = "#b07a3c"   # muted ochre for the data-movement cost cue
HAIR    = 0.9         # hairline width

fig = plt.figure(figsize=(7.2, 3.15))
axL = fig.add_axes([0.045, 0.07, 0.43, 0.86]); axL.set_xlim(0, 10); axL.set_ylim(0, 10)
axR = fig.add_axes([0.525, 0.07, 0.43, 0.86]); axR.set_xlim(0, 10); axR.set_ylim(0, 10)
for ax in (axL, axR):
    ax.axis("off")


def node(ax, x, y, w, h, label, edge, fill, fs=8.5):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.0,rounding_size=0.22",
        linewidth=1.2, edgecolor=edge, facecolor=fill, zorder=3))
    ax.text(x + w/2, y + h/2, label, ha="center", va="center",
            fontsize=fs, color=INK, zorder=4)


def panel_label(ax, letter, title, color):
    ax.text(-0.2, 10.4, letter, ha="left", va="top", fontsize=11,
            fontweight="bold", color=INK)
    ax.text(1.05, 10.4, title, ha="left", va="top", fontsize=9.5,
            fontweight="bold", color=color)


def footer(ax, items, color):
    # left margin, uniform baseline grid: heading + items share one step
    x0, y0, step = 0.2, 2.05, 0.62
    ax.add_line(Line2D([x0, 9.8], [y0 + 0.5, y0 + 0.5], color="#d7dde1",
                       lw=HAIR, zorder=1))
    ax.text(x0, y0, "Where it fits", ha="left", va="center",
            fontsize=7.4, fontweight="bold", color=color)
    for k, it in enumerate(items, start=1):
        ax.text(x0, y0 - k * step, it, ha="left", va="center",
                fontsize=7.3, color=SUBINK)


# ============================ a · Von Neumann ============================
panel_label(axL, "a", "Von Neumann", VN)
node(axL, 0.5, 6.4, 3.0, 1.9, "CPU", VN, VN_FILL)
node(axL, 6.5, 6.4, 3.0, 1.9, "Memory", VN, VN_FILL)

# data round-trip across the bus: two thin offset arrows + a constriction
axL.add_patch(FancyArrowPatch((3.6, 7.75), (6.4, 7.75), arrowstyle="-|>",
              mutation_scale=10, lw=1.1, color=INK,
              connectionstyle="arc3,rad=-0.18", zorder=2))
axL.add_patch(FancyArrowPatch((6.4, 6.95), (3.6, 6.95), arrowstyle="-|>",
              mutation_scale=10, lw=1.1, color=INK,
              connectionstyle="arc3,rad=-0.18", zorder=2))
# constriction marker (the bottleneck) at mid-bus
axL.add_line(Line2D([5.0, 5.0], [7.05, 7.65], color=COST, lw=2.4, zorder=3))
axL.text(5.0, 8.7, "data movement", ha="center", fontsize=7.0, color=INK)
axL.text(5.0, 5.95, "bus bottleneck\n(memory wall)", ha="center", va="top",
         fontsize=6.6, color=COST, style="italic", linespacing=1.3)
footer(axL, ["General-purpose computing",
             "Operating systems & databases",
             "Control-intensive / branchy logic"], VN)

# ============================ b · Processing-in-Memory ============================
panel_label(axR, "b", "Processing-in-Memory", PIM)
# single fused block: memory array where computation happens in place
node(axR, 1.7, 5.6, 6.6, 2.9, "", PIM, PIM_FILL)
# ReRAM-crossbar motif: thin word/bit lines with conductance cells at crossings
gx0, gx1, gy0, gy1 = 2.5, 7.5, 6.1, 8.1
nv, nh = 5, 3
for i in range(nv):
    x = gx0 + (gx1 - gx0) * i / (nv - 1)
    axR.add_line(Line2D([x, x], [gy0, gy1], color=PIM, lw=0.7, zorder=4))
for j in range(nh):
    y = gy0 + (gy1 - gy0) * j / (nh - 1)
    axR.add_line(Line2D([gx0, gx1], [y, y], color=PIM, lw=0.7, zorder=4))
for i in range(nv):
    for j in range(nh):
        x = gx0 + (gx1 - gx0) * i / (nv - 1)
        y = gy0 + (gy1 - gy0) * j / (nh - 1)
        axR.add_patch(Circle((x, y), 0.12, facecolor=PIM, edgecolor="none",
                             zorder=5))
axR.text(5.0, 5.05, "compute in place — data stays put", ha="center",
         va="top", fontsize=6.8, color=PIM, style="italic")
footer(axR, ["AI / deep-learning inference (ReRAM crossbar)",
             "Edge analytics",
             "Graph processing & databases (UPMEM, HBM-PIM)"], PIM)

# thin divider between the two paradigms
fig.add_artist(Line2D([0.5, 0.5], [0.07, 0.9], color="#e1e6e9", lw=HAIR,
                      transform=fig.transFigure))

fig.savefig("application_scenarios.pdf", bbox_inches="tight")
fig.savefig("application_scenarios.svg", bbox_inches="tight")
print("wrote application_scenarios.pdf / .svg")
