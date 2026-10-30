# Skill Plan — write-literature-review

## Summary

This external skill performs **writing one topic-specific Literature Review**.

## Description

This external skill exists to produce a comparative, limitation-aware review
for one existing topic. It applies the shared publication guide, records corpus
boundaries, follows the Literature Review section structure, and writes an
indexed topic-local publication. Activation: `Write literature review for
{topic}`. Workflow skills: `analyze-literature`, `maintain-paper-section`.

Complete this plan before authoring the final `SKILL.md`, code, or test units;
use its requirements and code-delegation instructions as their source of truth.

## Script Requirements

- It must require an existing topic, review question, source corpus or
  selection method, comparison dimensions, audience, and draft scope; missing
  corpus boundaries trigger clarification.
- It must apply `paper-propose/docs/publication-writing-standard.md` and write the
  required Literature Review sections: scope, method, landscape, comparative
  findings, disagreement, gaps, limitations, implications, and references.
- It must create and index a `literature-review-{slug}.md` file in the topic's
  publications folder and distinguish source claims from synthesis.
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Delegation to Code

- No code is delegated because corpus evaluation and synthesis require
  judgment. Add deterministic support only for a stable repeated operation.

## Code Requirements

N/A
