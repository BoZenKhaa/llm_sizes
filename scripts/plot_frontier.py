"""Plot frontier-at-release models over time on a log-scale param axis."""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from adjustText import adjust_text

CSV_PATH = Path(__file__).resolve().parent.parent / "llm_sizes.csv"
OUT_PATH = Path(__file__).resolve().parent.parent / "frontier_params.png"


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


def load_frontier() -> list[dict]:
    rows = []
    with CSV_PATH.open() as f:
        for r in csv.DictReader(f):
            if r["frontier_at_release"].lower() != "true":
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


ORG_COLORS = {
    "OpenAI": "#10a37f",
    "Anthropic": "#d97757",
    "Google": "#4285f4",
    "Google DeepMind": "#4285f4",
    "xAI": "#000000",
    "Meta": "#0668e1",
    "Mistral AI": "#ff7000",
    "DeepSeek": "#6366f1",
}

DISCLOSURE_MARKER = {
    "official": "o",
    "leaked": "s",
    "estimated": "^",
    "unknown": "x",
}


def main() -> None:
    rows = load_frontier()
    print(f"Plotting {len(rows)} frontier points")

    fig, ax = plt.subplots(figsize=(16, 10))

    orgs_seen = set()
    discs_seen = set()
    for r in rows:
        color = ORG_COLORS.get(r["org"], "#666666")
        marker = DISCLOSURE_MARKER.get(r["disclosure"], "o")
        label_org = r["org"] if r["org"] not in orgs_seen else None
        orgs_seen.add(r["org"])
        ax.scatter(
            r["date"], r["params"],
            s=80, c=color, marker=marker,
            edgecolors="black", linewidths=0.5,
            label=label_org, zorder=3,
        )
        discs_seen.add(r["disclosure"])

    texts = []
    for r in rows:
        label = f"{r['name']} ({fmt_params(r['params'])})"
        texts.append(ax.text(
            r["date"], r["params"], label,
            fontsize=8, zorder=4,
        ))

    ax.set_yscale("log")
    ax.set_xlabel("Announcement date")
    ax.set_ylabel("Total parameters (log scale)")
    ax.set_title(
        "Frontier LLM parameter counts over time\n"
        "(frontier_at_release=true rows with disclosed/leaked/estimated params)"
    )

    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=[1, 4, 7, 10]))
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%b"))
    ax.tick_params(axis="x", which="minor", labelsize=7, pad=16)

    ax.grid(which="major", axis="both", alpha=0.3)
    ax.grid(which="minor", axis="y", alpha=0.15)

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
    leg1 = ax.legend(handles=org_handles, title="Organization",
                     loc="upper left", fontsize=9)
    ax.add_artist(leg1)
    ax.legend(handles=disc_handles, title="Disclosure",
              loc="lower right", fontsize=9)

    adjust_text(
        texts, ax=ax,
        arrowprops=dict(arrowstyle="-", color="gray", alpha=0.5, lw=0.5),
        expand=(1.2, 1.4),
        force_text=(0.4, 0.6),
    )

    fig.tight_layout()
    fig.savefig(OUT_PATH, dpi=150)
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
