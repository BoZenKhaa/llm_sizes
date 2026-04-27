# llm_sizes

Reference CSV of large-language-model parameter counts across the transformer
era (2018 → present), curated from primary sources (lab blogs, papers, model
cards, system cards), with leaked/estimated counts marked separately and
plotting scripts that read directly from the CSV.

Operational details and the per-lab researcher/verifier workflow live in
`CLAUDE.md`. The full column schema and source-priority research methodology
live in `PLAN.md`. Lab-by-lab progress lives in `STATUS.md`.

## What "frontier" means in this dataset

Two boolean columns capture frontier status, and they are independent —
either, both, or neither can be `true`.

### `frontier_at_release`

`true` if the model was at or very near the **overall SOTA at release**,
regardless of whether weights were open or closed. This is a per-row
capability judgment made at row-authoring time; it is **not** a derived
size-ranking and **not** a strict convex-hull "biggest model on the date"
filter. Two consequences worth being explicit about:

- Smaller models can be flagged frontier when they overtake bigger
  predecessors on capability (Chinchilla 70B post-Gopher 280B; GPT-4o
  vs. the leaked 2T Claude 3 Opus; DeepSeek-V3 671B vs. older closed
  trillion-param models). The post-Chinchilla "smaller-better-trained"
  pattern is exactly what this flag is meant to capture.
- For sized-family launches on the same day (e.g. Llama 3.1 8/70/405B),
  typically only the largest member carries the flag.

### `frontier_open_at_release`

`true` if the model was the **largest *or* most capable open-weights
model at release**. This is typically a superset of
`frontier_at_release ∩ open_weights=true`, plus the open-weight leaders
during eras when the overall frontier was closed (e.g., BLOOM-176B in
2022, Falcon-180B in 2023, Llama 3.1 405B in mid-2024, DeepSeek-V3 671B
in late 2024).

The "or most capable" wording matters: an open-weight model can hold the
flag even when a strictly-larger contemporaneous open model exists, if
the contemporary was qualitatively weaker (LLaMA 65B in Feb 2023 outpacing
BLOOM 176B / OPT-175B; Llama 2 70B over BLOOMZ; Mixtral-8x7B / Llama 3
70B over the lightly-tuned Falcon-180B / Grok-1).

### Plotting use

The plot scripts filter on these two flags and additionally drop rows
where `total_params` is blank, which removes most undisclosed-and-no-leak
rows from the trend lines but does not change the flag itself.

## Field-fill rules

Full column schema is in `PLAN.md`. The non-obvious fill rules:

### Identity & dating

- **`model_name`** — canonical name *including* version where the same
  name ships twice with different behavior (e.g., `Claude 3.5 Sonnet
  (2024-06)` vs. `(2024-10)` are two rows with dated suffixes).
- **`announcement_date`** — earliest public announcement (blog / press /
  paper / system card), whichever came first. ISO format. Not the API
  general-availability date.

### Parameters

- **`total_params`** — total across the *whole* deployed model, stored as
  an integer count (e.g., `405000000000`, not `405B`).
  - **MoE**: sum of all experts. DeepSeek-V3 → `671000000000`.
  - **Multimodal with encoders**: decoder + vision/audio encoder(s)
    summed (Pixtral 12B → 12B decoder + 0.4B SigLIP →
    `12400000000`). Decomposition described in `param_source_note`.
- **`active_params`** — parameters activated per token.
  - Dense: equals `total_params`.
  - MoE: routed-active subset (DeepSeek-V3 → `37000000000`). When a lab
    reports both "routed active" and "active including embedding/output",
    use the routed figure and note the discrepancy.
- **`param_disclosure`** — one of:
  - `official` — lab disclosed the count (paper, model card, blog).
  - `leaked` — single widely-cited primary leak (e.g. SemiAnalysis on
    GPT-4 → ~1.8T MoE).
  - `estimated` — community estimates without a primary leak;
    architectural guesses; lineage inference from a sibling release.
  - `unknown` — no credible figure at all; both param columns left blank.
- **`param_source_note`** — short attribution when not `official`. May
  also describe how the components decompose (encoder + decoder), the
  active/routed nuance, or which secondary URL backs the figure. Per
  `CLAUDE.md`: every factual claim in this note must be substantiated by
  `release_url` or `supporting_url`.

### Architecture & context

- **`architecture_type`** — `dense`, `MoE`, `encoder-only`,
  `encoder-decoder`, `SSM`, `hybrid`, `other`. Marked `other` when sources
  describe the architecture only loosely (no clear MoE/dense
  confirmation).
- **`context_window`** — max input context **at release**. Later
  extensions (e.g., Qwen 2K → 8K retrain) are not retroactively applied;
  the release-time figure is preserved.

### Open-weights & frontier flags

- **`open_weights`** — `true` if weights were publicly downloadable at
  release under any license (research-only, non-commercial, and fully
  open all qualify); `false` otherwise. Later weight releases of an
  originally-closed model do not flip the row.
- **`frontier_at_release`** / **`frontier_open_at_release`** — see
  preceding section.

### Capability flags

Capabilities reflect what the model could do **at release**, not what
was added later. Several rows show this explicitly: GPT-4o mini's note
records "audio promised later" → `cap_audio=false` even though audio
landed shortly after; Grok-2's note records "vision input was added
later in October 2024" → `cap_vision=false` at the August launch row.

- **`cap_text`** — effectively always `true`; kept for schema uniformity.
- **`cap_vision`** — native image input.
- **`cap_audio`** — native audio input or output (not a TTS wrapper).
- **`cap_video`** — native video input.
- **`cap_code_specialized`** — `true` only when the model is *primarily
  trained or positioned* for code (Codex, Code Llama, DeepSeek-Coder,
  Qwen-Coder, StarCoder). General-purpose models that happen to code
  well → `false`.
- **`cap_reasoning`** — test-time-reasoning family (o1/o3, DeepSeek-R1,
  QwQ, Gemini Thinking, Magistral, Claude *Thinking* modes when they
  ship as a distinct row).
- **`cap_tool_use`** — native function/tool calling officially supported
  at release.

### Sourcing

- **`release_url`** — single primary source, picked in this priority
  order: lab blog/newsroom/press release > arXiv paper or tech report >
  Hugging Face model card > system card > reputable secondary (Verge,
  TechCrunch, SemiAnalysis for leaks).
- **`supporting_url`** — optional secondary backing facts not stated in
  `release_url` (e.g., the paper when the blog omits params, the HF card
  when the press release omits context window). Blank when
  `release_url` covers every populated field.
- **Source-substantiation rule** (from `CLAUDE.md`): every factual claim
  in a row — numbers, architecture, license, benchmark figures — must be
  supported by `release_url` or `supporting_url`. The verifier subagent
  fetches only those two columns; anything that lives only in
  `param_source_note` without a citation is unverifiable and gets
  removed or has its source added.

## Layout

- `llm_sizes.csv` — the dataset (one row per announced release event).
- `PLAN.md` — full schema and methodology.
- `STATUS.md` — lab-by-lab completion notes.
- `RESEARCH_NOTES.md` — provenance/decision notes accumulated during
  research.
- `labs/<lab>.csv` + `labs/<lab>.notes.md` — per-lab working files
  preserved as provenance after merge.
- `scripts/plot_params.py` — generates `frontier_params.png`,
  `open_params.png`, `frontier_and_open_params.png` (the third with
  log-linear trend lines fit through each group).
- `scripts/plot_params_interactive.py` — generates
  `frontier_and_open_params.html`, an interactive plotly version of the
  combined plot. Hover for a quick summary; click any point to populate
  a side panel with that model's capabilities and source links. Run with
  `uv run scripts/plot_params_interactive.py` (deps declared inline via
  PEP 723).
- `scripts/plot_frontier.py` — original frontier-only plotting script.
- `src/llm_sizes_tools/` — `csv-row` and `check-urls` helpers; see
  `CLAUDE.md` for the full workflow.
