# dbrx_arctic_grok1 research notes

## Grok-1
- Source: https://huggingface.co/xai-org/grok-1 (HF model card, Apache 2.0, 314B)
- Supporting: https://github.com/xai-org/grok-1 (GitHub README: explicit 8 experts / 2 active per token, max seq length 8192)
- Key facts: total_params=314B, active=~78.5B (25% of weights active per token, 2 of 8 experts), context=8192, released 2024-03-17, open weights Apache 2.0
- Notes: xAI blog x.ai/news/grok-os returns Cloudflare 403 to automated fetches, using HF card as release_url and GitHub README as supporting_url (supports context_window=8192, expert config, and active-params fraction). active_params = 314B * 0.25 ~= 78.5B (xAI/HF statement "25% of weights are active on a given token"). No native tool use, no vision. Not a test-time-reasoning model.
- Frontier open at release: true — on 2024-03-17 Grok-1 was the largest open-weight model by total parameters (larger than Falcon-180B, Mixtral 8x7B). Brief window before DBRX (Mar 27) and Llama 3 (Apr 18).

## DBRX
- Source: https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm (official Databricks announcement with 132B/36B, 16 experts / 4 active, 32K context, Databricks Open Model License)
- Supporting: none needed — release blog covers params, architecture, context, license.
- Key facts: total_params=132B, active=36B, context=32768, released 2024-03-27, open weights under Databricks Open Model License (bespoke non-Apache), 16 experts / 4 active (fine-grained MoE)
- Notes: Blog explicitly states "132B total / 36B active". Native tool/function calling NOT supported at release per HF model card and Databricks' own analysis ("DBRX models do not support native code execution, or other forms of function-calling"). Not vision, not reasoning-family, not code-specialized (general-purpose enterprise LLM).
- Frontier open at release: true — briefly led Mar 2024 open leaderboards (beat Mixtral 8x7B, Grok-1, Llama 2 70B on most benchmarks) until Llama 3 70B on 2024-04-18. ~3 week window.

## Snowflake Arctic
- Source: https://www.snowflake.com/en/blog/arctic-open-efficient-foundation-language-models-snowflake/ (Snowflake announcement, 480B/17B, Apache 2.0, Dense-MoE hybrid)
- Supporting: https://huggingface.co/Snowflake/snowflake-arctic-instruct (HF card confirms Dense-MoE Hybrid architecture: 10B dense + 128x3.66B MoE MLP, top-2 gating, Apache-2.0)
- Key facts: total_params=480B, active=17B, context=4096, released 2024-04-24, open weights Apache 2.0, architecture "Dense-MoE Hybrid" (categorized as MoE per our enum — hybrid enum value is reserved for SSM+transformer like Jamba)
- Notes: 4K context window is smallest of the three — blog mentions planned sliding-window extension but release-time is 4096. 17B active is small for 480B total; Snowflake's pitch was training-efficiency, not capability frontier. Not code-specialized (general-purpose enterprise model, though HumanEval is part of their "enterprise intelligence" suite). No native tool use announced.
- Frontier open at release: false — released 6 days after Llama 3 70B (Apr 18), which clearly outperformed Arctic on most open benchmarks despite having fewer total params. Arctic was notable for total-params and training efficiency but not capability-frontier.
