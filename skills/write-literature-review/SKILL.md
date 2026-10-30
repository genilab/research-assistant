---
name: write-literature-review
description: "Structure and draft a topic-specific literature review using the shared publication writing guide."
metadata:
  source: project
  action: Write one topic-specific literature review.
---

# Write Literature Review

## Scope

Primary agent role: writing-agent.

This is an external skill. Use it when the user says `Write literature review
for {topic}` or asks to structure or draft a review for one topic. It is
responsible only for **writing one topic-specific Literature Review**. Its
inputs are an existing topic, review question, identified corpus or selection
method, comparison dimensions, intended audience, and draft scope. It produces
one indexed file in that topic's `publications/` folder. User activation command: `Write literature review for {topic}`.

## Workflow

1. Read `docs/plan.md` and
   `../paper-propose/docs/publication-writing-standard.md`.
   Locate the topic and its `publications/INFO.md`. Ask for clarification when
   the review question, corpus boundary, selection method, or topic is missing.
2. Build a source inventory from the topic refs record and supplied corpus.
   Invoke `analyze-literature` when a comparative analysis is needed before
   drafting; never imply systematic-review coverage without a real search and
   inclusion method.
3. Structure the paper as: Abstract; Review Question and Scope; Corpus and
   Selection Method; Conceptual or Theoretical Landscape; Comparative Findings;
   Agreements and Disagreements; Gaps and Research Agenda; Limitations;
   Implications; References. Distinguish quoted/source conclusions from the
   review's own synthesis.
4. Write `knowledge/{topic-slug}/publications/literature-review-{slug}.md` and
   add a dated index entry with type, status, corpus note, and link. Use
   `maintain-paper-section` only for a later scoped revision.
5. Report the paper path, corpus coverage, central synthesis, and limitations
   that prevent a stronger conclusion.

## Constraints

- The shared guide is mandatory; the required Literature Review sections extend
  its document-control, source, uncertainty, and index rules.
- Do not fabricate study methods, citations, effect sizes, or consensus; do not
  count sources as proof or claim systematic coverage without evidence.
- Do not write a Vision or Positioning Paper, alter original source files, or
  create a missing topic. This is instruction-only; no code or test unit is
  delegated.

## Dependencies

- `analyze-literature`
- `maintain-paper-section`
