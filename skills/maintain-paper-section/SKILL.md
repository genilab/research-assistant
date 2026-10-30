---
name: maintain-paper-section
description: "Draft or revise one named paper section while preserving the existing argument and source boundaries."
metadata:
  source: project
  action: Maintain one named paper section.
---

# Maintain Paper Section

## Scope

Primary agent role: writing-agent.

This is an external skill. Use it when the user says `Maintain paper section
{topic}: {paper}: {section}` or asks to draft or revise a named section of an existing
paper. It is responsible only for **maintaining one named paper section**. Its
inputs are an existing topic, existing paper path, section identity, requested change, and
approved evidence or style constraints. It produces a scoped revision and a
summary of unresolved support issues. User activation command: `Maintain paper section {topic}: {paper}: {section}`.

## Workflow

1. Read `docs/plan.md` and
   `../paper-propose/docs/publication-writing-standard.md`.
   Confirm the topic, paper path, exact section, requested
   change, approved evidence, and style or word constraints. Ask for
   clarification when the target section cannot be identified or a new claim
   lacks a source or explicit user authorization as a provisional argument.
2. Read the surrounding structure before editing so the section continues to
   serve the paper's stated argument. Preserve source markers, quotations,
   citation style, and explicit uncertainty.
3. Make the smallest coherent revision that addresses the request. Draft new
   prose only for the named section; distinguish direct evidence, paraphrase,
   analysis, and proposed wording. Flag claims requiring verification instead
   of making their support appear settled.
4. Preserve the paper in `knowledge/{topic-slug}/publications/` and update its
   local index entry only if its title, location, or description changes. Report
   the exact section changed, evidence used, and open support or editorial
   questions.

## Constraints

- Do not edit a different section, restructure the whole paper, alter a source,
  or silently convert a provisional idea into a sourced claim.
- Do not invent quotations, citations, data, or authorial intent. Escalate
  missing evidence, ambiguous scope, or a request that changes the paper's
  central thesis.
- Do not create an outline or literature review in this workflow. This is
  instruction-only; no code or test unit is delegated.
