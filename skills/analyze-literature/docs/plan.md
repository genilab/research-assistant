# Skill Plan — analyze-literature

## Summary

This external skill performs **analysis of one defined literature corpus**.

## Description

This external skill exists to answer a stated research question by comparing a
known corpus, rather than merely summarizing isolated sources. It inventories
sources, compares claims and evidence basis, makes convergence and uncertainty
visible, and writes an indexed literature analysis. Activation: `Analyze
literature for {question}`. Workflow skills: None.

Complete this plan before authoring the final `SKILL.md`, code, or test units;
use its requirements and code-delegation instructions as their source of truth.

## Script Requirements

- It must require an existing topic, question, source corpus, and intended analysis depth;
  missing corpus or scope information triggers clarification.
- It must inventory source identity, type, relevant method/evidence basis, and
  limitations when available, then compare rather than count or paraphrase.
- It must apply the shared publication guide, write
  `knowledge/{topic-slug}/publications/literature-analysis-{slug}.md`, and
  index it locally.
- It must distinguish source claims, analysis inference, evidence gaps, and
  residual disagreement.
- It must use the authoritative minimal skill format: state its trigger, bounded responsibility, inputs, expected outcome, clarification conditions, and non-goals within Scope, Workflow, and Constraints.
- It must maintain the instruction script and only the supporting artifacts needed for the operation.

## Delegation to Code

- No code is delegated because corpus evaluation and analytical synthesis
  require judgment. Add deterministic support only for a repeated, stable
  reporting operation demonstrated by use.

## Code Requirements

N/A
