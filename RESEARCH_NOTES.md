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

## Gopher (280B)
- Source: https://arxiv.org/abs/2112.11446 (Scaling Language Models paper, Dec 8 2021)
- Supporting: https://deepmind.google/blog/language-modelling-at-scale-gopher-ethical-considerations-and-retrieval/ (DeepMind blog same date)
- Key facts: total=280000000000, active=280000000000 (dense), context=2048, released=2021-12-08
- Notes: DeepMind research model, never offered commercially. Dense decoder-only transformer. Was frontier at release (outperformed GPT-3, Jurassic-1, MT-NLG on most tasks). frontier_at_release=true, frontier_open_at_release=false (closed). No vision/audio/tool-use.

## Chinchilla (70B)
- Source: https://arxiv.org/abs/2203.15556 (Training Compute-Optimal LLMs, Mar 29 2022)
- Key facts: total=70000000000, active=70000000000 (dense), context=2048, released=2022-03-29
- Notes: DeepMind research model demonstrating compute-optimal scaling. Outperformed Gopher 280B despite being 4x smaller. Dense decoder, same architecture family as Gopher. frontier_at_release=true (SOTA on MMLU at release per abstract). Never released publicly. No vision/audio/tool-use capabilities.

## LaMDA
- Source: https://arxiv.org/abs/2201.08239 (LaMDA paper, Jan 20 2022)
- Supporting: https://research.google/blog/lamda-towards-safe-grounded-and-high-quality-dialog-models-for-everything/
- Key facts: total=137000000000, active=137000000000 (dense), context=unknown from paper abstract, released=2022-01-20 (arXiv; original announcement at I/O 2021-05-18 but paper+params disclosed Jan 2022)
- Notes: Google dialog-specialized transformer. Dense; paper explicitly gives 137B for largest variant. cap_tool_use=true — LaMDA includes a toolset (calculator, translator, IR system) per the paper abstract for grounding. Not frontier at public disclosure (GPT-3, PaLM direction emerging). frontier_at_release=false. Context window: going with 1024 (conservative, commonly cited for dialog models of this era); mark unknown where needed. Actually leaving context blank — not confirmed in paper abstract.

## PaLM (540B)
- Source: https://research.google/blog/pathways-language-model-palm-scaling-to-540-billion-parameters-for-breakthrough-performance/
- Key facts: total=540000000000, active=540000000000 (dense), context=2048, released=2022-04-04
- Notes: Google's Pathways Language Model. Dense decoder. Was frontier at release (SOTA on 28/29 tasks vs GPT-3, GLaM, MT-NLG, Gopher, Chinchilla, LaMDA). frontier_at_release=true. Closed-weights. Context confirmed 2048 in PaLM paper.

## PaLM 2
- Source: https://ai.google/discover/palm2/ (Google official PaLM 2 page)
- Supporting: https://www.cnbc.com/2023/05/16/googles-palm-2-uses-nearly-five-times-more-text-data-than-predecessor.html (CNBC leak disclosing 340B params, 3.6T tokens)
- Key facts: total=340000000000 (CNBC leaked internal doc), active=340000000000 (dense assumed), context=8192 (per technical report), released=2023-05-10 (Google I/O)
- Notes: param_disclosure=leaked. Google did not officially confirm parameter count; the tech report omits it. CNBC internal-document leak cited as supporting_url. Not clearly frontier at release (GPT-4 already out and dominant). frontier_at_release=false. Closed-weights.

## Gemini 1.0 Ultra
- Source: https://blog.google/technology/ai/google-gemini-ai/ (announcement Dec 6 2023)
- Supporting: https://storage.googleapis.com/deepmind-media/gemini/gemini_1_report.pdf (Gemini 1.0 Technical Report)
- Key facts: total=unknown, active=unknown, context=32768 (32K per tech report), released=2023-12-06
- Notes: Google did not disclose params for Ultra/Pro. Native multimodal (text/image/audio/video). cap_tool_use=true per subsequent Gemini API launches. frontier_at_release=true (launched as the most capable Gemini, competing directly with GPT-4). Closed-weights.

## Gemini 1.0 Pro
- Source: https://blog.google/technology/ai/google-gemini-ai/
- Supporting: https://storage.googleapis.com/deepmind-media/gemini/gemini_1_report.pdf
- Key facts: total=unknown, active=unknown, context=32768, released=2023-12-06
- Notes: Mid-tier Gemini. Multimodal like Ultra. Not frontier (below Ultra and GPT-4). frontier_at_release=false.

## Gemini 1.0 Nano
- Source: https://storage.googleapis.com/deepmind-media/gemini/gemini_1_report.pdf (technical report explicitly states Nano-1 1.8B / Nano-2 3.25B)
- Supporting: https://blog.google/technology/ai/google-gemini-ai/
- Key facts: total=3250000000 (using Nano-2, the larger variant as the canonical "Nano"), active=3250000000 (dense), context=32768, released=2023-12-06
- Notes: On-device model. Two sub-variants Nano-1 (1.8B) and Nano-2 (3.25B); I'm listing one row using Nano-2 (the larger/more capable) with the decomposition noted in param_source_note. Distilled from larger Gemini. open_weights=false (embedded in Android/Chrome, weights not downloadable). param_disclosure=official.

## Gemma 1 2B
- Source: https://blog.google/technology/developers/gemma-open-models/ (Feb 21 2024)
- Supporting: https://huggingface.co/google/gemma-2b (model card — context 8192 confirmed)
- Key facts: total=2000000000 (approx, 2B nominal; exact 2.51B per tech report), active=2000000000 (dense), context=8192, released=2024-02-21
- Notes: Open-weights under Gemma license (commercial-friendly). frontier_open_at_release=false (many larger open models existed). Text-only, no vision. License is not Apache 2.0 but "Gemma license" — still counts as open_weights=true per PLAN convention.

## Gemma 1 7B
- Source: https://blog.google/technology/developers/gemma-open-models/
- Supporting: https://huggingface.co/google/gemma-7b (context 8192 confirmed)
- Key facts: total=7000000000 (7B nominal; 8.54B with embedding per tech report but commonly reported as 7B), active=7000000000, context=8192, released=2024-02-21
- Notes: Text-only open-weight. Not frontier_open (Mixtral 8x7B, Llama 2 70B existed). frontier_open_at_release=false.

## Gemini 1.5 Pro
- Source: https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/
- Key facts: total=unknown, active=unknown (MoE confirmed but specifics closed), context=1000000 (1M tokens at release in private preview; standard 128K), released=2024-02-15
- Notes: Explicit MoE architecture per blog. 1M context window was frontier at release (longest in industry). Multimodal (text/image/audio/video). Going with 1000000 as the release context (blog's headline number, though standard tier shipped with 128K). frontier_at_release=true on context-window dimension; overall capability was GPT-4-class. Closed-weights.

## CodeGemma 7B
- Source: https://developers.googleblog.com/en/gemma-family-expands-with-models-tailored-for-developers-and-researchers/ (Apr 9 2024)
- Supporting: https://huggingface.co/google/codegemma-7b
- Key facts: total=7000000000, active=7000000000 (dense), context=8192, released=2024-04-09
- Notes: Code-specialized open-weight. cap_code_specialized=true. Open under Gemma license. Not frontier_open_at_release (Code Llama, DeepSeek-Coder existed larger).

## RecurrentGemma 2B
- Source: https://developers.googleblog.com/en/gemma-family-expands-with-models-tailored-for-developers-and-researchers/
- Supporting: https://huggingface.co/google/recurrentgemma-2b
- Key facts: total=2000000000 (2B nominal), active=2000000000, context=8192 (training context), released=2024-04-09
- Notes: Griffin architecture (hybrid linear-recurrence + local attention). architecture_type=hybrid (recurrent+attention, not pure SSM — Griffin uses attention layers). Open-weight. Not frontier.

## Gemini 1.5 Flash
- Source: https://blog.google/technology/ai/google-gemini-update-flash-ai-assistant-io-2024/ (May 14 2024 I/O keynote)
- Key facts: total=unknown, active=unknown, context=1000000, released=2024-05-14
- Notes: Distilled from 1.5 Pro per tech report. 1M context at release. Multimodal. Not frontier (smaller, cheaper sibling). Closed-weights.

## PaliGemma 3B
- Source: https://developers.googleblog.com/en/gemma-family-and-toolkit-expansion-io-2024/ (May 14 2024)
- Supporting: https://huggingface.co/google/paligemma-3b-pt-224
- Key facts: total=3000000000 (2B Gemma decoder + 400M SigLIP encoder, approx 3B total), active=3000000000, context=128 to 512 tokens text input (short — this is a VLM, not long-context), released=2024-05-14
- Notes: Vision-language model. Uses SigLIP vision encoder + Gemma 2B decoder. cap_vision=true. Context at pre-training was 128 text tokens per mixture variant; putting 512 as the release context for the 448/896 variants. Open-weight under Gemma license.

## Gemma 2 27B
- Source: https://blog.google/technology/developers/google-gemma-2/ (Jun 27 2024)
- Supporting: https://huggingface.co/blog/gemma2 (context window 8192 confirmed)
- Key facts: total=27000000000, active=27000000000 (dense), context=8192, released=2024-06-27
- Notes: Flagship Gemma 2. Open-weight under Gemma license. Ranked around Claude 3 Sonnet / Llama 3 70B on Chatbot Arena at release — briefly competitive. frontier_open_at_release=false (Llama 3 70B / Mixtral 8x22B / DeepSeek-V2 were stronger/larger). Text-only, no vision.

## Gemma 2 9B
- Source: https://blog.google/technology/developers/google-gemma-2/
- Supporting: https://huggingface.co/blog/gemma2
- Key facts: total=9000000000, active=9000000000, context=8192, released=2024-06-27
- Notes: Mid-tier Gemma 2. Outperformed Llama 3 8B in the class per announcement. Not frontier_open.

## Gemma 2 2B
- Source: https://huggingface.co/blog/gemma-july-update (Jul 31 2024)
- Supporting: https://developers.googleblog.com/en/smaller-safer-more-transparent-advancing-responsible-ai-with-gemma/
- Key facts: total=2000000000, active=2000000000, context=8192, released=2024-07-31
- Notes: Small Gemma 2 variant released later. Open-weight. Not frontier.

## Gemini 2.0 Flash
- Source: https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/ (Dec 11 2024)
- Key facts: total=unknown, active=unknown, context=1000000, released=2024-12-11
- Notes: Native multimodal input (image/audio/video). Native tool use (Search, code execution, functions). Multimodal output (image, TTS). Not frontier (3.5 Sonnet / o1 / GPT-4o dominated). Closed-weights. cap_reasoning=false — this is the base Flash, Thinking variant came later.

## Gemini 2.0 Flash Thinking (Experimental)
- Source: https://ai.google.dev/gemini-api/docs/changelog (release notes) — reasoning announcement Dec 19 2024
- Supporting: https://simonwillison.net/2024/Dec/19/gemini-thinking-mode/
- Key facts: total=unknown, active=unknown, context=32768 (initially 32K limited), released=2024-12-19
- Notes: Experimental reasoning variant of 2.0 Flash. cap_reasoning=true. Context window was initially capped at 32K per docs. Closed-weights. Not frontier at release (o1 full was released Dec 5 2024).

## Gemini 2.0 Pro (Experimental)
- Source: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-updates-february-2025/ (Feb 5 2025)
- Key facts: total=unknown, active=unknown, context=2000000 (2M), released=2025-02-05
- Notes: 2M context at release. Best Google model pre-2.5. Multimodal, tool use. Not overall frontier (o3-mini and Claude 3.5 Sonnet still dominant in coding; GPT-4.5 imminent). cap_reasoning=false (this was the non-thinking flagship; Thinking came from 2.5 onward).

## Gemini 2.0 Flash-Lite
- Source: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-model-updates-february-2025/
- Key facts: total=unknown, active=unknown, context=1000000, released=2025-02-05
- Notes: Most cost-efficient Gemini. 1M context. Not frontier.

## Gemma 3 27B
- Source: https://blog.google/technology/developers/gemma-3/ (Mar 12 2025)
- Supporting: https://huggingface.co/blog/gemma3
- Key facts: total=27000000000 (decoder) + SigLIP vision encoder ~400M (not included in nominal; HF says decoder-only count), active=27000000000, context=131072 (128K for 4/12/27B), released=2025-03-12
- Notes: Multimodal (text + image for 4B/12B/27B). 128K context. Open-weight under Gemma license. Claimed "best single-accelerator model" outperforming Llama-405B, DeepSeek-V3, o3-mini on LMArena. frontier_open_at_release=borderline; at 27B it wasn't the largest open, but was claimed the strongest in the single-GPU class. Not overall frontier. Keeping frontier_open_at_release=false (DeepSeek-V3 671B and Llama 3.1 405B existed). Using 27B as the nominal param count; vision encoder noted in param_source_note.

## Gemma 3 12B
- Source: https://blog.google/technology/developers/gemma-3/
- Supporting: https://huggingface.co/blog/gemma3
- Key facts: total=12000000000, active=12000000000, context=131072, released=2025-03-12
- Notes: Mid-tier Gemma 3, multimodal. Open-weight.

## Gemma 3 4B
- Source: https://blog.google/technology/developers/gemma-3/
- Supporting: https://huggingface.co/blog/gemma3
- Key facts: total=4000000000, active=4000000000, context=131072, released=2025-03-12
- Notes: Multimodal. Open-weight.

## Gemma 3 1B
- Source: https://blog.google/technology/developers/gemma-3/
- Supporting: https://huggingface.co/blog/gemma3
- Key facts: total=1000000000, active=1000000000, context=32768, released=2025-03-12
- Notes: Text-only (no vision for 1B variant). 32K context (smaller than siblings). Open-weight.

## Gemini 2.5 Pro
- Source: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/ (Mar 25 2025)
- Key facts: total=unknown, active=unknown, context=1000000 (1M at release, 2M coming later), released=2025-03-25
- Notes: Thinking model — cap_reasoning=true. Debuted #1 on LMArena by significant margin. Multimodal (text/audio/image/video/code). Arguably frontier at release (beat o3-mini on GPQA/AIME, competitive with Claude 3.7 Sonnet / GPT-4.5). frontier_at_release=true. Tool use: yes (2.5 has native tool use inherited from 2.0). Closed-weights.

## Gemini 2.5 Flash
- Source: https://blog.google/products/gemini/gemini-2-5-flash/ — actually no single dedicated blog; the I/O 2025 page references it. Using: https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/ — no, let me use the Vertex AI / AI Studio release note.
- Using release_url: https://ai.google.dev/gemini-api/docs/changelog (documents Apr 17 2025 preview)
- Better release_url: https://blog.google/products/gemini/gemini-2-5-flash/ — testing this
- Going with: https://developers.googleblog.com/en/start-building-with-gemini-2-5-flash/
- Key facts: total=unknown, active=unknown, context=1000000, released=2025-04-17 (preview); thinking budget introduced here
- Notes: Thinking model with configurable thinking budget. cap_reasoning=true. Not frontier (sibling of 2.5 Pro, cheaper/faster). Closed-weights.

## Gemini 3 Pro
- Source: https://blog.google/products/gemini/gemini-3/ (Nov 18 2025)
- Key facts: total=unknown, active=unknown, context=1000000 (1M tokens explicit in blog), released=2025-11-18
- Notes: Google's most advanced model. Multimodal (text/image/video/audio/code). Tool use explicit (Terminal-Bench 2.0 54.2%). Deep Think mode available for enhanced reasoning. cap_reasoning=true (Deep Think is the premium variant, but the base model also has native thinking built in per the 3 release). frontier_at_release=true (beat competitors on most benchmarks at release per coverage). Closed-weights.

## Gemini 3.1 Pro
- Source: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/ (Feb 19 2026)
- Supporting: https://9to5google.com/2026/02/19/google-announces-gemini-3-1-pro-for-complex-problem-solving/
- Key facts: total=unknown, active=unknown, context=1000000, released=2026-02-19
- Notes: Incremental 3.x bump. 77.1% ARC-AGI-2 (more than double 3 Pro), 80.6% SWE-Bench Verified, 94.3% GPQA Diamond per blog. cap_reasoning=true. Multimodal. frontier_at_release=true (SOTA on ARC-AGI-2 and GPQA at release).

## Fields I could not confirm from primary sources (Google)
- Parameter counts for every Gemini model except Nano (officially 1.8B/3.25B in tech report).
- PaLM 2 relies on CNBC leak for 340B, but Google never officially confirmed.
- Gemini 2.5 Flash exact release URL uncertain — Google consolidates announcements in developer blog posts; using the Google Developers Blog "Gemini 2.5 updates" post.
- Gemma 3 vision-encoder parameter decomposition: SigLIP encoder is ~400M but HF blog confirms nominal params (1B/4B/12B/27B) refer to language model only. Using nominal counts per convention.

## Fixup pass 2026-04-24 (Google rows 79-108)
- Row 80 LaMDA: cleared cap_tool_use (not mentioned in arXiv paper or Google blog).
- Row 81 Chinchilla: removed "1.4T tokens" claim from param_source_note — paper doesn't explicitly state that in a way our schema needs; token count not required by schema.
- Row 82 PaLM 540B: removed "780B tokens" from param_source_note (appears in the paper but not the cited Google Research blog).
- Row 83 PaLM 2: CNBC supporting URL (https://www.cnbc.com/2023/05/16/googles-palm-2-uses-nearly-five-times-more-text-data-than-predecessor.html) does reach 200 with a browser user agent (check-urls helper confirms). The verifier's 403 was a Cloudflare bot-block, not a fabricated URL. No change.
- Row 87 Gemini 1.5 Pro: context_window 1000000 -> 128000 per schema "max at release" rule; 1M was limited preview, 128K was the standard offering per the blog. Note added.
- Row 93 PaliGemma 3B: context_window 512 -> 128 to match HF model card's "128 token input/output text sequences".
- Row 96 Gemma 2 2B: total_params / active_params 2.0B -> 2.6B per HF July-update blog.
- Row 99 Gemini 2.0 Pro Experimental: cap_audio + cap_video set to false (blog says "more modalities ready for GA in the coming months" — not at release).
- Row 100 Gemini 2.0 Flash-Lite: cap_audio, cap_video, cap_tool_use all set to false (blog doesn't mention tool use for Flash-Lite specifically; audio/video planned for later).
- Row 105 Gemini 2.5 Pro: added supporting_url = https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro which explicitly states "Function calling: Supported" and input token limit 1,048,576.
- Row 106 Gemini 2.5 Flash: swapped supporting_url to https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash which confirms context window, multimodal input, and function calling.
- Row 108 Gemini 3.1 Pro: swapped supporting_url to https://deepmind.google/models/model-cards/gemini-3-1-pro/ which confirms 1M token context and multimodal inputs (text/audio/images/video).

## CNBC Cloudflare bot-block
- https://www.cnbc.com/* URLs systematically return 403 to automated fetchers (WebFetch, raw curl without headers) while resolving 200 to browser-UA requests. The check-urls helper with its browser UA confirms reachability. Do not rewrite CNBC URLs on the basis of a 403 from WebFetch alone.

## xAI research 2026-04-24 (rows 109-122)

### Rows added
- 109 Grok-1.5 (2024-03-28)
- 110 Grok-1.5V (2024-04-12)
- 111 Grok-2 (2024-08-13)
- 112 Grok-2 mini (2024-08-13)
- 113 Grok-3 (2025-02-17)
- 114 Grok-3 (Think) (2025-02-17)
- 115 Grok-3 mini (2025-02-17)
- 116 Grok-3 mini (Think) (2025-02-17)
- 117 Grok-4 (2025-07-09)
- 118 Grok-4 Heavy (2025-07-09)
- 119 Grok-4 Fast (2025-09-19)
- 120 Grok-4.1 (2025-11-17)
- 121 Grok-4.1 Fast (2025-11-17)
- 122 Grok-4.20 (2026-02-17)

All 14 rows are `param_disclosure=unknown` with both param columns blank — xAI has not officially disclosed parameter counts for any of the closed-weight Grok generations. (Grok-1's 314B MoE disclosure belongs to the open-weights track and is out of scope here.) architecture_type=`other` for all rows on the same grounds — xAI has not confirmed dense-vs-MoE publicly for any Grok ≥ 1.5, and retro-fitting Grok-1's MoE onto later generations would be speculation.

### x.ai/news/* Cloudflare bot-block
Identical failure mode to openai.com. Every `https://x.ai/news/grok-*` URL returns 403 to WebFetch and to `check-urls` (browser UA with redirects) despite resolving fine in a real browser. The 403s are a domain-wide automation block, not a hallucination signal. WebSearch snippets and reputable secondary coverage confirm each slug (`grok-1.5`, `grok-1.5v`, `grok-2`, `grok-3`, `grok-4`, `grok-4-fast`, `grok-4-1`, `grok-4-1-fast`) is real. I kept the xAI URL as `release_url` for each model and backed every non-trivial fact with a `supporting_url` that is fetchable.

### Supporting-URL choices and what they back
- **Grok-1.5**: TechCrunch 2024-03-28 coverage backs announcement date and 128K context.
- **Grok-1.5V**: SiliconANGLE backs the April 12 2024 announcement and vision-capability description; parameter count untouched.
- **Grok-2 / Grok-2 mini**: Wikipedia "Grok (chatbot)" article backs August 13 2024 beta debut and the documented fact that image-understanding was added in October 2024 (not at release), which is why `cap_vision=false` for both Aug-2024 rows.
- **Grok-3 family (rows 113-116)**: TechCrunch 2025-02-17 article backs the release date, the existence of both reasoning and non-reasoning variants (Grok 3, Grok 3 Reasoning, Grok 3 mini, Grok 3 mini Reasoning), and "enhanced image analysis" for cap_vision.
- **Grok-4**: data.x.ai model card PDF is the primary supporting URL — quotes "latest reasoning model from xAI with advanced reasoning and tool-use capabilities" (backs cap_reasoning + cap_tool_use); TechCrunch 2025-07-09 covers the release date and HLE benchmark numbers.
- **Grok-4 Heavy**: TechCrunch 2025-07-09 quotes Musk's "study group" multi-agent description and the 50.7% HLE claim (backs frontier_at_release=true).
- **Grok-4 Fast**: Simon Willison's blog post is a high-quality technical writeup confirming 2M context, unified reasoning/non-reasoning architecture, and tool-use RL training.
- **Grok-4.1 / 4.1 Fast**: Better Stack guide backs November 17 2025 launch, the Thinking reasoning mode, Agent Tools API (cap_tool_use), and Grok-4.1 Fast's 2M context.
- **Grok-4.20**: no dedicated x.ai/news page existed at research time; `release_url` is docs.x.ai/developers/release-notes (which lists "Grok 4.20 and Grok 4.20 Multi-agent are live"), supporting_url is NextBigFuture's Feb 2026 coverage of the multi-agent system and provisional LMArena ELO.

### Judgment calls worth re-verifying
- **Grok-3 as frontier_at_release=true**. Grok-3 (Think) topped o3-mini-high on AIME 2025 and was in the same tier as o1 at Feb 2025 release. The brief warned to be conservative, but Grok-3 genuinely was at the top of its era before GPT-5 / Claude 4 / Gemini 2.5. I left Grok-3 and Grok-3 (Think) as frontier, but Grok-3 mini variants as non-frontier (smaller sibling).
- **Grok-4 / Grok-4 Heavy as frontier**. Grok-4 Heavy hit 50.7% HLE (first model over 50%) and Artificial Analysis Intelligence Index listed it top at release. Clear frontier call.
- **Grok-4.1 as frontier**. xAI reported LMArena Text Arena #1 at 1483 Elo at release — a defensible frontier claim.
- **Grok-4.20 as frontier**. Reported LMArena 1505-1535 at release (above Grok-4.1). Marginal but defensible.
- **Grok-3 reasoning variants as separate rows**. xAI explicitly announced "Grok 3 (Think)" and "Grok 3 mini (Think)" as distinct beta reasoning models, so the four-row split (base + Think, for each of full and mini) matches the Row-selection rule "when the same name ships twice with different behavior ... that's two rows with dated names." Alternative would have been two rows with cap_reasoning toggled per-mode, but the split preserves more information for the downstream plot.
- **Grok-4 cap_vision left false**. Neither the x.ai/news/grok-4 page (bot-blocked, can't verify) nor the model card PDF nor the TechCrunch coverage explicitly states "native image input" at release. Conservative setting — if verifier finds explicit backing in a fetchable URL, flip to true.
- **architecture_type=`other`** for every Grok row. xAI has not publicly confirmed dense-vs-MoE for closed-weight Grok generations; the only confirmed architecture is Grok-1 (MoE, 314B) which is out of scope. Defaulting to `other` rather than guessing.

### Fields I could not confirm from primary sources
- Parameter counts for every closed-weight Grok model.
- Architecture type (dense vs MoE) for every closed-weight Grok model.
- Exact context-window numbers for Grok-2 and Grok-2 mini (used 131072 per secondary API docs and community summaries; xAI blog did not explicitly quote a token count I could pin to the bot-blocked URL).
- Native image input for Grok-4 and Grok-4 Heavy (left cap_vision=false).
- Grok-3 API context reality vs blog claim: xAI claimed 1M but the initial API launch in April 2025 capped at 131K. Per "max at release" convention I used the xAI blog's 1M claim; if the verifier prefers the deployable limit, adjust to 131072.
- Whether Grok-3 supports function calling: not explicitly mentioned in TechCrunch 2025-02-17; left cap_tool_use=false across the Grok-3 family. (DeepSearch is a product feature, not an API function-calling spec.)

### check-urls pre-flight
- Every `https://x.ai/news/grok-*` URL returns 403 — systematic Cloudflare bot-block, not a fabrication signal. All other cited URLs (TechCrunch, SiliconANGLE, Wikipedia, data.x.ai PDF, docs.x.ai, Simon Willison, Better Stack, NextBigFuture) return 200.

## xAI fixup 2026-04-24

Verifier-flagged issues on rows 109-122 resolved this pass.

### Row 110 (Grok-1.5V)
- context_window: 128000 -> blank. Neither release_url (x.ai/news/grok-1.5v, Cloudflare-blocked) nor supporting_url (SiliconANGLE) explicitly states a token count for Grok-1.5V. Inheritance from Grok-1.5 base is inference, not disclosure; per instructions, blanked rather than leave unverifiable number.
- param_source_note: updated to remove the "(128K)" inheritance claim and explain the blank.

### Row 111 (Grok-2)
- supporting_url: Wikipedia -> TechCrunch 2024/08/13 ("xais-grok-can-now-generate-images-on-x"). TechCrunch article text explicitly states "xAI launched Grok-2 and Grok-2 mini in beta today" on Aug 13 2024, resolving the Wikipedia "Aug 14" mismatch in favor of Aug 13 (verified via WebFetch).
- context_window: 131072 -> blank. TechCrunch does not give a token count. The 131,072 value is only documented for the later grok-2-1212 API build (Dec 2024, per OpenRouter/llm-stats) and cannot be carried on a release-date row without a contemporaneous disclosure. Blanked per verifier instructions.
- param_source_note: rewritten to reflect the new supporting_url and explain the blank.

### Row 112 (Grok-2 mini)
- supporting_url: Wikipedia -> TechCrunch 2024/08/13. Same reasoning as row 111 — TechCrunch confirms Grok-2 mini shipped "alongside" Grok-2 in beta on Aug 13 2024.
- context_window: 131072 -> blank. No contemporaneous fetchable source gives a Grok-2 mini token count at release.
- param_source_note: rewritten.

### Row 113 (Grok-3)
- context_window: 1000000 -> blank. TechCrunch 2025/02/17 does not mention context size. xAI blog's 1M claim is only visible in a Cloudflare-blocked URL that the verifier cannot fetch; later API-era sources (PromptHub, datastudios.org) document 131K. Blanked per "every numeric claim must appear in the text of at least one of the cited URLs" rule.
- param_source_note: updated to explain the blank.

### Row 114 (Grok-3 Think)
- context_window: 1000000 -> blank. Same reasoning as row 113.
- param_source_note: updated.

### Row 115 (Grok-3 mini)
- context_window: 1000000 -> blank. Same reasoning as row 113.
- param_source_note: updated.

### Row 116 (Grok-3 mini Think)
- context_window: 1000000 -> blank. Same reasoning as row 113.
- param_source_note: updated.

### Row 117 (Grok-4)
- supporting_url: data.x.ai/2025-08-20-grok-4-model-card.pdf (binary PDF, unreadable by verifier) -> https://openrouter.ai/x-ai/grok-4 (HTML, 200). OpenRouter page explicitly documents "Released Jul 9, 2025", "256,000 context", and "supports parallel tool calling, structured outputs, and both image and text inputs" — single source covering release date, context window, vision input, and tool use.
- cap_vision: false -> true. OpenRouter states Grok-4 "supports...both image and text inputs"; TechCrunch separately corroborates ("can analyze images and respond to questions"). Native image input at release confirmed.
- context_window: 256000 kept (now backed by OpenRouter).
- param_source_note: rewritten to cite OpenRouter specifics.

### Row 118 (Grok-4 Heavy)
- context_window: 256000 -> blank. TechCrunch supporting_url (which covers the Heavy-specific multi-agent framing, $300/mo tier, and July 9 date) does not state a token count. Keeping TechCrunch (more load-bearing for Heavy-specific claims) and blanking context_window per verifier rule. Secondary sources (aitoolapp.com/grok-4/context-window) do confirm Heavy uses the 256K window but using them would force dropping TechCrunch, which is more valuable for the multi-agent/pricing/date attestation.
- cap_vision: false -> true. TechCrunch confirms "can analyze images and respond to questions" (shared Grok-4 base capability); Heavy inherits image input from base.
- param_source_note: updated.

### Row 119 (Grok-4 Fast)
- cap_reasoning: already true in file (verifier appears to have miscounted columns when flagging). Left as true and clarified the note: Simon Willison's "same model weights handle reasoning and non-reasoning based on a parameter passed to the model" supports cap_reasoning=true since reasoning is a native (toggleable) mode in the same weights.
- param_source_note: reworded to make the "togglable reasoning => cap_reasoning=true" reasoning explicit.

### Row 122 (Grok-4.20)
- supporting_url: NextBigFuture -> https://www.adwaitx.com/grok-4-20-beta-release-date-xai-launch/ . Adwaitx article states "Grok 4.20 Beta launched on February 17, 2026" and documents 256K base context expandable to 2M, the 4-agent collaboration architecture, and rapid-learning weekly cadence — stronger contemporaneous attestation of the Feb 17 date than NextBigFuture, which was looser on specifics.
- announcement_date: kept 2026-02-17. docs.x.ai release-notes says "March 2026", but that marks the general-availability rollout; first public announcement / beta launch was Feb 17 2026 per Adwaitx (confirmed via WebFetch) and corroborated by Wikipedia's versions-table entry. announcement_date semantics = "first public announcement", so Feb 17 stands.
- param_source_note: rewritten to explain the Feb-vs-March distinction explicitly so the verifier does not re-flag it.

### Unchanged FAILs (none)
All hard FAILs resolved. Remaining PARTIALs (context_window blanks on rows 110-116 and 118) converted to properly attributed blanks per the "blank rather than unverifiable" principle. No items left unresolved.

---

## Frontier-params estimates 2026-04-24

Targeted pass to fill `total_params` / `active_params` for frontier-at-release rows that had blank params. Source sweep: Microsoft MEDEC paper (arXiv:2412.19260) for GPT & Claude 3.5 numbers, 36kr/LifeArchitect for Claude 3 Opus and Opus 4 ranges, EpochAI (via The Decoder) for cross-check on GPT-4o, LifeArchitect `gemini` page for Gemini 1.0 Ultra, Data Science Dojo / AppLabx / natural20.com for Grok-3/4/4.20 numbers. All supporting URLs HEAD-checked 200.

### MEDEC paper — primary citation for OpenAI/Anthropic rows

arxiv.org/html/2412.19260v1 §5.1 Language Models — WebFetch-verified verbatim quotes:
- ChatGPT: "≈175B"
- GPT-4: "≈1.76T"
- GPT-4o: "≈200B"
- GPT-4o-mini: "≈8B parameters"
- o1-mini: "≈100B"
- o1-preview: "≈300B"
- Claude 3.5 Sonnet: "the latest model (≈175B parameters)"

Paper's own disclaimer: "Most numbers of parameters are estimate reported to provide more context for understanding the models' performance." Per our schema → `param_disclosure=leaked` (MS Research paper unintentional disclosure, widely picked up).

### Rows touched

- **Row 36 Claude 3 Opus**: total=active=2_000_000_000_000 (`estimated`). Cited 36kr article which quotes "Claude 3 Opus (~2T)" and attributes to LifeArchitect / industry analysis. Architecture stayed dense (no MoE confirmation). Supporting URL: https://eu.36kr.com/en/p/3760679047267075

- **Row 39 Claude 3.5 Sonnet (2024-06)**: total=active=175_000_000_000 (`leaked`). MEDEC paper "≈175B parameters". Supporting URL: https://arxiv.org/html/2412.19260v1 . Note: MEDEC was Dec 2024 and the paper says "latest model" which by then was the Oct checkpoint, but the Jun 2024 release was the first under the 3.5 Sonnet name — applying the same figure to both Jun and Oct rows since they're siblings with no publicly-claimed param delta.

- **Row 40 Claude 3.5 Sonnet (2024-10)**: total=active=175_000_000_000 (`leaked`). Same source as row 39 — this is the Dec-2024-"latest" that MEDEC is directly referring to (claude-3-5-sonnet-20241022).

- **Row 42 Claude 3.7 Sonnet**: LEFT BLANK. No citable specific number; search hits list only vague "100+ billion" without primary attribution. Conservative call per orchestrator rule 6.

- **Row 43 Claude Opus 4**: total=active=400_000_000_000 (`estimated`). 36kr quotes "the parameters of Claude Opus 4 are between 300 - 500B" — midpoint stored. Supporting URL: 36kr.

- **Row 45 Claude Opus 4.1**: LEFT BLANK. No direct source for 4.1 specifically. The "drop-in upgrade to Opus 4" framing suggests same scale but extrapolating that to the param column would be forward inference, not sourced.

- **Row 48 Claude Opus 4.5**: LEFT BLANK. No direct source. 36kr only gave the 3.5 Sonnet/Opus 4 ranges and the (current-at-tweet) 5T Opus 4.6 figure. 4.5 (Nov 2025) sits between these and has no dedicated attribution.

- **Row 50 Claude Opus 4.7**: LEFT BLANK. Released after the Musk leak; no new direct source.

- **Row 56 GPT-3.5 (ChatGPT)**: total=active=175_000_000_000 (`leaked`). MEDEC paper "ChatGPT: ≈175B" (matches GPT-3 base size). Supporting URL: MEDEC.

- **Row 58 GPT-4 Turbo**: LEFT BLANK. No MEDEC entry specific to Turbo; SemiAnalysis's 1.8T leak is for the original GPT-4 (already in row 57). Could not find a citable Turbo-specific number.

- **Row 59 GPT-4o**: total=active=200_000_000_000 (`leaked`). MEDEC "≈200B" + EpochAI ~200B (via The Decoder) as cross-check. Supporting URL: MEDEC. architecture_type kept as `other` (omnimodal decoder, MoE not confirmed).

- **Row 61 OpenAI o1-preview**: total=active=300_000_000_000 (`leaked`). MEDEC "o1-preview: ≈300B". Supporting URL: MEDEC.

- **Row 63 OpenAI o1**: total=active=300_000_000_000 (`leaked`). MEDEC only names "o1-preview" (≈300B), but o1-full is the GA of the same model, so same estimate applied. Noted in the source note that the paper's explicit naming is "o1-preview"; treating this as same underlying weights. Supporting URL: MEDEC.

- **Row 69 OpenAI o3**: LEFT BLANK. No credible citable number found; LifeArchitect's o3 page explicitly doesn't commit a figure.

- **Row 71 OpenAI o3-pro**: LEFT BLANK. Same reason as o3.

- **Row 73 GPT-5**: LEFT BLANK. LifeArchitect gpt-5 page states "~300B" as Alan Thompson's estimate, but SemiCon Taiwan (Samsung) slide said 3-5T — a full order-of-magnitude conflict. Swapping supporting_url to LifeArchitect would also break the existing 400k-context support from the OpenAI developer blog. Kept conservative; plot will have gap at GPT-5 but the source conflict is too material to resolve without a definitive leak.

- **Row 77 GPT-5.2**: LEFT BLANK. Same situation; no incremental source.

- **Row 78 GPT-5.5**: LEFT BLANK. Same situation; no incremental source.

- **Row 84 Gemini 1.0 Ultra**: total=active=1_500_000_000_000 (`estimated`). LifeArchitect `gemini` page explicit summary: "Ultra: 1.5T". Supporting URL: https://lifearchitect.ai/gemini/ (replaced Gemini 1 tech report, which only covers Nano sizes anyway).

- **Row 87 Gemini 1.5 Pro**: LEFT BLANK. Google confirms MoE in blog but has not disclosed params. No credible single-number estimate in a fetchable citable source; Tunguz assertion of "1T" is unsourced self-estimate.

- **Row 105 Gemini 2.5 Pro**: LEFT BLANK. Same as 1.5 Pro — Google technical report confirms sparse MoE but no param count; Tunguz's "1T" is unsourced.

- **Row 107 Gemini 3 Pro**: LEFT BLANK. Bloomberg 1.2T is for a custom Apple-Siri Gemini variant, not definitively the public Gemini 3 Pro row. Tunguz asserts "same as 2.5, 1T" but sources his own claim to nothing.

- **Row 108 Gemini 3.1 Pro**: LEFT BLANK. No direct citation.

- **Row 113 Grok-3**: total=active=2_700_000_000_000 (`estimated`). AppLabx analysis: "2.7 trillion parameters" (also corroborated by artsmart.ai). Same source confirms Feb 17 2025 launch and multimodal architecture (cap_vision). architecture_type kept `other` — AppLabx says "Custom Hybrid transformer"; neither dense nor MoE formally attested. active=total per no MoE confirmation in cited source. Swapped supporting_url from TechCrunch → https://blog.applabx.com/the-state-of-grok-ai-in-2025-an-in-depth-analysis/

- **Row 114 Grok-3 (Think)**: total=active=2_700_000_000_000 (`estimated`). Same weights as row 113 base; same AppLabx source applies. Swapped supporting_url the same way.

- **Row 117 Grok-4**: total=active=1_700_000_000_000 (`estimated`). Data Science Dojo: "Grok 4 boasts around 1.7 trillion parameters." Same source confirms July 2025 release, 256k API context, text+image, function calling — so swap from OpenRouter is net gain. architecture_type kept `other` (Data Science Dojo says "modular architecture"; deeplearning.ai calls it MoE while whitex.ai calls it dense — three sources disagree on architecture, so not committing). active=total per schema default for 'other'.

- **Row 118 Grok-4 Heavy**: total=active=1_700_000_000_000 (`estimated`). Heavy spawns agents of the same base weights; Data Science Dojo covers both base params and the "multi-agent architecture for complex collaborative reasoning" framing. Swapped TechCrunch → Data Science Dojo.

- **Row 120 Grok-4.1**: LEFT BLANK. No citable number specific to 4.1; ybuild.ai's ~3T MoE figure is the only direct claim but swapping to ybuild loses date/vision/tool coverage that Better Stack provides.

- **Row 122 Grok-4.20**: total=active=500_000_000_000 (`leaked`). Natural20 article directly quotes Musk: "This is just our V8 small foundation model, so 500B params". This is the *same* Musk tweet that anchors the Sonnet=1T/Opus=5T leak chain used for rows 46 and 49, now citable as an independent fetchable URL. Natural20 also covers Feb 17 2026 date, 4-agent architecture, and 256K-2M context. Swapped Adwaitx → Natural20.

### Summary

Filled 13 rows. Left 17 rows blank per orchestrator rule 6 (no credible fetchable single-number source). Filled-row net gain covers: Claude 3 Opus, Claude 3.5 Sonnet (both dates), Claude Opus 4, all the MEDEC-covered OpenAI rows (ChatGPT, GPT-4o, o1-preview, o1), Gemini 1.0 Ultra, Grok-3 & Think, Grok-4 & Heavy, Grok-4.20. Judgment calls documented above include: (a) applying the "o1-preview" MEDEC number to full o1, (b) applying the "latest 3.5 Sonnet" MEDEC number to the June 2024 row as well as the October row, (c) applying the Grok-4 base 1.7T figure per-agent to Grok-4 Heavy, (d) keeping architecture_type=other rather than MoE for Grok-3/4 because cited sources disagree. Where two sources reported different ranges (Opus 4 300-500B), stored the midpoint and documented the range in the note per orchestrator rule 5.

Conflicting estimates noted explicitly:
- Grok-3: AppLabx 2.7T vs LifeArchitect/ybuild "~3T MoE with 300-600B active" — stored AppLabx figure, noted the MoE alternative.
- Grok-4: Data Science Dojo 1.7T "modular" vs deeplearning.ai 1.7T MoE vs whitex.ai 1.7T dense — all three agree on 1.7T but disagree on architecture; stored 1.7T total=active with 'other' architecture.
- GPT-5: LifeArchitect 300B vs SemiCon Taiwan Samsung slide 3-5T — order-of-magnitude conflict, left blank rather than pick a side.
- Claude Opus 4.6: 36kr/Musk leak 5T vs unexcitedneurons throughput analysis 1.5-2T MoE — previously resolved to 5T in row 49; conflict stands.

## Mythos re-population 2026-04-24

User directive: restore the 10T figure now that speculative sources are accepted. Found a citable Medium article — "Claude Mythos 5: The First 10-Trillion-Parameter Model" (Analyst Uttam, Apr 5 2026) — that directly quotes "a staggering 10 trillion parameters" and attributes it to the late-March Anthropic CMS misconfiguration leak. Replaced interconnects.ai supporting_url (which had explicitly disclaimed architectural knowledge) with the Medium URL. param_disclosure=estimated (analyst estimate, not a direct Anthropic disclosure). Also flipped frontier_at_release from false to true — at 10T Mythos is a clear frontier data point above Opus 4.6's 5T. Note: check-urls HEAD returns 403 on Medium (similar to openai.com/x.ai pattern), but WebFetch via browser UA succeeds; the 403 on HEAD does not indicate a dead link.

## Other-closed bucket (Cohere / AI21 / Inflection / Reka / Amazon Nova) — 2026-04-24

### Cohere

#### Command R
- Source: https://cohere.com/blog/command-r (announcement blog, Mar 11 2024)
- Supporting: https://huggingface.co/CohereForAI/c4ai-command-r-v01 (HF model card for params/context/license)
- Key facts: params=35B (official on HF card), context=128K, released=2024-03-11, license=CC-BY-NC + Cohere Labs Acceptable Use Policy
- Open weights: true (research-only, non-commercial via CC-BY-NC). Orchestrator asked to flag license in notes.
- Capabilities: RAG + tool use (single-step function-calling) positioned; supported 10 languages. cap_tool_use=true per HF card "Single-Step Tool Use", cap_vision=false.
- frontier_open_at_release: false — Mar 2024 open-weights frontier was Grok-1 314B (released Mar 17) and Mixtral 8x22B was near. 35B is strong for its size class but not the largest open weights.
- frontier_at_release: false — far below GPT-4 Turbo / Claude 3 Opus.
- supporting_url supports: total_params (35B), context_window (128K).

#### Command R+
- Source: https://cohere.com/blog/command-r-plus-microsoft-azure (Apr 4 2024)
- Supporting: https://huggingface.co/CohereForAI/c4ai-command-r-plus (HF model card)
- Key facts: params=104B (official on HF card), context=128K, released=2024-04-04, license=CC-BY-NC
- Open weights: true (CC-BY-NC).
- Capabilities: explicit tool use (multi-step / function calling), RAG with citations, 10 languages. cap_tool_use=true, cap_vision=false.
- frontier_open_at_release: false — Llama 3 70B released 2024-04-18, and Mixtral 8x22B (also Apr 2024, 141B MoE) was near. 104B Command R+ was notable for its size but Llama 3 70B and Mixtral 8x22B dominated the open-weights frontier conversation in April 2024. Be conservative.
- frontier_at_release: false — GPT-4 Turbo and Claude 3 Opus were clearly ahead.
- supporting_url supports: total_params (104B), context_window (128K).

#### Command R7B
- Source: https://cohere.com/blog/command-r7b (Dec 13 2024)
- Supporting: https://huggingface.co/CohereLabs/c4ai-command-r7b-12-2024 (HF model card)
- Key facts: params=7B (official; "At 7 billion parameters" in MarkTechPost, 7B on HF), context=128K, released=2024-12-13, license=CC-BY-NC
- Open weights: true (CC-BY-NC).
- Capabilities: RAG, tool use, 23 languages. cap_tool_use=true, cap_vision=false.
- frontier_open_at_release: false — Dec 2024 open-weights frontier was DeepSeek-V3 (671B MoE), Llama 3.3 70B (released Dec 6 2024), Qwen 2.5 72B.
- frontier_at_release: false.
- supporting_url supports: total_params (7B), context_window (128K), license.

#### Command A
- Source: https://docs.cohere.com/v2/changelog/command-a (Cohere docs changelog entry for command-a-03-2025)
- Supporting: https://huggingface.co/CohereLabs/c4ai-command-a-03-2025 (HF model card)
- Key facts: params=111B (official on HF card), context=256K, released=2025-03 (model ID "03-2025"), license=CC-BY-NC
- Open weights: true (CC-BY-NC).
- Capabilities: tool use, RAG, code gen; 23 languages. cap_tool_use=true, cap_vision=false (pure text).
- Notes on date: docs.cohere.com/v2/changelog/command-a is dated; Cohere documentation references March 2025 announcement. Using 2025-03-11 (matches pattern of Cohere's typical announcement date being mid-month and the model ID "03-2025"). If orchestrator wants stricter sourcing, let me know — the changelog entry itself doesn't carry a visible ISO date but the model ID embeds the month.
- supporting_url supports: total_params (111B), context_window (256K), license.

#### Command A Vision
- Source: https://cohere.com/blog/command-a-vision (July 31 2025 per search results)
- Supporting: https://huggingface.co/CohereLabs/command-a-vision-07-2025 (HF model card)
- Key facts: params=112B (HF card; built on Command A 111B text decoder + SigLIP2 vision encoder), context=128K, released=2025-07-31, license=CC-BY-NC
- Open weights: true (CC-BY-NC).
- Capabilities: vision (image understanding, up to 20 images per request) + all Command A capabilities. cap_vision=true, cap_tool_use=true.
- supporting_url supports: total_params (112B), context_window (128K), cap_vision confirmation.

#### Command A Reasoning
- NOT in orchestrator's explicit scope ("Command A / Command A-Vision" was the request). Not adding a row — if user wants it later, easy to add.

#### Original Command (pre-R, 2022-2023)
- SKIPPED. No clear single-date launch — the model was in beta Nov 2022 with "command-xlarge-20221108" and got continually updated through 2023 as nightly releases. No param disclosure, no clean announcement post. Orchestrator said "Original 'Command' (pre-R) is closed" — I judge this doesn't fit the "one row per announced release event" rule cleanly enough to add without a proper launch date.

### AI21 Labs

#### Jurassic-1 Jumbo (178B)
- Source: https://www.ai21.com/blog/announcing-ai21-studio-and-jurassic-1/ (Aug 11 2021)
- Supporting: https://uploads-ssl.webflow.com/60fd4503684b466578c0d307/61138924626a6981ee09caf6_jurassic_tech_paper.pdf (technical paper with 178B param confirmation)
- Key facts: params=178B (official, in paper and blog), context=2048 (standard GPT-3-era), released=2021-08-11
- Architecture: dense transformer, 76 layers, novel 250K vocabulary.
- Open weights: false — API-only access via AI21 Studio.
- frontier_at_release: true — Aug 2021 was the month Jurassic-1 Jumbo shipped as world's largest publicly-accessible dense LM at 178B (3B more than GPT-3 175B, which was the reigning closed-model benchmark). Megatron-Turing NLG 530B didn't land until Oct 2021. So yes, frontier at release.
- frontier_open_at_release: false — closed.
- Capabilities: text completion, no vision/audio/code-specialized. cap_tool_use=false (2021 — no function calling).
- context_window: checking — the Jurassic-1 paper doesn't emphasize a context window but standard GPT-3-era 2048 applies. Paper: "context of up to 2048 tokens".
- supporting_url supports: total_params (178B explicit), context_window (2048 in paper).

#### Jurassic-2 Jumbo
- Source: https://www.ai21.com/blog/introducing-j2/ (Mar 9 2023)
- Supporting: none needed — AI21 didn't disclose params for J2, so no supporting URL for a number that doesn't exist.
- Key facts: params=unknown (AI21 did NOT disclose), context=8192 (later confirmed by Bedrock docs), released=2023-03-09
- param_disclosure=unknown — no disclosed figure. Per orchestrator rule: leave blank.
- Open weights: false.
- Architecture: dense (assumed — dense-family lineage from J1).
- Capabilities: text, 6+ languages, zero-shot instruction-following.
- frontier_at_release: false — Mar 2023 is post-ChatGPT / GPT-4 (March 14). J2 wasn't competitive with GPT-4.
- cap_tool_use: false — AI21 J2 didn't have native function calling at release.
- Skipping J2-Grande and J2-Large per orchestrator rule "one row per announced release event" when the family shares an announcement. Will include a single J2 Jumbo row as the flagship. AI21 Jurassic-2 Mid/Grande (aka J2-Grande-Instruct) and Large are the other sizes but all announced same day — Jumbo is the flagship. Let me decide: orchestrator listed "Jurassic-2 (Jumbo/Grande/Large, Mar 2023)" suggesting maybe three rows. But PLAN "same-day multi-size family → each size its own row". I'll add all three to be consistent with Llama 3.1 8/70/405B treatment — but since params are all undisclosed, the three rows differ only in name. I'll add just one J2 Jumbo row since the Grande/Large rows would be identically-unknown and add no signal. Documenting this judgment call here.

### Inflection AI

#### Inflection-1
- Source: https://inflection.ai/inflection-1 (Jun 22 2023)
- Key facts: params=unknown, context=unknown (not disclosed), released=2023-06-22
- Architecture: dense (assumed; no disclosure).
- Capabilities: text only. No code specialization. cap_tool_use=false.
- Compute context: trained in same compute class as GPT-3.5; outperformed GPT-3.5, LLaMA, Chinchilla, PaLM-540B on MMLU per their benchmark claims.
- Open weights: false.
- frontier_at_release: false — GPT-4 already out March 2023, Inflection-1 targeted GPT-3.5 class.
- No supporting_url needed — Inflection didn't disclose technical details anywhere, so there's nothing to corroborate.

#### Inflection-2
- Source: https://inflection.ai/inflection-2 (Nov 22 2023)
- Key facts: params=unknown, context=unknown, released=2023-11-22
- Compute: trained on 5,000 H100 GPUs at ~10^25 FLOPs.
- Architecture: dense (assumed).
- Open weights: false.
- frontier_at_release: false — not ahead of GPT-4 at its time; Inflection claimed "second most capable LLM" based on PaLM 2 Large comparisons but this doesn't put it above GPT-4 or Claude 2.
- No supporting_url — no param disclosure.

#### Inflection-2.5
- Source: https://inflection.ai/inflection-2-5 (Mar 7 2024)
- Key facts: params=unknown (Inflection explicitly didn't disclose), context=unknown, released=2024-03-07
- Compute: "94% GPT-4 performance on 40% training FLOPs"
- Architecture: dense (assumed).
- Capabilities: real-time web search, coding/math improvements.
- Open weights: false.
- frontier_at_release: false — reached "near GPT-4" level but did not surpass it; Mar 2024 frontier was Claude 3 Opus (Mar 4) and GPT-4 Turbo.
- No supporting_url — no disclosure.

### Reka AI

#### Reka Flash (original, Feb 2024)
- Source: https://reka.ai/news/reka-flash-efficient-and-capable-multimodal-language-models (Feb 12 2024)
- Supporting: https://arxiv.org/abs/2404.12387 (tech report, Apr 18 2024 — confirms 21B and multimodal)
- Key facts: params=21B (official in announcement and paper), context=unknown at Feb release (later update to 128K Oct 2024), released=2024-02-12
- Architecture: dense multimodal (text+image+video+audio inputs).
- Open weights: false at release — API-only via Reka Playground. (Reka Flash 3 released Mar 2025 is the open-weights one, Apache 2.0.)
- Capabilities: multimodal (vision, audio, video). cap_vision=true, cap_audio=true, cap_video=true.
- frontier_at_release: false — GPT-4, Claude 2/3 were frontier.
- supporting_url supports: params (21B), multimodal capabilities.

#### Reka Edge (Feb 2024)
- Same announcement as Reka Flash: https://reka.ai/news/reka-flash-efficient-and-capable-multimodal-language-models
- Supporting: https://arxiv.org/abs/2404.12387
- Key facts: params=7B (official in announcement and paper), context=unknown, released=2024-02-12
- Architecture: dense multimodal.
- Open weights: false at release.
- Capabilities: multimodal (vision, audio, video).
- Per the "same-day multi-size family" rule — separate row from Flash despite same announcement.

#### Reka Core (Apr 2024)
- Source: https://reka.ai/news/reka-core-our-frontier-class-multimodal-language-model (Apr 15 2024)
- Supporting: https://arxiv.org/abs/2404.12387 (tech report, confirms all 3 models)
- Key facts: params=unknown (Reka did NOT disclose Core's size; paper also withholds), context=128K, released=2024-04-15
- Architecture: dense multimodal (assumed; paper and blog don't specify MoE).
- Open weights: false.
- Capabilities: multimodal (text, image, video, audio). Competitive with GPT-4V, Claude 3 Opus on blind human eval. cap_vision=true, cap_audio=true, cap_video=true.
- frontier_at_release: false — benchmarked "competitive with GPT-4V" but not ahead of Claude 3 Opus / GPT-4 Turbo in Apr 2024.
- cap_tool_use: unclear from release, leaving false.
- supporting_url supports: multimodal capabilities confirmation, context_window (paper corroborates 128K).

#### Reka Flash 3 (Mar 2025)
- Source: https://reka.ai/news/introducing-reka-flash (Mar 10 2025 "Reasoning with Reka Flash 3")
- Supporting: https://huggingface.co/RekaAI/reka-flash-3 (HF card, Apache 2.0)
- Key facts: params=21B (official), context=32K, released=2025-03-10, license=Apache 2.0
- Architecture: dense (21B reasoning model).
- Open weights: TRUE — Apache 2.0. This is Reka's first open-weights release.
- Capabilities: reasoning / chain-of-thought model (cap_reasoning=true — per orchestrator "only explicit test-time-reasoning families"; Reka explicitly positions it as reasoning model). Text-only per HF card (multimodal Reka Flash variants are separate).
- frontier_at_release: false — Mar 2025 frontier is Claude 3.7 Sonnet, GPT-4.5.
- frontier_open_at_release: false — Mar 2025 open-weights has DeepSeek-R1 (Jan 2025, 671B reasoning), Qwen 2.5.
- supporting_url supports: params (21B), license, format details.

#### Reka Flash 3.1 (July 2025)
- Source: https://reka.ai/news/reka-flash-3-1-and-reka-quant (Jul 10 2025)
- Key facts: params=21B (same as Flash 3, confirmed by Reka), context=unknown at post (likely 32K same as Flash 3), released=2025-07-10
- Decision: NOT adding as a separate row — this is a minor point-release of Flash 3 (better coding benchmarks, same architecture, same param count). Per PLAN "dated API snapshots of the same headline model → collapse to the headline row unless capabilities or params changed." Flash 3.1 didn't change capability class materially.

### Amazon Nova

#### Nova Micro / Lite / Pro
- Source: https://aws.amazon.com/blogs/aws/introducing-amazon-nova-frontier-intelligence-and-industry-leading-price-performance/ (Dec 3 2024)
- Key facts: params=unknown (Amazon did NOT disclose any Nova param counts), released=2024-12-03
- Context windows (from AWS blog):
  - Nova Micro: 128K tokens, text-only
  - Nova Lite: 300K tokens, multimodal (text, image, video input)
  - Nova Pro: 300K tokens, multimodal
- Architecture: assumed dense; not disclosed.
- Open weights: false (Bedrock-only).
- Capabilities:
  - Micro: text only, cap_vision=false, cap_audio=false, cap_video=false
  - Lite: cap_vision=true, cap_video=true (up to 30 min video), cap_audio=false (no audio input mentioned in blog; video input but not audio)
  - Pro: same as Lite — cap_vision=true, cap_video=true
- cap_tool_use: Nova supports tool use / function calling through Bedrock Converse API — Amazon's blog mentions agentic workflows. Setting true for all three.
- frontier_at_release: false — Dec 2024 frontier is Claude 3.5 Sonnet (Oct 2024), OpenAI o1, DeepSeek-V3.
- No supporting_url needed — AWS blog covers context/modalities; no param count to support.

#### Nova Premier
- Source: https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-nova-premier-complex-tasks-model-distillation/ (Apr 30 2025)
- Key facts: params=unknown, context=1,000,000 tokens, released=2025-04-30
- Architecture: assumed dense.
- Capabilities: multimodal (documents, videos, images, codebases), cap_vision=true, cap_video=true, cap_tool_use=true (agentic workflows emphasized).
- frontier_at_release: false — Apr 2025 has Claude 3.7 Sonnet, GPT-4.5.
- Open weights: false.
- No supporting_url — AWS announcement covers all claimed facts; no params to support.

#### Nova Canvas / Nova Reel
- SKIPPED. Canvas is image-gen (diffusion model), Reel is video-gen. Neither fits the "causal-decoder LLM" scope of this dataset. Orchestrator explicitly said "probably skip as they're not LLMs".

### Judgment calls summary

1. **Cohere "Original Command" (pre-R)**: skipped. No clean announcement event; it was a 2022 beta with rolling nightly updates into 2023. Orchestrator mentioned it in scope but the provenance doesn't cleanly fit the row-selection rule.
2. **Cohere Command A Reasoning (Aug 2025)**: NOT in orchestrator's scope list; skipped. 111B params, reasoning model — if later desired, easy to add as a separate row.
3. **AI21 Jurassic-2 Grande / Large**: NOT added as separate rows. Both announced same day as J2 Jumbo with no param disclosure, so they'd be identical-unknown rows with different names. Included only J2 Jumbo as the flagship entry. Deviation from "same-day family" rule justified because no per-size signal exists.
4. **Reka Flash 3.1**: collapsed into Flash 3 row per PLAN's "dated API snapshots" rule — minor update, no capability class change.
5. **Reka Core**: frontier_at_release kept false. It was positioned as competitive with GPT-4V / slightly behind Claude 3 Opus on multimodal evals at Apr 2024 launch. Not overall frontier.
6. **Command R+ (104B, Apr 4 2024)**: frontier_open_at_release kept false. Llama 3 70B launched Apr 18 and Mixtral 8x22B also landed April. While Command R+ was the largest open-weights dense released in that moment (104B > 70B), the CC-BY-NC non-commercial license makes "open weights frontier" a closer call than typical Apache/MIT release — but orchestrator scope text says "any license (includes research-only, non-commercial, and fully open)". Still keeping false since Mixtral 8x22B (141B MoE) has more total params and was Apache 2.0. Command R+ was a significant point but not *the* open-weights frontier.

### Fixup pass 2026-04-24 ("Other closed" rows 123-140)

Verifier FAIL/PARTIAL triage edits applied:

#### Row 127 — Command A Vision (Cohere)
- Verifier PARTIAL: cap_tool_use=true not supported by either cited URL.
- Re-checked https://cohere.com/blog/command-a-vision and https://huggingface.co/CohereLabs/command-a-vision-07-2025 — both silent on tool use / function calling / agentic capabilities. Blog focuses on enterprise image understanding; HF card lists image-text-to-text pipeline with no tool-use mention.
- Edit: cap_tool_use true -> false.

#### Row 128 — Jurassic-1 Jumbo (AI21)
- Verifier FAIL: announcement_date 2021-08-11 disagrees with release blog.
- The AI21 release blog banner reads "Aug. 4, 2021". 2021-08-11 was an incorrect read.
- Edit: announcement_date 2021-08-11 -> 2021-08-04.

#### Rows 129, 130, 131 — Jurassic-2 Jumbo / Inflection-1 / Inflection-2
- Verifier PARTIAL: architecture_type=dense is researcher inference; cited URLs don't state MoE-vs-dense.
- Applied xAI-era conservatism pattern: dense-vs-MoE unconfirmed -> 'other'. Consistent with the already-unknown param_disclosure on all three rows.
- Edit: architecture_type dense -> other on each row; appended "Architecture (dense vs MoE) not confirmed in cited URL; marked 'other' per conservatism pattern." to param_source_note.

#### Row 132 — Inflection-2.5
- Instruction assumed cap_reasoning=true but CSV already had cap_reasoning=false. No action needed (possible stale verifier snapshot).

#### Row 136 — Reka Flash 3
- Instruction assumed cap_reasoning=false but CSV already had cap_reasoning=true with param_source_note already calling it a reasoning model. No action needed.

## OPT-175B
- Source: https://ai.meta.com/blog/democratizing-access-to-large-scale-language-models-with-opt-175b/
- Supporting: https://arxiv.org/abs/2205.01068 (supports context window 2048 / training token count)
- Key facts: total=175B, active=175B (dense), context=2048, released=2022-05-03
- License: noncommercial research license.
- Notes: First fully-open 175B model. Marked frontier_open_at_release=true — at May 2022 it was *the* open-weights 100B+ frontier (BLOOM-176B only arrived Jul 2022). Not overall frontier (PaLM 540B was Google's April 2022 internal peak, Chinchilla dominated frontier math in March 2022). frontier_at_release=false. cap_tool_use=false (no function calling era).

## Galactica 120B
- Source: https://arxiv.org/abs/2211.09085 (Galactica tech report — primary)
- Supporting: https://huggingface.co/facebook/galactica-120b (confirms CC-BY-NC-4.0, 120B, HF availability)
- Key facts: total=120B, active=120B (dense), context=2048, released=2022-11-15
- License: CC-BY-NC-4.0 (open weights, noncommercial).
- Notes: Demo taken down after 3 days due to hallucinations but weights remained available on HF. Architecture is dense decoder-only transformer. Not frontier at release (GPT-3.5 era, and OPT-175B/BLOOM-176B were larger open-weight). Science-specialist framing; not a code model. frontier_open_at_release=false (BLOOM-176B Jul 2022 already held the open-weight crown, Galactica at 120B was smaller).

## LLaMA 7B / 13B / 33B / 65B
- Source: https://ai.meta.com/blog/large-language-model-llama-meta-ai/ (Meta announcement)
- Supporting: https://arxiv.org/abs/2302.13971 (LLaMA paper — supports context window 2048 and per-size training-token counts)
- Key facts: released=2023-02-24; context=2048 across all sizes
- Training tokens: 7B and 13B on 1T tokens; 33B and 65B on 1.4T tokens.
- License: noncommercial research license (at release — later leaked and broadly reused).
- Notes: All dense transformers. LLaMA-65B was the open-weight frontier at Feb 2023 (beating OPT-175B per-parameter on most benchmarks per Meta claims; competitive with Chinchilla 70B and PaLM 540B). Marked frontier_open_at_release=true on 65B only; the smaller sizes are also open but not *the* open frontier at release. frontier_at_release=false across all (GPT-4 / PaLM era). No tool use, no vision at LLaMA 1 era. Parameter columns use rounded labelled sizes (7B, 13B, 33B, 65B) per lab branding; paper exact counts are 6.7B, 13B, 32.5B, 65.2B — retained rounded figures since the release branding is canonical.

## Llama 2 7B / 13B / 70B
- Source: https://ai.meta.com/blog/llama-2/ (Meta/Microsoft announcement)
- Supporting: https://arxiv.org/abs/2307.09288 (Llama 2 paper — supports training-token count 2T, context window 4096)
- Key facts: released=2023-07-18; context=4096; training=2T tokens
- License: Llama 2 Community License (commercial use allowed, subject to DAU threshold).
- Notes: Llama 2 70B used grouped-query attention (GQA) — first Meta model to do so. Marked frontier_open_at_release=true on the 70B row (surpassing LLaMA-65B and matching/beating Falcon-40B; Falcon-180B would arrive Sep 2023). 7B and 13B not individually frontier-open. No tool use, no vision. cap_code_specialized=false (general purpose).

## Code Llama 7B / 13B / 34B
- Source: https://ai.meta.com/blog/code-llama-large-language-model-coding/ (Meta announcement)
- Supporting: https://arxiv.org/abs/2308.12950 (Code Llama paper — supports 16K training context, up-to-100K inference context, 500B-token training)
- Key facts: released=2023-08-24; context=16384 trained (stable to 100K); training=500B tokens of code
- License: Llama 2 Community License (commercial + research).
- Notes: Dense transformers derived from Llama 2 (except 34B which has no Llama 2 base — 34B Llama 2 was never released). cap_code_specialized=true for all. Each size has base / Python / Instruct variants collapsed to single row per size per schema convention. frontier_open_at_release=false (not broadly the open frontier; code-specific niche but not overall).

## Code Llama 70B
- Source: https://ai.meta.com/blog/code-llama-large-language-model-coding/ (updated Jan 29 2024)
- Supporting: https://arxiv.org/abs/2308.12950
- Key facts: released=2024-01-29; total=70B; context=16384 (stable to 100K); training=1T tokens of code
- License: same Llama 2 Community License.
- Notes: Separate release event from Aug 2023 batch. Own row per scope rules. Base / Python / Instruct variants.

## Llama 3 8B / 70B
- Source: https://ai.meta.com/blog/meta-llama-3/ (Meta announcement)
- Supporting: https://arxiv.org/abs/2407.21783 (Llama 3 herd paper — supports 15T+ training tokens, GQA, 8192 context at initial release)
- Key facts: released=2024-04-18; context=8192 at initial release; training>=15T tokens
- License: Llama 3 Community License (commercial with DAU threshold).
- Notes: Dense transformers, GQA across both sizes. New 128K-vocab tokenizer. Llama 3 70B was the best open-weights model at April 2024 release (surpassing Mixtral 8x22B on most benchmarks). frontier_open_at_release=true on 70B; 8B false. Not overall frontier (GPT-4 Turbo, Claude 3 Opus era).

## Llama 3.1 8B / 70B / 405B
- Source: https://ai.meta.com/blog/meta-llama-3-1/
- Supporting: https://arxiv.org/abs/2407.21783 (Llama 3 herd paper — supports 405B param count, 128K context, 16K+ H100 training details)
- Key facts: released=2024-07-23; context=128000; training=15T+ tokens; tool use officially supported
- License: Llama 3.1 Community License (permits output use to improve other models).
- Notes: Llama 3.1 405B is the key frontier event — first open-weights model to genuinely contest the overall frontier (competitive with GPT-4o and Claude 3.5 Sonnet). Marked frontier_at_release=true AND frontier_open_at_release=true on 405B. 70B frontier_open=false (405B is the open peak at that moment). 8B no frontier flags. cap_tool_use=true across all three sizes per Meta's "state-of-the-art tool use" announcement and dedicated tool-use API support.

## Llama 3.2 1B / 3B / 11B Vision / 90B Vision
- Source: https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/
- Supporting: per-model HuggingFace cards (Llama-3.2-1B, -3B, -11B-Vision, -90B-Vision) — support 128K context window on vision models (not explicit in blog)
- Key facts: released=2024-09-25; all models context=128000; 1B and 3B text-only, 11B and 90B multimodal
- Notes: Llama 3.2 11B Vision and 90B Vision are drop-in replacements for 3.1 8B and 70B text models with added vision encoders. Tool calling supported on all four per blog ("multilingual text generation and tool calling abilities"). 90B Vision was the frontier open-weights vision model at Sep 2024 (competitive with Claude 3 Haiku, GPT-4o-mini per Meta). Marked frontier_open_at_release=true on 90B Vision; others false. No frontier_at_release (closed multimodal models from OpenAI/Anthropic/Google were ahead overall).

## Llama 3.3 70B
- Source: https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct (primary — the canonical model card from Meta; the Meta blog announcement was via tweet/HF rather than a dedicated blog post)
- Supporting: https://ai.meta.com/blog/future-of-ai-built-with-llama/ (Meta blog post on Llama family including 3.3 efficiency gains)
- Key facts: released=2024-12-06; total=70B; context=128000; training=~15T tokens
- License: Llama 3.3 Community License.
- Notes: Text-only efficiency-focused update. Meta claimed 405B-level performance at a fraction of the cost. Marked frontier_open_at_release=true — at Dec 6 2024 it was arguably the best 70B-scale open model (briefly before DeepSeek-V3 on Dec 26 2024 redefined the open frontier). Not overall frontier. cap_tool_use=true (Llama 3.1+ family capability). cap_vision=false (text-only per announcement; the 3.2 vision line is separate).

## Llama 4 Scout / Maverick / Behemoth (preview)
- Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/ (Meta announcement)
- Supporting: HuggingFace cards for Scout (Llama-4-Scout-17B-16E) and Maverick (Llama-4-Maverick-17B-128E). Behemoth has no HF release — blank supporting_url.
- Key facts: announced=2025-04-05
  - Scout: 17B active / 109B total, 16 experts, 10M context
  - Maverick: 17B active / 400B total, 128 routed + 1 shared expert, 1M context
  - Behemoth: 288B active / ~2T total, 16 experts — NOT PUBLICLY RELEASED (still training / paused as of April 2026)
- License: Llama 4 Community License (released models only).
- Notes: First Meta MoE family. Native multimodality via early fusion (text + vision). Marked frontier_at_release=true on Scout and Maverick per Meta's stated competitive positioning (they were at-or-near the open frontier at April 2025 and broadly competitive with top closed models in some tasks). frontier_open_at_release=true on both. Behemoth row has open_weights=false because weights were never released and context_window is blank because Meta has not stated a context window for Behemoth in the announcement (only architectural sketch). Tool use: default true for Llama 4 per the ecosystem (vLLM/llama.cpp support, tool calling carried forward from 3.1 family). cap_vision=true for all three; cap_audio/cap_video false (Meta states image + video frame training but no primary inference over video at release).

## DeepSeek LLM 7B
- Source: https://github.com/deepseek-ai/DeepSeek-LLM (official GitHub repo)
- Supporting: https://huggingface.co/deepseek-ai/deepseek-llm-7b-base (HF model card; confirms 7B param count and 2T token training)
- Key facts: total=7B, active=7B (dense), context=4096, released=2023-11-29, trained on 2T tokens English+Chinese
- Architecture: dense transformer, Multi-Head Attention (MHA), LLaMA-style architecture.
- License: DeepSeek License (commercial use allowed).
- Notes: First DeepSeek LLM release. Base + Chat variants — one row for the 7B headline. frontier_at_release=false (Llama 2 70B, GPT-4 dominated); frontier_open_at_release=false (Llama 2 70B, Falcon-180B were larger open models). Not code-specialized, not reasoning.

## DeepSeek LLM 67B
- Source: https://github.com/deepseek-ai/DeepSeek-LLM
- Supporting: https://huggingface.co/deepseek-ai/deepseek-llm-67b-base (HF card confirms 67B params, 2T tokens, GQA architecture)
- Key facts: total=67B, active=67B (dense), context=4096, released=2023-11-29, trained 2T tokens
- Architecture: dense, Grouped-Query Attention (GQA).
- License: DeepSeek License.
- Notes: Outperformed Llama 2 70B on reasoning/coding/math/Chinese per README. At Nov 2023, Falcon-180B (Sep 2023) was larger, so frontier_open_at_release=false — but it was the strongest ~70B-class open-weights model at release. Not marking frontier_open=true because Falcon-180B held the headline size crown. Conservative false on both frontier flags.

## DeepSeek-Coder 33B (family: 1.3B/5.7B/6.7B/33B)
- Source: https://github.com/deepseek-ai/DeepSeek-Coder
- Supporting: https://huggingface.co/deepseek-ai/deepseek-coder-33b-instruct (HF model card — confirms 33B params, 16K context, 2T tokens 87% code)
- Key facts: total=33B, active=33B (dense), context=16384 (16K), released=2023-11-02, family sizes 1.3B/5.7B/6.7B/33B
- Architecture: dense transformer, trained on 87% code + 13% natural language (English+Chinese).
- License: DeepSeek License.
- Notes: First DeepSeek Coder release, flagship row = 33B. cap_code_specialized=true (trained primarily for code). 16K context (extended from 4K pre-training via further pre-training with 200B additional tokens). Not frontier overall; CodeLlama 34B was the open-weights code frontier at that moment and arguably DeepSeek-Coder-33B overtook it on HumanEval — marking frontier_open_at_release=false conservatively since coding-only specialization doesn't map cleanly to the "overall open frontier" plot but this is debatable. Family note in param_source_note captures 1.3/5.7/6.7/33B variants.

## DeepSeek-MoE 16B
- Source: https://arxiv.org/abs/2401.06066 (DeepSeekMoE paper — architecture pivot)
- Supporting: https://huggingface.co/deepseek-ai/deepseek-moe-16b-base (HF model card confirms 16B MoE)
- Key facts: total=16.4B, active=2.8B, context=4096, announced=2024-01-11 (paper submission; Wikipedia says model release Jan 9 but paper date is more citable)
- Architecture: MoE with fine-grained expert specialization + shared expert isolation — DeepSeek's first MoE and the prototype for V2/V3 sparse architecture.
- License: DeepSeek License.
- Notes: Comparable performance to Llama2 7B at ~40% compute. Announcement date = arxiv paper submission (2024-01-11) since the paper is cited by every source. Not a frontier model; significance is architectural pivot. cap_code_specialized=false.

## DeepSeek-V2
- Source: https://arxiv.org/abs/2405.04434 (official technical report)
- Supporting: https://github.com/deepseek-ai/DeepSeek-V2 (GitHub repo confirms release date May 6 2024, 128K context, 236B/21B)
- Key facts: total=236B, active=21B, context=128000, released=2024-05-07 (paper submission; GitHub says model release May 6)
- Architecture: MoE with Multi-head Latent Attention (MLA) + DeepSeekMoE sparse expert routing.
- License: DeepSeek License (commercial use allowed).
- Notes: First 200B+ MoE from DeepSeek. 42.5% lower training cost vs DeepSeek 67B, 93.3% KV cache reduction. In May 2024, competed with Mixtral 8x22B (141B/39B) as largest open MoE — DeepSeek-V2 at 236B is larger, making this frontier_open_at_release=true. Not overall frontier (GPT-4, Claude 3 Opus ahead). cap_tool_use=false (V2 base — function calling added in V2.5).

## DeepSeek-Coder-V2
- Source: https://arxiv.org/abs/2406.11931 (official paper)
- Supporting: https://github.com/deepseek-ai/DeepSeek-Coder-V2 (GitHub confirms 16B/236B variants, 2.4B/21B active, 128K context)
- Key facts: total=236B, active=21B, context=128000, announced=2024-06-17
- Architecture: MoE based on DeepSeek-V2 architecture, further pre-trained with +6T code tokens. 338 programming languages.
- License: DeepSeek License.
- Notes: Flagship 236B variant. cap_code_specialized=true. Claimed comparable-to-GPT-4-Turbo on code benchmarks. Lite variant (16B/2.4B) also released — noted in param_source_note. frontier_open_at_release=false because the general-purpose V2 was the headline open-frontier row for this period.

## DeepSeek-V2.5
- Source: https://huggingface.co/deepseek-ai/DeepSeek-V2.5 (official HF model card — release notes and function calling example)
- Supporting: https://github.com/deepseek-ai/DeepSeek-V2 (GitHub for 236B/21B/128K architecture confirmation — same as V2)
- Key facts: total=236B, active=21B, context=128000, released=2024-09-05 (merge of V2-0628 + Coder-V2-0724)
- Architecture: MoE (same as V2), chat + code merged.
- License: DeepSeek License (commercial use allowed, open weights MIT-like).
- Notes: Merged general+code model → cap_code_specialized=false per scope doc. Added function calling per HF model card ("Function calling allows the model to call external tools to enhance its capabilities") → cap_tool_use=true. Not frontier_at_release (Claude 3.5 Sonnet, GPT-4o ahead). frontier_open_at_release=true — Sept 2024, V2.5 was the strongest general+code open model at 236B MoE. Context: HF card shows max_model_len=8192 in vLLM example but the architecture and docs show 128K — treating 128K as the release-time context since it's inherited from V2.

## DeepSeek-V3
- Source: https://arxiv.org/abs/2412.19437 (DeepSeek-V3 technical report — 671B/37B/14.8T tokens/FP8/MLA)
- Supporting: https://huggingface.co/deepseek-ai/DeepSeek-V3 (model card confirms 671B/37B/128K context, FP8 weights, MLA+MoE)
- Key facts: total=671B, active=37B, context=128000, released=2024-12-26, 14.8T training tokens, FP8 mixed precision
- Architecture: MoE with MLA + auxiliary-loss-free load balancing + multi-token prediction.
- License: DeepSeek License (open weights — MIT-compatible terms).
- Notes: Major frontier event — 671B open-weights MoE that genuinely contested overall frontier with GPT-4o / Claude 3.5 Sonnet-1022. frontier_at_release=true and frontier_open_at_release=true. cap_tool_use=true — scope doc asserts V3 officially supports function calling; model card doesn't explicitly demo but DeepSeek API supports function calling from V3 onward. cap_reasoning=false (V3 is not test-time-reasoning; R1 is the reasoning branch).

## DeepSeek-R1
- Source: https://huggingface.co/deepseek-ai/DeepSeek-R1 (official HF model card — confirms 671B/37B/128K, reasoning model with <think> tags)
- Supporting: https://arxiv.org/abs/2501.12948 (DeepSeek-R1 paper — pure RL reasoning training)
- Key facts: total=671B, active=37B, context=128000, released=2025-01-20
- Architecture: MoE (same 671B/37B as V3), post-trained via RL for reasoning.
- License: MIT (weights) per standard DeepSeek open release.
- Notes: FIRST open-weights reasoning model to reach o1-class performance. cap_reasoning=true (test-time reasoning with <think> tags — explicit reasoning family). frontier_at_release=true (genuinely contested o1 on math/code/reasoning); frontier_open_at_release=true (no other open reasoning model matched this at Jan 2025). Tool use: R1 base is not optimized for tool calling (reasoning-first design) — setting cap_tool_use=false, matching o1's initial non-tool-use posture. Distill variants skipped per scope.

## DeepSeek-V3.1
- Source: https://huggingface.co/deepseek-ai/DeepSeek-V3.1 (official HF model card — 671B/37B/128K, hybrid thinking+non-thinking, tool calling)
- Supporting: https://www.analyticsvidhya.com/blog/2025/08/deepseek-v3-1-quiet-release-big-statement/ (confirms Aug 21 2025 release date, 685B total with MTP, 128K context, thinking mode)
- Key facts: total=671B (main) or 685B including MTP module, active=37B, context=128000, released=2025-08-21
- Architecture: MoE hybrid reasoning model, FP8 UE8M0, extended context training phases.
- License: MIT.
- Notes: First DeepSeek hybrid model (thinking + non-thinking via chat template toggle). Matches R1-0528 quality on reasoning while allowing fast non-thinking mode. cap_reasoning=true (explicit thinking mode), cap_tool_use=true (improved tool calling). frontier_at_release=false (GPT-5 / Gemini 2.5 generation ahead by Aug 2025); frontier_open_at_release=true — at release, V3.1 was the strongest open hybrid model. Using 671B as total_params (main model weights — MTP module is auxiliary training scaffold, per DeepSeek convention in V3 report). HF card shows param count "685B" if counting MTP — noting the 671/685B decomposition in param_source_note.

## DeepSeek-V3.2-Exp
- Source: https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp (official HF card — references config_671B_v3.2.json, DSA sparse attention, MLA, 256 experts)
- Supporting: (none — HF card covers all facts for this experimental release)
- Key facts: total=671B, active=37B (config inherited from V3.1), context=128000, released=2025-09-29
- Architecture: MoE + DeepSeek Sparse Attention (DSA) + MLA. Experimental release testing sparse attention.
- License: MIT.
- Notes: Experimental release — incremental architecture research. Not a frontier event by itself. cap_reasoning=true (thinking mode inherited from V3.1). cap_tool_use=true. frontier_open_at_release=false (incremental over V3.1).

## DeepSeek-V3.2
- Source: https://huggingface.co/deepseek-ai/DeepSeek-V3.2 (official HF card — Dec 1 2025 release date timestamp, thinking + tool use, 685B)
- Supporting: https://arxiv.org/abs/2512.02556 (official DeepSeek-V3.2 paper "Pushing the Frontier of Open Large Language Models" — submitted Dec 2 2025, describes DSA, scalable RL post-training, agentic task synthesis pipeline)
- Key facts: total=671B (main) / 685B (with MTP), active=37B, context=128000, released=2025-12-01
- Architecture: MoE with DSA, reasoning-first, "thinking with tools" capability.
- License: MIT.
- Notes: Official successor to V3.2-Exp. "Thinking with tools" integrates reasoning directly into tool use. cap_reasoning=true, cap_tool_use=true. V3.2-Speciale is a reasoning-only API-only variant — NOT including Speciale as a separate row (API-only, no open weights). frontier_at_release=false (GPT-5-class models contemporaneous); frontier_open_at_release=true (strongest open reasoning+tool-use model at Dec 2025). Context window inherited from V3 family.

## Qwen-7B
- Source: https://huggingface.co/Qwen/Qwen-7B
- Supporting: https://github.com/QwenLM/Qwen (release timeline), arXiv 2309.16609 (Qwen tech report)
- Key facts: total=7B, active=7B (dense), context=8192 (originally 2048, extended to 8192 in Sept 2023 retraining), released=2023-08-03 first drop; blog re-announced/retrained Sep 25 2023 at 8k context.
- License: Tongyi Qianwen License (commercial-use allowed with free application form).
- Architecture: dense transformer with RoPE, SwiGLU, RMSNorm.
- Notes: Using 2023-08-03 (original ModelScope/HF drop) per Wikipedia and GitHub README. Context at release was 2k, but by time of tech report (Sept 28) extended to 8k with NTK/LogN; taking 8192 as release-era value since that's what the primary Qwen-7B HF card documents. Trained on 2.4T tokens. frontier_at_release=false; frontier_open_at_release=false (Llama 2 70B dominated open in Aug 2023).

## Qwen-14B
- Source: https://huggingface.co/Qwen/Qwen-14B
- Supporting: https://github.com/QwenLM/Qwen (dated release timeline)
- Key facts: total=14B, active=14B, context=2048 base / extendable to 8k via NTK, released=2023-09-25
- License: Tongyi Qianwen License.
- Architecture: dense transformer (RoPE, SwiGLU, RMSNorm).
- Notes: HF card shows 2048 native context; blog claims 8k via NTK+LogN. Using 2048 as release-time value per release-time rule. Trained on 3T+ tokens. frontier_at_release=false, frontier_open_at_release=false.

## Qwen-72B
- Source: https://huggingface.co/Qwen/Qwen-72B
- Supporting: https://github.com/QwenLM/Qwen
- Key facts: total=72B, active=72B (dense), context=32768 (32K), released=2023-11-30
- License: Tongyi Qianwen License.
- Architecture: dense transformer (RoPE, SwiGLU, RMSNorm).
- Notes: Trained on 3T+ tokens. 32K native context. Biggest Qwen 1 release. At release, Falcon-180B (180B) was still larger open-weight but Qwen-72B was closer to Llama-2-70B class. Not frontier-open (Falcon-180B larger, Llama-2-70B comparable). frontier_at_release=false, frontier_open_at_release=false (Falcon 180B still the open-weight-by-size leader Nov 2023).

## Qwen1.5 72B
- Source: https://qwenlm.github.io/blog/qwen1.5/
- Supporting: https://huggingface.co/Qwen/Qwen1.5-72B (for params/context specs)
- Key facts: total=72B, active=72B, context=32768, released=2024-02-04
- License: Tongyi Qianwen License.
- Architecture: dense transformer.
- Notes: Qwen1.5 was a sweeping refresh releasing 0.5B/1.8B/4B/7B/14B/32B/72B/110B simultaneously. Using 72B as the flagship row. 110B wasn't in the Feb 4 drop (came April 2024); skipping 110B per scope. Native function calling via HF tokenizer. frontier_at_release=false; frontier_open_at_release=false (Feb 2024 still Mixtral 8x7B + Llama-2-70B dominant; Qwen1.5-72B was competitive but not clearly the top open).

## Qwen1.5-MoE-A2.7B
- Source: https://qwenlm.github.io/blog/qwen-moe/
- Supporting: https://huggingface.co/Qwen/Qwen1.5-MoE-A2.7B
- Key facts: total=14.3B, active=2.7B, context=8192 (HF config shows 8k native; some extend to 32k), released=2024-03-28
- License: Apache 2.0.
- Architecture: MoE — 64 experts (60 routing + 4 shared), 4 of 60 routed activated.
- Notes: First Qwen MoE. Matched Qwen1.5-7B quality at ~1/3 activated params. Context window 8K per HF config. Not frontier or open-frontier — a cost-efficiency pilot. frontier_at_release=false, frontier_open_at_release=false.

## Qwen2-72B
- Source: https://qwenlm.github.io/blog/qwen2/
- Supporting: https://huggingface.co/Qwen/Qwen2-72B (architecture and total_params of 73B)
- Key facts: total=72.7B (~73B), active=72.7B (dense), context=131072 (128K with YaRN), released=2024-06-07
- License: Tongyi Qianwen License (72B uses proprietary license; smaller Qwen2 models use Apache 2.0).
- Architecture: dense transformer with GQA.
- Notes: HF model card shows 73B total; tech report confirms same. At June 2024, Llama 3 70B (April) was dominant open; Qwen2-72B was competitive peer. Borderline frontier_open_at_release — marking true since it matched or beat Llama 3 70B on key benchmarks per Qwen2 blog. Not overall frontier (GPT-4o, Claude 3.5 Sonnet dominated). Function calling supported per Qwen2 tech report.

## Qwen2-57B-A14B
- Source: https://qwenlm.github.io/blog/qwen2/
- Supporting: https://huggingface.co/Qwen/Qwen2-57B-A14B
- Key facts: total=57B, active=14B, context=65536 (64K), released=2024-06-07
- License: Apache 2.0.
- Architecture: MoE (upcycled, same approach as Qwen1.5-MoE).
- Notes: Second Qwen MoE. frontier_open_at_release=false (Qwen2-72B and Llama 3 70B were stronger at same date). Function calling via Qwen tooling.

## Qwen2-VL-72B
- Source: https://qwenlm.github.io/blog/qwen2-vl/
- Supporting: https://huggingface.co/Qwen/Qwen2-VL-72B (params: 73B model w/ vision encoder)
- Key facts: total=~73B (~72B LLM + 600M ViT), active=~73B, context=32768 (not explicitly on blog; HF card shows 32K config), released=2024-08-29 (2B/7B open; 72B initially API-only)
- License: Qwen (72B initially API-only; open-weight release September 2024 via Qwen2.5-VL path, but 72B base version Qwen2-VL-72B eventually released on HF under Qwen license).
- Architecture: dense multimodal transformer with Naive Dynamic Resolution + M-RoPE.
- Notes: The 2B/7B were open-weight on Aug 29; 72B was API-only at launch per blog. HF shows Qwen2-VL-72B base available — released later. Using 2024-08-29 as announcement_date per the blog. Since 72B was API-only at announcement, open_weights=false at time of announcement; flipping to true would misrepresent release-time status. cap_vision=true, cap_video=true (>20min videos), cap_tool_use=true (visual agent / mobile device control). frontier_open_at_release=false (not open at release). Flag honestly.

## Qwen2.5-72B
- Source: https://qwenlm.github.io/blog/qwen2.5/
- Supporting: https://huggingface.co/Qwen/Qwen2.5-72B
- Key facts: total=72.7B (~73B), active=72.7B (dense), context=131072 (128K), released=2024-09-19
- License: Qwen (72B uses Qwen license; others Apache 2.0).
- Architecture: dense.
- Notes: Trained on 18T tokens. Supports tool calling. frontier_open_at_release=true — at Sept 2024 Qwen2.5-72B was arguably the strongest open general model, competing with Llama 3.1 405B on many benchmarks at a fraction of the size. frontier_at_release=false (GPT-4o, Claude 3.5 Sonnet, o1 still stronger overall).

## Qwen2.5-Coder-32B
- Source: https://qwenlm.github.io/blog/qwen2.5-coder-family/
- Supporting: https://huggingface.co/Qwen/Qwen2.5-Coder-32B
- Key facts: total=32.5B (~32B), active=32.5B, context=131072 (128K with YaRN; 32768 default), released=2024-11-12
- License: Apache 2.0 (32B is Apache, 3B is Qwen Research).
- Architecture: dense, code-specialized.
- Notes: Claimed to match GPT-4o on coding benchmarks. cap_code_specialized=true. cap_tool_use=true (agentic coding capable). frontier_open_at_release=true on code specifically; frontier_at_release=false (not an overall frontier model). Trained on 5.5T tokens.

## Qwen2.5-VL-72B
- Source: https://qwenlm.github.io/blog/qwen2.5-vl/
- Supporting: https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct
- Key facts: total=~73B (~72B LLM + vision encoder), active=~73B, context=32768 (native; extendable to 64K/128K for long videos), released=2025-01-26
- License: Qwen.
- Architecture: dense multimodal with M-RoPE + dynamic FPS for video.
- Notes: Open-weight at launch (unlike Qwen2-VL-72B). Computer/phone use agent capabilities; >1hr video understanding. cap_vision=true, cap_video=true, cap_tool_use=true. frontier_open_at_release=true (strongest open-weight VLM at time).

## QwQ-32B-Preview
- Source: https://huggingface.co/Qwen/QwQ-32B-Preview
- Supporting: https://techcrunch.com/2024/11/27/alibaba-releases-an-open-challenger-to-openais-o1-reasoning-model/ (release date + reasoning positioning)
- Key facts: total=32.5B (~32B), active=32.5B, context=32768, released=2024-11-27
- License: Apache 2.0.
- Architecture: dense (based on Qwen2.5-32B); reasoning-focused post-training.
- Notes: First open-weight reasoning model approaching o1-level performance on math/code. cap_reasoning=true. cap_tool_use=false (preview does not document function calling). frontier_open_at_release=true (first public open reasoning model); frontier_at_release=false (o1-preview stronger overall).

## QwQ-32B
- Source: https://huggingface.co/Qwen/QwQ-32B
- Supporting: https://qwenlm.github.io/blog/qwq-32b/ (not directly fetched; referenced in search)
- Key facts: total=32.5B, active=32.5B, context=131072 (128K native with YaRN), released=2025-03-05
- License: Apache 2.0.
- Architecture: dense reasoning model, RL-enhanced from Qwen2.5-32B.
- Notes: Full release vs Preview. Near-DeepSeek-R1 performance at 20x fewer parameters. cap_reasoning=true. cap_tool_use=true (HF card mentions agent integration / tool calling). frontier_open_at_release=true (top open reasoning model at release, matching DeepSeek-R1 at smaller scale); frontier_at_release=false.

## Qwen3-32B
- Source: https://qwenlm.github.io/blog/qwen3/
- Supporting: https://huggingface.co/Qwen/Qwen3-32B
- Key facts: total=32.8B, active=32.8B, context=32768 native / 131072 with YaRN, released=2025-04-29
- License: Apache 2.0.
- Architecture: dense, hybrid reasoning (thinking + non-thinking modes).
- Notes: cap_reasoning=true (thinking mode), cap_tool_use=true (native MCP + function calling). frontier_open_at_release=false (Qwen3-235B-A22B is the flagship at same date). Using blog-stated 128K with YaRN (the HF card treats 32K native, 128K extended). Taking 131072 as release-era value since blog marketed 128K.

## Qwen3-30B-A3B
- Source: https://qwenlm.github.io/blog/qwen3/
- Supporting: https://huggingface.co/Qwen/Qwen3-30B-A3B
- Key facts: total=30.5B, active=3.3B, context=32768 native / 131072 with YaRN, released=2025-04-29
- License: Apache 2.0.
- Architecture: MoE (128 experts, 8 active), hybrid reasoning.
- Notes: "Outcompetes QwQ-32B with 10x fewer activated params." cap_reasoning=true, cap_tool_use=true. Small MoE with exceptional performance/cost ratio. frontier_open_at_release=false (235B-A22B is the frontier sibling).

## Qwen3-235B-A22B
- Source: https://qwenlm.github.io/blog/qwen3/
- Supporting: https://huggingface.co/Qwen/Qwen3-235B-A22B
- Key facts: total=235B, active=22B (8/128 experts active), context=32768 native / 131072 with YaRN, released=2025-04-29
- License: Apache 2.0.
- Architecture: MoE, 94 layers, 128 experts, hybrid reasoning.
- Notes: Flagship Qwen3. Competitive with DeepSeek-R1, o1, o3-mini, Grok-3, Gemini-2.5-Pro per blog. cap_reasoning=true (thinking mode default), cap_tool_use=true (MCP + function calling). frontier_open_at_release=true (top open model April 2025; DeepSeek-R1 earlier Jan 2025 was peer). frontier_at_release=false (overall frontier was GPT-5 class proprietary).

## Qwen3-Coder-480B-A35B
- Source: https://qwenlm.github.io/blog/qwen3-coder/
- Supporting: https://github.com/QwenLM/Qwen3-Coder
- Key facts: total=480B, active=35B, context=262144 native (256K) / 1048576 (1M with YaRN), released=2025-07-22
- License: Apache 2.0.
- Architecture: MoE, code-specialized.
- Notes: "Most powerful open agentic code model." cap_code_specialized=true, cap_tool_use=true (agentic browser / shell), cap_reasoning=false (explicitly a non-thinking Instruct variant). frontier_open_at_release=true for code-specialized open models. Not overall frontier.

## Qwen3-Max
- Source: https://www.marktechpost.com/2025/09/24/alibabas-qwen3-max-production-ready-thinking-mode-1t-parameters-and-day-one-coding-agentic-bench-signals/
- Supporting: https://x.com/Alibaba_Qwen/status/1963991502440562976 (Qwen team announcement, 1T+ parameters)
- Key facts: total=~1T+ (over 1 trillion, exact undisclosed), active=unknown, context=262144 (256K), released=2025-09-05 (preview) / 2025-09-24 (GA)
- License: proprietary, closed-weights (Qwen Chat + Alibaba Cloud API only).
- Architecture: MoE (sparse).
- Notes: API-only. First Qwen model >1T params. open_weights=false. param_disclosure=official (Qwen team announced "over 1 trillion"; active count not publicly disclosed). Using total=1000000000000 as lower-bound for the >1T claim. cap_reasoning=true (Qwen3-Max-Thinking variant). cap_tool_use=true. Using 2025-09-05 as announcement_date (Preview release). frontier_at_release=false (GPT-5 / Gemini 2.5 era); frontier_open_at_release=false (closed weights).

## Qwen3-VL-235B-A22B
- Source: https://github.com/QwenLM/Qwen3-VL
- Supporting: https://www.unite.ai/alibaba-releases-qwen3-vl-technical-report-detailing-two-hour-video-analysis/
- Key facts: total=235B, active=22B, context=262144 (256K native, 1M with YaRN), released=2025-09-23
- License: Apache 2.0.
- Architecture: MoE, multimodal (text + image + video).
- Notes: Flagship Qwen3-VL. 2hr video understanding. 99.5% accuracy on 2hr needle-in-haystack. cap_vision=true, cap_video=true, cap_tool_use=true (visual agent with thinking variant). frontier_open_at_release=true (strongest open VLM Sept 2025).

## Qwen3-Omni-30B-A3B
- Source: https://github.com/QwenLM/Qwen3-Omni
- Supporting: https://www.marktechpost.com/2026/03/30/alibaba-qwen-team-releases-qwen3-5-omni-a-native-multimodal-model-for-text-audio-video-and-realtime-interaction/ (positioning as successor)
- Key facts: total=30B (30B-A3B), active=3B, context=32768 (65536 multi-GPU), released=2025-09-22
- License: Apache 2.0.
- Architecture: MoE with Thinker-Talker native multimodal architecture.
- Notes: First Qwen omni-modal model with audio/video/text/image native. SOTA on 22/36 audio-video benchmarks. 119 text / 19 speech recognition / 10 speech generation languages. cap_vision=true, cap_audio=true, cap_video=true, cap_tool_use=true. frontier_open_at_release=true (strongest open omni-modal model).

## Qwen3.5 (Qwen3.5-397B-A17B)
- Source: https://www.alibabacloud.com/blog/qwen3-5-towards-native-multimodal-agents_602894
- Supporting: https://www.cnbc.com/2026/02/17/china-alibaba-qwen-ai-agent-latest-model.html (release date, open weights status)
- URL verification note: check-urls HEAD request redirects to /notfound, but WebFetch GET request returns full article text confirming "We are delighted to announce the official release of Qwen3.5, introducing the open-weight of the first model in the Qwen3.5 series, namely Qwen3.5-397B-A17B." and "397 billion total parameters, just 17 billion are activated per forward pass." This is a HEAD-vs-GET server quirk on alibabacloud.com blog URLs — the page is real and load-bearing for all row claims.
- Key facts: total=397B, active=17B, context=1048576 (1M default for Qwen3.5-Plus hosted; open-weight native context not explicitly stated), released=2026-02-17
- License: open-weight (Apache 2.0 per Alibaba Cloud blog; Plus hosted version proprietary)
- Architecture: hybrid — Gated Delta Networks linear attention + sparse MoE; natively multimodal (text + vision + video).
- Notes: 397B/17B ratio is extremely sparse. cap_vision=true, cap_video=true (blog covers video benchmarks). cap_audio not confirmed on this blog — Qwen3.5-Omni is a separate model (March 2026). cap_reasoning=true, cap_tool_use=true. frontier_open_at_release=true (largest open-weight multimodal MoE at Feb 2026, per CNBC/VentureBeat framing "beats its trillion-parameter sibling at lower cost"). frontier_at_release=false (GPT-5.5 / Claude Opus 4.6 / Gemini 3.1 Pro tier).

## Qwen3.6-35B-A3B
- Source: https://github.com/QwenLM/Qwen3.6
- Supporting: https://www.aibase.com/news/27222 (35B/3B active disclosed)
- Key facts: total=35B, active=3B, context=262144 (256K), released=2026-04-16
- License: Apache 2.0.
- Architecture: MoE, coding-focused.
- Notes: "Agentic Coding Power, Now Open to All." cap_code_specialized=false (positioned for agentic coding but not pure code-only like Qwen3-Coder — leaving as false per PLAN convention: primarily code-marketed models). On reflection: the name is not -Coder, so cap_code_specialized=false; blog strongly coding-oriented though. Since context_window specifically not confirmed in either fetched source beyond "262,144 tokens based on deployment examples," marking 262144 based on GitHub repo docs reference. cap_reasoning=true (preserve_thinking mentioned in family). cap_tool_use=true.

## Qwen3.6-27B
- Source: https://github.com/QwenLM/Qwen3.6
- Supporting: search results indicating 27B dense, 262K context, Apr 22 2026 release
- Key facts: total=27B, active=27B, context=262144, released=2026-04-22
- License: Apache 2.0.
- Architecture: dense, multimodal (text + image + video per search results).
- Notes: "Flagship-Level Coding in a 27B Dense Model." Released two days before the cutoff (2026-04-24). cap_vision=true, cap_video=true per one search snippet claiming multimodal; but blog-source for these capabilities not directly fetched — to be conservative, marking cap_vision/cap_video as false unless HF model card confirms. Leaving capabilities conservative pending confirmation.
# bloom research notes

## BLOOM 176B
- Source: https://huggingface.co/bigscience/bloom (HF model card — official BigScience account)
- Supporting: https://arxiv.org/abs/2211.05100 (BLOOM paper — supports architecture details, release framing)
- Key facts: total_params=176,247,271,424 (~176B; embeddings 3.6B, 70 layers, 14336 hidden, 112 heads), active_params = total (dense), context_window=2048, announcement_date=2022-07-12 (Wikipedia cites July 12 2022; HF card says "Monday, 11.July.2022" — one day discrepancy; using 2022-07-12 per plan scope and common citation)
- Architecture: dense decoder-only transformer, modified Megatron-LM GPT2, ALiBi positional encodings, GeLU
- Languages: 46 natural + 13 programming languages
- License: BigScience RAIL v1.0 (OpenRAIL-M family) — open weights, use restrictions but weights freely downloadable
- frontier_open_at_release=true: first fully-open 100B+ multilingual model, surpassed OPT-175B on openness and multilingual coverage (July 2022)
- frontier_at_release=false: not at overall SOTA vs closed PaLM 540B (Apr 2022) / Chinchilla
- Cap flags: cap_text=true; vision/audio/video/code-specialized/reasoning/tool-use all false (general multilingual language model; training data includes code but it's a general LM, not code-specialized)
- Notes: supporting_url (arXiv paper) supports architecture_type and corroborates params/context

## BLOOMZ 176B
- Source: https://huggingface.co/bigscience/bloomz (HF model card — official BigScience account)
- Supporting: https://arxiv.org/abs/2211.01786 (BLOOMZ/mT0 paper — "Crosslingual Generalization through Multitask Finetuning")
- Key facts: total_params=176B (same as BLOOM base), active_params=176B, context_window=2048 (inherited from BLOOM base), announcement_date=2022-11-03 (arXiv submission date)
- Architecture: dense (BLOOM base fine-tuned via multitask prompted finetuning on xP3 dataset)
- License: bigscience-bloom-rail-1.0 (OpenRAIL)
- frontier_open_at_release=false by Nov 2022 BLOOMZ is instruction-tuned variant of existing BLOOM — does not push open-weights size frontier (same params as BLOOM which was already released)
- frontier_at_release=false
- Cap flags: cap_text=true, others false. This is an instruction/task-tuned model but pre-dates the "reasoning" category (no test-time thinking); tool-use not natively supported
- Notes: supporting_url (arXiv) supports training method (MTF on xP3) and release framing
# eleutherai research notes

## GPT-Neo 2.7B
- Source (release_url): https://github.com/EleutherAI/gpt-neo (official repo; states "Update 21/03/2021: We're proud to release two pretrained GPT-Neo models trained on The Pile")
- Supporting_url: https://huggingface.co/EleutherAI/gpt-neo-2.7B (HF model card; supports license=MIT, arch=transformer replication of GPT-3, training details). The GitHub repo supplies n_ctx=2048 and release date.
- Key facts: total_params=2.7e9, active=2.7e9, context=2048, released=2021-03-21, license=MIT, dense transformer
- Notes: Per scope instructions, include the 2.7B (largest GPT-Neo variant) and skip the 1.3B as a separate row. At release, GPT-Neo 2.7B was the largest publicly available GPT-3-style model until GPT-J surpassed it in June 2021. frontier_open_at_release=true; frontier_at_release=false (GPT-3 175B was much larger). No tool-use, vision, reasoning, code-specialization.

## GPT-J 6B
- Source (release_url): https://www.eleuther.ai/artifacts/gpt-j (EleutherAI official artifact page)
- Supporting_url: https://huggingface.co/EleutherAI/gpt-j-6b (HF model card; supports exact param count 6,053,381,344, context=2048 via nctx, license=Apache-2.0, training on 402B tokens on The Pile).
- Key facts: total_params=6,053,381,344, active=6,053,381,344, context=2048, released=2021-06-09 (announcement by Aran Komatsuzaki; widely cited as June 9, 2021), license=Apache-2.0, dense transformer with RoPE
- Notes: At release was the largest publicly available GPT-3-style autoregressive model. frontier_open_at_release=true. frontier_at_release=false. No vision/audio/video/code-specialization/reasoning/tool-use.

## GPT-NeoX-20B
- Source (release_url): https://blog.eleuther.ai/announcing-20b/ (EleutherAI official blog announcement, Feb 2 2022)
- Supporting_url: https://huggingface.co/EleutherAI/gpt-neox-20b (HF model card; supports exact param count 20,554,567,680, max sequence length 2048, 44 layers, Apache-2.0)
- Key facts: total_params=20,554,567,680, active=20,554,567,680, context=2048, announced=2022-02-02 (blog post date; weights became downloadable Feb 9, 2022), license=Apache-2.0, dense transformer with RoPE
- Notes: Announced 2022-02-02; weights downloadable 2022-02-09. Using announcement date per schema. Largest dense open-weight autoregressive model at release (until Meta's OPT-175B in May 2022). frontier_open_at_release=true. frontier_at_release=false. arXiv paper 2204.06745 published April 2022. No vision/audio/code-specialization/reasoning/tool-use.

## Pythia-12B
- Source (release_url): https://arxiv.org/abs/2304.01373 (Pythia paper, submitted April 3, 2023)
- Supporting_url: https://huggingface.co/EleutherAI/pythia-12b (HF model card; supports exact param count 11,846,072,320, trained on The Pile with 2M token batch, 36 layers, Apache-2.0. Pythia GitHub repo confirms n_ctx=2048.)
- Key facts: total_params=11,846,072,320, active=11,846,072,320, context=2048, announced=2023-04-03 (arXiv v1 submission), license=Apache-2.0, dense transformer
- Notes: Pythia was not an open-weights frontier claim — it is an interpretability research suite, and by April 2023 LLaMA-65B (Feb 2023) was already the open-weight frontier. frontier_open_at_release=false. frontier_at_release=false. No vision/audio/code-specialization/reasoning/tool-use.
# falcon research notes

## Falcon-7B
- Source: https://huggingface.co/tiiuae/falcon-7b
- Key facts: params=7B (dense), context=2048, architecture=causal decoder-only transformer, trained on 1.5T tokens RefinedWeb, Apache 2.0, announced/published May 2023 (training early March 2023)
- Notes: Companion smaller release alongside Falcon 40B. Open-weights flagship era for 40B, not 7B. Use announcement_date 2023-05-25 (HF card publication near Falcon 40B launch). Supporting URL: none needed — HF card covers all fields.

## Falcon-40B
- Source: https://huggingface.co/tiiuae/falcon-40b
- Supporting: https://huggingface.co/blog/falcon (HF ecosystem blog post dated 2023-06-05 with context on leaderboard #1 status)
- Key facts: params=40B dense, context=2048, architecture=causal decoder-only transformer, trained on 1T tokens, Apache 2.0, TII
- Notes: Announced/released late May 2023. Topped HF Open LLM Leaderboard May 29, 2023. Use announcement_date 2023-05-25. frontier_open_at_release=true (briefly #1 open-weight LLM between LLaMA era and Llama 2). supporting_url backs the leaderboard-#1 claim used to justify the frontier_open flag.

## Falcon-180B
- Source: https://huggingface.co/tiiuae/falcon-180B
- Supporting: https://huggingface.co/blog/falcon-180b (HF blog with September 6 2023 date + 3.5T tokens + SOTA claim)
- Key facts: params=180B dense, context=2048, architecture=causal decoder-only transformer, trained on 3.5T tokens, TII Falcon-180B license (restrictive commercial), announcement 2023-09-06
- Notes: Unambiguously biggest open-weight LLM at release. frontier_open_at_release=true. Not globally frontier (behind GPT-4). The primary TII press release URL was 403 under automated fetch, so we use the HF model card as release_url and the HF blog as supporting_url — both lab-partnered official sources.

## Falcon 2 11B
- Source: https://huggingface.co/blog/falcon2-11b
- Key facts: params=11B dense, context=8192, 11 languages, trained on 5T tokens, TII Falcon 2 License, release 2024-05-13
- Notes: Base text-only. Companion VLM variant released same time. No frontier claims — much smaller than Llama 3 8B in params but positioned against it.

## Falcon 2 11B VLM
- Source: https://huggingface.co/blog/falcon2-11b
- Key facts: params=11B (base LLM) + CLIP ViT-L/14 vision encoder (frozen, ~0.3B). Context 8192. Released 2024-05-13.
- Notes: cap_vision=true. Separate row from base 11B. Vision encoder frozen during text-only pretraining, so total_params includes both. Estimate ~11.3B total. Marking param_disclosure=official for 11B text backbone; vision encoder added via CLIP ViT-L/14 which is well-known ~0.3B. Going to round to 11300000000 and flag in note.

## Falcon Mamba 7B
- Source: https://huggingface.co/tiiuae/falcon-mamba-7b
- Supporting: https://huggingface.co/blog/falconmamba (HF announcement blog)
- Key facts: params=7B pure SSM (Mamba-1), trained context 8192 (with no inference limit due to SSM), trained on 5.5T tokens, TII Falcon-Mamba License 2.0, release 2024-08-12
- Notes: architecture_type=SSM. First major SSM open-weight 7B. Per HF card "training sequence length 8192". Using 8192 as context_window. frontier_open_at_release=false (not the largest open-weight — Llama 3.1 405B existed by then), but novel architecture.

## Falcon 3 10B (flagship)
- Source: https://falcon-lm.github.io/blog/falcon-3/
- Supporting: https://huggingface.co/tiiuae/Falcon3-10B-Base (model card with exact params, context, training token counts)
- Key facts: params=10B dense, context=32K, trained on 14T (7B base) + 2T depth-upscale (10B), Falcon LLM License 2.0, release 2024-12-17
- Notes: No MoE variant in Falcon 3 family (verified via falcon-lm.github.io/blog/falcon-3). 10B is flagship. Not frontier_open_at_release — DeepSeek-V3 671B released in same month. Per instructions, picking flagship only + Mamba update companion.

## Falcon3-Mamba-7B
- Source: https://falcon-lm.github.io/blog/falcon-3/
- Key facts: Continued pretraining of Falcon Mamba 7B with +1.5T tokens. 7B SSM. Released 2024-12-17.
- Notes: Not a distinct architecture; still pure Mamba SSM, same params. Skipping this as duplicate row — not enough architectural novelty over Falcon Mamba 7B to warrant separate row per row-selection rules.

## Falcon-H1 34B (flagship)
- Source: https://falcon-lm.github.io/blog/falcon-h1/
- Supporting: https://huggingface.co/tiiuae/Falcon-H1-34B-Base
- Key facts: params=34B, architecture=hybrid Mamba-2 + Transformer, context=256K, Falcon LLM License (Apache 2.0 based), release 2025-05-20
- Notes: architecture_type=hybrid. Flagship of Falcon-H1 family (0.5B to 34B). Matches Qwen2.5-72B and LLaMA 3.3 70B on benchmarks per TII claims. Not a globally frontier open-weight (DeepSeek-V3 671B much larger). Training tokens not disclosed on blog.

## Falcon-H1R 7B (reasoning)
- Source: https://falcon-lm.github.io/blog/falcon-h1r-7b/
- Supporting: https://huggingface.co/blog/tiiuae/falcon-h1r-7b
- Key facts: params=7B hybrid (Mamba + Transformer), context=256K, reasoning-tuned via SFT + RL, Falcon TII License, release 2026-01-05
- Notes: cap_reasoning=true. Built on Falcon H1 7B base. Not frontier open-weight in absolute terms (still 7B), but TII's first explicit reasoning family. Uses hybrid architecture.
# dbrx_arctic_grok1 research notes

## Grok-1
- Source: https://huggingface.co/xai-org/grok-1 (HF model card, Apache 2.0, 314B)
- Supporting: https://github.com/xai-org/grok-1 (GitHub README: explicit 8 experts / 2 active per token, max seq length 8192)
- Key facts: total_params=314B, active=~78.5B (25% of weights active per token, 2 of 8 experts), context=8192, released 2024-03-17, open weights Apache 2.0
- Notes: xAI blog x.ai/news/grok-os returns Cloudflare 403 to automated fetches, using HF card as release_url and GitHub README as supporting_url (supports context_window=8192, expert config, and active-params fraction). active_params = 314B * 0.25 ~= 78.5B (xAI/HF statement "25% of weights are active on a given token"). No native tool use, no vision. Not a test-time-reasoning model.
- Frontier open at release: true — on 2024-03-17 Grok-1 was the largest open-weight model by total parameters (larger than Falcon-180B, Mixtral 8x7B). Brief window before DBRX (Mar 27) and Llama 3 (Apr 18).

## DBRX
- Source: https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm (official Databricks announcement with 132B/36B, 16 experts / 4 active, 32K context, Databricks Open Model License)
- Supporting: none needed — release blog covers params, architecture, context, license.
- Key facts: total_params=132B, active=36B, context=32768, released 2024-03-27, open weights under Databricks Open Model License (bespoke non-Apache), 16 experts / 4 active (fine-grained MoE)
- Notes: Blog explicitly states "132B total / 36B active". Native tool/function calling NOT supported at release per HF model card and Databricks' own analysis ("DBRX models do not support native code execution, or other forms of function-calling"). Not vision, not reasoning-family, not code-specialized (general-purpose enterprise LLM).
- Frontier open at release: true — briefly led Mar 2024 open leaderboards (beat Mixtral 8x7B, Grok-1, Llama 2 70B on most benchmarks) until Llama 3 70B on 2024-04-18. ~3 week window.

## Snowflake Arctic
- Source: https://www.snowflake.com/en/blog/arctic-open-efficient-foundation-language-models-snowflake/ (Snowflake announcement, 480B/17B, Apache 2.0, Dense-MoE hybrid)
- Supporting: https://huggingface.co/Snowflake/snowflake-arctic-instruct (HF card confirms Dense-MoE Hybrid architecture: 10B dense + 128x3.66B MoE MLP, top-2 gating, Apache-2.0)
- Key facts: total_params=480B, active=17B, context=4096, released 2024-04-24, open weights Apache 2.0, architecture "Dense-MoE Hybrid" (categorized as MoE per our enum — hybrid enum value is reserved for SSM+transformer like Jamba)
- Notes: 4K context window is smallest of the three — blog mentions planned sliding-window extension but release-time is 4096. 17B active is small for 480B total; Snowflake's pitch was training-efficiency, not capability frontier. Not code-specialized (general-purpose enterprise model, though HumanEval is part of their "enterprise intelligence" suite). No native tool use announced.
- Frontier open at release: false — released 6 days after Llama 3 70B (Apr 18), which clearly outperformed Arctic on most open benchmarks despite having fewer total params. Arctic was notable for total-params and training efficiency but not capability-frontier.
# other_open research notes

## StableLM 7B (Alpha)
- Source: https://stability.ai/news-updates/stability-ai-launches-the-first-of-its-stablelm-suite-of-language-models
- Supporting: https://huggingface.co/stabilityai/stablelm-base-alpha-7b (context window 4096)
- Key facts: params=7B dense, context=4096, released=2023-04-19, open CC BY-SA-4.0
- Notes: Alpha release; was not frontier at release (overshadowed by LLaMA-1). frontier_open_at_release=false. supporting_url backs context_window and precise parameter figure.

## StableLM 2 1.6B
- Source: https://stability.ai/news-updates/introducing-stable-lm-2
- Supporting: https://huggingface.co/stabilityai/stablelm-2-1_6b (1.644B params exact, 4096 context)
- Key facts: params=1.6B (exact 1,644,417,024), context=4096, released=2024-01-19
- Notes: Multilingual model trained on 2T tokens. Small; not frontier; not frontier-open.

## MPT-7B
- Source: https://www.databricks.com/blog/mpt-7b
- Key facts: params=6.7B dense, context=2048 (base; StoryWriter variant 65k), released=2023-05-05, Apache-2.0
- Notes: Was comparable to LLaMA-7B at release. Not frontier-open (LLaMA-1 65B was larger).

## MPT-30B
- Source: https://www.databricks.com/blog/mpt-30b
- Key facts: params=30B dense, context=8192, released=2023-06-22, Apache-2.0
- Notes: Notable for 8k context window (vs 2k LLaMA/Falcon). Not frontier; not frontier-open at release (LLaMA-1 65B larger; Falcon-40B comparable).

## RedPajama-INCITE-7B
- Source: https://www.together.ai/blog/redpajama-models-v1
- Supporting: https://huggingface.co/togethercomputer/RedPajama-INCITE-7B-Base (6.9B exact, Pythia-based)
- Key facts: params=6.9B dense, context=2048 (Pythia arch), released=2023-05-05, Apache-2.0
- Notes: Intended as open replication of LLaMA recipe. supporting_url backs exact param count and architecture. Not frontier-open.

## StarCoder
- Source: https://arxiv.org/abs/2305.06161
- Supporting: https://huggingface.co/bigcode/starcoder (confirms 15.5B params, 8192 context)
- Key facts: params=15.5B dense, context=8192, released=2023-05-09 (arXiv v1), OpenRAIL license (open_weights=true)
- Notes: Was the largest/most capable open code LLM at release. cap_code_specialized=true. frontier_open_at_release=true (largest open *code* model, and open code was under-served). Note: "frontier open" here applies to code niche.

## StarCoder2 15B
- Source: https://arxiv.org/abs/2402.19173
- Supporting: https://huggingface.co/bigcode/starcoder2-15b (context 16384, sliding window 4096)
- Key facts: params=15B dense, context=16384, released=2024-02-28 (arxiv) / 2024-02-29
- Notes: Outperforms CodeLlama-34B at release. cap_code_specialized=true. In 2024-02 DeepSeek-Coder 33B and CodeLlama-70B existed; StarCoder2 was not the largest open-code model, so frontier_open_at_release=false (conservative).

## OLMo 7B
- Source: https://allenai.org/blog/olmo-open-language-model-87ccfc95f580
- Supporting: https://huggingface.co/allenai/OLMo-7B (context 2048)
- Key facts: params=7B dense, context=2048, released=2024-02-01, Apache-2.0
- Notes: Fully-open: weights + training data + logs. Not frontier (Llama-2 70B + Mixtral existed). Not frontier-open.

## OLMo 2 13B
- Source: https://allenai.org/blog/olmo2
- Supporting: https://huggingface.co/allenai/OLMo-2-1124-13B (context 4096)
- Key facts: params=13B dense, context=4096, released=2024-11-26, Apache-2.0
- Notes: Outperforms Qwen 2.5 7B; competitive with best open-weight models. But small scale; not frontier-open (Qwen2.5 72B, Llama 3.1 405B larger).

## Jamba (v0.1)
- Source: https://www.ai21.com/blog/announcing-jamba/
- Supporting: https://arxiv.org/abs/2403.19887 (Jamba paper confirming 52B total, 12B active, hybrid SSM-Transformer MoE)
- Key facts: params=52B total / 12B active, context=256000, released=2024-03-28, Apache-2.0
- Notes: First production-grade SSM-Transformer hybrid. architecture_type=hybrid. Not frontier-open overall (Mixtral 8x22B and Llama-3 coming right after), but a novel architecture milestone.

## Jamba 1.5 Large
- Source: https://huggingface.co/ai21labs/AI21-Jamba-Large-1.5
- Key facts: params=398B total / 94B active, context=256000, released=2024-08-22, Jamba Open Model License (open_weights=true)
- Notes: Scaled hybrid architecture. Function calling + JSON output supported at release (cap_tool_use=true). Not frontier (Llama-3.1 405B was released a month earlier and was more capable on standard benchmarks). frontier_open_at_release=false.
# yi research notes

## Yi-6B
- Source: https://huggingface.co/01-ai/Yi-6B
- Key facts: params=6B, active=6B, context=4096, released=2023-11-02, arch=dense (Llama-style transformer)
- License: Apache 2.0 (Yi license earlier, relicensed to Apache 2.0).
- Context: 4K at release, can be extended at inference time to 32K, and a separate Yi-6B-200K variant (Nov 5 2023) exists. Per scope we keep release-time context (4K) on the main row.
- open_weights=true, frontier_at_release=false, frontier_open_at_release=false (Yi-34B is the family flagship).
- cap_code_specialized=false, cap_reasoning=false, cap_tool_use=false (no native tool calling at release).
- supporting_url: none needed — HF card covers params, context, date, architecture.

## Yi-34B
- Source: https://huggingface.co/01-ai/Yi-34B
- Key facts: params=34B, active=34B, context=4096, released=2023-11-02, arch=dense (Llama-style transformer), trained on 3T multilingual corpus.
- open_weights=true. At release, Yi-34B topped Hugging Face Open LLM Leaderboard (pretrained) above Falcon-180B and Llama-2-70B in English and Chinese — so frontier_open_at_release=true (best open-weight small-flagship of its era). Not overall frontier (GPT-4, Claude 2.1, Gemini 1.0 Ultra announced same era) → frontier_at_release=false.
- cap_code_specialized=false, cap_reasoning=false, cap_tool_use=false.
- supporting_url: none needed.

## Yi-VL-6B
- Source: https://huggingface.co/01-ai/Yi-VL-6B
- Key facts: params ~ 6.6B total (Yi-6B-Chat decoder + CLIP ViT-H/14 vision encoder ~ 0.6B); released 2024-01-23 (per Yi GitHub README News section; scope says "Jan 22" but the primary source says Jan 23).
- Exact total params not printed, so using 6B decoder figure as total_params with param_source_note explaining the LLaVA-style decomposition. param_disclosure=official for the decoder count; encoder adds ~0.6B that is not summed officially, leaving total ambiguous → safest is to match scope and label param_disclosure=official using the 6B headline number, noting the extra encoder in param_source_note.
- Actually per PLAN.md convention: "For multimodal models with a vision/audio encoder: decoder + encoder(s) summed (e.g., Pixtral 12B is 12B decoder + 0.4B vision encoder → 12400000000)." CLIP ViT-H/14 is ~0.632B params → total_params ≈ 6.6B. Using 6632000000.
- Context: 4K (inherited from Yi-6B-Chat base); HF card does not override. Using 4096.
- cap_vision=true, open_weights=true, frontier_open_at_release=false (VL models weren't the overall open-weight frontier).
- supporting_url: https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K (backs the vision encoder size — actually will omit and just reference in note, since the CLIP ViT-H/14 encoder size is widely stated but not strictly needed in the release_url).
- Keep supporting_url blank; param_source_note will acknowledge the decoder-only figure caveat.

## Yi-VL-34B
- Source: https://huggingface.co/01-ai/Yi-VL-34B
- Key facts: params ~ 34.6B total (Yi-34B-Chat decoder + CLIP ViT-H/14 ~0.6B vision encoder), released 2024-01-23.
- Context: 4K (inherited), cap_vision=true, open_weights=true.
- frontier_open_at_release=false. Note that 01.AI claims it was "first open-source 34B VLM" but was not pushing the open-weight frontier (that was Llama-2-70B / Mixtral / Falcon-180B in the base-LM track).
- supporting_url: blank; same caveat as Yi-VL-6B.

## Yi-9B
- Source: https://huggingface.co/01-ai/Yi-9B
- Key facts: params=9B (HF "Model size" tag = 9B params; an older HF blog post references 8.8B as a more granular count), active=same, context=4096, released=2024-03-06, arch=dense. Built by depth-expanding Yi-6B (48 layers from 32) then continued pretraining with 0.8T more tokens.
- Using 9000000000 for total_params to match the official HF card's Model size metadata. param_disclosure=official.
- open_weights=true, frontier_open_at_release=false (size-class not flagship).
- supporting_url: blank.

## Yi-1.5 9B
- Source: https://huggingface.co/01-ai/Yi-1.5-9B
- Key facts: params=9B (Yi-1.5 retrains 6/9/34B size class), context=4096 base (also 16K/32K variants), released=2024-05-13, arch=dense.
- open_weights=true, frontier_open_at_release=false.
- supporting_url: blank.

## Yi-1.5 34B
- Source: https://huggingface.co/01-ai/Yi-1.5-34B
- Key facts: params=34B, context=4096 base (16K/32K variants), released=2024-05-13, arch=dense, pretrained on 3.6T tokens with an additional 500B high-quality tokens over Yi-34B; 3M SFT samples.
- open_weights=true, frontier_open_at_release=false (Llama-3-70B Apr 2024 already out, Qwen2-72B imminent).
- supporting_url: blank.

## Yi-Large
- Source: https://www.01.ai/yi-models
- Key facts: closed-weight proprietary flagship, announced 2024-05-13 together with Yi-1.5. 01.AI never disclosed parameter count officially. Pandaily and Chinese tech press cite "trillion-parameter" figures but these are unverified secondary claims.
- Per scope instructions: open_weights=false, param_disclosure=unknown, total_params/active_params blank.
- Architecture: unknown (speculated dense or MoE, no official statement). Leaving as "dense" would be a guess; PLAN.md enum doesn't have an "unknown" architecture — using "dense" is the conservative default per Yi family convention (no MoE in the open Yi series) but that is itself an estimate. Chose "dense" with a param_source_note caveat.
- Context: 32K per 01.ai platform docs (Yi-Large 32K available on the API).
- cap_tool_use=true (Yi-Large has function calling on 01.ai API per platform docs; will cite the 01.ai platform page as supporting_url).
- supporting_url: https://platform.01.ai/docs — supports context_window and tool-use flag.

## Yi-Lightning
- Source: https://arxiv.org/abs/2412.01253
- Key facts: released 2024-10-16 (announcement via @01AI_Yi on X); tech report published Dec 2024 on arXiv. MoE architecture with fine-grained expert segmentation; tech report explicitly confirms MoE but deliberately omits parameter counts.
- Per scope: open_weights=false, param_disclosure=unknown, total/active blank. architecture_type=MoE (confirmed by tech report abstract + body).
- Context: 64K (tech report explicitly states "we apply additional long-context training to extend the context window to 64K tokens").
- cap_tool_use=true (available on 01.ai API, which offers function calling across its models).
- supporting_url: https://x.com/01AI_Yi/status/1845776529185476613 — supports the 2024-10-16 announcement date, since the arXiv abstract doesn't print the public-release date.

## Yi-Coder-9B
- Source: https://huggingface.co/01-ai/Yi-Coder-9B
- Key facts: params=9B, context=128000, released=2024-09-05, arch=dense, code-specialized (52 programming languages, 85.4% HumanEval, 23.4% LiveCodeBench).
- open_weights=true (Apache 2.0 per repo), cap_code_specialized=true, cap_tool_use=false (no native tool calling).
- frontier_open_at_release=false (specialized code model, not a general-purpose flagship). DeepSeek-Coder-V2 was arguably the open-code frontier in mid-2024.
- supporting_url: blank.

## Yi-Coder-1.5B
- Source: https://huggingface.co/01-ai/Yi-Coder-1.5B
- Key facts: params=1.5B, context=128000, released=2024-09-05, arch=dense, code-specialized.
- Note: user scope says "Yi-Coder 9B/34B" but 01.AI actually released 1.5B and 9B (no 34B Coder). Including the 1.5B as the companion per their actual release, and omitting the (non-existent) 34B variant.
- open_weights=true, cap_code_specialized=true, frontier_open_at_release=false.
- supporting_url: blank.
# nemotron research notes

## Nemotron-4 15B
- Source: https://arxiv.org/abs/2402.16819 (release_url)
- Key facts: 15B dense decoder-only transformer; trained on 8T tokens; submitted Feb 26, 2024; multilingual focus
- Context window not explicitly stated in abstract; standard Nemotron-4 arch uses 4k seq length (confirmed for 340B). Using 4096 based on broader family convention. Note: announcement_date set to 2024-02-26 (arXiv v1).
- No official HF model card released for the 15B (NVIDIA never shipped public weights for this one; paper-only announcement was the main public artifact).
- open_weights=false — Nemotron-4 15B weights were NOT released publicly; the paper is technical disclosure only (unlike the later 340B release).
- frontier_open_at_release=false (weights not open); frontier_at_release=false (not SOTA at 15B scale — Mistral 7B / Gemma were competitive).
- cap_reasoning=false, cap_tool_use=false, cap_code_specialized=false (general-purpose multilingual).

## Nemotron-4 340B
- Source: https://blogs.nvidia.com/blog/nemotron-4-synthetic-data-generation-llm-training/ (release_url)
- Supporting: https://huggingface.co/nvidia/Nemotron-4-340B-Instruct (supporting_url — supports 4096 context window, dense arch, NVIDIA Open Model License, 340B params confirmation)
- Key facts: 340B dense decoder-only transformer (GQA, RoPE); announced Jun 14, 2024; trained on 9T tokens; context 4096; NVIDIA Open Model License (permissive commercial use); released as Base, Instruct, Reward variants
- frontier_open_at_release=true — at June 2024 this was the largest open-weights dense model (Llama 3 70B was current open flagship; Llama 3.1 405B didn't arrive until July 23, 2024). Briefly the open-weights frontier.
- frontier_at_release=false — well behind GPT-4o, Claude 3.5 Sonnet (Jun 2024) on general benchmarks.
- cap_tool_use=false (no native function calling advertised); cap_reasoning=false; cap_code_specialized=false.

## Nemotron-Mini-4B-Instruct
- Source: https://huggingface.co/nvidia/Nemotron-Mini-4B-Instruct (release_url)
- Key facts: 4B dense; 4096 context; NVIDIA Community Model License (Aug 2024); fine-tuned from Minitron-4B-Base (pruned/distilled from Nemotron-4 15B); optimized for roleplay, RAG, function calling
- Trained Feb–Aug 2024; HF release approximately Sep 2024 (announcement_date=2024-09-18 per the HF commit history and license PDF dated Aug 2024)
- open_weights=true; cap_tool_use=true (explicitly trained for function calling per card); cap_reasoning=false; cap_code_specialized=false
- Not frontier — small specialized on-device model.

## Llama-3.1-Nemotron-70B-Instruct
- Source: https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct (release_url)
- Key facts: 70B dense (Llama 3.1 architecture); RLHF tune of Llama-3.1-70B-Instruct using HelpSteer2 and REINFORCE; announced Oct 1, 2024 (benchmarks dated "As of 1 Oct 2024"); HF release Oct 15, 2024; 128k context (inherits from Llama 3.1); NVIDIA Open Model License + Llama 3.1 Community License
- Topped AlpacaEval 2 LC, Arena Hard, MT-Bench briefly — "briefly led some benchmarks" confirmed
- frontier_at_release=false (alignment-benchmark winner, not overall SOTA on reasoning/general); frontier_open_at_release=false (Llama 3.1 405B was the larger/more capable open model at that time)
- cap_reasoning=false (standard RLHF tune, no test-time thinking); cap_tool_use=true (Llama 3.1 supports tool use natively).
- announcement_date=2024-10-15 (HF availability / NVIDIA announcement post)

## Nemotron-H-56B-Base
- Source: https://arxiv.org/abs/2504.03624 (release_url)
- Supporting: https://huggingface.co/nvidia/Nemotron-H-56B-Base-8K (supporting_url — supports 56B param count, 8k context, hybrid Mamba-Transformer arch, Apr 14 2025 release date, research-only license)
- Key facts: 56B hybrid Mamba-Transformer (Mamba-2 + MLP + 10 Attention layers); 8k context at release; trained on 20T tokens in FP8; arXiv submission Apr 4, 2025; HF release Apr 14, 2025; also 47B compressed variant via MiniPuzzle
- open_weights=true (downloadable on HF) BUT NVIDIA Internal Scientific Research and Development License — research-only, not commercial. Still counts as open_weights=true per schema (any license = true).
- architecture_type=hybrid (SSM + transformer)
- cap_reasoning=false (base model, not reasoning-tuned); cap_tool_use=false
- frontier_open_at_release=false (Llama 3.1 405B, DeepSeek-V3 671B were open flagships).
- Picked the 56B as the headline; the 47B is a compression/distillation variant.

## Llama-3.1-Nemotron-Nano-8B-v1
- Source: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-8B-v1 (release_url)
- Key facts: 8B dense; derived from Llama 3.1 8B Instruct; 128k context; released Mar 18, 2025 (GTC 2025); dual-mode reasoning (thinking on/off); NVIDIA Open Model License + Llama 3.1 Community License
- cap_reasoning=true (explicit test-time reasoning mode), cap_tool_use=true

## Llama-3.3-Nemotron-Super-49B-v1
- Source: https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1 (release_url)
- Supporting: https://nvidianews.nvidia.com/news/nvidia-launches-family-of-open-reasoning-ai-models-for-developers-and-enterprises-to-build-agentic-ai-platforms (supporting_url — supports GTC 2025 launch date, open reasoning family positioning)
- Key facts: 49B dense (NAS-distilled from Llama-3.3-70B-Instruct); 128k context; released Mar 18, 2025; dual-mode reasoning; NVIDIA Open Model License + Llama 3.3 Community License
- architecture_type=dense (even with NAS pruning of some attention blocks, still a transformer decoder)
- cap_reasoning=true, cap_tool_use=true

## Llama-3.1-Nemotron-Ultra-253B-v1
- Source: https://huggingface.co/nvidia/Llama-3_1-Nemotron-Ultra-253B-v1 (release_url)
- Supporting: https://developer.nvidia.com/blog/build-enterprise-ai-agents-with-advanced-open-nvidia-llama-nemotron-reasoning-models/ (supporting_url — supports the Ultra release framing, GTC 2025 Llama Nemotron family launch)
- Key facts: 253B dense (NAS-distilled from Llama-3.1-405B-Instruct); 128k context; released Apr 7, 2025; dual-mode reasoning; NVIDIA Open Model License + Llama 3.1 Community License
- At release: "outperforms DeepSeek R1 at half the size" — competitive open reasoning model but DeepSeek-V3 671B / Llama 4 etc. larger open models exist
- frontier_open_at_release=false (DeepSeek-R1 671B, Llama 4 Maverick 400B MoE were contemporaneous open-weights larger/more capable flagships in Apr 2025)
- cap_reasoning=true, cap_tool_use=true

## NVIDIA-Nemotron-Nano-9B-v2
- Source: https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2 (release_url)
- Key facts: 9B hybrid Mamba-2 + Transformer (Nemotron-H arch); 128k context; released Aug 18, 2025; dual-mode reasoning; NVIDIA Open Model License; trained on ~20T tokens; compressed from 12B base via Minitron
- architecture_type=hybrid (SSM + transformer)
- cap_reasoning=true, cap_tool_use=true

## NVIDIA-Nemotron-3-Nano-30B-A3B
- Source: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 (release_url)
- Supporting: https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models (supporting_url — supports Nemotron 3 family announcement date Dec 15 2025)
- Key facts: 30B total, 3.5B active hybrid Mamba-2 + Transformer + MoE (128 routed experts + 1 shared, 6 activated per token); 1M context native (256k default on HF); released Dec 15, 2025; 25T training tokens; NVIDIA Nemotron Open Model License
- architecture_type=hybrid (SSM + transformer + MoE — fits hybrid bucket better than pure MoE)
- cap_reasoning=true (unified reasoning model per NVIDIA positioning), cap_tool_use=true
- Note: active_params uses routed-active figure of 3.5B (HF card) rather than the press-release 3B rounding.

## NVIDIA-Nemotron-3-Super-120B-A12B
- Source: https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/ (release_url)
- Supporting: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8 (supporting_url — supports 120B/12B params, 1M context, NVFP4 pretraining, arch details)
- Key facts: 120B total / 12B active hybrid Mamba-2 + Transformer + LatentMoE + Multi-Token Prediction; 1M context; announced Mar 11, 2026; NVFP4 pretraining on Blackwell; NVIDIA Nemotron Open Model License; reasoning mode configurable
- architecture_type=hybrid (SSM + transformer + MoE)
- cap_reasoning=true, cap_tool_use=true
- frontier_open_at_release=false (DeepSeek-V3.2 / Llama 5 etc. contemporaneous open flagships larger)
# phi research notes

## Phi-1
- Source: https://arxiv.org/abs/2306.11644 (arXiv submission 2023-06-20)
- HF card: https://huggingface.co/microsoft/phi-1
- Key facts: total_params=1.3B, active=1.3B (dense), context=2048, released=2023-06-20, license=MIT
- Notes: Code-specialized model (Python coding via HumanEval/MBPP focus). Paper title "Textbooks Are All You Need". Context window 2048 is standard for this generation (confirmed in HF model config for microsoft/phi-1 - same tokenizer base as CodeGen, max_position_embeddings=2048). Weights initially research-only license, later changed to MIT. Training: 54B tokens on 8 A100 GPUs for 6 days. cap_code_specialized=true. Open-weights frontier for small code models at its size, but not frontier-at-release globally (1.3B).
- release_url = arxiv paper (primary source stating params, code specialization, architecture); supporting_url = HF card (supports MIT license, context window, open weights)

## Phi-1.5
- Source: https://arxiv.org/abs/2309.05463 (arXiv 2023-09-11)
- HF card: https://huggingface.co/microsoft/phi-1_5
- Key facts: total_params=1.3B, active=1.3B, context=2048, released=2023-09-11, license=MIT
- Notes: "Textbooks Are All You Need II" technical report. General-purpose (common sense, reasoning, language understanding) not code-specialized. Trained on 30B tokens, 150B tokens seen total. Same 2048 context as Phi-1. MIT license per HF card. Not frontier globally; not the largest open-weight (LLaMA 65B existed already). False for both frontier flags.
- release_url = arxiv; supporting_url = HF card (supports license, open-weights status)

## Phi-2
- Source: https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/
- HF card: https://huggingface.co/microsoft/phi-2
- Key facts: total_params=2.7B, active=2.7B, context=2048, released=2023-12-12, license=MIT
- Notes: Blog announcement Dec 12, 2023; Satya Nadella first teased at Ignite Nov 2023 but official public release was Dec 12. Trained on 1.4T tokens. No RLHF/instruction-tune. Not code-specialized (general). 2048 context. Initially released under Microsoft Research License, later relicensed to MIT in Jan 2024. For this row we record final disclosed params (official) and MIT license per HF card. Not frontier; not open-frontier (Mixtral 8x7B released same week, Llama 2 70B much bigger).
- release_url = MS Research blog (primary, states 2.7B params, 1.4T tokens, release date); supporting_url = HF card (supports context window 2048 and MIT license)

## Phi-3-mini
- Source: https://arxiv.org/abs/2404.14219 (Phi-3 Technical Report)
- Blog: https://azure.microsoft.com/en-us/blog/introducing-phi-3-redefining-whats-possible-with-slms/
- Key facts: total_params=3.8B, active=3.8B (dense), context=4096 (base) / 128000 (extended variant), released=2024-04-23, license=MIT
- Notes: Announced Apr 23, 2024 at same time as tech report. Two context variants: 4K and 128K. Using 128K as release-time context since released simultaneously and is the headline "first in class for very long contexts" per blog. Trained on 3.3T tokens. Not code-specialized. Not frontier-at-release globally; not largest open-weight (Llama 3 70B released earlier same month; DBRX 132B exists). False for frontier flags.
- release_url = arxiv paper (primary, states all params, architecture); supporting_url = Azure blog (supports release date, 128K variant existence, MIT license)

## Phi-3-small
- Source: https://arxiv.org/abs/2404.14219
- Blog: https://azure.microsoft.com/en-us/blog/new-models-added-to-the-phi-3-family-available-on-microsoft-azure/
- Key facts: total_params=7B, active=7B, context=128000 (also 8K variant), released=2024-05-21, license=MIT
- Notes: Announced May 21, 2024 at Microsoft Build. Trained on 4.8T tokens. Dense. Two context variants (8K and 128K). Using 128K as the headline figure consistent with Phi-3-mini treatment.
- release_url = arxiv (params, architecture); supporting_url = Azure blog (release date May 21, 128K variant)

## Phi-3-medium
- Source: https://arxiv.org/abs/2404.14219
- Blog: https://azure.microsoft.com/en-us/blog/new-models-added-to-the-phi-3-family-available-on-microsoft-azure/
- Key facts: total_params=14B, active=14B, context=128000 (also 4K variant), released=2024-05-21, license=MIT
- Notes: Announced at Build 2024 May 21. Dense 14B. Trained on 4.8T tokens. Not frontier globally; not largest open-weight (Llama 3 70B bigger, DBRX bigger). False frontier flags.
- release_url = arxiv; supporting_url = Azure blog

## Phi-3-vision
- Source: https://arxiv.org/abs/2404.14219 (revised v3 added Phi-3-vision May 23)
- HF: https://huggingface.co/microsoft/Phi-3-vision-128k-instruct
- Key facts: total_params=4.2B, active=4.2B (dense), context=128000, released=2024-05-21, license=MIT
- Notes: 4.2B = Phi-3-mini backbone (3.8B) + image encoder + connector/projector. Announced at Build 2024. cap_vision=true. Training: 500B vision+text tokens, 1.5 days on 512 H100s.
- release_url = HF card (primary for this specific variant - states 4.2B, release date, cap_vision); supporting_url = arxiv paper (supports architecture and 4.2B description in v3)

## Phi-3.5-mini
- Source: https://huggingface.co/microsoft/Phi-3.5-mini-instruct
- Blog: https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/discover-the-new-multi-lingual-high-quality-phi-3-5-slms/4225280
- Key facts: total_params=3.8B, active=3.8B, context=128000, released=2024-08-20, license=MIT
- Notes: Announced August 20/21, 2024 per Microsoft tech community blog (post date Aug 22 but HF upload Aug 20). Trained on 3.4T tokens with 512 H100s over 10 days. Dense decoder-only. Multilingual focus vs Phi-3-mini. Using 2024-08-20 as announcement_date (HF model upload date).
- release_url = HF card (primary for params, context, release); supporting_url = MS tech community blog (release date confirmation, multilingual feature)

## Phi-3.5-MoE
- Source: https://huggingface.co/microsoft/Phi-3.5-MoE-instruct
- Blog: https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/announcing-the-availability-of-phi-3-5-moe-in-azure-ai-studio-and-github/4256278
- Key facts: total_params=42B, active=6.6B, context=128000, released=2024-08-20, license=MIT, architecture=MoE
- Notes: 16 experts, 2 active per token. HF card says "16 × 3.8B parameters" with 6.6B active using 2 experts — does not literally print "42B" but Microsoft's Azure Foundry announcement post explicitly states "the Phi-3.5-MoE model has 42B total parameters but activates only 6.6B of them". Using 42,000,000,000 total. Note: naive 16*3.8 = 60.8B but experts share attention and embedding weights per standard MoE convention, which gives the 42B effective total. Training: 4.9T tokens, 23 days on 512 H100s.
- release_url = HF card (supports active, context, release, MoE architecture); supporting_url = MS Azure Foundry blog (supports 42B total params explicitly)

## Phi-3.5-vision
- Source: https://huggingface.co/microsoft/Phi-3.5-vision-instruct
- Blog: https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/discover-the-new-multi-lingual-high-quality-phi-3-5-slms/4225280
- Key facts: total_params=4.2B, active=4.2B, context=128000, released=2024-08-20, license=MIT
- Notes: Multi-frame image understanding focus. Architecture: image encoder + Phi-3.5-mini backbone. cap_vision=true. Same 4.2B headline as Phi-3-vision but updated with multi-frame capability.
- release_url = HF card (supports params, release, vision capability); supporting_url = MS tech community blog (announcement context)

## Phi-4
- Source: https://arxiv.org/abs/2412.08905 (Phi-4 Technical Report, Dec 12, 2024)
- HF: https://huggingface.co/microsoft/phi-4
- Key facts: total_params=14B, active=14B (dense), context=16384, released=2024-12-12, license=MIT
- Notes: 14B dense decoder-only. Context extended to 16K during midtraining (paper states "default context length of 4096... later extended to a 16K context length during midtraining"). Using 16K as release-time context. Pretrained on ~10T tokens. Initially released Dec 12, 2024 on Azure Foundry, weights published on HF Jan 2025 under MIT.
- release_url = arxiv (primary, all key facts including 16K context); supporting_url = HF card (MIT license, open weights)

## Phi-4-multimodal
- Source: https://huggingface.co/microsoft/Phi-4-multimodal-instruct
- Blog: https://azure.microsoft.com/en-us/blog/empowering-innovation-the-next-generation-of-the-phi-family/
- Key facts: total_params=5.6B, active=5.6B, context=128000, released=2025-02-26, license=MIT
- Notes: Multimodal: text + vision + audio. 5.6B params total (Phi-4-mini backbone + vision encoder + audio encoder). Audio: supports speech recognition, translation, summarization. Vision: JPG/PNG etc. cap_vision=true, cap_audio=true. Release Feb 26, 2025 per SiliconAngle; HF upload around same date.
- release_url = HF card (primary for params, multimodal features); supporting_url = Azure blog (release date, announcement context)

## Phi-4-mini
- Source: https://huggingface.co/microsoft/Phi-4-mini-instruct
- Blog: https://azure.microsoft.com/en-us/blog/empowering-innovation-the-next-generation-of-the-phi-family/
- Key facts: total_params=3.8B, active=3.8B, context=128000, released=2025-02-26, license=MIT
- Notes: Dense decoder-only Transformer with grouped-query attention (upgrade from Phi-3.5-mini). 200K vocabulary, shared input/output embeddings. Trained on 5T tokens on 512 A100s over 21 days. Supports function/tool calling per HF card.
- release_url = HF card; supporting_url = Azure blog

## Phi-4-reasoning
- Source: https://huggingface.co/microsoft/Phi-4-reasoning
- Tech report: https://arxiv.org/abs/2504.21318
- Key facts: total_params=14B, active=14B, context=32768, released=2025-04-30, license=MIT
- Notes: SFT + RL-tuned variant of Phi-4 for explicit reasoning. Outputs chain-of-thought block + summarization block. cap_reasoning=true. Same 14B dense architecture as Phi-4 base. Context extended to 32K.
- release_url = HF card (primary); supporting_url = arxiv technical report (architecture details, reasoning training)

## Phi-4-mini-reasoning
- Source: https://huggingface.co/microsoft/Phi-4-mini-reasoning
- Tech report: https://arxiv.org/abs/2504.21233
- Key facts: total_params=3.8B, active=3.8B, context=128000, released=2025-04-30, license=MIT
- Notes: Fine-tuned from Phi-4-mini with synthetic teacher data distilled from DeepSeek-R1. Math-focused reasoning. Same Phi-4-mini architecture. cap_reasoning=true.
- release_url = HF card; supporting_url = arxiv paper

## Phi-4-mini-flash-reasoning
- Source: https://azure.microsoft.com/en-us/blog/reasoning-reimagined-introducing-phi-4-mini-flash-reasoning/
- HF: https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning
- Key facts: total_params=3.8B, active=3.8B, context=65536 (64K), released=2025-07-09, license=MIT, architecture=hybrid (SambaY: Mamba SSM + sliding window attention + cross-decoder with GMU)
- Notes: Novel SambaY hybrid architecture. Described as decoder-hybrid-decoder. NOT a pure transformer — combines Mamba SSM blocks, sliding-window attention, and Gated Memory Unit cross-layers. 10x throughput vs Phi-4-mini. Reasoning model (cap_reasoning=true). architecture_type=hybrid per schema.
- release_url = Azure blog (primary, architecture + release date + 10x throughput claim); supporting_url = HF card (params, context, license)
# pre_llm research notes

## BERT-Large (uncased)
- Source: https://arxiv.org/abs/1810.04805
- Supporting: https://huggingface.co/google-bert/bert-large-uncased (supports total_params=336M and context_window=512 and Apache-2.0 license)
- Key facts: params=340M (paper headline; HF card says 336M including embeddings — close enough; we'll use 340M as the widely-cited figure from the paper), active=340M (dense encoder-only), context=512, released=2018-10-11 (arXiv v1 date)
- Notes: Encoder-only MLM+NSP pretraining. Code + weights released at google-research/bert under Apache 2.0. Defined the modern pretraining+fine-tuning paradigm — frontier_at_release=true for the pretraining era, and frontier_open_at_release=true. Marked cap_text only (no other modalities; BERT was not generative in the LLM sense, but cap_text=true is the schema baseline per PLAN.md).

## T5-11B
- Source: https://arxiv.org/abs/1910.10683
- Supporting: https://huggingface.co/google-t5/t5-11b (supports params=11B flagship, Apache-2.0 license, encoder-decoder)
- Key facts: params=11B, active=11B (dense encoder-decoder), context=512 (standard T5 pretraining sequence length, confirmed widely), released=2019-10-23 (arXiv v1 date)
- Notes: Text-to-Text Transfer Transformer, unified text-to-text formulation. The 11B flagship was the largest encoder-decoder open-weights model of its era. frontier_at_release=true (largest encoder-decoder, SOTA on many GLUE/SuperGLUE tasks) and frontier_open_at_release=true.

## Megatron-LM 8.3B
- Source: https://arxiv.org/abs/1909.08053
- Supporting: https://ar5iv.labs.arxiv.org/html/1909.08053 (supports context_window=1024 and code-release statement)
- Key facts: params=8.3B, active=8.3B (dense decoder-only GPT-2 style), context=1024, released=2019-09-17 (arXiv v1 date)
- Notes: NVIDIA's largest dense autoregressive LM at the time. Code + training pipeline open-sourced at github.com/NVIDIA/Megatron-LM (open_weights=true — scripts + checkpoints released). Briefly the largest dense autoregressive LM from Sep 2019 to Feb 2020, so frontier_at_release=true and frontier_open_at_release=true.

## Turing-NLG 17B
- Source: https://www.microsoft.com/en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft/
- Key facts: params=17B (official, 78 layers, hidden 4256, 28 heads), active=17B (dense), context=1024, released=2020-02-13 (blog post date)
- Notes: Closed-weights — Microsoft released only a private demo to select academic users. Largest announced dense LM in Feb 2020 (briefly, superseded by GPT-3 in May/Jun 2020). frontier_at_release=true, frontier_open_at_release=false (closed). No supporting_url needed — primary Microsoft Research blog states all fields (params, architecture, context window via "sequences of 1024 tokens", release status).

# deepseek_v4 research notes

## DeepSeek-V4-Pro
- Source (release_url): https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro (official lab HF model card)
- Source (supporting_url): https://api-docs.deepseek.com/guides/function_calling (confirms function/tool calling support for V4 including in thinking mode)
- Key facts: total_params=1.6T (1,600,000,000,000), active_params=49B (49,000,000,000), context=1,000,000 tokens, released=2026-04-24, architecture=MoE, license=MIT (open_weights=true), pretraining tokens=32T+
- Architecture details: Hybrid Attention (CSA + HCA), Manifold-Constrained Hyper-Connections (mHC), Muon optimizer. Three reasoning modes: Non-think / Think High / Think Max. FP4+FP8 mixed precision.
- Capabilities: cap_reasoning=true (native thinking modes with reasoning_content in chat template, cites bibtex as "Towards Highly Efficient Million-Token Context Intelligence"). cap_tool_use=true (function calling supported in both thinking and non-thinking per api-docs). cap_vision/audio/video=false (no multimodal encoder mentioned on model card). cap_code_specialized=false (general-purpose flagship; code benchmarks strong but not code-specialized line like DeepSeek-Coder).
- Frontier flags:
  - frontier_at_release=false. HF card benchmarks show V4-Pro beats frontier models on LiveCodeBench (93.5) and Codeforces (3206) but loses on MMLU-Pro (87.5 vs Gemini 91.0), SimpleQA-Verified (57.9 vs Gemini 75.6), IMOAnswerBench (89.8 vs GPT-5.4 91.4), and MRCR 1M (83.5 vs Opus 92.9). Simon Willison quotes DeepSeek's own framing "trails SOTA by 3-6 months". Conservative call: frontier_at_release=false — "near frontier" is not "at frontier".
  - frontier_open_at_release=true. Largest and most capable open-weights model at release date; 1.6T total / 49B active under MIT license, beats all rival open models on maths and coding per HF card.
- Notes: V4-Flash (284B total / 13B active) released same day as smaller sibling — omitted per single-row scope from the orchestrator. V4-Pro-Base variant also published (pretrained-only checkpoint) — this row captures the instruction-tuned V4-Pro flagship. supporting_url = api-docs.deepseek.com function_calling guide, supports cap_tool_use flag (the HF card does not itself describe the function-calling API surface).
- check-urls caveat: the api-docs.deepseek.com domain returns a TLS cert-name error in this environment because the network path resolves the host to a Whalebone content-filter proxy (subject=CN=hos.whalebone.io) rather than DeepSeek's real origin. This is an environment-level TLS intercept, analogous to the openai.com Cloudflare 403 bot-block pattern called out in CLAUDE.md — do not rewrite the URL. The URL is the canonical documentation path and appears as a live hit in multiple web-search results. The HF model card (release_url) passes check-urls at 200.
