---
name: result-catalog
description: Catalog observed experiment results with provenance, conditions, measures, analysis, and interpretation boundaries.
metadata:
  source: project
  action: Catalog one experiment result set.
---

# Catalog Results

## Scope

Use when the researcher says `Catalog results for {topic}` and identifies an
experiment and observed results. It receives the result material and produces a
linked, provenance-aware record. Ask for clarification when the experiment,
source data, conditions, or measurement meaning is unknown.
Primary agent role: experiment-agent.

## Workflow

1. Read the experiment plan and
   `../experiment-plan/docs/experimentation-standard.md`.
2. Record result provenance, conditions, measures, transformations, analysis,
   and observed outcome separately from interpretation.
3. Write `experiments/{experiment-id}-results.md`, update the experiment index
   and topic `INFO.md`, and link any supporting artifact without overwriting it.
4. Identify deviations from the plan, threats to validity, and what remains
   unmeasured. Route reporting to `report-experiment` on request.

## Constraints

- Do not manufacture results, hide exclusions, or treat a result as proof
  beyond the plan's scope.
- Do not alter raw data, execute analysis code, or write a paper here.

## Dependencies

- `report-experiment`
