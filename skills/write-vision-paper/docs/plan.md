# Skill Plan — write-vision-paper

## Summary

This external skill performs **writing one topic-specific Vision Paper**.

## Description

This external skill exists to create a future-oriented, evidence-aware paper
for one existing topic. It applies the shared publication guide, makes
assumptions and uncertainty visible, follows the Vision Paper section
structure, and writes an indexed topic-local publication. Activation: `Write
vision paper for {topic}`. Workflow skills: `maintain-paper-section`.

Complete this plan before authoring the final `SKILL.md`, code, or test units;
use its requirements and code-delegation instructions as their source of truth.

## Script Requirements

- It must require an existing topic, audience, horizon, vision/question,
  evidence, and draft scope; missing or falsely certain inputs trigger
  clarification.
- It must apply `paper-propose/docs/publication-writing-standard.md` and write the
  required Vision Paper sections: summary, drivers, vision, scenarios,
  capabilities, evidence, risks, indicators, and references.
- It must create and index a `vision-paper-{slug}.md` file in the topic's
  publications folder and distinguish evidence from proposals and assumptions.
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Delegation to Code

- No code is delegated because research synthesis and future framing require
  judgment. Add deterministic support only if actual use establishes a stable
  repeated operation.

## Code Requirements

N/A
