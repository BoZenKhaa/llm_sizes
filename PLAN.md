# LLM model-sizes dataset

## Context

Short research project to build a reference CSV of LLM model sizes over the transformer era. Goal: a dataset keyed on major-lab model releases (parameter counts, architecture, capabilities) sourced preferentially from official press releases / papers / model cards, with transparent handling of models whose counts were never officially disclosed.

**Ultimate downstream use**: plot two lines over time — (1) size of the *overall frontier* model at each point, (2) size of the *frontier open-weights* model at each point. This means open-weight coverage is equal-priority to proprietary coverage, and the schema must let a plotter distinguish "was frontier at release" from "was notable at release" cleanly.

Workflow is pure web research + CSV authoring — no codebase involved. Output lands at `/home/mrkos/projects/llm_sizes/` (currently empty).

## Output artifact

Single file: `/home/mrkos/projects/llm_sizes/llm_sizes.csv`, UTF-8, comma-delimited, RFC 4180 quoting.

## CSV schema

Columns in order:

| # | column | type | definition |
|---|---|---|---|
| 1 | `model_name` | string | Canonical name, including version (e.g., `Claude 3.5 Sonnet (2024-10)`, `Llama 3.1 405B`, `GPT-4o`, `DeepSeek-V3`). |
| 2 | `organization` | string | Lab / publisher (`OpenAI`, `Anthropic`, `Google DeepMind`, `Meta`, `Mistral AI`, `xAI`, `DeepSeek`, `Alibaba/Qwen`, etc.). |
| 3 | `announcement_date` | ISO date | Date of first public announcement (blog post / press release / paper), whichever came first. |
| 4 | `total_params` | number (integer or decimal in billions) | Total parameters. For MoE, this is all experts summed. Units: store as number of parameters (e.g., `405000000000`) to keep it unambiguous. |
| 5 | `active_params` | number | Parameters activated per token. For dense models: equals `total_params`. For MoE: the active subset (e.g., DeepSeek-V3 → 37B). |
| 6 | `param_disclosure` | enum | `official` / `leaked` / `estimated` / `unknown`. |
| 7 | `param_source_note` | string | Short note if not `official` — e.g., `SemiAnalysis 2023-07 leak`, `community estimate`, `blank`. |
| 8 | `architecture_type` | enum | `dense`, `MoE`, `encoder-only`, `encoder-decoder`, `SSM`, `hybrid`, `other`. |
| 9 | `context_window` | integer (tokens) | Max input context at release. If extended later, use release-time value. |
| 10 | `open_weights` | boolean | `true` if weights publicly downloadable at release (any license — includes research-only, non-commercial, and fully open), `false` otherwise. |
| 10a | `frontier_at_release` | boolean | `true` if this model was at or very near the overall SOTA at release (regardless of open/closed). Used to filter the "frontier" plot line. |
| 10b | `frontier_open_at_release` | boolean | `true` if this model was the largest/most capable *open-weights* model at release — i.e., a candidate point on the open-weights frontier line. Typically a superset of `frontier_at_release` for open-weight models, plus open-weight leaders during eras when the overall frontier was closed. |
| 11 | `cap_text` | boolean | Text input/output. Effectively `true` for all rows; included for schema uniformity. |
| 12 | `cap_vision` | boolean | Native image input. |
| 13 | `cap_audio` | boolean | Native audio input or output (not TTS wrapper). |
| 14 | `cap_video` | boolean | Native video input. |
| 15 | `cap_code_specialized` | boolean | Model primarily trained/positioned for code (Codex, Code Llama, DeepSeek-Coder, Qwen-Coder, StarCoder). General models that happen to code well → `false`. |
| 16 | `cap_reasoning` | boolean | Test-time-reasoning family (o1, o3, DeepSeek-R1, QwQ, Gemini Thinking). |
| 17 | `cap_tool_use` | boolean | Native function/tool calling officially supported at release. |
| 18 | `release_url` | URL | Primary source: official announcement blog > paper > model card > reputable secondary source. |
| 19 | `supporting_url` | URL or blank | Optional secondary source that backs facts not stated in `release_url` (e.g., the paper when the blog omits params, the Hugging Face card when the press release omits context window). Leave blank if `release_url` covers every populated field. Describe *what* this URL supports in `param_source_note` or RESEARCH_NOTES.md. |

## Scope

Transformer era, 2018 → 2026-04-24. Two parallel frontiers to cover equally well:

### Proprietary / closed-weight frontier track

- **Pre-LLM-era foundations (closed or semi-closed)**: BERT (2018), GPT-1 (2018), GPT-2 (2019 — weights eventually released), T5 (2019), Megatron-LM, Turing-NLG, Jurassic-1.
- **OpenAI**: GPT-3, GPT-3.5, GPT-4, GPT-4 Turbo, GPT-4o, GPT-4o mini, o1 preview/full, o3, o3-mini, o4-mini, GPT-4.1, GPT-5 (verify).
- **Anthropic**: Claude 1, Claude 2, Claude 2.1, Claude Instant, Claude 3 Opus/Sonnet/Haiku, Claude 3.5 Sonnet (Jun 2024), Claude 3.5 Sonnet (Oct 2024), Claude 3.5 Haiku, Claude 3.7 Sonnet, Claude 4 family (verify through 2026-04).
- **Google/DeepMind (closed)**: Gopher, Chinchilla, PaLM, PaLM 2, LaMDA, Gemini 1.0 Ultra/Pro/Nano, Gemini 1.5 Pro/Flash, Gemini 2.0/2.5 (verify).
- **xAI**: Grok-1.5, Grok-2, Grok-3, Grok-4 (verify). (Grok-1 open-weight — see other track.)
- **Others**: Cohere Command / Command R+ (note: Command R/R+ weights released under CC-BY-NC — flag carefully), AI21 Jurassic, Inflection Pi/Inflection-2, Reka Core/Flash, Amazon Nova.

### Open-weights frontier track (first-class)

Cover every plausible "largest open-weight at the time" point. Order roughly chronological:

- **EleutherAI**: GPT-Neo (2021), GPT-J 6B (2021), GPT-NeoX-20B (2022) — pivotal early open-weight frontier points.
- **Meta**: OPT-175B (2022), Galactica (2022), LLaMA 1 (7/13/33/65B, Feb 2023), Llama 2 (7/13/70B, Jul 2023), Code Llama, Llama 3 (8/70B, Apr 2024), Llama 3.1 (8/70/405B, Jul 2024), Llama 3.2 vision (11/90B) + small (1/3B, Sep 2024), Llama 3.3 70B (Dec 2024), Llama 4 family (verify).
- **BigScience**: BLOOM 176B (2022) — first fully-open 100B+ multilingual.
- **TII (UAE)**: Falcon 7B/40B (2023), Falcon 180B (Sep 2023) — biggest open-weight at release, Falcon 2, Falcon 3.
- **Mistral AI**: Mistral 7B (Sep 2023), Mixtral 8x7B (Dec 2023), Mixtral 8x22B (Apr 2024), Mistral Large (verify open-weight status by version), Codestral, Ministral, Pixtral, Mistral Small/Large-2.
- **DeepSeek**: DeepSeek LLM 7B/67B, DeepSeek-V2 (236B/21B MoE), DeepSeek-V2.5, DeepSeek-V3 (671B/37B MoE, Dec 2024), DeepSeek-Coder / Coder-V2, DeepSeek-R1 (Jan 2025) — major open-weight frontier entrants.
- **Alibaba/Qwen**: Qwen 7/14/72B, Qwen1.5, Qwen2 (inc. 72B), Qwen2.5 (inc. 72B), Qwen2.5-Coder, Qwen2.5-VL, QwQ-32B, Qwen3 (if released by 2026-04-24 — verify).
- **Google**: Gemma 1 (2/7B, Feb 2024), Gemma 2 (2/9/27B), Gemma 3 (verify). Open-weight companion line to Gemini.
- **xAI**: Grok-1 (Mar 2024, 314B MoE open-weight).
- **Databricks**: DBRX (132B/36B MoE, Mar 2024).
- **Snowflake**: Arctic (480B/17B MoE, Apr 2024).
- **Microsoft**: Phi-1, Phi-1.5, Phi-2, Phi-3 (mini/small/medium), Phi-3.5, Phi-4.
- **01.AI**: Yi-6B/34B, Yi-1.5, Yi-Large.
- **NVIDIA**: Nemotron family (Nemotron-4 340B, Llama-Nemotron variants).
- **Others to check**: StableLM, MPT, RedPajama, StarCoder/StarCoder2, OLMo/OLMo-2 (AI2), Jamba (AI21, hybrid SSM), Command R+ (if counted open).

### Row-selection rules

- One row per announced release event. Dated API snapshots of the same headline model (e.g., `gpt-4-0613` vs `gpt-4-0314`) → collapse to the headline row unless capabilities or params changed.
- **Versioning rule**: when the same name ships twice with different behavior (e.g., Claude 3.5 Sonnet Jun vs Oct 2024), that's two rows with dated names.
- For model families released as multiple sizes the same day (Llama 3.1 8/70/405B), give each size its own row — critical for the frontier plot.
- Drop obscure fine-tunes and derivative merges; keep lab-published base and instruct variants only.

Estimate: ~120–160 rows with open-weight coverage expanded.

## Research methodology

1. For each candidate model, search in this source-priority order and stop at the first authoritative hit:
   - Lab's official blog / newsroom / press release
   - arXiv paper or technical report
   - Hugging Face model card (for open-weight)
   - System card (OpenAI, Anthropic)
   - Reputable secondary: The Verge, TechCrunch, SemiAnalysis (for leaks only)
2. Capture the single best URL as `release_url`. Prefer the primary source even if it says less about params than a secondary analysis.
3. For undisclosed params: cite the estimate's origin in `param_source_note` and set `param_disclosure` accordingly. Widely-cited single estimates (e.g., GPT-4 ~1.8T MoE from SemiAnalysis) → `leaked`. Community guesses without a primary leak → `estimated`. No credible figure at all → `unknown` with both param columns blank.
4. Tool usage: `WebSearch` to locate sources, `WebFetch` to pull announcement pages when needed for context-window or capability details.

## Execution steps

0. Copy this plan file to `/home/mrkos/projects/llm_sizes/PLAN.md` so it lives alongside the CSV.
1. Build a working model list from the scope section above (expand as discoveries surface).
2. Batch research lab-by-lab to reuse context (Anthropic together, OpenAI together, etc.).
3. Write rows incrementally to `llm_sizes.csv` — write after each lab batch rather than at the end, so progress is inspectable.
4. Spot-check ~5 rows against their cited URLs before declaring done.

## Verification

- Open `llm_sizes.csv` in a spreadsheet tool or `column -s, -t < llm_sizes.csv | less -S` to confirm schema alignment.
- For each row: `release_url` must resolve (HTTP 200 via `curl -I`) and visibly mention the model.
- Sanity checks:
  - For every `architecture_type = dense` row, `active_params == total_params`.
  - For every `architecture_type = MoE` row, `active_params < total_params`.
  - `open_weights = true` rows should have a Hugging Face or official download link reachable.
  - `param_disclosure = official` rows should cite a lab-owned URL, not a third party.
- Confirm row count is in the expected 120–160 range; investigate if far off.
- **Two-line-plot dry run**: sort by `announcement_date` and walk `frontier_at_release = true` rows chronologically, eyeballing the sequence. Expect zig-zags (e.g., GPT-4o reportedly smaller than GPT-4; Claude 3.5 Sonnet smaller than Claude 3 Opus) — that's fine. What must hold: for every time window, there should be no obvious missing flagship from the covered labs. Repeat for `frontier_open_at_release = true` on the open-weights side (e.g., BLOOM-176B should appear in 2022, Falcon-180B in 2023, Llama-3.1-405B in mid-2024, DeepSeek-V3 671B in late 2024).
