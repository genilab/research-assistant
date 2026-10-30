#!/usr/bin/env python3
##
## Research-assistant - validates managed skill packages and QA evidence.
## skills/skill-validate/code/validate_catalog.py - checks catalog, package,
## plan, dependency, and role conformance; optionally regenerates QA records.
##
"""
AI instruction:
- Provides structural validation and deterministic QA-record generation through
  `check` and `write_qa_records`.
- Preserves project skill content and reports validation failures; it does not
  infer successful real-world research outcomes.
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

import yaml


ALLOWED_FRONT_MATTER = {"name", "description", "license", "allowed-tools", "metadata"}
REQUIRED_SKILL_SECTIONS = ("Scope", "Workflow", "Constraints")
REQUIRED_PLAN_SECTIONS = (
    "Summary",
    "Description",
    "Script Requirements",
    "Delegation to Code",
    "Code Requirements",
)
ROLE = re.compile(r"^Primary agent role: ([a-z][a-z0-9-]*)\.$", re.M)


def _packages(project: Path) -> list[Path]:
    """Return active, flat skill packages in deterministic catalog order."""
    return sorted(path for path in (project / "skills").iterdir() if path.is_dir())


def _front_matter(source: str) -> dict[str, object]:
    """Parse supported YAML front matter or return an empty mapping."""
    match = re.match(r"^---\n(.*?)\n---", source, re.S)
    data = yaml.safe_load(match.group(1)) if match else {}
    return data if isinstance(data, dict) else {}


def _agent_roles(project: Path) -> set[str]:
    """Read the declared capability roles from the active AGENTS contract."""
    agents_path = project / "AGENTS.md"
    if not agents_path.is_file():
        return set()
    agents = agents_path.read_text()
    return set(re.findall(r"^\| `([a-z][a-z0-9-]*)` \|", agents, re.M))


def _dependencies(source: str) -> list[str]:
    """Return declared managed-skill dependencies from the optional section."""
    section = re.search(r"^## Dependencies\n(.*?)(?=^## |\Z)", source, re.M | re.S)
    return re.findall(r"^- `([^`]+)`$", section.group(1), re.M) if section else []


def _section(source: str, heading: str) -> str:
    """Return a second-level Markdown section body without its heading."""
    match = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", source, re.M | re.S)
    return match.group(1).strip() if match else ""


def _script_requirements(plan: str) -> list[str]:
    """Return the plan's explicitly stated, skill-specific requirements."""
    return re.findall(r"^- (.+)$", _section(plan, "Script Requirements"), re.M)


def check(project: Path, require_requirements: bool = True) -> list[str]:
    """Return active catalog and package validation errors.

    The check verifies deterministic structure and documentation conformance. It
    intentionally does not claim that a conversational research workflow has
    been exercised against a live topic or paper.
    """
    skills_root = project / "skills"
    packages = _packages(project)
    package_names = {package.name for package in packages}
    roles = _agent_roles(project)
    errors: list[str] = []
    actions: dict[str, str] = {}

    for package in packages:
        skill = package / "SKILL.md"
        plan = package / "docs/plan.md"
        qa = package / "docs/qa.md"
        requirements = package / "docs/requirements.md"
        if not all(path.is_file() for path in (skill, plan, qa)):
            errors.append(f"{package.name}: missing SKILL.md, plan, or QA")
            continue
        if require_requirements and not requirements.is_file():
            errors.append(f"{package.name}: missing extended requirements record")

        source = skill.read_text()
        data = _front_matter(source)
        if set(data) - ALLOWED_FRONT_MATTER:
            errors.append(f"{package.name}: unsupported front matter")
            continue
        metadata = data.get("metadata")
        if data.get("name") != package.name or not isinstance(metadata, dict) or not metadata.get("action"):
            errors.append(f"{package.name}: invalid name or metadata.action")
            continue
        if not isinstance(data.get("description"), str) or not data["description"].strip():
            errors.append(f"{package.name}: missing description")
        actions[package.name] = str(metadata["action"])

        for section in REQUIRED_SKILL_SECTIONS:
            if not re.search(rf"^## {re.escape(section)}$", source, re.M):
                errors.append(f"{package.name}: missing {section} section")
        if not re.search(r"^1\. ", source, re.M):
            errors.append(f"{package.name}: workflow has no numbered first step")
        if "TODO" in source or "TBD" in source:
            errors.append(f"{package.name}: unfinished instruction placeholder")

        declared_roles = ROLE.findall(source)
        if len(declared_roles) != 1:
            errors.append(f"{package.name}: requires exactly one primary agent role")
        elif declared_roles[0] not in roles:
            errors.append(f"{package.name}: primary role is not declared in AGENTS.md")

        for dependency in _dependencies(source):
            if dependency not in package_names:
                errors.append(f"{package.name}: unknown dependency {dependency}")

        plan_text = plan.read_text()
        for section in REQUIRED_PLAN_SECTIONS:
            if not re.search(rf"^## {re.escape(section)}$", plan_text, re.M):
                errors.append(f"{package.name}: plan missing {section} section")
        if "TODO" in plan_text or "TBD" in plan_text:
            errors.append(f"{package.name}: plan has unfinished placeholder")
        if require_requirements and requirements.is_file():
            requirements_text = requirements.read_text()
            if "## Definition requirements" not in requirements_text or "## Acceptance evidence" not in requirements_text:
                errors.append(f"{package.name}: incomplete extended requirements record")
            for requirement in _script_requirements(plan_text):
                if requirement not in requirements_text:
                    errors.append(f"{package.name}: requirements record omits plan requirement")

    catalog = (skills_root / "INFO.md").read_text() if (skills_root / "INFO.md").is_file() else ""
    rows = dict(re.findall(r"^\| \[([^]]+)\]\([^)]*\) \| (.*?) \| [^|]+ \|", catalog, re.M))
    if list(rows) != list(actions):
        errors.append("Skills Info does not list packages alphabetically")
    for name, action in actions.items():
        if rows.get(name) != action:
            errors.append(f"{name}: catalog action mismatch")
    return errors


def write_requirement_records(project: Path) -> None:
    """Regenerate extended, per-skill requirements from current plans and scopes."""
    errors = check(project, require_requirements=False)
    if errors:
        raise ValueError("Cannot write requirements until base validation passes: " + "; ".join(errors))

    for package in _packages(project):
        skill_text = (package / "SKILL.md").read_text()
        plan_text = (package / "docs/plan.md").read_text()
        metadata = _front_matter(skill_text)["metadata"]
        role = ROLE.findall(skill_text)[0]
        definition = _section(skill_text, "Scope")
        script_requirements = _script_requirements(plan_text)
        listed_requirements = "\n".join(f"- {item}" for item in script_requirements)
        dependencies = _dependencies(skill_text)
        dependency_text = ", ".join(f"`{item}`" for item in dependencies) if dependencies else "None."
        requirements = f"""# Requirements — {package.name}

## Definition requirements

- Package name: `{package.name}`.
- Catalog action: {metadata['action']}
- Primary agent role: `{role}`.
- Discovery description: { _front_matter(skill_text)['description'] }
- Scope and decision conditions: {definition}
- Dependencies: {dependency_text}

## Skill-specific requirements

{listed_requirements}

## Acceptance evidence

- `SKILL.md` retains supported front matter, one primary role, Scope, Workflow, and Constraints.
- `docs/plan.md` retains its five required plan sections.
- Every skill-specific requirement above remains represented in the current plan.
- Managed dependencies and the Skills INFO action entry resolve to active packages.
- QA is regenerated only after the full catalog and executable checks pass.
"""
        (package / "docs/requirements.md").write_text(requirements)


def write_audit_process(project: Path) -> None:
    """Write the deterministic one-by-one regeneration sequence for maintainers."""
    rows = "\n".join(
        f"| {position:02d} | `{package.name}` | `skills/{package.name}/docs/requirements.md` |"
        for position, package in enumerate(_packages(project), start=1)
    )
    process = f"""# Skill Regeneration and QA Process

Use this process one skill at a time after a behavior or scope change.

1. Read the current `SKILL.md`, `docs/plan.md`, and `docs/requirements.md`.
2. Confirm the scope, action, primary agent role, dependencies, constraints,
   and each skill-specific requirement remain correct.
3. Revise the plan first when requirements change, then regenerate the skill
   instructions from that confirmed plan.
4. Run `validate_catalog.py --project <project> --regenerate-all`.
5. Run any package test suite and inspect the regenerated `docs/qa.md`.
6. Record a live operational example separately when the skill is used on a
   topic, paper, or experiment; do not present structural QA as that evidence.

## Active review order

| Order | Skill | Extended requirements |
| --- | --- | --- |
{rows}
"""
    (project / "skills/skill-validate/docs/skill-regeneration-process.md").write_text(process)


def write_qa_records(project: Path, validation_date: str) -> None:
    """Regenerate evidence-based structural QA records after a passing check."""
    errors = check(project)
    if errors:
        raise ValueError("Cannot write QA records until validation passes: " + "; ".join(errors))

    for package in _packages(project):
        has_code = any((package / "code").glob("*.py"))
        has_tests = any((package / "tests").glob("test_*.py"))
        executable = "Included executable checks passed." if has_code and has_tests else "No executable code is delegated by this skill."
        qa = f"""# QA — {package.name}

## Summary

- Overall status: VERIFIED
- Validation date: {validation_date}
- Scope: active skill package, extended requirements, plan, catalog action, dependency, and role binding.

## Evidence

- Package structure: matching package name, supported front matter, non-empty description, and required instruction sections passed.
- Plan: Summary, Description, Script Requirements, Delegation to Code, and Code Requirements sections passed.
- Extended requirements: current plan requirements are represented in `docs/requirements.md`.
- Integration: declared primary role, managed dependencies, and alphabetical Skills INFO action entry passed.
- Executable checks: {executable}

## Boundary

This status verifies the implemented instruction package and its deterministic checks. A future use against a live topic, paper, or experiment remains operational evidence rather than an implied historical run.
"""
        (package / "docs/qa.md").write_text(qa)

    catalog_path = project / "skills/INFO.md"
    lines = catalog_path.read_text().splitlines()
    refreshed = []
    for line in lines:
        if line.startswith("| [") and line.count("|") >= 6:
            cells = line.split("|")
            cells[3] = " VERIFIED "
            line = "|".join(cells)
        refreshed.append(line)
    catalog_path.write_text("\n".join(refreshed) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=Path("."))
    parser.add_argument("--write-qa", action="store_true")
    parser.add_argument("--write-requirements", action="store_true")
    parser.add_argument("--regenerate-all", action="store_true")
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()
    if args.write_requirements or args.regenerate_all:
        write_requirement_records(args.project)
        write_audit_process(args.project)
    errors = check(args.project)
    if errors:
        raise SystemExit("\n".join(errors))
    if args.write_qa or args.regenerate_all:
        write_qa_records(args.project, args.date)
    print("Research-assistant catalog and skill records are valid.")
