---
name: debate-topic
description: "Prepare a balanced, evidence-aware debate brief for a clearly stated proposition or contested research question."
metadata:
  source: project
  action: Develop one debate brief.
---

# Debate Topic

## Scope

Primary agent role: argument-agent.

This is an external skill. Use it when the user says `Debate topic
{topic}: {proposition}` or needs a balanced analysis of a contested research question.
It is responsible only for **developing one debate brief**. Its inputs are an
existing topic, proposition or question, relevant context, intended audience, evaluation
criteria, and available evidence or source constraints. It produces one
indexed brief with charitable cases and visible uncertainty. User activation command: `Debate topic {topic}: {proposition}`.

## Workflow

1. Read `docs/plan.md` and
   `../paper-propose/docs/publication-writing-standard.md`.
   Confirm the topic, exact proposition or question, context,
   audience, scope, evaluation criteria, and available evidence. Ask for
   clarification when the proposition is ambiguous, positions cannot be
   distinguished, or the requested conclusion depends on missing criteria.
2. Frame the disagreement precisely: define material terms, identify who bears
   the burden for each claim, and state what evidence or consequences would
   count under the chosen criteria.
3. Construct the strongest reasonable case for each materially distinct
   position. For every key point, separate source-supported premise, inference,
   value judgment, and uncertainty. Include meaningful rebuttals rather than
   caricatures.
4. Test the cases against the stated criteria and evidence, then identify what
   follows, what remains disputed, and what additional evidence would change
   the assessment. Write `knowledge/{topic-slug}/publications/debate-{slug}.md`
   and add a dated, concise entry to that topic's `publications/INFO.md`.
5. Report the created brief, strongest points on each side, criteria-sensitive
   conclusion if any, and residual uncertainty.

## Constraints

- Do not equate balance with equal evidentiary weight, manufacture a false
  two-sided controversy, or hide a conclusion's dependence on chosen values or
  criteria.
- Do not fabricate sources, quotes, opponents, motives, or empirical support.
  Escalate unsafe, ambiguous, or insufficiently bounded propositions.
- Do not write a full paper or update a knowledge topic unless separately
  requested. This is instruction-only; no code or test unit is delegated.
