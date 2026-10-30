---
name: structure-paper
description: "Design an evidence-aware paper structure before drafting when a research argument needs a defensible outline."
metadata:
  source: project
  action: Create one paper structure.
---

# Structure Paper

## Scope

Primary agent role: writing-agent.

This is an external skill. Use it when the user says `Structure paper for {topic}: {title}`
or asks for a research paper outline before drafting. It is responsible only for
**creating one paper structure**. Its inputs are an existing topic, title or working title,
research question or thesis, intended audience or format, available evidence,
and constraints. It produces an indexed argument map and section outline; it
does not draft the paper itself. User activation command: `Structure paper for {topic}: {title}`.

## Workflow

1. Read `docs/plan.md` and
   `../paper-propose/docs/publication-writing-standard.md`.
   Confirm the topic, working title, question or provisional
   thesis, audience or required format, word or section constraints, and
   available evidence. Ask for clarification when the core question, intended
   argument, or deliverable constraints are missing.
2. Identify the central claim and the burden of proof. If the thesis is still
   exploratory, represent it as a question or provisional claim rather than
   manufacturing a conclusion.
3. Build a sectioned argument map. For each section, state its purpose, claim
   or question, required evidence, relationship to adjacent sections, and
   known caveat or open dependency. Include counterargument placement when it
   materially affects the argument.
4. Write `knowledge/{topic-slug}/publications/{paper-slug}-outline.md` with
   document controls, the brief, argument map, section outline, evidence gaps,
   and next drafting decisions. Add a dated, concise entry to that topic's
   `publications/INFO.md`.
5. Report the created outline and name the unresolved thesis, evidence, or
   format decisions that block a stronger paper plan.

## Constraints

- Do not draft body prose, fabricate evidence, or make citation claims for
  unavailable sources. Evidence needs are explicit placeholders, not support.
- Do not equate an outline with a publication-ready paper or silently choose a
  contested thesis for the user.
- Do not edit an existing paper in this workflow; use `maintain-paper-section`
  for that. This is instruction-only; no code or test unit is delegated.
