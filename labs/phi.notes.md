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
