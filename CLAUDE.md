# Operational notes for the llm_sizes project

Read `PLAN.md` for schema and scope and `STATUS.md` for lab-by-lab progress.
This file captures harness conventions so the orchestrator and subagents
don't reinvent workflows each run.

## Python execution

Always run Python through `uv` — never use a bare `python3` / `python`
or assume packages are importable from the system interpreter. Examples:

- Run a script with inline PEP 723 deps:
  `uv run --with matplotlib --with plotly scripts/plot_params.py`
- Run a project entry point: `uv run csv-row 5`
- Ad-hoc one-liner: `uv run --with plotly python -c "..."`

The project's `.venv` only contains the local `llm_sizes_tools` package;
plotting deps (matplotlib, plotly, adjustText, numpy) are pulled in
on-demand by `uv run --with ...` or via PEP 723 headers in the scripts.

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
uv run check-urls --from-csv 52-78                        # main CSV
uv run check-urls --from-csv --field release_url 52-78
uv run check-urls --from-csv --csv labs/qwen.csv 2-20     # per-lab CSV
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

## Per-lab working files + merge workflow

Each lab gets its own working CSV + notes file under `labs/`. This lets
multiple researchers run in parallel without racing on a shared file.
Merging into the main CSV + `RESEARCH_NOTES.md` happens only after the
verifier has cleared the lab.

File layout:

- `labs/<lab>.csv` — pre-populated with the main CSV header line
  only; researcher appends rows here.
- `labs/<lab>.notes.md` — per-lab research notes (same format as
  the main `RESEARCH_NOTES.md`).
- `labs/.header` — stashed copy of the main CSV header, used to
  initialize new lab files.

Orchestrator helpers (plain shell — no script needed):

```bash
# Initialize a new lab file pair
LAB=qwen
head -1 llm_sizes.csv > labs/$LAB.csv
printf '# %s research notes\n\n' "$LAB" > labs/$LAB.notes.md

# Merge a verified lab into the main files
tail -n +2 labs/$LAB.csv >> llm_sizes.csv
cat labs/$LAB.notes.md >> RESEARCH_NOTES.md
```

Step-by-step workflow per lab:

1. **Orchestrator** creates `labs/<lab>.csv` (header only) and
   `labs/<lab>.notes.md` (empty / heading only).
2. **`researcher` subagent** is invoked with the `labs/<lab>.*` paths,
   appends rows + notes there. Never touches the main files.
3. **`verifier` subagent(s)** in parallel batches run against the lab
   CSV via `uv run csv-row --csv labs/<lab>.csv <range>`. The verifier
   first diff-checks the lab CSV header against the main CSV header
   (schema conformance) before fact-checking rows.
4. If hard FAILs exist, `researcher` fixup pass on the same lab file
   with the specific list.
5. **Orchestrator** spot-checks anything unfamiliar, especially rows
   where `param_source_note` asserts facts not in either URL column
   (the Mythos + GPT-5.5 failure mode — numbers that read plausible
   but live only in the note).
6. **Orchestrator** merges the lab file into the main CSV + notes
   file (shell snippet above). Keep the lab file around as provenance
   — don't delete it after merge.
7. Update `STATUS.md` completion notes and commit.

Parallelism rules:

- Researchers write only to their own `labs/<lab>.*` files, so any
  number of researchers can run concurrently.
- Verifiers are read-only and can run concurrently with each other
  and with researchers (on different files).
- Merges are orchestrator-only and serialized — do one lab at a time.

## Source-substantiation rule

Non-negotiable, stated in `researcher.md`: every factual claim in a row
(including numbers, architecture, licensing, benchmark figures) must be
supported by `release_url` or `supporting_url`. Anything that is only in
`param_source_note` but not in either cited URL is unverifiable and
should be removed or have its source added. The verifier can only fetch
the two URL columns.
