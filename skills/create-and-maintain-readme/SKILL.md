---
name: create-and-maintain-readme
description: Create or update the external README master index for a topic-based knowledge worker.
metadata:
  short-description: Maintain the knowledge-worker README index
---

# Create and Maintain README

Use this skill whenever the external `README.md` of this Knowledge Worker is
created or changed. Its purpose is to orient a reader and provide the canonical
master index of knowledge topics; it is not a copy of every topic record.

## Compose the README

Open with a short description of what this knowledge base contains, who or what
it serves when known, and why its organization is useful. Write for a reader
who has not seen the repository before. Do not claim a purpose, audience, or
coverage that is not supported by the stored knowledge.

Follow the description with one `Knowledge topics` table. Use these columns:

| Topic | Description | Information record |
| --- | --- | --- |

Each row links to `knowledge/{topic}/{topic}_info.md` and describes the topic
in one factual sentence or phrase. Order topics alphabetically unless another
order makes their relationship materially clearer. Do not list topic folders
that lack their required info record.

## Reconcile the index

Before editing, inspect the `knowledge/` directory and its topic records. On a
new topic, add a row; on a rename or removal, update or remove its row in the
same change. Check every relative link. If no topic exists yet, retain a clear
empty-state row rather than inventing an example.

Keep contribution guidance brief and point readers to `AGENTS.md`, the relevant
guideline, and the topic-management skill. Do not turn the README into a
requirements ledger, implementation plan, or uncurated link collection.
