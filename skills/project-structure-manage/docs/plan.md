# Plan

## Summary

Create or reconcile one confirmed agent-worker project structure through a
single safe workflow.

## Description

This skill replaces the separate structure-creation and structure-maintenance
workflows. It first establishes whether the target structure is absent or
already present, then creates missing approved elements or reconciles existing
navigation without overwriting material.

## Script Requirements

- It must confirm project identity, role, required structure, and external
  README need before changing a target.
- It must create required folders, `AGENTS.md`, and main and local `INFO.md`
  documents when the target structure is absent.
- It must reconcile missing required elements and stale navigation when the
  target structure exists.
- It must preserve unexpected or conflicting material and report it rather
  than deleting or overwriting it.
- It must distinguish permanent project structure from temporary migration
  material.

## Delegation to Code

No code is delegated. Structure decisions require project-specific inspection
and human confirmation when a conflict exists.

## Code Requirements

No deterministic code or test unit is required for this instruction-only
workflow.
