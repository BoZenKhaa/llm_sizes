# Research status

Lab-by-lab progress. Ordering reflects perceived importance for the
two-line plot (overall frontier + open-weights frontier). Check a lab
off once every release event in PLAN.md scope has been researched,
verifier-reviewed, and any fixups applied.

## Closed-weights track (priority order)

- [ ] **OpenAI** — GPT-3, 3.5, 4, 4 Turbo, 4o, 4o-mini, o1, o3, o3-mini, o4-mini, 4.1, 5 (verify)
- [ ] **Google / Google DeepMind** — Gemini 1.0/1.5/2.0/2.5 family + Gemma open-weights companion; historical PaLM, PaLM 2, LaMDA, Gopher, Chinchilla
- [x] **Anthropic** — Claude 1 → Opus 4.7 + Mythos (19 + 1 rows). Two leaks populated (Sonnet 4.5, Opus 4.6 via Musk-tweet chain).
- [ ] **xAI** — Grok-1.5, Grok-2, Grok-3, Grok-4.x (Grok-1 open-weight under open-weights track)
- [ ] **Other closed** — Cohere Command / Command R+ (flag CC-BY-NC license), AI21 Jurassic, Inflection Pi / Inflection-2, Reka Core/Flash, Amazon Nova

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

- **Mistral (done 2026-04-24)**: researcher added 30 rows; verifier caught 8 hard FAILs (context window, tool-use booleans, vision-encoder param totals, inferred `official` disclosures); researcher fixup pass corrected all. Defensible-as-is.
- **Anthropic (done 2026-04-24)**: researcher added 19 rows; 17 stayed `param_disclosure=unknown` (no credible third-party estimates); Sonnet 4.5 and Opus 4.6 populated from the April 2026 Musk-tweet leak chain. Mythos row added then trimmed — `total_params` pulled back to blank after verification found the 10T figure wasn't in either cited URL. See RESEARCH_NOTES.md "Mythos revision 2026-04-24" for the rollback.

## Workflow for each new lab

1. Dispatch `researcher` subagent scoped to the single lab.
2. Dispatch `verifier` subagent on the new rows (batch by 10 for parallelism).
3. If verifier reports hard FAILs, dispatch `researcher` in fixup mode with the exact FAIL list.
4. Spot-check any row whose cited URL looks unfamiliar — the Mythos pass showed that "source text in `param_source_note` that isn't in the two URL columns" is the main hallucination failure mode.
5. Check the lab off here and commit.
