# Skill Plan — debate-topic

## Summary

This external skill performs **development of one debate brief**.

## Description

This external skill exists to help the user reason fairly about a bounded
contested proposition. It frames the disagreement, steelmans meaningful
positions, evaluates them against declared criteria and evidence, and makes
residual uncertainty visible. Activation: `Debate topic {proposition}`.
Workflow skills: None.

Complete this plan before authoring the final `SKILL.md`, code, or test units;
use its requirements and code-delegation instructions as their source of truth.

## Script Requirements

- It must require an existing topic, proposition/question, context, audience, evidence or source
  constraints, and evaluation criteria; unclear framing or criteria triggers
  clarification.
- It must separate evidence-supported premises, inference, value judgment, and
  uncertainty while presenting charitable cases and substantive rebuttals.
- It must apply the shared publication guide and create/index
  `knowledge/{topic-slug}/publications/debate-{slug}.md`, recording the
  criteria that condition any conclusion and the evidence that would update it.
- It must reject false balance and fabricated support while preserving material
  uncertainty.
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Delegation to Code

- No code is delegated because fair argument construction and evidence
  evaluation require judgment. Introduce code only for future deterministic,
  demonstrated reporting needs.

## Code Requirements

N/A
