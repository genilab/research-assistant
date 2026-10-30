---
name: write-positioning-paper
description: "Structure and draft a topic-specific positioning paper using the shared publication writing guide."
metadata:
  source: project
  action: Write one topic-specific positioning paper.
---

# Write Positioning Paper

## Scope

Primary agent role: writing-agent.

This is an external skill. Use it when the user says `Write positioning paper
for {topic}` or asks to structure or draft a defensible position for one topic.
It is responsible only for **writing one topic-specific Positioning Paper**.
Its inputs are an existing topic, a bounded position or question, intended
audience, decision context, evidence, material alternatives, and draft scope.
It produces one indexed file in that topic's `publications/` folder. User activation command: `Write positioning paper for {topic}`.

## Workflow

1. Read `docs/plan.md` and
   `../paper-propose/docs/publication-writing-standard.md`.
   Locate the topic and its `publications/INFO.md`. Ask for clarification when
   the proposed position, decision context, audience, alternatives, or topic is
   missing.
2. Set the document controls required by the shared guide. Identify the thesis,
   its burden of proof, material alternatives, and criteria for assessment.
3. Structure the paper as: Executive Summary; Context and Decision; Position
   Statement; Premises and Evidence; Alternatives and Counterarguments;
   Assessment Against Criteria; Implications and Boundaries; Limitations and
   Open Questions; References. Mark value judgments, proposals, and empirical
   inferences distinctly.
4. Write `knowledge/{topic-slug}/publications/positioning-paper-{slug}.md` and
   add a dated index entry with type, status, purpose, and link. Use
   `maintain-paper-section` only for a later scoped revision.
5. Report the paper path, position, supporting evidence, counterarguments, and
   remaining decision or evidence dependency.

## Constraints

- The shared guide is mandatory; the required Positioning Paper sections extend
  its document-control, source, uncertainty, and index rules.
- Do not present advocacy as evidence, conceal material alternatives, invent
  sources, or claim that a value judgment is empirically settled.
- Do not write a Vision or Literature Review, alter source material, or create
  a missing topic. This is instruction-only; no code or test unit is delegated.

## Dependencies

- `maintain-paper-section`
