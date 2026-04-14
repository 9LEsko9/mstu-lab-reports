"""
Генерация ВАХ идеальных источников напряжения (V1) и тока (I1)
для лабораторной работы №1 по электротехнике.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os

# Путь для сохранения
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "images")

# ── Общие настройки стиля ──────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Serif",
    "font.size": 12,
    "axes.linewidth": 1.2,
    "axes.grid": True,
    "grid.linestyle": "--",
    "grid.alpha": 0.5,
    "lines.linewidth": 2.2,
})

# ══════════════════════════════════════════════════════════════════════════════
# 1. ВАХ идеального источни��а напряжения V1 = 38 В
#    Горизонтальная прямая u = 38 В при любом i
# ══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(7, 5))

# Диапазон токов: от 0 до 0.5 А
i_v = np.array([0, 0.5])
u_v = np.full_like(i_v, 38.0)

ax.plot(i_v, u_v, color="#1f77b4", marker="o", markersize=6, markevery=[0,1], zorder=3)

# Точки из таблицы 1.11
i_pts = np.array([0.038, 0.076, 0.38])
u_pts = np.array([38.004, 38.004, 38.004])
ax.scatter(i_pts, u_pts, color="#d62728", zorder=5, s=60, label="Точки измерений")

# Аннотация горизонтальной прямой
ax.annotate(r"$u = 38$ В", xy=(0.25, 38), xytext=(0.25, 39.2),
            fontsize=12, ha="center",
            color="#1f77b4")

ax.set_xlabel("$i$, А", fontsize=13)
ax.set_ylabel("$u$, В", fontsize=13)
ax.set_title("ВАХ идеального источника напряжения $V_1 = 38$ В", fontsize=13)
ax.set_xlim(-0.02, 0.52)
ax.set_ylim(37.5, 39.5)
ax.legend(fontsize=11)
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

plt.tight_layout()
out_v1 = os.path.join(OUT_DIR, "VAH_V1.png")
fig.savefig(out_v1, dpi=200, bbox_inches="tight")
plt.close(fig)
print(f"Сохранено: {out_v1}")

# ══════════════════════════════════════════════════════════════════════════════
# 2. ВАХ идеального источника тока I1 = 38 А
#    Вертикальная прямая i = 38 А при любом u
# ══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(7, 5))

# Диапазон напряжений: от 0 до 40000 В
u_range = np.array([0, 40000])
i_range = np.full_like(u_range, 38.0)

ax.plot(u_range, i_range, color="#ff7f0e", marker="o", markersize=6, markevery=[0,1], zorder=3)

# Точки из таблицы 1.12
u_pts2 = np.array([0.0038, 7600, 19000, 38000])
i_pts2 = np.array([38, 38, 38, 38])
ax.scatter(u_pts2, i_pts2, color="#d62728", zorder=5, s=60, label="Точки измерений")

ax.annotate(r"$i = 38$ А", xy=(15000, 38), xytext=(15000, 38.35),
            fontsize=12, ha="center",
            color="#ff7f0e")

ax.set_xlabel("$u$, В", fontsize=13)
ax.set_ylabel("$i$, А", fontsize=13)
ax.set_title("ВАХ идеального источника тока $I_1 = 38$ А", fontsize=13)
ax.set_xlim(-2000, 42000)
ax.set_ylim(37.5, 38.5)
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", " ")))
ax.legend(fontsize=11)
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

plt.tight_layout()
out_i1 = os.path.join(OUT_DIR, "VAH_I1.png")
fig.savefig(out_i1, dpi=200, bbox_inches="tight")
plt.close(fig)
print(f"Сохранено: {out_i1}")
