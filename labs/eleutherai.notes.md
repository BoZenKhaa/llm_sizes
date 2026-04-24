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
