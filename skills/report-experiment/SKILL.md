---
name: report-experiment
description: Write one evidence-bounded experiment report from a topic experiment plan and catalogued results.
metadata:
  source: project
  action: Report one topic experiment.
---

# Report Experiment

## Scope

Use when the researcher says `Report experiment for {topic}` and identifies a
planned experiment with catalogued results. It receives those records and
produces a topic-local experimental report. Ask for clarification when the
plan, results, target audience, or requested claim scope is unclear.
Primary agent role: experiment-agent.

## Workflow

1. Read `../experiment-plan/docs/experimentation-standard.md`,
   `../writing-refine/docs/scholarly-writing-standard.md`, the experiment plan,
   and result catalog.
2. Structure the report as question, design, materials or data, results,
   interpretation, limitations, and implications.
3. Link every substantive outcome to its catalogued result. Distinguish observed
   findings from inferences and state deviations and validity threats.
4. Write `publications/experimental-report-{slug}.md`, then update the
   publication index, experiment index, and topic `INFO.md`.

## Constraints

- Do not suppress null, conflicting, or inconclusive results.
- Do not add analysis, data, claims, or future-work commitments not supported
  by the plan and result records.

## Dependencies

- `result-catalog`
