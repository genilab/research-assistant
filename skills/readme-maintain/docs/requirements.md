# Requirements — readme-maintain

## Definition requirements

- Package name: `readme-maintain`.
- Catalog action: Maintain external GitHub documentation when required.
- Primary agent role: `publication-agent`.
- Discovery description: Create or refresh an accurate root README when an external project or an explicit request requires user-facing documentation.
- Scope and decision conditions: This is an internal skill. Use it when the project's `AGENTS.md` declares a
README profile or the user directly requests a README. It selects either the
public-release or private-repository template and maintains only the root
document. Its inputs are the declared visibility/profile, approved project
identity, verified implementation evidence, existing README, and available
assets. It produces an accurate README or a clear gap report. It has no user
activation command; a calling workflow invokes it.
Primary agent role: publication-agent.
- Dependencies: None.

## Skill-specific requirements

- It must read repository visibility and README profile from `AGENTS.md`
- It must select the public-release or private-repository template without
- It must generate public-release README content in this order: title,
- It must reserve infographics for an approved generation process and use only
- It must maintain the root README automatically for a development project with full publication and leave an application project unchanged unless directly requested.
- It must collect composition evidence from the project plan, architecture, release and roadmap records, module requirements, QA, existing README, and available assets, preserving accurate existing content.
- It must use the plan's Title, Tagline, Core Proposition, and Key Ideas; verified architecture and requirements; QA-backed claims; and real assets to compose the infographic, banners, What is, Why, optional Key Ideas, Getting Started, and Examples layout.
- It must ask the embedded audience, setup, example, public-capability, visual-asset, and support/contribution/license questions when the maintained records do not supply a required user-facing fact.
- It must create or refresh the README when a full-publication development project is created or receives a direct request, and it must never infer that an application is safe to publish.
- It must report unavailable required facts or assets instead of fabricating content.

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
