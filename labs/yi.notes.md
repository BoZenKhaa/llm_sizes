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
