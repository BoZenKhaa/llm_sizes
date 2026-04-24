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
