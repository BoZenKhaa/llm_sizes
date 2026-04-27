# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "plotly>=5.22",
#     "numpy>=1.26",
# ]
# ///
"""Interactive plotly version of the combined frontier + open-weight plot.

Exports a self-contained HTML file with:
  - hover tooltip showing model name, org, date, params, disclosure, capabilities
  - click handler that populates a side panel with capabilities + source links
  - per-org and per-disclosure custom legend
  - log-linear trend lines for both groups
"""
from __future__ import annotations

import csv
import html
import json
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "llm_sizes.csv"
OUT_PATH = ROOT / "frontier_and_open_params.html"

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

DISCLOSURE_SYMBOL = {
    "official": "circle",
    "leaked": "square",
    "estimated": "triangle-up",
    "unknown": "x",
}

CAPABILITY_FIELDS = [
    ("cap_text", "text"),
    ("cap_vision", "vision"),
    ("cap_audio", "audio"),
    ("cap_video", "video"),
    ("cap_code_specialized", "code"),
    ("cap_reasoning", "reasoning"),
    ("cap_tool_use", "tool use"),
]


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


def decimal_year(d: date) -> float:
    start = date(d.year, 1, 1).toordinal()
    end = date(d.year + 1, 1, 1).toordinal()
    return d.year + (d.toordinal() - start) / (end - start)


def from_decimal_year(x: float) -> date:
    year = int(x)
    frac = x - year
    days = (date(year + 1, 1, 1) - date(year, 1, 1)).days
    return date(year, 1, 1) + timedelta(days=int(frac * days))


def load_rows() -> list[dict]:
    """Load every row that's flagged as either frontier or open-weight frontier."""
    rows = []
    with CSV_PATH.open() as f:
        for r in csv.DictReader(f):
            frontier = r["frontier_at_release"].lower() == "true"
            open_w = r["frontier_open_at_release"].lower() == "true"
            if not (frontier or open_w):
                continue
            if not r["total_params"]:
                continue
            caps = [label for col, label in CAPABILITY_FIELDS
                    if r.get(col, "").strip().lower() == "true"]
            rows.append({
                "name": r["model_name"],
                "org": r["organization"],
                "date": date.fromisoformat(r["announcement_date"]),
                "params": float(r["total_params"]),
                "active_params": (float(r["active_params"])
                                  if r.get("active_params") else None),
                "disclosure": r["param_disclosure"] or "unknown",
                "architecture": r.get("architecture_type", "") or "—",
                "context_window": r.get("context_window", "") or "—",
                "open_weights": r.get("open_weights", "").lower() == "true",
                "capabilities": caps,
                "release_url": r.get("release_url", "") or "",
                "supporting_url": r.get("supporting_url", "") or "",
                "frontier": frontier,
                "frontier_open": open_w,
            })
    rows.sort(key=lambda x: x["date"])
    return rows


def fit_loglinear(rows: list[dict]) -> tuple[np.ndarray, float]:
    x = np.array([decimal_year(r["date"]) for r in rows])
    y = np.log10(np.array([r["params"] for r in rows]))
    coeffs = np.polyfit(x, y, 1)
    slope = coeffs[0]
    doubling = np.log10(2) / slope if slope > 0 else float("inf")
    return coeffs, doubling


def make_customdata(r: dict) -> list:
    """Per-point payload consumed by the click handler in JS."""
    return [
        r["name"],
        r["org"],
        r["date"].isoformat(),
        fmt_params(r["params"]),
        r["disclosure"],
        r["architecture"],
        ", ".join(r["capabilities"]) or "—",
        r["release_url"],
        r["supporting_url"],
    ]


def hover_template() -> str:
    return (
        "<b>%{customdata[0]}</b><br>"
        "%{customdata[1]} · %{customdata[2]}<br>"
        "Params: %{customdata[3]} (%{customdata[4]})<br>"
        "Architecture: %{customdata[5]}<br>"
        "Capabilities: %{customdata[6]}<br>"
        "<i>click for source links</i>"
        "<extra></extra>"
    )


def build_scatter(rows: list[dict], *, hollow: bool, name: str) -> go.Scatter:
    xs = [r["date"] for r in rows]
    ys = [r["params"] for r in rows]
    colors = [ORG_COLORS.get(r["org"], "#666666") for r in rows]
    # Use "-open" variants for hollow group; "x" has an "x-open" too but its
    # outline can be invisible at small sizes, so keep it as "x".
    def sym(d: str) -> str:
        base = DISCLOSURE_SYMBOL.get(d, "circle")
        if hollow and base != "x":
            return f"{base}-open"
        return base
    symbols = [sym(r["disclosure"]) for r in rows]
    customdata = [make_customdata(r) for r in rows]

    if hollow:
        marker = dict(
            symbol=symbols,
            size=14,
            color=colors,
            line=dict(width=2, color=colors),
        )
    else:
        marker = dict(
            symbol=symbols,
            size=13,
            color=colors,
            line=dict(width=0.6, color="black"),
        )
    names = [r["name"] for r in rows]
    return go.Scatter(
        x=xs, y=ys, mode="markers+text",
        name=name,
        marker=marker,
        text=names,
        textposition="top center",
        textfont=dict(size=9, color=colors),
        cliponaxis=False,
        customdata=customdata,
        hovertemplate=hover_template(),
        legendgroup=name,
    )


def build_trend(rows: list[dict], all_rows: list[dict], *, name: str,
                color: str) -> tuple[go.Scatter, str]:
    coeffs, doubling = fit_loglinear(rows)
    all_dates = [r["date"] for r in all_rows]
    xs_year = np.array([decimal_year(min(all_dates)),
                        decimal_year(max(all_dates))])
    ys = 10 ** np.polyval(coeffs, xs_year)
    x_dates = [from_decimal_year(x) for x in xs_year]
    label = f"{name} (×2 every {doubling:.2f} yr)"
    trace = go.Scatter(
        x=x_dates, y=ys, mode="lines",
        name=label,
        line=dict(color=color, width=2.4, dash="dash"),
        hoverinfo="skip",
        legendgroup=name,
    )
    return trace, label


def build_figure(frontier: list[dict], open_rows: list[dict]) -> go.Figure:
    fig = go.Figure()
    # open first (drawn behind), then frontier
    fig.add_trace(build_scatter(open_rows, hollow=True,
                                name="Open-weight frontier"))
    fig.add_trace(build_scatter(frontier, hollow=False,
                                name="Frontier (closed-weight)"))

    all_rows = frontier + open_rows
    trend_open, _ = build_trend(open_rows, all_rows,
                                name="Open-weight trend", color="#10a37f")
    trend_front, _ = build_trend(frontier, all_rows,
                                 name="Frontier trend", color="#d97757")
    fig.add_trace(trend_open)
    fig.add_trace(trend_front)

    fig.update_layout(
        title=dict(
            text=("Frontier and open-weight frontier LLM parameter counts<br>"
                  "<sub>solid markers = frontier_at_release · "
                  "hollow markers = frontier_open_at_release · "
                  "click a point for capabilities &amp; source links</sub>"),
            x=0.5, xanchor="center",
        ),
        xaxis=dict(title="Announcement date", showgrid=True,
                   gridcolor="rgba(0,0,0,0.08)"),
        yaxis=dict(title="Total parameters (log scale)", type="log",
                   showgrid=True, gridcolor="rgba(0,0,0,0.08)"),
        legend=dict(orientation="h", x=0.5, y=-0.18, xanchor="center",
                    yanchor="top",
                    entrywidth=210, entrywidthmode="pixels",
                    bgcolor="rgba(255,255,255,0.85)"),
        hoverlabel=dict(bgcolor="white", font_size=12,
                        bordercolor="#999"),
        plot_bgcolor="white",
        margin=dict(l=70, r=40, t=90, b=140),
        height=760,
    )
    return fig


def render_org_legend() -> str:
    items = []
    for org, color in ORG_COLORS.items():
        items.append(
            f'<li><span class="swatch" style="background:{color}"></span>'
            f'{html.escape(org)}</li>'
        )
    return "\n".join(items)


def render_disclosure_legend() -> str:
    # Tiny inline SVG glyphs that mirror the plotly markers.
    glyphs = {
        "official":  '<circle cx="9" cy="9" r="5" fill="#555" />',
        "leaked":    '<rect x="4" y="4" width="10" height="10" fill="#555" />',
        "estimated": '<polygon points="9,3 15,14 3,14" fill="#555" />',
        "unknown":   ('<line x1="4" y1="4" x2="14" y2="14" '
                      'stroke="#555" stroke-width="2" />'
                      '<line x1="14" y1="4" x2="4" y2="14" '
                      'stroke="#555" stroke-width="2" />'),
    }
    items = []
    for disc, glyph in glyphs.items():
        items.append(
            f'<li><svg width="18" height="18" viewBox="0 0 18 18">{glyph}'
            f'</svg>{html.escape(disc)}</li>'
        )
    return "\n".join(items)


PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LLM parameter counts — interactive</title>
<style>
  :root {{ --border:#e1e4e8; --muted:#6b7280; --accent:#1f6feb; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
          margin:0; color:#1f2328; background:#fafbfc; }}
  header {{ padding:18px 24px; border-bottom:1px solid var(--border);
            background:#fff; }}
  header h1 {{ margin:0 0 4px; font-size:18px; }}
  header p  {{ margin:0; color:var(--muted); font-size:13px; }}
  .layout {{ display:flex; flex-direction:column; gap:16px;
             padding:16px 24px; }}
  #chart-wrap {{ background:#fff; border:1px solid var(--border);
                 border-radius:6px; padding:8px; }}
  .chart-tools {{ display:flex; justify-content:flex-end; gap:8px; }}
  .chart-tools button {{ font:inherit; font-size:12px; cursor:pointer;
                          background:#fff; border:1px solid var(--border);
                          border-radius:6px; padding:6px 12px;
                          color:#1f2328; }}
  .chart-tools button:hover {{ background:#f3f4f6; }}
  .chart-tools button[aria-pressed="true"] {{ background:#eef2ff;
                                                border-color:#c7d2fe;
                                                color:#3730a3; }}
  .cards-row {{ display:grid; grid-template-columns: 1fr 1fr 2fr;
                gap:16px; }}
  @media (max-width: 900px) {{
    .cards-row {{ grid-template-columns: 1fr; }}
  }}
  .card {{ background:#fff; border:1px solid var(--border); border-radius:6px;
           padding:14px 16px; }}
  .card h2 {{ margin:0 0 8px; font-size:14px;
              text-transform:uppercase; letter-spacing:0.04em;
              color:var(--muted); font-weight:600; }}
  .card h3 {{ margin:0 0 4px; font-size:16px; }}
  .card .meta {{ color:var(--muted); font-size:12px; margin-bottom:10px; }}
  .card ul {{ list-style:none; padding:0; margin:0; font-size:12px; }}
  .card li {{ display:flex; align-items:center; gap:8px;
              margin:3px 0; line-height:1.4; }}
  .swatch {{ display:inline-block; width:14px; height:14px;
             border-radius:50%; border:1px solid #00000020; }}
  #info .links a {{ color:var(--accent); text-decoration:none;
                    margin-right:10px; }}
  #info .links a:hover {{ text-decoration:underline; }}
  #info .caps {{ display:flex; flex-wrap:wrap; gap:6px;
                 margin:6px 0 12px; }}
  #info .caps span {{ background:#eef2ff; color:#3730a3;
                      border-radius:12px; padding:2px 10px;
                      font-size:11px; }}
  #info .empty {{ color:var(--muted); font-size:13px; }}
  .legend-grid {{ display:grid;
                  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
                  gap:6px 14px; }}
</style>
</head>
<body>
<header>
  <h1>Frontier &amp; open-weight frontier LLM parameter counts</h1>
  <p>Click any point to see its capabilities and source links.
     Drag to zoom; double-click to reset. Toggle traces using the
     legend below the chart.</p>
</header>
<div class="layout">
  <div class="chart-tools">
    <button id="toggle-labels" type="button" aria-pressed="true"
            title="Show or hide model name labels on the chart">
      Hide model labels
    </button>
  </div>
  <div id="chart-wrap">{chart_div}</div>
  <div class="cards-row">
    <div class="card" id="info">
      <h2>Selection</h2>
      <p class="empty">No point selected yet — click any marker on the
        chart and its details will appear here.</p>
    </div>
    <div class="card">
      <h2>Disclosure (marker shape)</h2>
      <ul>
        {disclosure_legend}
      </ul>
    </div>
    <div class="card">
      <h2>Organization (color)</h2>
      <ul class="legend-grid">
        {org_legend}
      </ul>
    </div>
  </div>
</div>
<script>
(function() {{
  const div = document.getElementById({chart_div_id_json});
  if (!div) return;
  const info = document.getElementById('info');
  const escapeHtml = (s) => String(s ?? '').replace(/[&<>"']/g, c => ({{
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }}[c]));
  const renderPoint = (cd) => {{
    const [name, org, dateStr, params, disclosure, arch, caps,
           releaseUrl, supportingUrl] = cd;
    const capChips = caps && caps !== '—'
      ? caps.split(',').map(s => s.trim())
            .filter(Boolean)
            .map(c => `<span>${{escapeHtml(c)}}</span>`).join('')
      : '<span style="background:#f3f4f6;color:#6b7280">none flagged</span>';
    const links = [];
    if (releaseUrl) {{
      links.push(`<a href="${{escapeHtml(releaseUrl)}}" target="_blank" `
                 + `rel="noopener">release announcement ↗</a>`);
    }}
    if (supportingUrl) {{
      links.push(`<a href="${{escapeHtml(supportingUrl)}}" target="_blank" `
                 + `rel="noopener">supporting source ↗</a>`);
    }}
    info.innerHTML = `
      <h2>Selection</h2>
      <h3>${{escapeHtml(name)}}</h3>
      <div class="meta">${{escapeHtml(org)}} · ${{escapeHtml(dateStr)}}
        · ${{escapeHtml(params)}} (${{escapeHtml(disclosure)}})
        · ${{escapeHtml(arch)}}</div>
      <div><strong>Capabilities</strong></div>
      <div class="caps">${{capChips}}</div>
      <div><strong>Sources</strong></div>
      <div class="links">${{links.join(' · ') || '<span class="empty">no URLs on file</span>'}}</div>
    `;
  }};
  div.on('plotly_click', (data) => {{
    if (data && data.points && data.points.length) {{
      renderPoint(data.points[0].customdata);
    }}
  }});

  const toggleBtn = document.getElementById('toggle-labels');
  if (toggleBtn) {{
    toggleBtn.addEventListener('click', () => {{
      const visible = toggleBtn.getAttribute('aria-pressed') === 'true';
      const next = !visible;
      // traces 0 and 1 are the two scatter traces (open + frontier);
      // traces 2 and 3 are the trend lines and stay 'lines'
      Plotly.restyle(div,
        {{ mode: next ? 'markers+text' : 'markers' }},
        [0, 1]);
      toggleBtn.setAttribute('aria-pressed', String(next));
      toggleBtn.textContent = next ? 'Hide model labels' : 'Show model labels';
    }});
  }}
}})();
</script>
</body>
</html>
"""


def main() -> None:
    rows = load_rows()
    frontier = [r for r in rows if r["frontier"]]
    open_rows = [r for r in rows if r["frontier_open"]]

    fig = build_figure(frontier, open_rows)
    chart_div_id = "llm-sizes-chart"
    chart_div = pio.to_html(
        fig,
        include_plotlyjs="cdn",
        full_html=False,
        div_id=chart_div_id,
        config={
            "responsive": True,
            "displaylogo": False,
            "displayModeBar": True,
            "scrollZoom": True,
            "modeBarButtonsToRemove": ["lasso2d", "select2d"],
        },
    )

    page = PAGE_TEMPLATE.format(
        chart_div=chart_div,
        chart_div_id_json=json.dumps(chart_div_id),
        org_legend=render_org_legend(),
        disclosure_legend=render_disclosure_legend(),
    )

    OUT_PATH.write_text(page, encoding="utf-8")
    print(f"Wrote {OUT_PATH}  "
          f"(frontier n={len(frontier)}, open n={len(open_rows)})")


if __name__ == "__main__":
    main()
