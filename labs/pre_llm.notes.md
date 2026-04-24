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

