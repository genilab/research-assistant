---
name: manage-knowledge-topics
description: Create and maintain evidence-based topic records and references in a Knowledge Worker.
metadata:
  short-description: Maintain topic knowledge and references
---

# Manage Knowledge Topics

Use this skill to add, update, reorganize, or retire knowledge about a topic.

## Create a topic

Choose a specific, lowercase, hyphenated `{topic}` name. Create:

```text
knowledge/{topic}/{topic}_info.md
```

Create `knowledge/{topic}/references/` only when reference material must be
stored. Read `guidelines/knowledge-entries.md` before writing.

Start the info record with the topic name and a short statement of why the
information matters. Organize the remainder around the facts, constraints,
decisions, or context a future reader needs. Include the source, basis, and date
for claims whose accuracy depends on external or time-sensitive information.

## Preserve signal

Synthesize sources instead of pasting them into the information record. Place
supporting files or source notes under `references/` and link them from the
record where helpful. Distinguish confirmed facts from interpretation, proposed
ideas, and open questions. Never invent missing information to fill a template.

Update an existing topic when the subject is the same. If an earlier conclusion
has changed, retain enough context to explain the successor rather than silently
rewriting history. Keep sensitive data out of a shareable repository unless its
inclusion is explicitly authorized.

## Complete the change

Use `create-and-maintain-readme` to add, update, or remove the topic in the root
README master index. Verify that the topic row and its information-record link
match the actual files before reporting the work complete.
