# Skill Plan — write-positioning-paper

## Summary

This external skill performs **writing one topic-specific Positioning Paper**.

## Description

This external skill exists to make a transparent, evidence-aware case for one
bounded position in an existing topic. It applies the shared publication guide,
states alternatives and criteria, follows the Positioning Paper section
structure, and writes an indexed topic-local publication. Activation: `Write
positioning paper for {topic}`. Workflow skills: `maintain-paper-section`.

Complete this plan before authoring the final `SKILL.md`, code, or test units;
use its requirements and code-delegation instructions as their source of truth.

## Script Requirements

- It must require an existing topic, position/question, audience, decision
  context, evidence, alternatives, and draft scope; missing decision framing
  or counterpositions triggers clarification.
- It must apply `paper-propose/docs/publication-writing-standard.md` and write the
  required Positioning Paper sections: summary, context, position, evidence,
  alternatives, criteria, implications, limitations, and references.
- It must create and index a `positioning-paper-{slug}.md` file in the topic's
  publications folder and distinguish evidence, inference, and value judgment.
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Delegation to Code

- No code is delegated because argumentative framing and evidence evaluation
  require judgment. Add deterministic support only for a stable repeated
  operation.

## Code Requirements

N/A
