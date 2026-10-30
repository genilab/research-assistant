---
name: write-vision-paper
description: "Structure and draft a topic-specific vision paper using the shared publication writing guide."
metadata:
  source: project
  action: Write one topic-specific vision paper.
---

# Write Vision Paper

## Scope

Primary agent role: writing-agent.

This is an external skill. Use it when the user says `Write vision paper for
{topic}` or asks to structure or draft one topic's future-oriented paper. It
is responsible only for **writing one topic-specific Vision Paper**. Its inputs
are an existing topic, working title, intended audience, future horizon,
central vision or question, available evidence, and draft scope. It produces
one indexed file in that topic's `publications/` folder. User activation command: `Write vision paper for {topic}`.

## Workflow

1. Read `docs/plan.md` and
   `../paper-propose/docs/publication-writing-standard.md`.
   Locate the topic and its `publications/INFO.md`. Ask for clarification when
   the topic is missing, the intended audience or horizon is absent, or the
   request treats a speculative forecast as a confirmed finding.
2. Set the document controls required by the shared guide. Use the topic's
   references, information, and ideas records to distinguish evidence from the
   proposed vision.
3. Structure the paper as: Executive Summary; Context and Drivers; Vision
   Statement; Future State or Scenarios; Enabling Capabilities and Pathways;
   Assumptions and Evidence; Risks, Trade-offs, and Ethics; Indicators and Next
   Steps; References. Draft only the requested scope, marking unsupported
   content as an assumption, proposal, or open question.
4. Write `knowledge/{topic-slug}/publications/vision-paper-{slug}.md` and add
   a dated index entry with type, status, purpose, and link. Use
   `maintain-paper-section` only for a later scoped revision.
5. Report the paper path, status, evidence used, material assumptions, and the
   most important unresolved decision.

## Constraints

- The shared guide is mandatory; the required Vision Paper sections extend its
  document-control, source, uncertainty, and index rules.
- Do not manufacture forecasts, citations, stakeholder agreement, or a roadmap
  commitment. Do not convert an idea record into established information.
- Do not write a Literature Review or Positioning Paper, modify source files,
  or create a missing topic. This is instruction-only; no code or test unit is
  delegated.

## Dependencies

- `maintain-paper-section`
