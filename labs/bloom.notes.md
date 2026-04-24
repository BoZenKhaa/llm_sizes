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
