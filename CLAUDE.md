# Operational notes for the llm_sizes project

Read `PLAN.md` for schema and scope and `STATUS.md` for lab-by-lab progress.
This file captures harness conventions so the orchestrator and subagents
don't reinvent workflows each run.

## Project helpers

Two `uv run` entry points live in `src/llm_sizes_tools/`. Use them instead
of hand-rolled shell loops — the loops trigger a permission prompt for
each compound command, while helpers run under a single approval.

### `csv-row` — read rows with labelled fields

Parses with `csv.reader` (RFC 4180 quoting), so it is safe against the
commas-inside-quoted-notes trap that misaligns `awk -F,` splits.

```bash
uv run csv-row 5                             # whole row, labelled
uv run csv-row 5 --field cap_tool_use        # single field, bare value
uv run csv-row 52 71 78 --field model_name   # multi-row, auto-separated
uv run csv-row 52-61 --field release_url     # range
```

Prefer `csv-row 52-61` over `for n in $(seq 52 61); do csv-row $n; done`.
Multi-row output auto-prefixes each row with `=== line N ===`.

### `check-urls` — HEAD-check a batch of URLs

```bash
uv run check-urls https://foo https://bar
uv run check-urls --from-csv 52-78           # pulls release_url+supporting_url
uv run check-urls --from-csv --field release_url 52-78
```

Browser user agent and redirect-following by default. Exit 1 if any URL
is not 2xx/3xx. Useful for:

- **Researcher pre-commit**: catch 404s on URLs you just added, before
  the verifier cycle.
- **Orchestrator triage**: when the verifier reports mass fetch
  failures, `check-urls` disambiguates a real hallucinated slug (unique
  404/500 among 2xx siblings) from a domain-wide Cloudflare bot-block
  (uniform 403 across every URL at that domain). openai.com is known
  to Cloudflare-block automated fetches; do not rewrite those URLs on
  the basis of a 403 alone — cross-check with `WebSearch`.

## Two-agent workflow per lab

Documented in `STATUS.md` step-list. Shorthand:

1. `researcher` subagent scoped to one lab → appends rows.
2. `verifier` subagent(s) in parallel batches of ~10 rows → report
   FAIL / PARTIAL / PASS against the cited URLs.
3. If hard FAILs exist, `researcher` fixup pass with the specific list.
4. Orchestrator spot-checks anything unfamiliar, especially rows where
   `param_source_note` asserts facts not in either URL column (the
   Mythos + GPT-5.5 failure mode — numbers that read plausible but
   live only in the note).
5. Update `STATUS.md` completion notes and commit.

## Source-substantiation rule

Non-negotiable, stated in `researcher.md`: every factual claim in a row
(including numbers, architecture, licensing, benchmark figures) must be
supported by `release_url` or `supporting_url`. Anything that is only in
`param_source_note` but not in either cited URL is unverifiable and
should be removed or have its source added. The verifier can only fetch
the two URL columns.
