# AGENTS

This file explains how Codex and any supporting agents should work on ROS AI Debugger.

## Operating Rules

- Use required skills automatically when a task calls for them.
- Follow the phase and sub-phase structure in `PLANS.md` and `docs/project_memory.md`.
- Do not skip phases.
- Work on the requested phase or sub-phase only.
- Do not implement backend code before Phase 2.
- Do not implement frontend code before Phase 3.
- Keep the project beginner-friendly and Windows-development friendly.
- Update `docs/project_memory.md` at the end of every phase and sub-phase.

## Agent Strategy

Codex can create specialized agents when useful for larger work:

- Architecture agents for system design, API boundaries, and data flow.
- Backend agents for FastAPI, analyzer logic, and backend tests.
- Frontend agents for React UI, API integration, and user flows.
- Testing agents for fixtures, regression tests, and validation.
- Documentation agents for README files, architecture docs, examples, and beginner-friendly explanations.

Agents should have clear ownership of files or responsibilities and should not overwrite unrelated work.

## Memory And Progress

`docs/project_memory.md` is the source of truth for project progress.

Before starting work:

- Read `docs/project_memory.md`.
- Read relevant planning docs.
- Confirm the current phase and sub-phase.

After finishing work:

- Update completed work.
- Update pending work.
- Update known issues.
- Update GitHub status when relevant.
- Set the next recommended action.

## GitHub Workflow

- Commit after each completed sub-phase.
- Push after meaningful milestones.
- Tag releases and major milestones.
- Keep commits focused and easy to understand.

