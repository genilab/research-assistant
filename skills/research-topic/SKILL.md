---
name: research-topic
description: "Research a focused topic and preserve a source-aware synthesis in the knowledge base."
metadata:
  source: project
  action: Research one focused knowledge topic.
---

# Research Topic

## Scope

Primary agent role: research-agent.

This is an external skill. Use it when the user says `Research topic {topic}`
or requests a focused, durable investigation. It is responsible only for
**researching one focused knowledge topic**. Its inputs are a topic, a question
or angle, an optional source set or research constraints, and an intended
depth. It produces an attributed synthesis in one knowledge topic, with sources
and open questions preserved. User activation command: `Research topic {topic}`.

## Workflow

1. Read `docs/plan.md`; identify the research question, scope, source
   constraints, and desired depth. Ask for clarification when the topic or
   question is too broad to research responsibly, the intended scope conflicts,
   or a required source restriction is absent.
2. Locate the topic. If it does not exist, invoke `topic-create` before doing
   research. Retain the established topic schema rather than creating a second
   research store.
3. Use the supplied corpus or, when the request calls for external research,
   gather traceable sources appropriate to the question. Prefer primary sources
   and original research where they are available; record enough citation or
   URL detail to revisit every source. Do not imply that search ranking proves
   quality.
4. Evaluate relevance, source type, date, and material limitations. Use
   `info-learn` to preserve the sources and concise, attributed learning in the
   topic. Put interpretations, hypotheses, conflicts, and unanswered questions
   in the ideas record rather than presenting them as established facts.
5. Report the topic updated, sources added, central findings, limitations, and
   a small set of next questions. State when the result is a preliminary scan
   rather than a comprehensive review.

## Constraints

- Do not turn a broad topic request into an unbounded literature review; agree
  on a focused question or a bounded scan when necessary.
- Do not manufacture citations, copy source claims without attribution, or
  treat an interpretation as a verified finding.
- Do not write a literature analysis, paper, or debate brief in this workflow;
  those are separate skills. Do not overwrite supplied source files or prior
  topic learning.
- This is an instruction-only skill: no deterministic code or test unit is
  delegated. Keep the completed plan and QA evidence in `docs/`.

## Dependencies

- `topic-create`
- `info-learn`
