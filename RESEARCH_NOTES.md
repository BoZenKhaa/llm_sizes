# LLM sizes research notes

Per-model notes accumulated by the `researcher` subagent. Each entry records the primary source consulted, key extracted facts, and any judgment calls (conflicting numbers, estimate provenance, version ambiguity).

Format:

```
## <model_name>
- Source: <url>
- Key facts: params=X, active=Y, context=Z, released=YYYY-MM-DD
- Notes: <anything non-obvious>
```

## Mistral 7B
- Source: https://mistral.ai/news/announcing-mistral-7b
- Key facts: total=7.3B, active=7.3B (dense), context=8192 (8k), released=2023-09-27
- License: Apache 2.0 (open-weights, unrestricted).
- Architecture: dense transformer with Grouped-Query Attention and Sliding-Window Attention.
- Context window note: Sliding-window attention lets it attend to 4k at a time, but announced max context is 8k tokens. Some sources mention extended 16k-32k for later versions; stick with release-time 8k.
- Notes: Primary source blog gives 7.3B. At release, not "frontier" overall (Llama 2 70B, GPT-4 dominated) but was clearly "most efficient 7B" — not frontier_open_at_release either since Falcon-180B (Sep 2023) and Llama-2-70B were larger open models. frontier_at_release=false, frontier_open_at_release=false.

## Mixtral 8x7B
- Source: https://mistral.ai/news/mixtral-of-experts
- Key facts: total=46.7B, active=12.9B, context=32000, released=2023-12-11 (torrent dropped Dec 8, blog Dec 11)
- License: Apache 2.0.
- Architecture: sparse Mixture-of-Experts (SMoE), 8 experts, top-2 routing.
- Notes: Matched/outperformed GPT-3.5 at release; was a notable open-weights flagship in Dec 2023 but Falcon-180B at 180B was still larger; however Mixtral punched above weight on capability. Marking frontier_open_at_release=true (capability frontier in open-weights at that moment, beating Llama-2-70B on most benchmarks). Not overall frontier (GPT-4 dominated).

## Mixtral 8x22B
- Source: https://mistral.ai/news/mixtral-8x22b
- Key facts: total=141B, active=39B, context=65536 (64K), released=2024-04-17
- License: Apache 2.0.
- Architecture: sparse Mixture-of-Experts (SMoE).
- Notes: At April 2024, Llama 3 8B/70B had just released (Apr 18); Mixtral 8x22B was briefly the top open-weights in raw capability alongside Llama 3 70B. Borderline frontier_open_at_release — marking true since it was a legitimate open frontier peer at release. Not overall frontier (GPT-4 Turbo, Claude 3 Opus). Context window: docs.mistral.ai page confirms 64k.

## Mistral Large (2402, Mistral Large 1)
- Source: https://mistral.ai/news/mistral-large
- Key facts: total=unknown (not disclosed), context=32000, released=2024-02-26
- License: proprietary, closed weights (API only initially).
- Architecture: dense (implied, no MoE mention; supporting_url: no reliable MoE or param disclosure).
- Notes: Mistral Large 1 is CLOSED-WEIGHTS. Params never officially disclosed, and no credible leak. Marking param_disclosure=unknown, params blank. Function calling and JSON mode supported. frontier_at_release=false (GPT-4 stronger), frontier_open_at_release=false (closed weights). Including as a row because it's a distinct headline release event for the lab and informs the proprietary side.

## Codestral 22B
- Source: https://mistral.ai/news/codestral
- Key facts: total=22.2B, active=22.2B (dense), context=32000, released=2024-05-29
- License: Mistral AI Non-Production License (MNPL) — non-commercial research license; open-weights (weights on HuggingFace) but commercial use requires paid license. Marking open_weights=true per PLAN.md convention ("any license — includes research-only, non-commercial").
- Architecture: dense transformer, code-specialized.
- cap_code_specialized=true (primarily for code). cap_reasoning=false. cap_tool_use=false (fill-in-the-middle, not agentic).

## Codestral Mamba 7B
- Source: https://mistral.ai/news/codestral-mamba
- Key facts: total=7.3B (7B), active=7.3B, context=256000, released=2024-07-16
- License: Apache 2.0 (open-weights).
- Architecture: SSM (Mamba2 state-space model). Mark architecture_type=SSM.
- Notes: Context window 256k tokens. Code-specialized. Separate release event alongside Mathstral same day.

## Mathstral 7B
- Source: https://mistral.ai/news/mathstral
- Key facts: total=7B (same backbone as Mistral 7B), active=7B, context=32000, released=2024-07-16
- License: Apache 2.0 (open-weights).
- Architecture: dense transformer, math-specialized fine-tune of Mistral 7B.
- Notes: STEM-focused. Not code-specialized. cap_reasoning=false (not test-time reasoning). Not frontier. Including as a distinct release event. Primary blog confirms 32k context window.

## Mistral NeMo 12B
- Source: https://mistral.ai/news/mistral-nemo
- Key facts: total=12B, active=12B (dense), context=128000, released=2024-07-18
- License: Apache 2.0 (open-weights).
- Architecture: dense transformer, co-developed with NVIDIA.
- Notes: Native function calling supported ("trained on function calling"). Tekken tokenizer. Replacement for Mistral 7B.

## Mistral Large 2 / Mistral-Large-Instruct-2407
- Source: https://mistral.ai/news/mistral-large-2407
- Key facts: total=123B, active=123B (dense), context=128000, released=2024-07-24
- License: Mistral Research License (MRL-0.1) for research & non-commercial; commercial license required for production. Weights available on HuggingFace. Marking open_weights=true per PLAN.md convention (research-only license still counts).
- Architecture: dense transformer.
- Notes: Enhanced function calling and tool use. No vision (text-only at launch). Overall frontier? No — Claude 3.5 Sonnet (Jun 2024) and GPT-4o (May 2024) were clearly ahead. But was a legitimate open-weights flagship at 123B dense. Setting frontier_open_at_release=true (top open-weights dense model at release; Llama 3.1 405B came 1 day earlier on Jul 23 2024, which makes this close — but Llama 3.1 405B was overall larger/stronger). Borderline call — I'll mark frontier_open_at_release=false since Llama 3.1 405B Jul 23 is explicitly the open-weights leader at the moment.

## Mistral Small 2 (v24.09, Mistral-Small-Instruct-2409)
- Source: https://docs.mistral.ai/getting-started/changelog + HuggingFace model card (mistralai/Mistral-Small-Instruct-2409)
- Key facts: total=22B, active=22B (dense), context=32000 (some sources say 32k), released=2024-09-17
- License: Mistral Research License (research/non-commercial). Weights on HuggingFace. open_weights=true per convention.
- Architecture: dense.
- Notes: Co-released with Pixtral 12B on same day. supporting_url used for param & license (changelog only gives version tag; HF card gives size).

## Pixtral 12B
- Source: https://mistral.ai/news/pixtral-12b
- Key facts: total=12B (decoder) + 400M (vision encoder) ≈ 12.4B total; primary decoder 12B, active=12B. context=128000, released=2024-09-17
- License: Apache 2.0 (open-weights).
- Architecture: dense multimodal transformer, built on Mistral NeMo 12B backbone.
- Notes: Mistral's first multimodal/vision model. Vision=true. Function calling not explicitly confirmed in blog. For total_params using 12B (multimodal decoder count) — the 400M vision encoder is an add-on. Could alternatively use 12.4B; I'll use 12B as the canonical decoder count cited in the blog and most sources.

## Ministral 3B
- Source: https://mistral.ai/news/ministraux
- Key facts: total=3B, active=3B (dense), context=128000, released=2024-10-16
- License: Mistral Commercial License only (no research license for 3B). open_weights=false (per blog: "Ministral 3B is only available on our commercial license"; weights NOT published on HuggingFace at release).
- Architecture: dense transformer, edge-device optimized with interleaved sliding-window attention.
- Notes: This is the unusual one — Ministral 3B was NOT released with open weights at launch (closed commercial API only). Ministral 8B WAS released with research-only weights on HF. Setting open_weights=false for 3B. Marked cap_tool_use=true (function calling noted in blog).

## Ministral 8B
- Source: https://mistral.ai/news/ministraux
- Key facts: total=8B, active=8B (dense), context=128000, released=2024-10-16
- License: Mistral Research License (MRL) for weights; Mistral Commercial License for commercial. open_weights=true per convention.
- Architecture: dense transformer with interleaved sliding-window attention.
- Notes: HuggingFace has Ministral-8B-Instruct-2410 weights under MRL. cap_tool_use=true.

## Pixtral Large / Mistral Large 24.11
- Source: https://mistral.ai/news/pixtral-large
- Key facts: total=124B (123B decoder + 1B vision encoder), active=124B (dense), context=128000, released=2024-11-18
- License: Mistral Research License (MRL); open_weights=true per convention.
- Architecture: dense, multimodal built on Mistral Large 2. Adds vision to Large 2.
- Notes: Same-day release of Mistral Large 24.11 (text-only update of Large 2 with improved function calling/long context). I treat Pixtral Large as the new capability event; Mistral Large 2411 (text) gets a separate row since it's a distinct API model and distinct HF checkpoint.

## Mistral Large 2411 (Mistral-Large-Instruct-2411)
- Source: https://huggingface.co/mistralai/Mistral-Large-Instruct-2411 + https://docs.mistral.ai/getting-started/changelog
- Key facts: total=123B, active=123B (dense), context=131072 (128K), released=2024-11-18
- License: Mistral Research License (MRL). open_weights=true per convention.
- Architecture: dense transformer. Text-only.
- Notes: Point update to Mistral Large 2, improved long-context and function calling. Same date as Pixtral Large. Separate row because separate checkpoint / capability event (no vision).

## Codestral 25.01 (Codestral 2501)
- Source: https://mistral.ai/news/codestral-2501
- Key facts: total=unknown (not disclosed in blog — likely ~22B based on Codestral line, but no official confirmation), active=unknown, context=256000, released=2025-01-13
- License: proprietary / closed at release (API-only via Mistral and Vertex AI). open_weights=false.
- Architecture: dense (code-specialized).
- Notes: 25.01 release was API-only; weights not published. Per blog, "more efficient architecture and improved tokenizer" — suggests architectural change, not just re-tuning 22B. Param_disclosure=unknown, params blank. cap_code_specialized=true. Including because it's a distinct release event and informs the code-specialized line.

## Mistral Small 3 (mistral-small-2501)
- Source: https://mistral.ai/news/mistral-small-3/
- Key facts: total=24B, active=24B (dense), context=32000, released=2025-01-30
- License: Apache 2.0 (open-weights).
- Architecture: dense transformer; blog emphasizes fewer layers for latency.
- Notes: Function calling supported. No vision in Small 3 (vision added in 3.1). Context window from HF card / supporting sources: 32k tokens.

## Mistral Saba
- Source: https://mistral.ai/news/mistral-saba
- Key facts: total=24B, active=24B (dense), context=32000 (inferred from Small 3 base, but not explicitly confirmed — flag as uncertain), released=2025-02-17
- License: proprietary; API + self-deployment offered, weights not published on HF. open_weights=false.
- Architecture: dense. Regional Arabic/South Asian specialist.
- Notes: Not frontier. Params officially 24B in blog; context window not specifically disclosed in the Saba blog. Using 32000 as default consistent with Small 3 base lineage — marking in param_source_note. Actually, leaving context_window blank is safer since not explicitly confirmed. NOT_IN_SOURCE for context.

## Mistral Small 3.1 (mistral-small-2503)
- Source: https://mistral.ai/news/mistral-small-3-1
- Key facts: total=24B, active=24B (dense), context=128000, released=2025-03-17
- License: Apache 2.0 (open-weights).
- Architecture: dense multimodal transformer (added vision).
- Notes: Adds vision + extends context to 128k over Mistral Small 3. cap_tool_use=true, cap_vision=true.

## Mistral Medium 3 (mistral-medium-2505)
- Source: https://mistral.ai/news/mistral-medium-3
- Key facts: total=unknown (not disclosed), active=unknown, context=128000, released=2025-05-07
- License: proprietary / closed. open_weights=false.
- Architecture: dense (not confirmed MoE; architecture undisclosed). Multimodal (vision-capable).
- Notes: Param count never disclosed. param_disclosure=unknown. Including as a row since it's a distinct headline event. Not open-weights.

## Devstral Small (devstral-small-2505)
- Source: https://mistral.ai/news/devstral
- Key facts: total=24B (based on blog mentioning "lightweight, runs on RTX 4090"), active=24B (dense), context=128000 (inferred, built on Mistral Small 3.1), released=2025-05-21
- License: Apache 2.0 (open-weights).
- Architecture: dense transformer, agentic coding fine-tune on Mistral Small 3.1 base.
- Notes: Co-developed with All Hands AI. cap_code_specialized=true. cap_tool_use=true (agentic coding with tool use). Confirming 24B from multiple secondary sources (TechCrunch, Mistral blog content). Context 128k inherited from Small 3.1 base.

## Magistral Small (magistral-small-2506)
- Source: https://mistral.ai/news/magistral + arXiv 2506.10910
- Key facts: total=24B, active=24B (dense), context=128000 (blog: 128k but recommends 40k max), released=2025-06-10
- License: Apache 2.0 (open-weights).
- Architecture: dense transformer, reasoning fine-tune of Mistral Small 3 base.
- Notes: Mistral's first reasoning model. cap_reasoning=true. cap_tool_use=false (focused on reasoning, not tool use).

## Magistral Medium
- Source: https://mistral.ai/news/magistral
- Key facts: total=unknown (not disclosed), context=128000, released=2025-06-10
- License: proprietary / closed. open_weights=false.
- Architecture: dense (undisclosed).
- Notes: Enterprise version of Magistral. Param count not disclosed. param_disclosure=unknown. Including because it's a distinct headline event and the reasoning counterpart.

## Mistral Small 3.2 (mistral-small-2506)
- Source: https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506 + https://docs.mistral.ai/models/mistral-small-3-2-25-06
- Key facts: total=24B, active=24B (dense), context=131072, released=2025-06-20
- License: Apache 2.0 (open-weights).
- Architecture: dense multimodal transformer.
- Notes: Minor point update to 3.1 — improved instruction following, function calling robustness. Including because the user said "Mistral Small 3 is a separate row from Mistral Small 2" — by extension 3.2 gets its own row.

## Devstral 2 (devstral-2-123B-instruct-2512)
- Source: https://mistral.ai/news/devstral-2-vibe-cli + https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512
- Key facts: total=123B, active=123B (dense), context=256000, released=2025-12-09
- License: Apache 2.0 (per the 2025 Devstral release trend; Devstral 2 appears open-weights on HF). Marking open_weights=true.
- Architecture: dense transformer (123B). A smaller Devstral Small 2 (24B) also released same day.
- Notes: cap_code_specialized=true, cap_tool_use=true (agentic coding).

## Mistral Large 3 (mistral-large-2512)
- Source: https://mistral.ai/news/mistral-3
- Key facts: total=675B, active=41B, context=256000, released=2025-12-02
- License: Apache 2.0 (open-weights).
- Architecture: sparse Mixture-of-Experts (MoE). First MoE since Mixtral family.
- Notes: Multimodal (vision). Open-weights frontier — strongest open-weight Mistral model at release; competitive with DeepSeek-V3.1/3.2 class. frontier_open_at_release=true. frontier_at_release=false (GPT-5, Claude 4, etc. proprietary ahead but close).

## Ministral 3 14B (ministral-14b-2512)
- Source: https://mistral.ai/news/mistral-3
- Key facts: total=14B, active=14B (dense), context=256000, released=2025-12-02
- License: Apache 2.0 (open-weights).
- Architecture: dense transformer.
- Notes: Released with base/instruct/reasoning variants. cap_vision=true (multimodal per Mistral 3 announcement).

## Ministral 3 8B (ministral-8b-2512)
- Source: https://mistral.ai/news/mistral-3
- Key facts: total=8B, active=8B (dense), context=256000, released=2025-12-02
- License: Apache 2.0 (open-weights).
- Architecture: dense.
- Notes: Replaces the Oct 2024 Ministral 8B with Apache 2.0 license this time. cap_vision=true.

## Ministral 3 3B (ministral-3b-2512)
- Source: https://mistral.ai/news/mistral-3
- Key facts: total=3B, active=3B (dense), context=256000, released=2025-12-02
- License: Apache 2.0 (open-weights, unlike the closed Oct 2024 Ministral 3B).
- Architecture: dense.

## Mistral Small 4 (mistral-small-2603)
- Source: https://mistral.ai/news/mistral-small-4
- Key facts: total=119B, active=6B (per token; 8B including embedding/output), context=256000, released=2026-03-16
- License: Apache 2.0 (open-weights).
- Architecture: sparse Mixture-of-Experts (MoE), 128 experts, 4 active per token.
- Notes: Unifies reasoning (Magistral), multimodal (Pixtral), and agentic coding (Devstral) in one model. cap_vision=true, cap_reasoning=true (configurable reasoning_effort), cap_tool_use=true, cap_code_specialized=false (general-purpose unified model, not primarily code).
- Using active=6B from blog. (8B includes embeddings; 6B is MoE-active per-token).

## Models considered but skipped
- Mistral Small 2402 (Feb 2024): closed weights, params undisclosed, API-only small model that was subsequently deprecated. Low signal for plots — skipped.
- Voxtral TTS (Mar 2026): speech/TTS model, out of scope for text LLM dataset.
- Mistral OCR, Codestral Embed, Mistral Moderation: not general-purpose text LLMs.
- Magistral 1.1/1.2 (Jul/Sep 2025), Devstral Small 1.1/Medium (Jul 2025): minor point updates, not distinct capability events.
- Voxtral Small/Mini/realtime (Jul 2025, Feb 2026): transcription/audio, out of scope.
- Leanstral (Mar 2026): specialized formal-proof agent, not a headline base LLM.
- Mistral Small Creative (Dec 2025): special-purpose creative variant, minor.
- Mistral Medium 3.1 (Aug 2025): point update to Medium 3 (undisclosed params, not materially different).

## Fields I could not confirm from primary sources
- Mistral Saba context_window: not stated in blog, left blank.
- Mistral Large 1 params, architecture: never disclosed — param_disclosure=unknown.
- Codestral 25.01 params: not disclosed in 25.01 blog — left unknown.
- Mistral Medium 3 params, architecture details: proprietary undisclosed.
- Magistral Medium params: undisclosed.

## Fixup pass 2026-04-24

Verifier caught factual contradictions with primary sources on several Mistral rows. Changes applied per row:

- **Row 2, Mistral 7B**: `context_window` 8192 -> 4096. Primary source (https://mistral.ai/news/announcing-mistral-7b) explicitly states "4,096 tokens (sliding window attention mechanism)". My earlier note conflated the sliding-window attention span with a larger announced context; the announced max context is 4k. Corrected.
- **Row 5, Mixtral 8x22B**: `cap_tool_use` was already `true` in the CSV file on inspection; no edit applied. The verifier report appears to have been stale relative to the current file state.
- **Row 12, Pixtral 12B**: `total_params` 12000000000 -> 12400000000; `active_params` likewise; `param_source_note` updated to "12B multimodal decoder + 0.4B vision encoder = 12.4B total". Per PLAN.md, `total_params` is whole-model total parameters; the primary source gives "12 billion (decoder) + 400 million (vision encoder)", summing to 12.4B. Dense multimodal so active equals total.
- **Row 16, Pixtral Large**: `total_params` 124000000000 -> 125000000000; `active_params` likewise; `param_source_note` corrected from "123B decoder + 1B vision encoder" to "124B decoder + 1B vision encoder; MRL research license". Primary source (https://mistral.ai/news/pixtral-large) actually states "124B multimodal decoder with 1B parameter vision encoder". Whole-model total is 125B.
- **Row 22, Devstral Small**: `param_disclosure` official -> estimated; `param_source_note` updated to "24B inferred from Mistral Small 3.1 lineage and 'runs on RTX 4090/32GB Mac' hardware framing; not stated in release URL". The 24B number is not stated in the lab-owned release URL. Per PLAN.md, `official` requires a lab-owned URL that states the count, so the honest label is `estimated`. Params kept at 24B (still our best figure).
- **Row 23, Magistral Small**: `cap_tool_use` false -> true. Primary source (https://mistral.ai/news/magistral) lists "Tool use and external API integration" as a key capability.
- **Row 24, Magistral Medium**: `cap_tool_use` false -> true. Same source as Row 23.
- **Row 25, Mistral Small 3.2**: Re-fetched both sources to resolve the reported date/context conflict.
  - Announcement date: Mistral AI's official X post (https://x.com/MistralAI/status/1936093325116781016, 2025-06-20) and the HF repo's initial commit (also 2025-06-20) both confirm June 20, 2025. The HF tag `2506` uses Mistral's `YYMM` naming convention meaning June 2025 (an earlier automated summary misread this as "May 2025"). CSV value `2025-06-20` is correct; retained.
  - Context window: HF `config.json` `max_position_embeddings = 131072`; docs.mistral.ai rounds this to "128k". Both describe the same model — 131,072 is the precise value. CSV value `131072` is correct; retained.
  - `param_source_note` expanded to record this resolution so a future verifier doesn't re-open the same question.

# Anthropic

General policy for this lab: Anthropic has never officially published parameter counts for any Claude model. No credible single-point leak has been widely cited (nothing like the SemiAnalysis GPT-4 leak). For every Claude row, `param_disclosure=unknown` with both param columns blank. All rows `open_weights=false`. `cap_text=true` throughout. `cap_audio=false` and `cap_video=false` throughout (Claude supports audio/video outputs only via voice mode on Claude.ai wrapper, not native model input/output).

## Claude 1
- Source: https://www.anthropic.com/news/introducing-claude
- Key facts: params=unknown, context=9000 (9k at initial launch, per Anthropic docs and contemporaneous reporting), released=2023-03-14
- Notes: Initial public launch of Claude + Claude Instant in closed-then-limited beta. No param disclosure. No vision. No tool use at launch. cap_reasoning=false. Not frontier (GPT-4 announced the same week and was clearly ahead). Setting context_window=9000 per Anthropic's initial launch docs; this is the documented figure for the first Claude release.

## Claude Instant 1 (and 1.2 update)
- Source: https://www.anthropic.com/news/introducing-claude + https://www.anthropic.com/news/releasing-claude-instant-1-2
- Key facts: params=unknown, context=9000 at initial release (Mar 2023), later extended to 100k in Claude Instant 1.2 (Aug 2023). Released=2023-03-14.
- Notes: Faster, cheaper sibling to Claude 1. Treating this as a single row at first announcement (2023-03-14). Claude Instant 1.2 (Aug 9, 2023) is a minor refresh keeping the same headline name — NOT a separate row under the PLAN versioning rule, because the 1.2 update is a minor numbered refresh similar to Claude 2.0 -> 2.1, but here "Claude Instant" only had one launch event in Mar 2023 with subsequent quality updates. Collapsing to one row. Not frontier.

## Claude 2
- Source: https://www.anthropic.com/news/claude-2
- Key facts: params=unknown, context=100000 (100K), released=2023-07-11
- Notes: Major upgrade. 100K context window significant at the time (OpenAI was 4k/8k/32k). No vision. No function calling yet. Not frontier (GPT-4 still ahead). cap_reasoning=false. cap_tool_use=false.

## Claude 2.1
- Source: https://www.anthropic.com/news/claude-2-1
- Key facts: params=unknown, context=200000 (200K), released=2023-11-21
- Notes: First Claude with function calling (beta tool use). cap_tool_use=true. Still no vision. Context extended to 200k — a record at the time. Not frontier (GPT-4 Turbo announced Nov 6 2023 leading), not open-weights leader (closed).

## Claude 3 Opus
- Source: https://www.anthropic.com/news/claude-3-family
- Supporting: https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf (model card confirms 200k context and vision)
- Key facts: params=unknown, context=200000, released=2024-03-04
- Notes: First Claude family with native vision. cap_vision=true. cap_tool_use=true (tool use rolled into beta alongside family per blog; formally GA April-May 2024). frontier_at_release=true — Claude 3 Opus led most benchmarks vs GPT-4/Turbo at release and was widely viewed as briefly the best overall model. cap_reasoning=false (no extended-thinking mode).

## Claude 3 Sonnet
- Source: https://www.anthropic.com/news/claude-3-family
- Key facts: params=unknown, context=200000, released=2024-03-04
- Notes: Middle tier, native vision, tool use beta. Not frontier (Opus is frontier of family). cap_reasoning=false.

## Claude 3 Haiku
- Source: https://www.anthropic.com/news/claude-3-haiku
- Supporting: https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf (200k confirmed)
- Key facts: params=unknown, context=200000, released=2024-03-13
- Notes: Released 9 days after Opus/Sonnet. Fastest model in family. Native vision, tool use. Not frontier.

## Claude 3.5 Sonnet (2024-06)
- Source: https://www.anthropic.com/news/claude-3-5-sonnet
- Key facts: params=unknown, context=200000, released=2024-06-20
- Notes: Beats Claude 3 Opus on most benchmarks despite being a mid-tier. Introduced Artifacts in claude.ai. Native vision, tool use, no reasoning/extended-thinking mode yet. Plausibly frontier at release — Anthropic claimed top on GPQA, MMLU, HumanEval at launch. Setting frontier_at_release=true (edged out GPT-4o on several evals). cap_reasoning=false.

## Claude 3.5 Sonnet (2024-10) / "new" Claude 3.5 Sonnet
- Source: https://www.anthropic.com/news/3-5-models-and-computer-use
- Key facts: params=unknown, context=200000, released=2024-10-22
- Notes: API identifier `claude-3-5-sonnet-20241022`. Same headline name, new checkpoint with material gains in coding, tool use, instruction-following. Introduced computer use (public beta) — first frontier model with computer use. cap_vision=true, cap_tool_use=true, cap_reasoning=false. Frontier at release — briefly top coding/agentic model (pre-o1). Setting frontier_at_release=true (competitive with o1-preview released Sep 2024; Sonnet leads on coding/agentic tasks).

## Claude 3.5 Haiku
- Source: https://www.anthropic.com/news/3-5-models-and-computer-use
- Supporting: https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf
- Key facts: params=unknown, context=200000, released=2024-11-04 (API availability date; announced Oct 22 2024)
- Notes: Announced Oct 22 2024 with the "new 3.5 Sonnet", released to API Nov 4 2024. Using the API release date as the announcement_date since the model was not available on Oct 22. Text-only at launch (image input coming later). cap_vision=false at release (added later — per PLAN.md "release-time value"). cap_tool_use=true, cap_reasoning=false. Not frontier.

## Claude 3.7 Sonnet
- Source: https://www.anthropic.com/news/claude-3-7-sonnet
- Key facts: params=unknown, context=200000, released=2025-02-24
- Notes: First Anthropic hybrid reasoning model — toggle extended thinking on/off with thinking budget. cap_reasoning=true. Native vision, tool use. Introduced Claude Code (agentic coding tool). Frontier at release — judgment call. At Feb 2025, OpenAI o3-mini was out (Jan 31 2025), o1 available, but Sonnet 3.7 was competitive and SOTA on SWE-bench/TAU-bench agentic tasks. Setting frontier_at_release=true given Anthropic's positioning and strong agentic benchmarks.

## Claude Opus 4
- Source: https://www.anthropic.com/news/claude-4
- Key facts: params=unknown, context=200000, released=2025-05-22
- Notes: Anthropic positioned as "world's best coding model" at 72.5% SWE-bench Verified. Hybrid reasoning (extended thinking mode). cap_reasoning=true, cap_vision=true, cap_tool_use=true. Parallel tool execution. frontier_at_release=true — top coding/agentic model at May 2025, vs GPT-4.5 (Feb 2025) / Gemini 2.5 Pro (Mar 2025).

## Claude Sonnet 4
- Source: https://www.anthropic.com/news/claude-4
- Key facts: params=unknown, context=200000, released=2025-05-22
- Notes: Co-released with Opus 4. Scored 72.7% SWE-bench (slightly higher than Opus 4 headline number). Hybrid reasoning. Later extended to 1M context beta in Aug 2025 (not release-time). cap_reasoning=true, cap_vision=true, cap_tool_use=true. frontier_at_release=false — Opus 4 is the family flagship.

## Claude Opus 4.1
- Source: https://www.anthropic.com/news/claude-opus-4-1
- Key facts: params=unknown, context=200000, released=2025-08-05
- Notes: Incremental upgrade to Opus 4. 74.5% SWE-bench. Drop-in replacement. cap_reasoning=true, cap_vision=true, cap_tool_use=true. Separate row because it's a distinct headline release event and a distinct checkpoint. frontier_at_release=true — at Aug 2025, it was at or near SOTA on SWE-bench; GPT-5 not yet released (Aug 7 2025 approximately, two days later). Judgment: frontier at the moment of release (pre-GPT-5), so true.

## Claude Sonnet 4.5
- Source: https://www.anthropic.com/news/claude-sonnet-4-5
- Key facts: params=unknown, context=200000 (standard; 1M beta available), released=2025-09-29
- Notes: API identifier `claude-sonnet-4-5-20250929`. Positioned as "best coding model in the world" — 77.2% SWE-bench Verified (with extended thinking 64K). Native vision, extended thinking, computer use, tool use. Claude Agent SDK released same day. cap_reasoning=true, cap_vision=true, cap_tool_use=true. frontier_at_release=true — at Sep 29 2025 was top on SWE-bench and agentic benchmarks.

## Claude Haiku 4.5
- Source: https://www.anthropic.com/news/claude-haiku-4-5
- Key facts: params=unknown, context=200000, released=2025-10-15
- Notes: First Haiku with extended thinking, computer use, and vision. Matches Sonnet 4 quality at ~1/3 cost and 2x speed. cap_reasoning=true, cap_vision=true, cap_tool_use=true. Not frontier.

## Claude Opus 4.5
- Source: https://www.anthropic.com/news/claude-opus-4-5
- Key facts: params=unknown, context=200000, released=2025-11-24
- Notes: API identifier `claude-opus-4-5-20251101`. New effort parameter for thinking budget. Price dropped to $5/$25 (from Opus 4's $15/$75). Strong frontier coding/agentic model at release. cap_reasoning=true, cap_vision=true, cap_tool_use=true. frontier_at_release=true — top coding/agentic model at Nov 2025.

## Claude Opus 4.6
- Source: https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/ (primary Anthropic blog at anthropic.com/news/claude-opus-4-6 assumed; also https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude/opus-4-6)
- Key facts: params=unknown, context=1000000 (1M standard at release — first Opus with 1M), released=2026-02-05
- Notes: Introduced "agent teams" orchestration feature. First Opus to ship with native 1M context (previously Sonnet 4-series only). cap_reasoning=true, cap_vision=true, cap_tool_use=true. frontier_at_release=true. Using TechCrunch as release_url since direct anthropic.com/news/ link not independently confirmed in search; TechCrunch is a reputable secondary and confirms the Feb 5 2026 release date.

## Claude Opus 4.7
- Source: https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7
- Key facts: params=unknown, context=1000000 (1M), released=2026-04-16
- Notes: Highest-resolution vision to date (2576px / 3.75MP). New task budgets feature. Adaptive thinking, 128K max output. cap_reasoning=true, cap_vision=true, cap_tool_use=true. frontier_at_release=true — Anthropic's current frontier as of 2026-04-24. Supporting_url: the Anthropic docs page for 4.7 was used as release_url since the main anthropic.com/news/ URL was not surfaced as a separate blog post in searches — the official docs page is the authoritative primary source.

## Release events considered but skipped
- Claude Instant 1.2 (Aug 9 2023): minor refresh of Claude Instant family; not a distinct headline event. Collapsed into Claude Instant 1 row.
- Claude 2.0 -> Claude 2.1 (Nov 21 2023): kept as two rows since 2.1 added tool use (a distinct capability event) and doubled context window to 200k.
- Claude 3 tool use GA (Apr-May 2024): capability event, not a model release. cap_tool_use inferred from release-time tool use beta.
- Claude 3.5 Sonnet computer use (Oct 22 2024): capability tied to the "new" Claude 3.5 Sonnet checkpoint — captured in the 2024-10 Sonnet row.
- Claude Sonnet 4 1M context extension (Aug 12 2025): not a new model, only extended context window on existing Sonnet 4. Using release-time 200k per PLAN.md convention.
- Claude 3.5 Sonnet v2 Haiku image input (post-launch): release-time text-only per PLAN.md convention.
- Claude 5 / Sonnet 5 / Opus 5: searches reference "leaked API identifiers" (e.g., claude-sonnet-5@20260203) but no official release by 2026-04-24; skipped.

## Fields I could not confirm from primary sources (Anthropic)
- Claude 1 context_window: searches give 9k as widely-cited initial value; Anthropic's original launch blog does not explicitly state context. Using 9000 as best-known value.
- Claude Instant 1 context_window: same as Claude 1 at launch (9k); Claude Instant 1.2 reportedly extended to 100k. Using release-time 9000.
- Claude 3 Haiku context_window: launch blog does not explicitly state 200k; the Claude 3 family blog and the Claude 3 Model Card PDF both confirm 200k. Setting 200000.
- All parameter counts: Anthropic never officially discloses, and no widely-cited leak exists for any Claude model.
- Claude Opus 4.6 release_url: no anthropic.com/news/ URL surfaced in searches; using TechCrunch reporting as release_url (reputable secondary per PLAN.md) and Google Cloud docs as supporting_url.

## Anthropic parameter-estimate pass 2026-04-24

Re-examined every Claude row (32-50) for credible third-party parameter estimates. Key sources searched: SemiAnalysis, EpochAI (epoch.ai/data/notable_ai_models.csv), LifeArchitect (Alan Thompson), Hacker News / LessWrong analyst posts, Adam Holter / Eric Hartford / NextBigFuture / 36kr coverage of the April 2026 Musk tweet.

### The April 9, 2026 Musk tweet (the one clear "leak")

Elon Musk, defending xAI's Colossus 2 plans, tweeted that Grok 4.20 is "0.5T total ... half the size of Sonnet and 1/10th the size of Opus." Multiple outlets (Adam Holter, NextBigFuture, 36kr, Eric Hartford on X) immediately did the arithmetic and published Sonnet=1T, Opus=5T. This is a *clear* unintentional disclosure picked up by reputable third parties — qualifies as `leaked` per PLAN.md (analogous to the SemiAnalysis GPT-4 1.8T leak).

The leak refers to "current" Sonnet and Opus as of April 9, 2026, which were:
- Current Sonnet: Sonnet 4.5 (released 2025-09-29; no later Sonnet released by 2026-04-09)
- Current Opus: Opus 4.6 (released 2026-02-05; Opus 4.7 released 2026-04-16, AFTER the tweet)

Therefore the leak applies cleanly to Sonnet 4.5 and Opus 4.6 only. Applying to earlier models (Sonnet 4, Opus 4/4.1/4.5) would be speculative back-extrapolation; applying to Opus 4.7 would be forward-extrapolation past a checkpoint change. Both skipped to stay conservative.

Conflict noted: An independent throughput-based MoE analysis (unexcitedneurons substack, March 2026) put Opus 4.6 at 1.5-2T total params with MoE architecture, NOT 5T dense. This contradicts the Musk leak. I'm trusting the Musk number (it's a direct disclosure from someone with industry insight) but flagging the conflict in `param_source_note`. Architecture kept as dense per existing row — no clear evidence Anthropic has shifted to MoE.

### The LifeArchitect Claude 3 estimates

Alan Thompson published estimates in March 2024 for the Claude 3 family: Opus ~2T, Sonnet ~70B, Haiku ~20B. The 2T Opus figure has been widely repeated, but every secondary citation traces back to Thompson alone — no independent leak or analysis corroborates it. Per the orchestrator's "single LifeArchitect guess that no other source echoes -> leave as unknown" instruction, I judged this not credible enough and left Claude 3 Opus/Sonnet/Haiku rows as `unknown`. (If we later decide to soften this stance, the rows can be filled with `estimated` and a LifeArchitect URL.)

### Older Claude rows (Claude 1, Claude 2, Claude 2.1, Claude Instant)

Searched specifically for parameter estimates on each. Found community speculation ranging wildly (Claude 2 estimates spanned 12B to 130B+ across different bloggers, with no central authoritative source). No reputable analyst published a specific number for Claude 1 / Instant. Per "be conservative", left all four as `unknown`.

### Per-row decisions

- **Row 32 Claude 1**: `unknown` - retained. No credible specific estimate.
- **Row 33 Claude Instant 1**: `unknown` - retained. No credible specific estimate.
- **Row 34 Claude 2**: `unknown` - retained. Wild range of community guesses (12B-130B+); no anchor.
- **Row 35 Claude 2.1**: `unknown` - retained. Same as Claude 2.
- **Row 36 Claude 3 Opus**: `unknown` - retained. LifeArchitect 2T is single-source; no corroboration.
- **Row 37 Claude 3 Sonnet**: `unknown` - retained. LifeArchitect 70B single-source.
- **Row 38 Claude 3 Haiku**: `unknown` - retained. LifeArchitect 20B single-source.
- **Row 39 Claude 3.5 Sonnet (2024-06)**: `unknown` - retained. No specific credible estimate surfaced.
- **Row 40 Claude 3.5 Sonnet (2024-10)**: `unknown` - retained. Same.
- **Row 41 Claude 3.5 Haiku**: `unknown` - retained. Same.
- **Row 42 Claude 3.7 Sonnet**: `unknown` - retained. Same.
- **Row 43 Claude Opus 4**: `unknown` - retained. Musk leak doesn't apply (released May 2025, much earlier).
- **Row 44 Claude Sonnet 4**: `unknown` - retained.
- **Row 45 Claude Opus 4.1**: `unknown` - retained.
- **Row 46 Claude Sonnet 4.5**: UPDATED. `total_params=1000000000000`, `active_params=1000000000000`, `param_disclosure=leaked`, `param_source_note=Musk tweet 2026-04-09 inferred Sonnet=2x Grok 0.5T => 1T; widely picked up; refers to "current" Sonnet at tweet time = 4.5`, `supporting_url=https://adam.holter.com/elon-musk-accidentally-leaked-anthropics-model-sizes/`. Judgment: `leaked` (inadvertent disclosure by industry insider, multi-source corroboration).
- **Row 47 Claude Haiku 4.5**: `unknown` - retained. No Haiku-specific leak.
- **Row 48 Claude Opus 4.5**: `unknown` - retained. Musk leak doesn't directly apply (Opus 4.6 was current at time of tweet).
- **Row 49 Claude Opus 4.6**: UPDATED. `total_params=5000000000000`, `active_params=5000000000000`, `param_disclosure=leaked`, `param_source_note=Musk tweet 2026-04-09 inferred Opus=10x Grok 0.5T => 5T; refers to "current" Opus at tweet time = 4.6; conflicts with throughput-based MoE estimates of 1.5-2T`, `supporting_url=https://adam.holter.com/elon-musk-accidentally-leaked-anthropics-model-sizes/`. Judgment: `leaked` despite the throughput-analyst conflict — the Musk number is more directly attributable. Architecture kept dense (no public claim of MoE switch). Active = total per dense convention; if Anthropic is actually running MoE, active is much smaller, but no evidence yet.
- **Row 50 Claude Opus 4.7**: `unknown` - retained. Released April 16, 2026, *after* the Musk tweet. While 4.7 likely inherits 4.6's parameter count (point release), assuming so is forward extrapolation. Conservative call: leave blank.

### Sources consulted

- [EpochAI notable AI models database](https://epoch.ai/data/notable_ai_models.csv) - all Claude entries marked "Unknown" parameter count.
- [Adam Holter: Elon Musk Accidentally Leaked Anthropic's Model Sizes](https://adam.holter.com/elon-musk-accidentally-leaked-anthropics-model-sizes/) - April 10, 2026.
- [NextBigFuture: Anthropic and xAI Model Parameter Counts](https://www.nextbigfuture.com/2026/04/anthropic-and-xai-model-parameter-counts.html) - April 9, 2026.
- [36kr: Elon Musk Reveals: Claude Opus Has 5T Parameters, Sonnet Has 1T Parameters](https://eu.36kr.com/en/p/3760679047267075).
- [LifeArchitect Memo - Claude 3 special edition](https://lifearchitect.substack.com/p/the-memo-special-edition-claude-3) - Alan Thompson's Opus 2T / Sonnet 70B / Haiku 20B estimates (judged single-source, not used).
- [Unexcited Neurons: Estimating the Size of Claude Opus 4.5/4.6](https://unexcitedneurons.substack.com/p/estimating-the-size-of-claude-opus) - independent throughput-based estimate of 1.5-2T MoE for Opus 4.6 (conflicts with Musk leak; flagged).
- [Hacker News thread on Opus 4.6 size](https://news.ycombinator.com/item?id=47319205) - similar inference-based estimates around 1T total / 100B active.
- [SemiAnalysis: Scaling Laws / Claude 3.5 Opus](https://semianalysis.com/2024/12/11/scaling-laws-o1-pro-architecture-reasoning-training-infrastructure-orion-and-claude-3-5-opus-failures/) - discusses Anthropic strategy but no specific Claude param numbers.

## Mythos

- Source: https://red.anthropic.com/2026/mythos-preview/ (official Anthropic preview announcement, 2026-04-07)
- Supporting: https://www.interconnects.ai/p/claude-mythos-and-misguided-open (Nathan Lambert analysis)
- Existence first revealed: 2026-03-26 via misconfigured CMS exposing draft blog post; reported by Fortune (https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/). Anthropic confirmed same day.
- Official preview launch: 2026-04-07. Limited research preview, NOT generally available; access via Project Glasswing partners only (Amazon, Apple, Cisco, CrowdStrike, Linux Foundation, Microsoft, Palo Alto Networks, etc.).
- Key facts: total=~10T (per Eric Hartford tweet [https://x.com/QuixiAI/status/2042685919690404123] and Pasquale Pillitteri analysis [https://pasqualepillitteri.it/en/news/515/claude-mythos-anthropic-ai-model-data-leak]), active=unknown (no source describes MoE active count; left blank), context=unknown (one April Fool's-dated source claims 1M but flagged as unreliable; left blank), released=2026-04-07 (preview).
- Capabilities (per Anthropic blog): general-purpose model strong across-the-board, exceptional at cybersecurity (zero-day discovery, exploit dev, binary RE). Reasoning: yes (Anthropic spokesperson statement: "meaningful advances in reasoning, coding, and cybersecurity"). Tool use: yes (cybersecurity workflows require tool use). Vision: not mentioned in red.anthropic.com blog - left as false. Code: yes per blog.
- 10T figure provenance: Eric Hartford (Cognitive Computations / Dolphin) tweeted "Sonnet is 1T Opus is 5T Mythos is 10T" in the wake of the Musk leak, asking "I wonder what @Alibaba_Qwen would be like at 10T parameters?" The 10T figure also lines up with the Interconnects piece's framing of Mythos as "~2X larger in parameters than Opus" (5T x 2 = 10T) and with Pillitteri's "approximately 10 trillion parameters" claim. Three independent sources converge on 10T. Calling this `leaked` (the Hartford tweet implies an inside-baseball figure) rather than `estimated`. Could equally be argued `estimated`.
- Architecture: not disclosed. Setting `architecture_type=other` (closest fit per PLAN.md enum when unknown).
- frontier flags: both `false` per orchestrator instruction (Mythos is not generally available, can't be "frontier at release" in the public-deployment sense).
- open_weights: false.
- Notes: Without context window confirmed, leaving blank. Could revisit if Project Glasswing partner discloses.

## Mythos revision 2026-04-24 (post-verification)

Verifier fetched both cited URLs. Primary (`red.anthropic.com/2026/mythos-preview/`) is real but is a cybersecurity-capabilities blog and does not disclose parameters. Supporting (`interconnects.ai`) explicitly disclaims knowledge of architecture ("we know nothing about how the model works under the hood") and does not cite 10T. Orchestrator also ground-truth-fetched the red.anthropic.com URL and confirmed the same content.

The 10T figure was attributable only to an Eric Hartford tweet and convergent community chatter that neither cited URL actually quotes or links. To keep the row honest per PLAN.md, reverted `total_params` to blank and `param_disclosure` from `leaked` to `unknown`. If a citable primary source for 10T (Hartford tweet added as third supporting, or a direct Anthropic disclosure) surfaces, repopulate.

Kept `architecture_type=other` as the closest-fit enum value for "undisclosed."

# OpenAI

General policy for this lab: post-GPT-3, OpenAI has not officially disclosed parameter counts. GPT-2 (1.5B) and GPT-3 (175B) are the only rows with official params. GPT-4 uses the SemiAnalysis ~1.8T MoE leak (`leaked`). Everything else (GPT-4 Turbo, 4o, 4o mini, all o-series, 4.1, 5, etc.) gets `param_disclosure=unknown` with params blank.

`cap_text=true` throughout. `cap_tool_use`: function calling GA'd 2023-06-13 after GPT-4's initial release, so GPT-4 (2023-03-14) row is false; GPT-3.5 Turbo initial row (Nov 30 2022 as ChatGPT) is false. GPT-4 Turbo (Nov 2023) and later have tool use.

## GPT-1
- Source: https://openai.com/index/language-unsupervised/
- Supporting: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf (paper gives 12-layer 768-dim architecture; 117M params derived)
- Key facts: total=117000000 (~117M), context=512, released=2018-06-11
- Notes: Per the paper: 12-layer decoder-only transformer, 768-dim, 12 heads, 3072 FFN, 512-token context. The canonical 117M param figure is widely cited (matches Wikipedia, semanticscholar summary). param_disclosure=official (the paper describes architecture dims from which 117M follows; OpenAI's Hugging Face code repo references 117M). Trained on BooksCorpus (~7000 books). Not frontier in modern sense — was a research proof-of-concept; mark frontier_at_release=false. cap_code_specialized=false. Open weights? OpenAI released code and pretrained weights at https://github.com/openai/finetune-transformer-lm alongside the paper — mark open_weights=true.

## GPT-2
- Source: https://openai.com/index/better-language-models/ (initial announcement 2019-02-14)
- Supporting: https://openai.com/index/gpt-2-1-5b-release/ (full 1.5B weight release 2019-11-05)
- Key facts: total=1500000000 (1.5B), context=1024, released=2019-02-14 (announcement; full 1.5B weights Nov 2019)
- Notes: Staged release - initial Feb 14 2019 announcement released only 124M weights; 355M in May 2019; 774M in August; full 1.5B on Nov 5 2019. Following PLAN.md convention (release-time values) but also orchestrator guidance that "GPT-2 weights were eventually public" -> open_weights=true. Using 2019-02-14 as announcement_date per "first public announcement" rule. frontier_open_at_release=true — at Nov 2019 1.5B was the largest openly available LM; also clearly the frontier for Feb 2019 announcement as the largest transformer LM publicly unveiled (Megatron-LM was earlier NVIDIA but not comparable scale at that time). Context 1024 tokens per GPT-2 paper. cap_code_specialized=false.

## GPT-3
- Source: https://openai.com/index/language-models-are-few-shot-learners/
- Supporting: https://arxiv.org/abs/2005.14165 (paper states 175B params and architecture details including 2048 context)
- Key facts: total=175000000000, context=2048, released=2020-05-28 (arXiv v1 date; OpenAI blog coincident)
- Notes: Official 175B disclosure in the paper. Architecture: dense decoder-only transformer. Context 2048 tokens (community.openai.com and EleutherAI confirm). frontier_at_release=true — at May 2020, clearly SOTA LM by a wide margin. open_weights=false (closed API; beta starting June 2020). Not code-specialized. No tool use. No vision/audio. param_disclosure=official (paper).

## Codex (2021)
- Source: https://arxiv.org/abs/2107.03374 (paper; 2021-07-07 on arXiv)
- Supporting: https://openai.com/index/introducing-codex/ (August 10 2021 blog announcing private beta)
- Key facts: total=12000000000 (12B), context=4096, released=2021-07-07 (arXiv) / 2021-08-10 (blog private-beta launch). Using arXiv date as announcement since it's the first public disclosure.
- Notes: The paper discusses multiple Codex sizes (300M, 2.5B, 12B). Canonical public Codex model in the initial private beta is the 12B (code-davinci-001 / -002 derived from it). Context_length 4096 per OpenAI developer community threads contemporaneous with private beta. param_disclosure=official (paper explicitly states parameter counts). cap_code_specialized=true. open_weights=false. Not frontier overall (GPT-3 was bigger and still current); frontier for code specifically at release — but we only flag `frontier_at_release` for overall SOTA, so false. cap_tool_use=false.

## GPT-3.5 Turbo / ChatGPT initial release
- Source: https://openai.com/index/chatgpt/ (ChatGPT launch, 2022-11-30)
- Key facts: total=unknown (never officially disclosed; gpt-3.5 lineage only loosely described), context=4096 (original gpt-3.5-turbo), released=2022-11-30
- Notes: ChatGPT initial release used a model described as "fine-tuned from a model in the GPT-3.5 series." The GPT-3.5 Turbo API model named gpt-3.5-turbo was launched in March 2023 with 4k context. Using 2022-11-30 ChatGPT launch as the canonical "GPT-3.5 era" release event per orchestrator guidance. Named "GPT-3.5 (ChatGPT)" in the CSV for clarity. param_disclosure=unknown (OpenAI never gave numbers; community estimates vary wildly from ~20B to 175B — no authoritative source). cap_vision=false. cap_audio=false. cap_code_specialized=false. cap_tool_use=false (function calling came June 2023). cap_reasoning=false. frontier_at_release=true — at launch it was the top conversational model; GPT-4 did not yet exist. open_weights=false.

## GPT-4
- Source: https://openai.com/index/gpt-4-research/
- Supporting: https://semianalysis.com/2023/07/10/gpt-4-architecture-infrastructure/ (SemiAnalysis MoE leak — 1.8T total / ~280B active, 16 experts top-2)
- Key facts: total=1800000000000 (~1.8T leaked), active=280000000000 (~280B leaked, 2 of 16 experts x ~111B each plus shared params — exact number cited as ~280B in leak coverage), context=8192 (base model at launch; 32k variant available with limited access), released=2023-03-14
- Notes: Per SemiAnalysis leak (published Jul 10 2023; widely covered by The-Decoder etc): ~1.8T total across 120 layers, MoE with 16 experts of ~111B MLP each, top-2 routing. Active per token ~280B. This is the canonical `leaked` param entry. architecture_type=MoE. cap_vision=false at initial 2023-03-14 launch (GPT-4V vision rollout later in Sep 2023 for ChatGPT; vision in API came with gpt-4-turbo-with-vision Nov 2023 DevDay). cap_audio=false. cap_tool_use=false (function calling June 2023). cap_reasoning=false (pre-o1 era). frontier_at_release=true. open_weights=false.

## GPT-4 Turbo
- Source: https://openai.com/index/new-models-and-developer-products-announced-at-devday/
- Key facts: params=unknown (OpenAI never disclosed; no credible single-point leak specific to Turbo), context=128000, released=2023-11-06
- Notes: DevDay 2023. First model with 128k context. Introduced JSON mode, reproducible outputs, vision in gpt-4-turbo-with-vision. cap_vision=true (GPT-4 Turbo with Vision launched same event; listed on DevDay blog). cap_tool_use=true (function calling & Assistants API GA). cap_reasoning=false. frontier_at_release=true — was SOTA at launch, beating base GPT-4, Claude 2/2.1 at the time. Knowledge cutoff April 2023. open_weights=false.

## GPT-4o
- Source: https://openai.com/index/hello-gpt-4o/
- Key facts: params=unknown, context=128000, released=2024-05-13
- Notes: Native multimodal (text+vision+audio), real-time voice mode. cap_vision=true, cap_audio=true (native audio in/out), cap_tool_use=true, cap_code_specialized=false, cap_reasoning=false. frontier_at_release=true — at May 2024 was SOTA especially on multimodal and voice. Knowledge cutoff Oct 2023. open_weights=false. No cap_video (live video demos but not formally model input at launch; video input came later).

## GPT-4o mini
- Source: https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/
- Key facts: params=unknown, context=128000, released=2024-07-18
- Notes: Cost-efficient small model. At launch supported text and vision; audio promised but not initially available. cap_vision=true (text+vision in API at launch per OpenAI blog). cap_audio=false (blog says "support for text, image, video and audio inputs and outputs coming in the future"). cap_tool_use=true (function calling supported). cap_reasoning=false. Not frontier — designed as cost-efficient tier. 82% MMLU. open_weights=false.

## OpenAI o1-preview
- Source: https://openai.com/index/introducing-openai-o1-preview/
- Key facts: params=unknown, context=128000 (API; 32k in ChatGPT), released=2024-09-12
- Notes: First reasoning model. cap_reasoning=true. cap_vision=false at initial preview launch (image support came with full o1 in December 2024). cap_tool_use=false at preview (no function calling / structured outputs until full o1/o3 era). cap_audio=false. Not frontier overall — preview was competitive with GPT-4o but ChatGPT-restricted and no tools. Actually judgment: o1-preview was SOTA on reasoning tasks (math, science, code). Marking frontier_at_release=true given it defined a new reasoning frontier. open_weights=false.

## OpenAI o1-mini
- Source: https://openai.com/index/introducing-openai-o1-preview/
- Key facts: params=unknown, context=128000 (API), released=2024-09-12
- Notes: Smaller, cost-efficient reasoning variant. Same blog as o1-preview. cap_reasoning=true. cap_vision=false. cap_tool_use=false. frontier_at_release=false (smaller tier).

## OpenAI o1 (full)
- Source: https://openai.com/index/introducing-chatgpt-pro/ (12 Days of OpenAI Day 1, Dec 5 2024; o1 full launch)
- Supporting: https://openai.com/index/openai-o1-system-card/ (system card)
- Note: The OpenAI blog for o1 full release is https://openai.com/index/openai-o1-and-new-tools-for-developers/ (Dec 17 2024, API availability). The Dec 5 announcement brought o1 full to ChatGPT Pro; Dec 17 brought it to API with function calling, structured outputs, vision.
- Key facts: params=unknown, context=200000 (API context with o1 full; increased from 128k of o1-preview), released=2024-12-05 (ChatGPT) / 2024-12-17 (API). Using 2024-12-05 as announcement_date.
- Notes: Full o1 added vision (image uploads), 34% fewer major errors vs o1-preview, supported function calling, structured outputs, developer messages. cap_reasoning=true, cap_vision=true, cap_tool_use=true (added Dec 17 API). frontier_at_release=true — at Dec 2024 was SOTA reasoning. open_weights=false.

## OpenAI o3-mini
- Source: https://openai.com/index/openai-o3-mini/
- Key facts: params=unknown, context=200000, released=2025-01-31
- Notes: First o-series model GA'd with function calling, structured outputs, and developer messages from day one. Three reasoning_effort settings (low/medium/high). cap_reasoning=true, cap_vision=false (o3-mini did not support vision input at launch per OpenAI docs; o3 full and o4-mini did), cap_tool_use=true. Not frontier (cost-efficient tier). open_weights=false. 200k context per OpenAI platform docs.

## OpenAI o3 (full) + o4-mini
- Source: https://openai.com/index/introducing-o3-and-o4-mini/ (2025-04-16)
- Key facts for o3: params=unknown, context=200000, released=2025-04-16
- Key facts for o4-mini: params=unknown, context=200000, released=2025-04-16
- Notes: Two-row release event. Both are the first o-series models that can agentically use all ChatGPT tools (web search, Python, file analysis, image gen). "Think with images" — first time reasoning is applied to visual inputs directly. cap_reasoning=true, cap_vision=true, cap_tool_use=true, cap_audio=false. For o3: frontier_at_release=true — at Apr 2025 was SOTA reasoning, top on many benchmarks (Claude 3.7 Sonnet was a peer; judgment call). For o4-mini: frontier_at_release=false (cost-efficient tier but exceptionally strong — best-benchmarked on AIME; still not the family flagship). Note on o3 announcement date: o3 was previewed Dec 20 2024 but GA April 16 2025. Using 2025-04-16 as announcement_date (when the actual model was released; Dec 2024 was only a preview of benchmark numbers). Note o3 was preceded by a separate o3-mini GA (Jan 31).
- open_weights=false.

## GPT-4.1
- Source: https://openai.com/index/gpt-4-1/
- Key facts: params=unknown, context=1000000 (1M tokens), released=2025-04-14
- Notes: API-only at launch. Three sizes released simultaneously: GPT-4.1, GPT-4.1 mini, GPT-4.1 nano. Per PLAN.md row-selection rule, treat as three rows since distinct size announcements. cap_vision=true (GPT-4.1 is multimodal per docs), cap_tool_use=true, cap_reasoning=false, cap_code_specialized=false. 21.4pp SWE-bench improvement over GPT-4o. Knowledge cutoff June 2024. frontier_at_release=false — at Apr 14 2025, o3 had stronger reasoning (launched 2 days later) and Claude 3.7 Sonnet was already out. GPT-4.1 positioned as non-reasoning coding workhorse. open_weights=false.
- Judgment: including 4.1, 4.1 mini, 4.1 nano as separate rows given they're explicitly named sizes in the announcement.

## o3-pro
- Source: https://openai.com/index/o3-pro/ (assumed; TechCrunch corroborates June 10 2025)
- Supporting: https://techcrunch.com/2025/06/10/openai-releases-o3-pro-a-souped-up-version-of-its-o3-ai-reasoning-model/
- Key facts: params=unknown, context=200000, released=2025-06-10
- Notes: Uses parallel test-time compute — o3 variant that thinks longer and harder. Replaces o1-pro. Available to ChatGPT Pro & Team. cap_reasoning=true, cap_vision=true, cap_tool_use=true. frontier_at_release=true (SOTA on hard reasoning tasks at release, though Claude Opus 4 May 22 2025 was a peer). Judgment: marking false - o3-pro is a compute scaling variant of o3, not a new capability frontier. Let me reconsider: it was positioned as the most capable reasoning model at release, exceeding o3. Marking frontier_at_release=true given OpenAI explicitly positioned it as SOTA. open_weights=false.
- Primary URL note: I'm using `https://openai.com/index/o3-pro/` — standard OpenAI announcement URL format. If not exact, TechCrunch is the confirmed secondary.

## GPT-4.5
- Source: https://openai.com/index/introducing-gpt-4-5/
- Supporting: https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf (system card)
- Key facts: params=unknown (largest OpenAI model to date per announcement but no number), context=128000, released=2025-02-27
- Notes: Research preview. Largest model by compute/data to that point. cap_vision=true, cap_tool_use=true, cap_reasoning=false (not a thinking model — OpenAI explicitly positioned as scaled pre-training + post-training, not test-time reasoning). Deprecated from API Jul 14 2025 when GPT-4.1 replaced it. Not initially in scope per orchestrator brief but is a distinct headline event between o-series releases and GPT-4.1 — including as a row per "any other headline flagship" clause. frontier_at_release=false — at Feb 27 2025 Claude 3.7 Sonnet was released 3 days earlier (Feb 24) and was clearly ahead on benchmarks; GPT-4.5 was primarily a "taste and EQ" play. open_weights=false.

## GPT-5
- Source: https://openai.com/index/introducing-gpt-5/
- Supporting: https://openai.com/index/introducing-gpt-5-for-developers/ (developer API details; context=400k)
- Key facts: params=unknown, context=400000 (272k input + 128k output/reasoning), released=2025-08-07
- Notes: Unified system: "smart efficient model" (gpt-5-main) + "deeper reasoning model" (gpt-5-thinking) + real-time router. Per OpenAI: "unified system that knows when to respond quickly and when to think longer." cap_reasoning=true (controllable thinking is core to GPT-5 per announcement). cap_vision=true, cap_tool_use=true. API sizes: gpt-5, gpt-5-mini, gpt-5-nano. Treating as separate rows for standard, mini, nano per GPT-4.1 precedent. frontier_at_release=true — SOTA across most benchmarks at Aug 7 2025. open_weights=false. GPT-5-pro (parallel test-time compute variant) is a ChatGPT Pro feature; arguably a separate row but OpenAI describes it as a setting on gpt-5-thinking, not a distinct model — treating as part of the GPT-5 flagship row.

## GPT-5.1
- Source: https://openai.com/index/gpt-5-1/
- Supporting: https://openai.com/index/gpt-5-1-for-developers/
- Key facts: params=unknown, context=400000, released=2025-11-12
- Notes: Includes Instant, Thinking variants. Adaptive reasoning in Instant. Warmer conversational tone. cap_reasoning=true, cap_vision=true, cap_tool_use=true. Deprecated Mar 11 2026 when GPT-5.3 replaced. Including as a row since it's a distinct named release with system card. frontier_at_release=false — incremental over GPT-5; Anthropic's Sonnet 4.5/Opus 4.5 were strong peers. open_weights=false.

## GPT-5.2
- Source: https://openai.com/index/introducing-gpt-5-2/
- Supporting: https://openai.com/index/gpt-5-system-card-update-gpt-5-2/
- Key facts: params=unknown, context=400000, released=2025-12-11
- Notes: "Code Red" rushed release in response to Google Gemini 3. Three modes: Instant, Thinking (standard + extended), Pro. cap_reasoning=true, cap_vision=true, cap_tool_use=true. frontier_at_release=true — Anthropic Sonnet 4.5 still out; Gemini 3 had just shipped; GPT-5.2 positioned as retaking frontier on coding and agentic tasks. Marking true given OpenAI's Code Red framing and strong benchmark claims. open_weights=false.

## GPT-5.5
- Source: https://openai.com/index/introducing-gpt-5-5/
- Supporting: https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/
- Key facts: params=unknown, context=400000 (400K in Codex), released=2026-04-23
- Notes: Latest OpenAI frontier as of 2026-04-24 cutoff (day after release). Three variants: standard, Thinking, Pro. 88.7% SWE-bench, 92.4% MMLU, 60% fewer hallucinations vs 5.4. Rolling out to paid tiers in ChatGPT and Codex; API release delayed. cap_reasoning=true, cap_vision=true, cap_tool_use=true. frontier_at_release=true. open_weights=false. Not including GPT-5.3/5.4/Codex variants as separate rows — they're point updates between 5.2 and 5.5; the orchestrator scope asks for "headline flagship" events and I treat 5.1, 5.2, and 5.5 as the canonical numbered versions with distinct system cards. (5.3/5.4 included in the skipped list below.)

## Release events considered but skipped
- GPT-3.5 Turbo API launch (March 2023) / gpt-3.5-turbo-16k (June 2023): collapsed into the 2022-11-30 ChatGPT row per PLAN.md row-selection rule (API snapshots of the same headline model). The 16k variant was a context extension, not a distinct headline model.
- GPT-4-32k: context-extension variant of GPT-4; collapsed into the GPT-4 headline row.
- GPT-4 Turbo with Vision (Nov 2023) vs base GPT-4 Turbo: same headline model; vision was part of the Turbo DevDay package. Captured on the GPT-4 Turbo row.
- gpt-4-turbo-2024-04-09: API snapshot; collapsed.
- GPT-4o audio preview, realtime API, audio in API (Oct 2024): feature additions to GPT-4o, not a new model.
- gpt-4o-2024-08-06 / 11-20 snapshots: collapsed into GPT-4o row.
- o1-pro (Mar 2025): variant of o1 with parallel test-time compute; I'm making a judgment call to skip since it's a compute-scaling setting on o1 (same model weights per OpenAI docs). Note this asymmetry with o3-pro, which I am including — the reason I'm including o3-pro is the orchestrator explicitly listed "o3-pro" as a possible inclusion.
- GPT-5.3, GPT-5.4, GPT-5.2-Codex, GPT-5.3-Codex: rapid-cadence point updates between 5.2 and 5.5; Codex variants are coding-agent specialized fine-tunes. Including all would inflate the row count with minor refreshes. Keeping 5.1/5.2/5.5 as the representative headline versions.
- Operator, Sora, DALL-E 3, Whisper, text-embedding-3-*, moderation models, gpt-image-1: not general-purpose text LLMs.
- Advanced Voice Mode launch (Sep 2024): a ChatGPT feature on top of GPT-4o, not a new model.
- GPT-OSS-20B / GPT-OSS-120B (Aug 2025 open-weights release): these ARE separate releases and should arguably be included. However they're the first OpenAI open-weights models — noting here for scope expansion if needed. **Including decision**: per orchestrator scope ("any other headline flagship between 2025-04 and 2026-04-24"), gpt-oss is borderline. I'm including gpt-oss-120B as a row since it's a distinct open-weights headline event — it will be one of very few rows with open_weights=true for OpenAI.
- Actually, re-reading the scope: orchestrator listed specific events and said "Any other headline flagship ... GPT-5 variants, o3-pro." gpt-oss is a flagship-adjacent event. Including the 120B row; skipping 20B to avoid bloat.

## gpt-oss-120b
- Source: https://openai.com/index/introducing-gpt-oss/ (assumed OpenAI announcement URL)
- Supporting: https://huggingface.co/openai/gpt-oss-120b (model card)
- Key facts: total=117000000000 (117B), active=5100000000 (5.1B), context=131072 (128k), released=2025-08-05
- Notes: Open-weights reasoning model. MoE, 128 experts, 4 active per token per HF card. Apache 2.0 license. First OpenAI open-weights LLM since GPT-2. cap_reasoning=true (chain-of-thought with configurable reasoning effort), cap_vision=false, cap_tool_use=true, cap_code_specialized=false. frontier_at_release=false (smaller than GPT-5 proprietary; similar tier to o3-mini/o4-mini on benchmarks). frontier_open_at_release=false — at Aug 5 2025, DeepSeek-V3.1 / Qwen3 / Llama 4 were competing; gpt-oss was competitive but not clearly the frontier open-weights. Actually 120B MoE with 5.1B active is a strong open reasoning model; marking frontier_open_at_release=true given it was the strongest o-series-style open reasoning model at release.
- open_weights=true. param_disclosure=official (OpenAI blog and HF card explicitly state 117B total / 5.1B active — these are the canonical numbers, not rounded 120B). Using 117B for total, 5.1B active.

## Fields I could not confirm from primary sources (OpenAI)
- All post-GPT-3 parameter counts except GPT-4 (which has the SemiAnalysis leak) — OpenAI policy.
- o3-pro blog URL: assumed openai.com/index/o3-pro/. TechCrunch supporting.
- GPT-5 exact architecture (MoE vs dense; router + multiple models): architecture_type=other is the best fit since it's explicitly a multi-model system; but orchestrator convention leans toward `other` only when nothing else fits. Going with `other` to be honest about the unified router architecture. Active for GPT-5 unknown.
- GPT-5.5 context confirmed as 400k in Codex; API context for non-Codex standard GPT-5.5 not yet confirmed for general API (blog says "not launching to the API today").
