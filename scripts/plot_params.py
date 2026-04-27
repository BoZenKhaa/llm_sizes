"""Plot LLM param counts over time — frontier-only, open-only, and combined."""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
from adjustText import adjust_text

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "llm_sizes.csv"

ORG_COLORS = {
    "OpenAI": "#10a37f",
    "Anthropic": "#d97757",
    "Google": "#4285f4",
    "Google DeepMind": "#4285f4",
    "xAI": "#000000",
    "Meta": "#0668e1",
    "Mistral AI": "#ff7000",
    "DeepSeek": "#6366f1",
    "Alibaba/Qwen": "#a855f7",
    "Microsoft": "#00bcf2",
    "NVIDIA": "#76b900",
    "TII": "#b91c1c",
    "01.AI": "#f59e0b",
    "Cohere": "#ec4899",
    "EleutherAI": "#8b5cf6",
    "AI21 Labs": "#ef4444",
    "Databricks": "#ff3621",
    "Snowflake": "#29b5e8",
    "Reka AI": "#14b8a6",
}

DISCLOSURE_MARKER = {
    "official": "o",
    "leaked": "s",
    "estimated": "^",
    "unknown": "x",
}


def fmt_params(n: float) -> str:
    if n >= 1e12:
        v = n / 1e12
        return f"{v:.1f}T" if v < 10 else f"{v:.0f}T"
    if n >= 1e9:
        v = n / 1e9
        return f"{v:.1f}B" if v < 10 else f"{v:.0f}B"
    if n >= 1e6:
        return f"{n / 1e6:.0f}M"
    return f"{n:.0f}"


def load_rows(flag: str) -> list[dict]:
    rows = []
    with CSV_PATH.open() as f:
        for r in csv.DictReader(f):
            if r[flag].lower() != "true":
                continue
            if not r["total_params"]:
                continue
            rows.append({
                "name": r["model_name"],
                "org": r["organization"],
                "date": date.fromisoformat(r["announcement_date"]),
                "params": float(r["total_params"]),
                "disclosure": r["param_disclosure"],
            })
    rows.sort(key=lambda x: x["date"])
    return rows


def decimal_year(d: date) -> float:
    start = date(d.year, 1, 1).toordinal()
    end = date(d.year + 1, 1, 1).toordinal()
    return d.year + (d.toordinal() - start) / (end - start)


def fit_loglinear(rows: list[dict]) -> tuple[np.ndarray, float]:
    """Returns (poly_coeffs, doubling_years) for log10(params) vs decimal_year."""
    x = np.array([decimal_year(r["date"]) for r in rows])
    y = np.log10(np.array([r["params"] for r in rows]))
    coeffs = np.polyfit(x, y, 1)
    slope = coeffs[0]  # log10(params) per year
    doubling = np.log10(2) / slope if slope > 0 else float("inf")
    return coeffs, doubling


def scatter_points(ax, rows, face_alpha=1.0, edge="black", marker_override=None):
    orgs_seen = set()
    discs_seen = set()
    for r in rows:
        color = ORG_COLORS.get(r["org"], "#666666")
        marker = marker_override or DISCLOSURE_MARKER.get(r["disclosure"], "o")
        ax.scatter(
            r["date"], r["params"],
            s=80, c=color, marker=marker,
            edgecolors=edge, linewidths=0.5,
            alpha=face_alpha, zorder=3,
        )
        orgs_seen.add(r["org"])
        discs_seen.add(r["disclosure"])
    return orgs_seen, discs_seen


def annotate(ax, rows):
    texts = []
    for r in rows:
        label = f"{r['name']} ({fmt_params(r['params'])})"
        texts.append(ax.text(
            r["date"], r["params"], label,
            fontsize=8, zorder=4,
        ))
    return texts


def style_axes(ax, title):
    ax.set_yscale("log")
    ax.set_xlabel("Announcement date")
    ax.set_ylabel("Total parameters (log scale)")
    ax.set_title(title)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%b"))
    ax.tick_params(axis="x", which="minor", labelsize=7, pad=16)
    ax.grid(which="major", axis="both", alpha=0.3)
    ax.grid(which="minor", axis="y", alpha=0.15)


def legend_handles(orgs_seen, discs_seen):
    org_handles = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
                   markeredgecolor="black", markersize=8, label=org)
        for org, c in ORG_COLORS.items() if org in orgs_seen
    ]
    disc_handles = [
        plt.Line2D([0], [0], marker=m, color="w", markerfacecolor="#888",
                   markeredgecolor="black", markersize=8, label=d)
        for d, m in DISCLOSURE_MARKER.items() if d in discs_seen
    ]
    return org_handles, disc_handles


def plot_single(rows, title, out_path, trend_color="#333333", trend_label_prefix="trend"):
    fig, ax = plt.subplots(figsize=(16, 10))
    orgs_seen, discs_seen = scatter_points(ax, rows)
    texts = annotate(ax, rows)

    coeffs, doubling = fit_loglinear(rows)
    xs = np.array([decimal_year(min(r["date"] for r in rows)),
                   decimal_year(max(r["date"] for r in rows))])
    ys = 10 ** np.polyval(coeffs, xs)
    x_dates = [date(int(x), 1, 1).replace(
        month=max(1, min(12, int((x % 1) * 12) + 1))) for x in xs]
    ax.plot(x_dates, ys, "--", color=trend_color, lw=2, alpha=0.7,
            label=f"{trend_label_prefix}: ×2 every {doubling:.2f} yr "
                  f"(10^({coeffs[0]:+.3f}·yr{coeffs[1]:+.1f}))",
            zorder=2)

    style_axes(ax, title)
    org_handles, disc_handles = legend_handles(orgs_seen, discs_seen)

    leg1 = ax.legend(handles=org_handles, title="Organization",
                     loc="upper left", fontsize=9)
    ax.add_artist(leg1)
    leg2 = ax.legend(handles=disc_handles, title="Disclosure",
                     loc="lower right", fontsize=9)
    ax.add_artist(leg2)
    ax.legend(loc="upper center", fontsize=9)

    adjust_text(
        texts, ax=ax,
        arrowprops=dict(arrowstyle="-", color="gray", alpha=0.5, lw=0.5),
        expand=(1.2, 1.4),
        force_text=(0.4, 0.6),
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"Wrote {out_path}  (n={len(rows)}, doubling={doubling:.2f} yr)")


def plot_combined(frontier, open_rows, out_path):
    fig, ax = plt.subplots(figsize=(18, 11))

    orgs_all = set()
    discs_all = set()

    # open-weight (hollow markers)
    for r in open_rows:
        color = ORG_COLORS.get(r["org"], "#666666")
        marker = DISCLOSURE_MARKER.get(r["disclosure"], "o")
        ax.scatter(r["date"], r["params"], s=90,
                   facecolors="none", edgecolors=color,
                   marker=marker, linewidths=1.6, zorder=3)
        orgs_all.add(r["org"])
        discs_all.add(r["disclosure"])
    # frontier (solid)
    for r in frontier:
        color = ORG_COLORS.get(r["org"], "#666666")
        marker = DISCLOSURE_MARKER.get(r["disclosure"], "o")
        ax.scatter(r["date"], r["params"], s=80, c=color,
                   marker=marker, edgecolors="black", linewidths=0.5,
                   zorder=4)
        orgs_all.add(r["org"])
        discs_all.add(r["disclosure"])

    # labels: dedupe models flagged in both sets
    seen = set()
    combined = []
    for r in frontier + open_rows:
        key = (r["name"], r["date"])
        if key in seen:
            continue
        seen.add(key)
        combined.append(r)
    texts = annotate(ax, combined)

    # trend lines
    all_dates = [r["date"] for r in combined]
    xs_full = np.array([decimal_year(min(all_dates)),
                        decimal_year(max(all_dates))])

    for label_prefix, group, color in [
        ("Frontier trend", frontier, "#d97757"),
        ("Open-weight frontier trend", open_rows, "#10a37f"),
    ]:
        coeffs, doubling = fit_loglinear(group)
        ys = 10 ** np.polyval(coeffs, xs_full)
        x_dates = [date(int(x), 1, 1).replace(
            month=max(1, min(12, int((x % 1) * 12) + 1))) for x in xs_full]
        ax.plot(x_dates, ys, "--", color=color, lw=2.2, alpha=0.85,
                label=f"{label_prefix}: ×2 every {doubling:.2f} yr "
                      f"(slope={coeffs[0]:+.3f} log10(params)/yr)",
                zorder=5)

    style_axes(ax,
               "Frontier and open-weight frontier LLM parameter counts over time\n"
               "(solid = frontier_at_release; hollow = frontier_open_at_release)")
    org_handles, disc_handles = legend_handles(orgs_all, discs_all)

    leg1 = ax.legend(handles=org_handles, title="Organization",
                     loc="upper left", fontsize=9, ncol=2)
    ax.add_artist(leg1)
    leg2 = ax.legend(handles=disc_handles, title="Disclosure",
                     loc="lower right", fontsize=9)
    ax.add_artist(leg2)
    ax.legend(loc="upper center", fontsize=10)

    adjust_text(
        texts, ax=ax,
        arrowprops=dict(arrowstyle="-", color="gray", alpha=0.5, lw=0.5),
        expand=(1.2, 1.4),
        force_text=(0.4, 0.6),
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"Wrote {out_path}  "
          f"(frontier n={len(frontier)}, open n={len(open_rows)})")


def main() -> None:
    frontier = load_rows("frontier_at_release")
    open_rows = load_rows("frontier_open_at_release")

    plot_single(
        frontier,
        "Frontier LLM parameter counts over time\n"
        "(frontier_at_release=true rows with disclosed/leaked/estimated params)",
        ROOT / "frontier_params.png",
        trend_color="#d97757",
        trend_label_prefix="Frontier trend",
    )
    plot_single(
        open_rows,
        "Open-weight frontier LLM parameter counts over time\n"
        "(frontier_open_at_release=true rows with disclosed/leaked/estimated params)",
        ROOT / "open_params.png",
        trend_color="#10a37f",
        trend_label_prefix="Open-weight frontier trend",
    )
    plot_combined(frontier, open_rows, ROOT / "frontier_and_open_params.png")


if __name__ == "__main__":
    main()
