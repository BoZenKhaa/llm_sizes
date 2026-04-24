# Research status

Lab-by-lab progress. Ordering reflects perceived importance for the
two-line plot (overall frontier + open-weights frontier). Check a lab
off once every release event in PLAN.md scope has been researched,
verifier-reviewed, and any fixups applied.

## Closed-weights track (priority order)

- [x] **OpenAI** — GPT-1 → GPT-5.5 + gpt-oss-120b (27 rows)
- [x] **Google / Google DeepMind** — Gopher → Gemini 3.1 Pro + Gemma 1/2/3 (30 rows)
- [x] **Anthropic** — Claude 1 → Opus 4.7 + Mythos (19 + 1 rows). Two leaks populated (Sonnet 4.5, Opus 4.6 via Musk-tweet chain).
- [x] **xAI** — Grok-1.5 → Grok-4.20 (14 rows). Grok-1 open-weight deferred to open-weights track.
- [x] **Other closed** — Cohere (Command R/R+/R7B/A/A-Vision), AI21 Jurassic-1/2, Inflection-1/2/2.5, Reka Flash/Edge/Core/Flash 3, Amazon Nova Micro/Lite/Pro/Premier (18 rows)

## Open-weights track (priority order)

- [ ] **Meta / Llama** — LLaMA 1 → Llama 4; Code Llama; Llama 3.2 multimodal; OPT-175B, Galactica (historical)
- [ ] **DeepSeek** — LLM 7B/67B, V2, V2.5, V3, Coder / Coder-V2, R1
- [ ] **Alibaba / Qwen** — Qwen → Qwen2.5 → Qwen3 (verify); Qwen2.5-Coder, -VL, QwQ-32B
- [x] **Mistral AI** — Mistral 7B → Mistral Small 4 (30 rows). Includes Pixtral, Codestral, Ministral, Magistral, Devstral, Nemo, Mathstral.
- [ ] **Google Gemma** — Gemma 1, 2, 3 (verify) — tracked under Google above if combined
- [ ] **EleutherAI** — GPT-Neo, GPT-J 6B, GPT-NeoX-20B
- [ ] **TII (Falcon)** — Falcon 7/40/180B, Falcon 2, Falcon 3
- [ ] **BigScience** — BLOOM 176B
- [ ] **Microsoft (Phi)** — Phi-1, 1.5, 2, 3 mini/small/medium, 3.5, 4
- [ ] **01.AI (Yi)** — Yi-6B/34B, Yi-1.5, Yi-Large
- [ ] **NVIDIA (Nemotron)** — Nemotron-4 340B, Llama-Nemotron variants
- [ ] **Databricks** — DBRX (132B/36B MoE)
- [ ] **Snowflake** — Arctic (480B/17B MoE)
- [ ] **AI21 (hybrid)** — Jamba (SSM hybrid), Jurassic open-weight if counted
- [ ] **Grok-1 (xAI open-weight)** — 314B MoE, Mar 2024 — often batched with xAI closed track
- [ ] **Other open** — StableLM, MPT, RedPajama, StarCoder / StarCoder2, OLMo / OLMo-2, Command R+ (if counted open)

## Pre-LLM / foundational (low priority, fill last)

- [ ] BERT, GPT-1, GPT-2, T5, Megatron-LM, Turing-NLG, Jurassic-1

---

## Completion notes

- **Google / DeepMind (done 2026-04-24)**: researcher added 30 rows (lines 79–108) covering Gopher, LaMDA, Chinchilla, PaLM, PaLM 2, Gemini 1.0 Ultra/Pro/Nano, Gemini 1.5 Pro/Flash, Gemma 1 (2B/7B), CodeGemma, RecurrentGemma, PaliGemma, Gemma 2 (27B/9B/2B), Gemini 2.0 Flash/Flash Thinking/Pro Experimental/Flash-Lite, Gemma 3 (27B/12B/4B/1B), Gemini 2.5 Pro/Flash, Gemini 3 Pro, Gemini 3.1 Pro. Three parallel verifier batches caught 9 hard FAILs — cap_tool_use on LaMDA, unsupported token-count claims in Chinchilla/PaLM notes, cap_code_specialized on Gemini 1.5 Flash / Gemma 1 7B (later found to already be false — verifier misread), context window on PaliGemma (512→128) and Gemini 1.5 Pro (1M experimental→128K standard), Gemma 2 2B params (2B→2.6B), and audio/video caps on Gemini 2.0 Pro Experimental / Flash-Lite (future-planned, not at release). PARTIALs tightened by swapping supporting URLs to ai.google.dev model pages and the DeepMind model card for Gemini 3.1. CNBC PaLM 2 leak URL bot-blocks automated WebFetch but resolves fine via browser UA — logged in RESEARCH_NOTES.md. All Gemini rows except Nano stay `param_disclosure=unknown`; Gemma family is `official`; PaLM 2 is `leaked` via CNBC.
- **Mistral (done 2026-04-24)**: researcher added 30 rows; verifier caught 8 hard FAILs (context window, tool-use booleans, vision-encoder param totals, inferred `official` disclosures); researcher fixup pass corrected all. Defensible-as-is.
- **Anthropic (done 2026-04-24)**: researcher added 19 rows; 17 stayed `param_disclosure=unknown` (no credible third-party estimates); Sonnet 4.5 and Opus 4.6 populated from the April 2026 Musk-tweet leak chain. Mythos row added then trimmed — `total_params` pulled back to blank after verification found the 10T figure wasn't in either cited URL. See RESEARCH_NOTES.md "Mythos revision 2026-04-24" for the rollback.
- **xAI (done 2026-04-24)**: researcher added 14 rows (lines 109–122): Grok-1.5, Grok-1.5V, Grok-2, Grok-2 mini, Grok-3, Grok-3 (Think), Grok-3 mini, Grok-3 mini (Think), Grok-4, Grok-4 Heavy, Grok-4 Fast, Grok-4.1, Grok-4.1 Fast, Grok-4.20. All `param_disclosure=unknown`/blank — xAI has not disclosed params for any closed-weight Grok, and the researcher correctly avoided retro-fitting Grok-1's 314B MoE. `architecture_type=other` for all (dense-vs-MoE unconfirmed). Every `x.ai/news/grok-*` URL Cloudflare-403s automated fetchers; rely on supporting URLs. Two parallel verifier batches caught 4 hard FAILs: Grok-2 / Grok-2 mini date (Aug 13 vs Wikipedia's Aug 14 — TechCrunch 2024/08/13 confirmed Aug 13), Grok-4 supporting URL being an unfetchable PDF (swapped to OpenRouter; also flipped cap_vision true), Grok-4.20 date contradiction between docs.x.ai "March 2026" GA and the Feb 17 beta (kept Feb 17 as first public announcement, swapped NextBigFuture → adwaitx for fetchable attestation). Verifier-flagged context_window NOT_IN_SOURCE on rows 110-116 and 118 all resolved by blanking rather than keeping unverifiable numbers (1M Grok-3 claim survives only on the Cloudflare-blocked xAI blog; later API-era coverage quotes 131K). Rows 120 (Grok-4.1) and 121 (Grok-4.1 Fast) passed cleanly backed by BetterStack. Row 119 (Grok-4 Fast) cap_reasoning verifier FAIL was a column-miscount — field was already true. adwaitx.com as a supporting URL for Grok-4.20 is a weaker citation than preferred but was the only fetchable contemporaneous source pinning Feb 17 2026.
- **Other closed (done 2026-04-24)**: researcher added 18 rows (lines 123–140) covering Cohere (Command R 35B, R+ 104B, R7B 7B, Command A 111B, Command A Vision 112B — all `open_weights=true` under CC-BY-NC with `param_disclosure=official` from HF cards), AI21 (Jurassic-1 Jumbo 178B official, Jurassic-2 Jumbo unknown), Inflection (1/2/2.5 all unknown, no params ever disclosed), Reka (Flash 21B, Edge 7B, Core unknown, Flash 3 21B — Flash 3 is the only open-weight under Apache 2.0 and is a reasoning model), Amazon Nova (Micro/Lite/Pro Dec 3 2024, Premier Apr 30 2025 — all unknown). Two parallel verifier batches caught 3 hard FAILs: Jurassic-1 date (Aug 11→Aug 4 per AI21 blog), Command A Vision `cap_tool_use` (true→false, neither cited URL mentions tool use), and `architecture_type=dense` unverifiable for Jurassic-2/Inflection-1/Inflection-2 → swapped to `other` per the xAI conservatism pattern. Two verifier-flagged FAILs (Inflection-2.5 cap_reasoning, Reka Flash 3 cap_reasoning) turned out to be stale snapshots — rows already correct. No Cloudflare bot-blocks in this bucket; all 23 cited URLs return 200. Skipped Cohere's pre-R original "Command" (no clean launch date), Jurassic-2 Grande/Large (identical rows without param disclosure would be noise), Reka Flash 3.1 (minor point release), and Amazon Nova Canvas/Reel (image/video gen, not LLMs).
- **OpenAI (done 2026-04-24)**: researcher added 27 rows (lines 52–78): GPT-1, GPT-2, GPT-3, Codex (2021), GPT-3.5/ChatGPT, GPT-4, GPT-4 Turbo, GPT-4o/4o-mini, o1-preview/mini/full, o3-mini, GPT-4.5, GPT-4.1/mini/nano, o3, o4-mini, o3-pro, gpt-oss-120b, GPT-5/5-mini/5-nano, 5.1, 5.2, 5.5. All `openai.com/index/*` URLs 403 to WebFetch/curl (Cloudflare), so verifier couldn't confirm content directly; orchestrator cross-checked the late-dated rows (5.1/5.2/5.5) via WebSearch and all are real releases. Researcher-side fixups: stripped unsupported benchmark numbers from GPT-5.5's `param_source_note` (88.7% SWE-bench / 92.4% MMLU / 400K Codex context were not in either cited URL), tightened o3-pro's "assumed URL" confessional wording, dropped GitHub repo reference from GPT-1's note. Only GPT-3 (175B official) and GPT-4 (~1.8T leaked, SemiAnalysis as supporting_url) carry param figures from the pre-GPT-4 era; gpt-oss-120b is the only post-GPT-4 row with `official` params (117B/5.1B MoE). Everything else is `unknown` per OpenAI's disclosure policy.

## Workflow for each new lab

1. Dispatch `researcher` subagent scoped to the single lab.
2. Dispatch `verifier` subagent on the new rows (batch by 10 for parallelism).
3. If verifier reports hard FAILs, dispatch `researcher` in fixup mode with the exact FAIL list.
4. Spot-check any row whose cited URL looks unfamiliar — the Mythos pass showed that "source text in `param_source_note` that isn't in the two URL columns" is the main hallucination failure mode.
5. Check the lab off here and commit.
