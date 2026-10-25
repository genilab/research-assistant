---
name: readme-maintain
description: Create or refresh an accurate root README when an external project or an explicit request requires user-facing documentation.
metadata:
  source: core
  action: Maintain external GitHub documentation when required.
---

# Maintain Readme

## Scope

This is an internal skill. Use it only when an external GitHub repository
requires a README or a user directly requests one. For Knowledge-worker, use
the defined minimal README format: one purpose paragraph and a Topics table
maintained by `knowledge-base-maintain`. It is responsible only for that
external-facing root document. Its inputs are the approved public project
identity, verified implementation evidence, existing README, and available
assets. It produces an accurate README or a clear gap report. It has no user
activation command; a calling workflow invokes it.

## Workflow

1. Confirm that external documentation is required and identify the public
   audience and publication boundary. Otherwise, use `INFO.md` for internal
   navigation and do not create a README.
2. Use approved public identity, verified capabilities, validation evidence,
   real assets, and accurate existing README material. Do not expose private
   operating details or planned capabilities as present facts.
3. For Knowledge-worker, retain only the project title, one verified purpose
   paragraph, and the Topics table. For another project, compose only the
   externally useful layout supported by verified evidence.
4. Ask for clarification with these questions for any material gap before creating the affected section: “Who is the intended reader and what outcome do they need?”; “What is the shortest verified setup path, including prerequisites, command, and expected result?”; “Which real example best demonstrates the result, including input and output?”; “Which capabilities, limitations, or integrations are safe to state publicly?”; “Is there an approved infographic or banner asset, and what does it depict?”; “Which support, contribution, license, or release information should be linked?” Do not infer an answer from a planned or unverified capability.
5. Produce the updated README and a concise gap report for any unanswered question or unavailable required asset.

## Constraints

- Do not invent setup steps, capabilities, integrations, support channels, banners, or release claims.
- Preserve accurate existing material and use only real assets. If the infographic is required but unavailable, report the gap rather than adding a broken reference.
- Non-goals include using README as an internal info, exposing private
 information, and changing implementation, plans, or release evidence.
