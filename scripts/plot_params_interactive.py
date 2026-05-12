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


# Power-of-two context lengths get binary labels (64k for 65536); decimal-round
# values like 200k or 1M get decimal labels.
_BINARY_CTX = {8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576}


def fmt_context(raw: str) -> str:
    if not raw or not raw.strip():
        return "—"
    try:
        n = int(raw)
    except ValueError:
        return raw
    if n in _BINARY_CTX:
        return f"{n // 1024}k tokens"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.0f}M tokens"
    if n >= 1000:
        return f"{round(n / 1000)}k tokens"
    return f"{n} tokens"


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
                "context_window": fmt_context(r.get("context_window", "")),
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
    params_str = fmt_params(r["params"])
    if r["active_params"] and r["active_params"] < r["params"]:
        params_str = f"{params_str} · {fmt_params(r['active_params'])} active"
    return [
        r["name"],
        r["org"],
        r["date"].isoformat(),
        params_str,
        r["disclosure"],
        r["architecture"],
        ", ".join(r["capabilities"]) or "—",
        r["release_url"],
        r["supporting_url"],
        r["context_window"],
        "open weights" if r["open_weights"] else "closed weights",
    ]


def hover_template() -> str:
    return (
        "<b>%{customdata[0]}</b><br>"
        "%{customdata[1]} · %{customdata[2]}<br>"
        "Params: %{customdata[3]} (%{customdata[4]})<br>"
        "Architecture: %{customdata[5]} · %{customdata[10]}<br>"
        "Context: %{customdata[9]}<br>"
        "Capabilities: %{customdata[6]}<br>"
        "<i>click for details</i>"
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
        x=xs, y=ys, mode="markers",
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


def compute_takeaways(frontier: list[dict], open_rows: list[dict]) -> dict:
    """Stats for the headline takeaway paragraph.

    `lag_years` measures the horizontal distance between the two trend lines:
    at the mean announcement year across both groups, how many years later
    does the open-weight trend reach the same log10(params) the frontier
    trend predicts? Positive values mean open-weight trails the frontier.
    """
    cf, doubling_f = fit_loglinear(frontier)
    co, doubling_o = fit_loglinear(open_rows)
    all_years = ([decimal_year(r["date"]) for r in frontier]
                 + [decimal_year(r["date"]) for r in open_rows])
    eval_year = sum(all_years) / len(all_years)
    log_p = float(np.polyval(cf, eval_year))
    open_year = (log_p - co[1]) / co[0]
    return {
        "doubling_yr_frontier": doubling_f,
        "doubling_yr_open": doubling_o,
        "doubling_mo_frontier": round(doubling_f * 12),
        "doubling_mo_open": round(doubling_o * 12),
        "lag_years": float(open_year - eval_year),
    }


def render_takeaways(t: dict) -> str:
    return (
        '<div class="takeaways">'
        '<strong>Main findings:</strong>'
        '<ul>'
        f'<li>Frontier-model parameter counts are '
        f'<strong>doubling every ~{t["doubling_mo_frontier"]} months</strong> '
        f'(~{t["doubling_yr_frontier"]:.2f} years).</li>'
        f'<li>Open-weight models grow at the same pace '
        f'(doubling every ~{t["doubling_mo_open"]} months) but '
        f'<strong>their size is behind the closed-weight frontier by '
        f'~{t["lag_years"]:.1f} years</strong>.</li>'
        '</ul>'
        '</div>'
    )


def build_trend(rows: list[dict], all_rows: list[dict], *, name: str,
                color: str, dash: str = "dash") -> tuple[go.Scatter, str]:
    coeffs, _doubling = fit_loglinear(rows)
    all_dates = [r["date"] for r in all_rows]
    xs_year = np.array([decimal_year(min(all_dates)),
                        decimal_year(max(all_dates))])
    ys = 10 ** np.polyval(coeffs, xs_year)
    x_dates = [from_decimal_year(x) for x in xs_year]
    trace = go.Scatter(
        x=x_dates, y=ys, mode="lines",
        name=name,
        line=dict(color=color, width=2.0, dash=dash),
        hoverinfo="skip",
        legendgroup=name,
    )
    return trace, name


def build_figure(frontier: list[dict], open_rows: list[dict]) -> go.Figure:
    fig = go.Figure()
    # open first (drawn behind), then frontier
    fig.add_trace(build_scatter(open_rows, hollow=True,
                                name="Open-weight frontier"))
    fig.add_trace(build_scatter(frontier, hollow=False,
                                name="Frontier (closed-weight)"))

    all_rows = frontier + open_rows
    trend_open, _ = build_trend(open_rows, all_rows,
                                name="Open-weight trend",
                                color="#9ca3af", dash="dash")
    trend_front, _ = build_trend(frontier, all_rows,
                                 name="Frontier trend",
                                 color="#374151", dash="dash")
    fig.add_trace(trend_open)
    fig.add_trace(trend_front)

    fig.update_layout(
        xaxis=dict(title="Announcement date", showgrid=True,
                   gridcolor="rgba(0,0,0,0.08)"),
        yaxis=dict(title="Total parameters (log scale)", type="log",
                   showgrid=True, gridcolor="rgba(0,0,0,0.08)"),
        legend=dict(orientation="h", x=0.5, y=-0.12, xanchor="center",
                    yanchor="top",
                    entrywidth=190, entrywidthmode="pixels",
                    bgcolor="rgba(255,255,255,0.85)"),
        hovermode="closest",
        hoverlabel=dict(bgcolor="white", font_size=12,
                        bordercolor="#999"),
        plot_bgcolor="white",
        margin=dict(l=56, r=20, t=14, b=96),
        height=720,
    )
    return fig


def render_org_legend(orgs_present: set[str]) -> str:
    items = []
    for org, color in ORG_COLORS.items():
        if org not in orgs_present:
            continue
        items.append(
            f'<li><span class="swatch" style="background:{color}"></span>'
            f'{html.escape(org)}</li>'
        )
    return "\n".join(items)


def render_disclosure_legend() -> str:
    # Tiny inline SVG glyphs that mirror the plotly markers.
    glyphs = {
        "official":  ('<circle cx="9" cy="9" r="5" fill="#555" />',
                      "filled circle"),
        "leaked":    ('<rect x="4" y="4" width="10" height="10" fill="#555" />',
                      "filled square"),
        "estimated": ('<polygon points="9,3 15,14 3,14" fill="#555" />',
                      "filled triangle"),
        "unknown":   (('<line x1="4" y1="4" x2="14" y2="14" '
                       'stroke="#555" stroke-width="2" />'
                       '<line x1="14" y1="4" x2="4" y2="14" '
                       'stroke="#555" stroke-width="2" />'),
                      "x mark"),
    }
    items = []
    for disc, (glyph, shape) in glyphs.items():
        items.append(
            f'<li><svg width="18" height="18" viewBox="0 0 18 18" '
            f'role="img" aria-label="{shape}">{glyph}'
            f'</svg>{html.escape(disc)}</li>'
        )
    return "\n".join(items)


PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Frontier &amp; open-weight LLM parameter counts</title>
<style>
  :root {{ --border:#e1e4e8; --muted:#6b7280; --accent:#1f6feb; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
          margin:0; color:#1f2328; background:#fafbfc; }}
  header {{ padding:14px 14px 10px; border-bottom:1px solid var(--border);
            background:#fff; }}
  header h1 {{ margin:0 0 4px; font-size:18px; }}
  header p  {{ margin:0; color:var(--muted); font-size:13px; }}
  .takeaways {{ margin:8px 0 6px; padding:8px 12px;
                background:#eef2ff; border-left:4px solid #6366f1;
                border-radius:4px; font-size:13.5px; color:#1e1b4b; }}
  .takeaways ul {{ margin:4px 0 0; padding-left:20px; }}
  .takeaways li {{ line-height:1.5; margin:1px 0; }}
  .layout {{ padding:6px 8px 2px; }}
  #chart-wrap {{ position:relative;
                 background:#fff; border:1px solid var(--border);
                 border-radius:6px; padding:4px; }}
  header button.toggle {{ font:inherit; font-size:12px; cursor:pointer;
                          background:#fff; border:1px solid var(--border);
                          border-radius:6px; padding:2px 10px;
                          color:#1f2328; margin-left:4px;
                          vertical-align:baseline; }}
  header button.toggle:hover {{ background:#f3f4f6; }}
  header button.toggle[aria-pressed="true"] {{ background:#eef2ff;
                                                border-color:#c7d2fe;
                                                color:#3730a3; }}
  .legend-panel {{ position:absolute; top:12px; right:12px; z-index:50;
                   background:#fff; border:1px solid var(--border);
                   border-radius:8px;
                   box-shadow:0 6px 18px rgba(0,0,0,0.12);
                   padding:10px 14px 8px; font-size:12px;
                   max-width:340px;
                   max-height:calc(100% - 24px); overflow:auto; }}
  .legend-panel[hidden] {{ display:none; }}
  .legend-panel section + section {{ margin-top:10px; }}
  .legend-panel h2 {{ margin:0 0 6px; font-size:11px;
                      text-transform:uppercase; letter-spacing:0.04em;
                      color:var(--muted); font-weight:600;
                      padding-right:20px; }}
  .legend-panel ul {{ list-style:none; padding:0; margin:0; }}
  .legend-panel li {{ display:flex; align-items:center; gap:8px;
                      margin:2px 0; line-height:1.4; }}
  .legend-panel .close {{ position:absolute; top:4px; right:6px;
                          background:transparent; border:0; cursor:pointer;
                          color:var(--muted); font-size:18px; padding:2px 6px;
                          line-height:1; border-radius:4px; }}
  .legend-panel .close:hover {{ background:#f3f4f6; color:#111; }}
  .swatch {{ display:inline-block; width:14px; height:14px;
             border-radius:50%; border:1px solid #00000020; }}
  .legend-grid {{ display:grid;
                  grid-template-columns: repeat(2, minmax(130px, 1fr));
                  gap:2px 14px; }}
  @media (max-width: 700px) {{
    #chart-wrap {{ display:flex; flex-direction:column; }}
    .legend-panel {{ position:static; top:auto; right:auto;
                     max-width:none; max-height:none;
                     box-shadow:none; margin:0 0 6px;
                     border-radius:6px; order:-1; }}
    .legend-grid {{ grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); }}
  }}
  /* On touch devices, hide Plotly's hover tooltip via CSS rather than
     turning hovermode off — disabling hovermode also disables point-hit
     detection, which breaks plotly_click on taps. */
  @media (hover: none) {{
    #chart-wrap .hoverlayer {{ display: none !important; }}
  }}
  .popover {{ position:absolute; z-index:100; max-width:340px;
              background:#fff; border:1px solid #d0d7de;
              border-radius:8px;
              box-shadow:0 6px 18px rgba(0,0,0,0.15);
              padding:12px 14px; font-size:13px; line-height:1.45; }}
  .popover[hidden] {{ display:none; }}
  .popover h3 {{ margin:0 0 4px; font-size:15px; padding-right:24px; }}
  .popover .meta {{ color:var(--muted); font-size:11.5px;
                    margin-bottom:8px; }}
  .popover .caps {{ display:flex; flex-wrap:wrap; gap:5px;
                    margin:5px 0 8px; }}
  .popover .caps span {{ background:#eef2ff; color:#3730a3;
                         border-radius:12px; padding:1px 9px;
                         font-size:11px; }}
  .popover .links a {{ color:var(--accent); text-decoration:none;
                       margin-right:10px; font-size:12px; }}
  .popover .links a:hover {{ text-decoration:underline; }}
  .popover .close {{ position:absolute; top:4px; right:6px;
                     background:transparent; border:0; cursor:pointer;
                     color:var(--muted); font-size:18px; padding:2px 6px;
                     line-height:1; border-radius:4px; }}
  .popover .close:hover {{ background:#f3f4f6; color:#111; }}
  .footer {{ display:flex; flex-wrap:wrap; gap:6px 18px;
             justify-content:space-between;
             padding:4px 14px 12px; color:var(--muted); font-size:12px; }}
  .footer a {{ color:var(--accent); text-decoration:none; }}
  .footer a:hover {{ text-decoration:underline; }}
</style>
</head>
<body>
<header>
  <h1>Frontier &amp; open-weight frontier LLM parameter counts</h1>
  {takeaways_html}
  <p>Click any point to see its capabilities and source links.
     Drag to zoom; double-click to reset. Toggle traces using the
     legend below the chart.
     <button id="toggle-labels" class="toggle" type="button"
             aria-pressed="false"
             title="Show or hide model name labels on the chart">
       Show model labels
     </button>
     <button id="toggle-legend" class="toggle" type="button"
             aria-pressed="false"
             title="Show or hide the color/shape key">
       Show key
     </button></p>
</header>
<div class="layout">
  <div id="chart-wrap">
    {chart_div}
    <div id="point-popover" class="popover" hidden></div>
    <aside id="legend-panel" class="legend-panel" hidden>
      <button class="close" type="button" aria-label="Close key">×</button>
      <section>
        <h2>Disclosure (marker shape)</h2>
        <ul>
          {disclosure_legend}
        </ul>
      </section>
      <section>
        <h2>Organization (color)</h2>
        <ul class="legend-grid">
          {org_legend}
        </ul>
      </section>
    </aside>
  </div>
</div>
<footer class="footer">
  <span>{n_frontier} frontier · {n_open} open-weight · last data point {last_date}</span>
  <a href="https://github.com/BoZenKhaa/llm_sizes" target="_blank"
     rel="noopener">github.com/BoZenKhaa/llm_sizes ↗</a>
</footer>
<script>
(function() {{
  const div = document.getElementById({chart_div_id_json});
  if (!div) return;
  const wrap = document.getElementById('chart-wrap');
  const popover = document.getElementById('point-popover');
  const escapeHtml = (s) => String(s ?? '').replace(/[&<>"']/g, c => ({{
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }}[c]));
  const renderPopover = (cd) => {{
    const [name, org, dateStr, params, disclosure, arch, caps,
           releaseUrl, supportingUrl, ctx, openWeights] = cd;
    const capChips = caps && caps !== '—'
      ? caps.split(',').map(s => s.trim())
            .filter(Boolean)
            .map(c => `<span>${{escapeHtml(c)}}</span>`).join('')
      : '<span style="background:#f3f4f6;color:#6b7280">none flagged</span>';
    const links = [];
    if (releaseUrl) {{
      links.push(`<a href="${{escapeHtml(releaseUrl)}}" target="_blank" `
                 + `rel="noopener">release ↗</a>`);
    }}
    if (supportingUrl) {{
      links.push(`<a href="${{escapeHtml(supportingUrl)}}" target="_blank" `
                 + `rel="noopener">supporting ↗</a>`);
    }}
    return `
      <button class="close" type="button" aria-label="Close details">×</button>
      <h3>${{escapeHtml(name)}}</h3>
      <div class="meta">${{escapeHtml(org)}} · ${{escapeHtml(dateStr)}}<br>
        ${{escapeHtml(params)}} (${{escapeHtml(disclosure)}})<br>
        ${{escapeHtml(arch)}} · ${{escapeHtml(openWeights)}}
        · context ${{escapeHtml(ctx)}}</div>
      <div class="caps">${{capChips}}</div>
      <div class="links">${{links.join(' ') || '<span style="color:#6b7280">no URLs on file</span>'}}</div>
    `;
  }};
  const isCoarsePointer = !!(window.matchMedia
      && window.matchMedia('(hover: none)').matches);
  // Keep hovermode 'closest' on touch so taps still resolve to a point and
  // plotly_click can populate the popover; the tooltip itself is hidden via
  // the `@media (hover: none)` CSS rule.
  let hoverEnabled = true;
  if (isCoarsePointer) {{
    // Single-finger drag pans; two-finger pinch zooms (scrollZoom).
    Plotly.relayout(div, {{dragmode: 'pan'}});
  }}
  const setHoverEnabled = (enabled) => {{
    if (isCoarsePointer) return;
    if (hoverEnabled === enabled) return;
    hoverEnabled = enabled;
    Plotly.relayout(div, {{hovermode: enabled ? 'closest' : false}});
  }};
  const hidePopover = () => {{
    popover.hidden = true;
    popover.innerHTML = '';
    setHoverEnabled(true);
  }};
  const showPopover = (cd, ax, ay) => {{
    setHoverEnabled(false);
    popover.innerHTML = renderPopover(cd);
    popover.hidden = false;
    popover.style.visibility = 'hidden';
    popover.style.left = '0px';
    popover.style.top = '0px';
    const pw = popover.offsetWidth;
    const ph = popover.offsetHeight;
    const ww = wrap.clientWidth;
    const wh = wrap.clientHeight;
    const m = 8;
    let left = ax + 14;
    let top = ay + 14;
    if (left + pw > ww - m) left = Math.max(m, ax - pw - 14);
    if (top + ph > wh - m) top = Math.max(m, ay - ph - 14);
    if (left < m) left = m;
    if (top < m) top = m;
    popover.style.left = `${{left}}px`;
    popover.style.top = `${{top}}px`;
    popover.style.visibility = 'visible';
    const closeBtn = popover.querySelector('.close');
    if (closeBtn) closeBtn.addEventListener('click', hidePopover);
  }};
  let suppressOutsideClose = false;
  div.on('plotly_click', (data) => {{
    if (!data || !data.points || !data.points.length) return;
    const pt = data.points[0];
    if (!pt.customdata) return;
    const ev = data.event || {{}};
    const rect = wrap.getBoundingClientRect();
    const x = (ev.clientX || 0) - rect.left;
    const y = (ev.clientY || 0) - rect.top;
    showPopover(pt.customdata, x, y);
    suppressOutsideClose = true;
    setTimeout(() => {{ suppressOutsideClose = false; }}, 0);
  }});
  div.on('plotly_relayout', (eventData) => {{
    // Our own setHoverEnabled() calls relayout with only `hovermode` —
    // skip those so they don't close the popover we just opened.
    const keys = Object.keys(eventData || {{}});
    if (keys.length === 1 && keys[0] === 'hovermode') return;
    if (!popover.hidden) hidePopover();
  }});
  document.addEventListener('click', (e) => {{
    if (suppressOutsideClose) return;
    if (popover.hidden) return;
    if (popover.contains(e.target)) return;
    hidePopover();
  }});
  const legendBtn = document.getElementById('toggle-legend');
  const legendPanel = document.getElementById('legend-panel');
  const setLegendVisible = (visible) => {{
    if (!legendPanel) return;
    legendPanel.hidden = !visible;
    if (legendBtn) {{
      legendBtn.setAttribute('aria-pressed', String(visible));
      legendBtn.textContent = visible ? 'Hide key' : 'Show key';
    }}
  }};
  if (legendBtn && legendPanel) {{
    legendBtn.addEventListener('click', () => {{
      setLegendVisible(legendPanel.hidden);
    }});
    const legendCloseBtn = legendPanel.querySelector('.close');
    if (legendCloseBtn) {{
      legendCloseBtn.addEventListener('click', () => setLegendVisible(false));
    }}
  }}
  document.addEventListener('keydown', (e) => {{
    if (e.key !== 'Escape') return;
    if (!popover.hidden) hidePopover();
    if (legendPanel && !legendPanel.hidden) setLegendVisible(false);
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

  // Pinch-to-zoom on touch. Plotly's cartesian plots don't natively bind
  // 2-finger pinch, so we intercept touch events in the capture phase,
  // compute new axis ranges anchored at the pinch midpoint, and apply
  // via Plotly.relayout. Single-finger touches fall through to Plotly's
  // pan handler unchanged.
  if (isCoarsePointer) {{
    let pinchState = null;
    const rangeToNum = (v) => typeof v === 'number' ? v : Date.parse(v);
    const numToRange = (axType, v) => axType === 'date'
      ? new Date(v).toISOString()
      : v;
    const onPinchStart = (e) => {{
      if (e.touches.length !== 2) {{ pinchState = null; return; }}
      const dragLayer = div.querySelector('.nsewdrag');
      if (!dragLayer) return;
      const rect = dragLayer.getBoundingClientRect();
      const t1 = e.touches[0], t2 = e.touches[1];
      const midX = (t1.clientX + t2.clientX) / 2;
      const midY = (t1.clientY + t2.clientY) / 2;
      if (midX < rect.left || midX > rect.right
          || midY < rect.top || midY > rect.bottom) return;
      const fl = div._fullLayout;
      if (!fl || !fl.xaxis || !fl.yaxis) return;
      e.preventDefault();
      e.stopPropagation();
      pinchState = {{
        W: rect.width, H: rect.height,
        midPx: midX - rect.left, midPy: midY - rect.top,
        dist: Math.hypot(t2.clientX - t1.clientX, t2.clientY - t1.clientY),
        xType: fl.xaxis.type,
        yType: fl.yaxis.type,
        xRange: [rangeToNum(fl.xaxis.range[0]),
                 rangeToNum(fl.xaxis.range[1])],
        yRange: [rangeToNum(fl.yaxis.range[0]),
                 rangeToNum(fl.yaxis.range[1])],
      }};
      if (!popover.hidden) hidePopover();
    }};
    const onPinchMove = (e) => {{
      if (!pinchState || e.touches.length !== 2) return;
      e.preventDefault();
      e.stopPropagation();
      const t1 = e.touches[0], t2 = e.touches[1];
      const dist = Math.hypot(t2.clientX - t1.clientX,
                              t2.clientY - t1.clientY);
      if (dist < 10) return;
      const s = dist / pinchState.dist;
      const {{ W, H, midPx, midPy, xRange, yRange, xType, yType }} = pinchState;
      const fx = midPx / W;
      const fy = (H - midPy) / H;  // pixel-y is top-down; axis is bottom-up
      const wX = xRange[1] - xRange[0];
      const wY = yRange[1] - yRange[0];
      const aX = xRange[0] + fx * wX;
      const aY = yRange[0] + fy * wY;
      const nwX = wX / s;
      const nwY = wY / s;
      Plotly.relayout(div, {{
        'xaxis.range': [numToRange(xType, aX - fx * nwX),
                        numToRange(xType, aX + (1 - fx) * nwX)],
        'yaxis.range': [numToRange(yType, aY - fy * nwY),
                        numToRange(yType, aY + (1 - fy) * nwY)],
      }});
    }};
    const onPinchEnd = (e) => {{
      if (e.touches.length < 2) pinchState = null;
    }};
    div.addEventListener('touchstart', onPinchStart,
                         {{ passive: false, capture: true }});
    div.addEventListener('touchmove', onPinchMove,
                         {{ passive: false, capture: true }});
    div.addEventListener('touchend', onPinchEnd, {{ capture: true }});
    div.addEventListener('touchcancel', onPinchEnd, {{ capture: true }});
  }}

  // On narrow viewports, drop the rotated y-axis title and tighten the
  // left margin — the page heading and takeaways block already say what
  // the y-axis is. Pass `margin` as a full object: Plotly's relayout
  // dot-notation works for some nested fields but margin.l silently
  // no-ops, leaving the original width in place.
  const narrowMQ = window.matchMedia('(max-width: 600px)');
  const applyResponsiveLayout = () => {{
    if (narrowMQ.matches) {{
      Plotly.relayout(div, {{
        'yaxis.title.text': '',
        'yaxis.title.standoff': 0,
        margin: {{ l: 32, r: 12, t: 8, b: 96 }},
      }});
    }} else {{
      Plotly.relayout(div, {{
        'yaxis.title.text': 'Total parameters (log scale)',
        margin: {{ l: 56, r: 20, t: 14, b: 96 }},
      }});
    }}
  }};
  applyResponsiveLayout();
  narrowMQ.addEventListener('change', applyResponsiveLayout);
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

    takeaways = compute_takeaways(frontier, open_rows)
    orgs_present = {r["org"] for r in frontier + open_rows}
    last_date = max(r["date"] for r in frontier + open_rows).isoformat()
    page = PAGE_TEMPLATE.format(
        chart_div=chart_div,
        chart_div_id_json=json.dumps(chart_div_id),
        org_legend=render_org_legend(orgs_present),
        disclosure_legend=render_disclosure_legend(),
        takeaways_html=render_takeaways(takeaways),
        n_frontier=len(frontier),
        n_open=len(open_rows),
        last_date=last_date,
    )

    OUT_PATH.write_text(page, encoding="utf-8")
    print(
        f"Wrote {OUT_PATH}  "
        f"(frontier n={len(frontier)}, open n={len(open_rows)}, "
        f"frontier ×2 every {takeaways['doubling_yr_frontier']:.2f} yr, "
        f"open lag ≈ {takeaways['lag_years']:.2f} yr)"
    )


if __name__ == "__main__":
    main()
