#!/usr/bin/env python3
"""Figure 2: application scenarios for the Project 3 report.

The layout intentionally echoes figure1.png: a bold title, blue Von Neumann
panel, green PIM panel, and a bottom key-difference strip.  The output is a
deterministic vector figure for LaTeX, avoiding generated-text artifacts.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import (
    FancyArrowPatch,
    FancyBboxPatch,
    Circle,
    Polygon,
    Rectangle,
)
from matplotlib.lines import Line2D


mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans", "sans-serif"],
        "pdf.fonttype": 42,
        "svg.fonttype": "none",
        "font.size": 9,
    }
)


INK = "#0f172a"
MUTED = "#334155"
LIGHT_TEXT = "#ffffff"
BLUE = "#1d4fb7"
BLUE_DARK = "#153a8a"
BLUE_LINE = "#4d7bd9"
BLUE_FILL = "#f3f7ff"
GREEN = "#208444"
GREEN_DARK = "#166534"
GREEN_LINE = "#39a766"
GREEN_FILL = "#f1fbf4"
PURPLE = "#6538c4"
ORANGE = "#f59e0b"
RED = "#d83a34"
GRAY_LINE = "#cbd5e1"


def rounded(ax, xy, w, h, edge, fill, lw=1.5, radius=0.18, z=2):
    box = FancyBboxPatch(
        xy,
        w,
        h,
        boxstyle=f"round,pad=0.02,rounding_size={radius}",
        linewidth=lw,
        edgecolor=edge,
        facecolor=fill,
        zorder=z,
    )
    ax.add_patch(box)
    return box


def label_box(ax, x, y, w, h, text, edge, fill, fs=10, weight="bold"):
    rounded(ax, (x, y), w, h, edge, fill, lw=1.35, radius=0.13)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        color=INK,
        fontsize=fs,
        fontweight=weight,
        linespacing=1.18,
        zorder=5,
    )


def arrow(ax, p0, p1, color, lw=2.2, style="-|>", ms=13, dashed=False):
    ax.add_patch(
        FancyArrowPatch(
            p0,
            p1,
            arrowstyle=style,
            mutation_scale=ms,
            linewidth=lw,
            color=color,
            linestyle=(0, (3, 2)) if dashed else "solid",
            zorder=5,
        )
    )


def chip_icon(ax, cx, cy, scale=1.0, color=BLUE_DARK):
    body_w, body_h = 0.62 * scale, 0.62 * scale
    rounded(
        ax,
        (cx - body_w / 2, cy - body_h / 2),
        body_w,
        body_h,
        color,
        "#eaf1ff",
        lw=1.4,
        radius=0.06 * scale,
        z=5,
    )
    for i in range(4):
        offset = (-0.32 + i * 0.21) * scale
        ax.add_line(Line2D([cx - 0.46 * scale, cx - 0.35 * scale], [cy + offset, cy + offset], color=color, lw=1.4))
        ax.add_line(Line2D([cx + 0.35 * scale, cx + 0.46 * scale], [cy + offset, cy + offset], color=color, lw=1.4))
        ax.add_line(Line2D([cx + offset, cx + offset], [cy - 0.46 * scale, cy - 0.35 * scale], color=color, lw=1.4))
        ax.add_line(Line2D([cx + offset, cx + offset], [cy + 0.35 * scale, cy + 0.46 * scale], color=color, lw=1.4))
    rounded(
        ax,
        (cx - 0.2 * scale, cy - 0.2 * scale),
        0.4 * scale,
        0.4 * scale,
        color,
        "#ffffff",
        lw=1.1,
        radius=0.04 * scale,
        z=6,
    )


def memory_stack(ax, x, y, w, h, color, fill):
    rounded(ax, (x, y), w, h, color, fill, lw=1.35, radius=0.08, z=4)
    rows, cols = 3, 6
    pad_x, pad_y = 0.13, 0.13
    cell_w = (w - 2 * pad_x - (cols - 1) * 0.06) / cols
    cell_h = (h - 2 * pad_y - (rows - 1) * 0.08) / rows
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(
                Rectangle(
                    (x + pad_x + c * (cell_w + 0.06), y + pad_y + r * (cell_h + 0.08)),
                    cell_w,
                    cell_h,
                    facecolor="#dbeafe" if color == BLUE_DARK else "#dff4e5",
                    edgecolor=color,
                    linewidth=0.6,
                    zorder=5,
                )
            )


def pim_array(ax, x, y, w, h):
    rounded(ax, (x, y), w, h, GREEN_DARK, "#e9f8ee", lw=1.5, radius=0.12, z=3)
    # Memory-bank grid.
    rows, cols = 3, 7
    pad_x, pad_y = 0.18, 0.18
    cell_w = (w - 2 * pad_x - (cols - 1) * 0.08) / cols
    cell_h = (h - 2 * pad_y - (rows - 1) * 0.08) / rows
    for r in range(rows):
        for c in range(cols):
            ax.add_patch(
                Rectangle(
                    (x + pad_x + c * (cell_w + 0.08), y + pad_y + r * (cell_h + 0.08)),
                    cell_w,
                    cell_h,
                    facecolor="#bde7c7",
                    edgecolor=GREEN_DARK,
                    linewidth=0.55,
                    zorder=4,
                )
            )
    # Compute units beside memory.
    for i, text in enumerate(["AI", "Graph", "DB"]):
        label_box(ax, x + 0.35 + i * 1.18, y + h - 0.78, 0.9, 0.42, text, GREEN_LINE, "#bff0cc", fs=7.6)
        arrow(ax, (x + 0.8 + i * 1.18, y + h - 0.8), (x + 0.8 + i * 1.18, y + h - 1.16), GREEN_DARK, lw=1.5, ms=8)


def warning_icon(ax, x, y):
    tri = Polygon([[x, y + 0.35], [x - 0.33, y - 0.25], [x + 0.33, y - 0.25]], closed=True, facecolor="#fee2e2", edgecolor=RED, linewidth=1.3, zorder=6)
    ax.add_patch(tri)
    ax.text(x, y - 0.02, "!", ha="center", va="center", fontsize=16, color=RED, fontweight="bold", zorder=7)


def check_icon(ax, x, y):
    ax.add_patch(Circle((x, y), 0.33, facecolor="#dff7e6", edgecolor=GREEN_LINE, linewidth=1.4, zorder=6))
    ax.add_line(Line2D([x - 0.12, x - 0.02], [y - 0.02, y - 0.13], color=GREEN, lw=3.0, solid_capstyle="round", zorder=7))
    ax.add_line(Line2D([x - 0.02, x + 0.16], [y - 0.13, y + 0.14], color=GREEN, lw=3.0, solid_capstyle="round", zorder=7))


def bottom_metric(ax, x0, title, detail, color, icon_kind):
    if icon_kind == "flow":
        ax.add_patch(Circle((x0, 1.0), 0.27, facecolor="#dbeafe", edgecolor=BLUE_LINE, linewidth=1.3, zorder=4))
        arrow(ax, (x0 - 0.07, 0.78), (x0 - 0.07, 1.22), BLUE, lw=2.1, ms=8)
        arrow(ax, (x0 + 0.07, 1.22), (x0 + 0.07, 0.78), BLUE, lw=2.1, ms=8)
    elif icon_kind == "pin":
        ax.add_patch(Circle((x0, 1.0), 0.27, facecolor="#dcfce7", edgecolor=GREEN_LINE, linewidth=1.3, zorder=4))
        ax.text(x0, 1.0, "●", ha="center", va="center", fontsize=16, color=GREEN, zorder=5)
    elif icon_kind == "bolt":
        bolt = Polygon(
            [
                [x0 - 0.07, 1.28],
                [x0 - 0.23, 0.95],
                [x0 - 0.04, 0.95],
                [x0 - 0.12, 0.68],
                [x0 + 0.22, 1.07],
                [x0 + 0.03, 1.07],
            ],
            closed=True,
            facecolor="#fbbf24",
            edgecolor=ORANGE,
            linewidth=1.5,
            zorder=5,
        )
        ax.add_patch(bolt)
    else:
        ax.add_patch(Circle((x0, 1.0), 0.27, facecolor="#ede9fe", edgecolor=PURPLE, linewidth=1.3, zorder=4))
        arrow(ax, (x0 - 0.18, 1.0), (x0 + 0.18, 1.0), PURPLE, lw=1.8, ms=7)
        arrow(ax, (x0 + 0.18, 0.9), (x0 - 0.18, 0.9), PURPLE, lw=1.8, ms=7)
    ax.text(x0 + 0.45, 1.18, title, ha="left", va="center", fontsize=9.2, color=color, fontweight="bold")
    ax.text(x0 + 0.45, 0.72, detail, ha="left", va="center", fontsize=8.0, color=INK, fontweight="bold", linespacing=1.12)


fig = plt.figure(figsize=(14.4, 8.0), facecolor="white")
ax = fig.add_axes([0.02, 0.02, 0.96, 0.96])
ax.set_xlim(0, 14.4)
ax.set_ylim(0, 8.0)
ax.axis("off")

ax.text(
    7.2,
    7.72,
    "Application Scenarios and Problems Solved",
    ha="center",
    va="center",
    fontsize=25,
    fontweight="bold",
    color="#050816",
)

# Main top panels.
rounded(ax, (0.08, 2.28), 6.25, 4.82, BLUE_LINE, "#fbfdff", lw=1.4, radius=0.13, z=1)
rounded(ax, (6.58, 2.28), 7.74, 4.82, GREEN_LINE, "#fbfffc", lw=1.4, radius=0.13, z=1)
rounded(ax, (0.08, 6.62), 6.25, 0.48, BLUE_DARK, BLUE, lw=1.4, radius=0.13, z=2)
rounded(ax, (6.58, 6.62), 7.74, 0.48, GREEN_DARK, GREEN, lw=1.4, radius=0.13, z=2)
ax.text(3.2, 6.86, "Von Neumann Architecture", ha="center", va="center", fontsize=13.5, color=LIGHT_TEXT, fontweight="bold")
ax.text(10.45, 6.86, "Processing-in-Memory (PIM)", ha="center", va="center", fontsize=13.5, color=LIGHT_TEXT, fontweight="bold")

# Left panel: control-centric execution.
label_box(ax, 0.55, 5.0, 1.65, 0.8, "CPU", BLUE_LINE, BLUE_FILL, fs=12)
chip_icon(ax, 1.38, 4.18, scale=0.9, color=BLUE_DARK)
memory_stack(ax, 4.55, 4.45, 1.25, 1.15, BLUE_DARK, "#f2f7ff")
ax.text(5.18, 5.82, "Memory", ha="center", va="center", fontsize=12, color=INK, fontweight="bold")
arrow(ax, (2.35, 5.34), (4.35, 5.34), BLUE_LINE, lw=2.3)
arrow(ax, (4.35, 4.82), (2.35, 4.82), RED, lw=2.3)
ax.text(3.35, 5.62, "instructions & data", ha="center", va="bottom", fontsize=8.2, color=BLUE_DARK, fontweight="bold")
ax.text(3.35, 4.55, "results", ha="center", va="top", fontsize=8.2, color=RED, fontweight="bold")
ax.add_line(Line2D([0.58, 5.82], [3.68, 3.68], color=BLUE_DARK, lw=2.2))
ax.text(3.2, 3.4, "control flow + mature software ecosystem", ha="center", fontsize=10, color=BLUE_DARK, fontweight="bold")

# Workload tiles, left.
left_tiles = [
    ("Operating\nsystems", 0.55, 2.78),
    ("Compilers", 2.0, 2.78),
    ("Branch-heavy\nlogic", 3.45, 2.78),
    ("General\npurpose", 4.9, 2.78),
]
for text, x, y in left_tiles:
    label_box(ax, x, y, 1.2, 0.58, text, "#9bb8ef", "#eef5ff", fs=7.7)

rounded(ax, (0.98, 2.45), 4.48, 0.48, RED, "#fff6f5", lw=1.1, radius=0.07, z=2)
warning_icon(ax, 1.35, 2.69)
ax.text(
    3.45,
    2.69,
    "Flexible general-purpose computing,\nbut costly data movement",
    ha="center",
    va="center",
    fontsize=8.6,
    color=INK,
    fontweight="bold",
    linespacing=1.1,
)

# Right panel: near-data execution.
label_box(ax, 7.05, 5.15, 1.15, 0.72, "Host\nCPU", GREEN_LINE, GREEN_FILL, fs=9)
chip_icon(ax, 7.62, 4.42, scale=0.82, color=GREEN_DARK)
pim_array(ax, 9.1, 3.95, 4.0, 1.95)
ax.text(11.1, 6.13, "Memory with Compute Units", ha="center", va="center", fontsize=12.5, color=INK, fontweight="bold")
arrow(ax, (8.25, 5.4), (8.98, 5.4), GREEN, lw=2.1, dashed=True)
arrow(ax, (8.98, 4.48), (8.25, 4.48), GREEN, lw=2.1)
ax.text(8.62, 5.62, "commands", ha="center", fontsize=8.0, color=GREEN_DARK, fontweight="bold")
ax.text(8.62, 4.15, "reduced\nresults", ha="center", fontsize=8.0, color=GREEN_DARK, fontweight="bold")

right_tiles = [
    ("AI inference", 7.0, 2.98),
    ("Graph\nprocessing", 8.42, 2.98),
    ("Database\nscan/filter", 9.84, 2.98),
    ("Bioinformatics", 11.26, 2.98),
    ("Edge\nanalytics", 12.68, 2.98),
]
for text, x, y in right_tiles:
    label_box(ax, x, y, 1.17, 0.62, text, "#93d7a8", "#effbf2", fs=7.35)

rounded(ax, (8.0, 2.45), 4.95, 0.48, GREEN_LINE, "#f2fff5", lw=1.1, radius=0.07, z=2)
check_icon(ax, 8.38, 2.69)
ax.text(
    10.78,
    2.69,
    "Compute near data\nless traffic & lower energy",
    ha="center",
    va="center",
    fontsize=8.8,
    color=INK,
    fontweight="bold",
    linespacing=1.08,
)

# Bottom strip.
rounded(ax, (0.08, 0.20), 14.24, 1.6, "#b8b5e8", "#fbfaff", lw=1.35, radius=0.12, z=1)
ax.text(7.2, 1.56, "Key Difference", ha="center", va="center", fontsize=14, color=PURPLE, fontweight="bold")
for x in [3.48, 7.25, 10.62]:
    ax.add_line(Line2D([x, x], [0.42, 1.28], color="#9b8bd7", lw=1.0, linestyle=(0, (4, 3))))

bottom_metric(ax, 0.75, "Best Fit", "Von Neumann:\ncontrol flow", BLUE, "flow")
bottom_metric(ax, 4.15, "Data Pattern", "PIM:\nmemory-bound parallelism", GREEN, "pin")
bottom_metric(ax, 7.9, "Energy Driver", "Data movement\nis the bottleneck", ORANGE, "bolt")
bottom_metric(ax, 11.12, "Hybrid Future", "CPU orchestrates;\nPIM accelerates", PURPLE, "hybrid")

fig.savefig("application_scenarios.pdf", bbox_inches="tight")
fig.savefig("application_scenarios.svg", bbox_inches="tight")
fig.savefig("application_scenarios.png", dpi=220, bbox_inches="tight")
print("wrote application_scenarios.pdf / .svg / .png")
