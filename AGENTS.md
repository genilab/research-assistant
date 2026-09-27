# Knowledge Worker

This repository is a Knowledge Worker: it maintains durable, topic-based
knowledge that can be discovered through the root `README.md` master index.

## Operating model

1. Read the master index, the applicable guideline, and the relevant skill
   before creating or changing a knowledge record.
2. Store each topic at `knowledge/{topic}/` using a lowercase, hyphenated topic
   name.
3. Keep the topic's current, synthesized information in
   `knowledge/{topic}/{topic}_info.md`.
4. Store supporting material in `knowledge/{topic}/references/`. Do not put
   the source content in the info record when a concise summary and a reference
   will do.
5. Add or update the row for every topic in the root `README.md` master index.
   The index must include a plain description of the knowledge base before its
   topics table.

## Required records

Every topic info record identifies its topic, the information it contains, the
source or basis for time-sensitive claims, and any important uncertainty. Keep
facts, interpretations, and open questions distinct. Preserve useful history
by linking to superseding information instead of silently losing the rationale.

## Skills

- `skills/create-and-maintain-readme/SKILL.md` governs the external README and
  its master topics index.
- `skills/manage-knowledge-topics/SKILL.md` governs topic records and their
  references.

Keep this worker lean: do not introduce product plans, QA ledgers, module
indexes, or unrelated runtime tooling unless explicitly requested.
