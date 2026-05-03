# AGENTS

## 1. Project Identity

- Name: ROS AI Debugger
- Purpose: AI-assisted debugging for ROS and ROS 2 systems.
- MVP 1 approach: software-first, text-based analysis, no robot hardware required.

ROS AI Debugger helps users understand ROS errors from pasted terminal output and uploaded files such as logs, launch files, `package.xml`, `CMakeLists.txt`, YAML, Python, and C++ files.

## 2. Global Rules

- Always read `docs/project_memory.md` before starting work.
- Always follow the phase and sub-phase structure in `PLANS.md` and `docs/project_memory.md`.
- Do not skip ahead to later phases.
- Work only on the current requested phase or sub-phase.
- Update `docs/project_memory.md` at the end of every phase and sub-phase.
- Do not implement backend code unless the current phase asks for backend implementation.
- Do not implement frontend code unless the current phase asks for frontend implementation.
- Keep all documentation and user-facing language beginner-friendly.
- Keep MVP 1 small, realistic, and focused on text-based ROS debugging.
- Use required skills automatically when a task calls for them.
- Ask before making large implementation changes that are outside the active phase.
- Whenever behavior is added or changed, document exact commands for beginners to run, test, and verify it.

## 3. Agent Roles

Codex may create specialized agents when useful for larger tasks. Agents must have clear ownership and must not overwrite unrelated work.

### Planning Agent

- Responsibility: Define scope, phase plans, acceptance criteria, and project sequencing.
- Use when: Creating or revising roadmap, scope, milestones, or release plans.
- May edit:
  - `PLANS.md`
  - `docs/project_plan.md`
  - `docs/mvp_scope.md`
  - `docs/project_memory.md`
- Avoid editing unless necessary:
  - Backend source files.
  - Frontend source files.
  - Test implementation files.

### Architecture Agent

- Responsibility: Design system boundaries, data flow, API shape, analyzer pipeline, and module responsibilities.
- Use when: Creating or changing architecture docs or making major backend/frontend design decisions.
- May edit:
  - `docs/system_architecture.md`
  - `docs/project_plan.md`
  - `docs/project_memory.md`
- Avoid editing unless necessary:
  - Frontend UI files.
  - Analyzer implementation files.
  - Test fixtures.

### ROS Taxonomy Agent

- Responsibility: Define ROS error categories, detection patterns, root causes, fixes, verification commands, and confidence rules.
- Use when: Adding or changing analyzer categories, rule definitions, examples, or ROS debugging guidance.
- May edit:
  - `docs/ros_error_taxonomy.md`
  - `examples/`
  - Future analyzer rule files during backend phases.
  - `docs/project_memory.md`
- Avoid editing unless necessary:
  - Frontend source files.
  - GitHub workflow docs.
  - General project planning docs.

### Backend Agent

- Responsibility: Implement FastAPI routes, request models, response models, input handling, file parsing, analyzer orchestration, rule-based detection, AI abstraction, and backend tests.
- Use when: Current phase is Phase 2 or another explicitly approved backend implementation phase.
- May edit:
  - `backend/`
  - Backend-related tests under `tests/`
  - Backend sections of documentation.
  - `docs/project_memory.md`
- Avoid editing unless necessary:
  - `frontend/`
  - Release workflow files.
  - Unrelated documentation.

### Frontend Agent

- Responsibility: Implement React UI, text input, file upload, backend API calls, result display, loading states, and frontend tests if added.
- Use when: Current phase is Phase 3 or another explicitly approved frontend implementation phase.
- May edit:
  - `frontend/`
  - Frontend-related tests under `tests/`
  - Frontend setup documentation.
  - `docs/project_memory.md`
- Avoid editing unless necessary:
  - Backend analyzer logic.
  - Backend route implementation.
  - ROS taxonomy docs.

### Testing Agent

- Responsibility: Add and maintain tests, test fixtures, example-driven checks, and regression coverage.
- Use when: Adding backend tests, frontend tests, analyzer rule tests, or example validation.
- May edit:
  - `tests/`
  - `examples/`
  - Test configuration files.
  - Small source changes needed to make tested behavior correct.
  - `docs/project_memory.md`
- Avoid editing unless necessary:
  - Product roadmap docs.
  - GitHub release docs.
  - Unrelated UI or API files.

### Documentation Agent

- Responsibility: Keep README files, architecture docs, workflow docs, examples, and beginner explanations clear and current.
- Use when: Creating or revising documentation, setup instructions, examples, or release notes.
- May edit:
  - `README.md`
  - `PLANS.md`
  - `AGENTS.md`
  - `docs/`
  - `backend/README.md`
  - `frontend/README.md`
  - `examples/README.md`
  - `tests/README.md`
  - `docs/project_memory.md`
- Avoid editing unless necessary:
  - Backend implementation files.
  - Frontend implementation files.
  - Test logic.

### GitHub/Release Agent

- Responsibility: Prepare commits, pushes, tags, GitHub milestones, release notes, and repository status updates.
- Use when: A phase asks for commit, push, tag, release, or GitHub checkpoint work.
- May edit:
  - `docs/github_workflow.md`
  - `docs/project_memory.md`
  - Release notes or changelog files if added later.
- Avoid editing unless necessary:
  - Backend source files.
  - Frontend source files.
  - Analyzer rules.
  - Tests.

## 4. Coding Rules For Future Phases

- Use modular code.
- Keep FastAPI route handlers thin.
- Put request validation, parsing, analyzer orchestration, and response formatting in focused modules.
- Do not execute uploaded files.
- Treat uploads as text only.
- Do not trust uploaded content.
- Add tests for analyzer rules.
- Add tests for API response shape.
- Keep the AI layer optional and abstracted.
- The rule-based analyzer must work without API keys or an LLM provider.
- Return structured responses using the planned fields:
  - `summary`
  - `detected_errors`
  - `likely_root_causes`
  - `recommended_fixes`
  - `verification_commands`
  - `confidence`
  - `ros_version_guess`
  - `related_files`
  - `next_debugging_steps`

## 5. Git Rules

- Commit after each completed sub-phase.
- Use clear commit messages that include the phase or sub-phase when possible.
- Push after meaningful milestones.
- Tag phase releases when requested.
- Update `docs/project_memory.md` before committing.
- Review changed files before committing.
- Do not rewrite shared history unless the user explicitly asks.

## 6. Safety And Scope Rules

- No destructive commands unless clearly needed and explicitly justified.
- No secrets in the repository.
- No API keys committed.
- No tokens committed.
- No private credentials in examples, tests, or documentation.
- No real robot control in MVP 1.
- No hardware commands in MVP 1 implementation.
- No automatic command execution based on uploaded user content.
- No backend or frontend implementation before the correct phase.
- Keep MVP 1 focused on local, text-based analysis.

## 7. Memory Rules

`docs/project_memory.md` is the source of truth for project progress.

Before starting work:

- Read `docs/project_memory.md`.
- Read relevant planning and architecture docs.
- Confirm the current phase and sub-phase.

Before stopping:

- Update completed work.
- Update pending work.
- Update files created or changed.
- Update GitHub status when relevant.
- Update known issues.
- Set the next recommended action.
- Add concise session notes.

At minimum, every memory update should record:

- Completed work.
- Pending work.
- Known issues.
- Next action.
