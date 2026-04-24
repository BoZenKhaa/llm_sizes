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
