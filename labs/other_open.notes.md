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
