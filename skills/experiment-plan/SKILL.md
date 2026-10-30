---
name: experiment-plan
description: Design one topic-local experiment with a testable question, method, measures, validity checks, and decision conditions.
metadata:
  source: project
  action: Plan one topic experiment.
---

# Plan Experiment

## Scope

Use when the researcher says `Plan experiment for {topic}` and supplies a
research question, claim, or decision to test. It receives the topic and
available constraints, then produces an experiment plan. Ask for clarification
when the question, comparison, measure, available materials, or ethical scope
is insufficiently defined.
Primary agent role: experiment-agent.

## Workflow

1. Read `docs/experimentation-standard.md`, topic ideas, and relevant evidence.
2. Define the question, hypothesis or claim, baseline, materials or data,
   variables, measures, procedure, analysis plan, and decision rule.
3. Record validity threats, limitations, ethical or operational constraints,
   and conditions for stopping or revising the plan.
4. Write `experiments/{experiment-id}-plan.md`, add a dated index entry, and
   update topic `INFO.md` with the linked experiment status.
5. Route observed output to `result-catalog`; do not report anticipated results.

## Constraints

- Do not invent data access, approval, feasibility, or expected findings.
- Do not execute an experiment, alter data, or write a result report here.

## Dependencies

- `result-catalog`
