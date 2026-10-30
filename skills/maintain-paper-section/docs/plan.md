# Skill Plan — maintain-paper-section

## Summary

This external skill performs **maintenance of one named paper section**.

## Description

This external skill exists to make one bounded, evidence-aware revision inside
an existing paper. It first confirms the exact target and surrounding argument,
then makes the smallest coherent revision and surfaces unresolved support.
Activation: `Maintain paper section {paper}: {section}`. Workflow skills: None.

Complete this plan before authoring the final `SKILL.md`, code, or test units;
use its requirements and code-delegation instructions as their source of truth.

## Script Requirements

- It must require an existing topic, paper path, named section, requested change, approved
  evidence, and applicable style/word constraints; missing targets or support
  trigger clarification.
- It must inspect the surrounding argument, preserve source/citation markers,
  and limit prose changes to the named section.
- It must apply the shared publication guide, report the section changed,
  evidence used, and unresolved factual or editorial issues; it must keep the
  topic publication index accurate.
- It must not change the central thesis or unrelated sections without a new,
  explicit request.
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Delegation to Code

- No code is delegated because interpreting prose, argument, and source support
  requires judgment. Add deterministic tooling only if a repeated mechanical
  operation becomes well-defined.

## Code Requirements

N/A
