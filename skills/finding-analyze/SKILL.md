---
name: finding-analyze
description: Analyze catalogued experimental findings against their plan, measures, validity limits, and research claim.
metadata:
  source: project
  action: Analyze one experiment finding set.
---

# Analyze Findings

## Scope

Use when the researcher says `Analyze findings for {topic}` and identifies an
experiment plan and catalogued result set. It receives those records and
produces a bounded interpretation with claim alignment, alternative
explanations, and validity limits. Ask for clarification when the plan, result
provenance, measures, or target claim is missing.
Primary agent role: experiment-agent.

## Workflow

1. Read the experiment plan, result catalog, and
   `../experiment-plan/docs/experimentation-standard.md`.
2. Compare observations with the planned question, baseline, measures, and
   decision rule; identify deviations and unmeasured conditions.
3. Separate observations, supported inference, alternative explanation, and
   open question. State validity and scope limits.
4. Append the analysis to the result record, update the experiment index and
   topic INFO, and route requested prose to `report-experiment` or
   `results-paper`.

## Constraints

- Do not run code, alter data, fabricate significance, or claim causal support
  beyond the design and catalogued evidence.
- Do not write a report or results paper outside its dedicated workflow.

## Dependencies

- `result-catalog`
- `report-experiment`
