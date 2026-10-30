# Skill Plan — structure-paper

## Summary

This external skill performs **creation of one paper structure**.

## Description

This external skill exists to turn a bounded research question or provisional
thesis into a defensible, evidence-aware outline. It maps claims, evidence,
sections, dependencies, and caveats before prose drafting begins. Activation:
`Structure paper {title}`. Workflow skills: None.

Complete this plan before authoring the final `SKILL.md`, code, or test units;
use its requirements and code-delegation instructions as their source of truth.

## Script Requirements

- It must accept an existing topic, title, question or thesis, audience/format, available
  evidence, and constraints; missing material inputs trigger clarification.
- It must express each section's purpose, claim/question, evidence need,
  relationship to the argument, and caveat or dependency.
- It must apply the shared publication guide and create/index
  `knowledge/{topic-slug}/publications/{paper-slug}-outline.md` without
  drafting paper prose or inventing support.
- It must make the status of a provisional thesis and unresolved evidence
  visible.
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Delegation to Code

- No code is delegated because argument design depends on research and writing
  judgment. Only a repeated deterministic template operation may justify code
  later.

## Code Requirements

N/A
