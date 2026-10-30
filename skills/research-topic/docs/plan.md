# Skill Plan — research-topic

## Summary

This external skill performs **researching one focused knowledge topic**.

## Description

This external skill exists to research one focused question or bounded scan and
retain the result in the durable topic record. It creates a missing topic,
assesses supplied or externally gathered sources for relevance and limitations,
and routes sources, attributed synthesis, and open questions to their proper
topic records. Activation: `Research topic {topic}`. Workflow skills:
`create-topic`, `learn-info`.

Complete this plan before authoring the final `SKILL.md`, code, or test units;
use its requirements and code-delegation instructions as their source of truth.

## Script Requirements

- It must accept a topic, focused question or angle, optional source set or
  constraints, and desired depth; it must produce a traceable topic update and
  concise outcome summary.
- It must create a missing topic through `create-topic`, and use `learn-info`
  to retain citations, source-aware learning, interpretations, and questions.
- It must ask for a narrower question or missing constraint when responsible
  research scope cannot otherwise be determined.
- It must preserve the distinction between source evidence, synthesis, and
  exploratory ideas; it must identify material limitations.
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Delegation to Code

- No code is delegated because source evaluation, research scoping, and
  synthesis require research judgment. Delegate only repeated deterministic
  citation or filing mechanics if they later emerge from actual use.

## Code Requirements

N/A
