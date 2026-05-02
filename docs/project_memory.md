# ROS AI Debugger Project Memory

Codex must update this file at the end of every phase and sub-phase.

## 1. Project Goal

Build MVP 1 of ROS AI Debugger: a Windows-development-friendly, software-first tool that helps robotics engineers debug ROS and ROS 2 systems by analyzing pasted terminal errors and uploaded text files such as logs, launch files, package.xml, CMakeLists.txt, YAML, Python, and C++ files.

## 2. MVP Scope

MVP 1 focuses on text-based ROS debugging for common ROS 1 Noetic and ROS 2 Humble errors.

In scope:

- Pasted ROS terminal errors.
- Uploaded ROS log files.
- Uploaded launch files.
- Uploaded `package.xml`.
- Uploaded `CMakeLists.txt`.
- Uploaded YAML, Python, and C++ files as text inputs.
- Rule-based analysis for common ROS error categories.
- Structured diagnosis output with root causes, fixes, verification commands, confidence, related files, and next steps.
- FastAPI backend in a later phase.
- React with Vite frontend by default in a later phase.
- AI-provider abstraction for future LLM integration.

Out of scope for MVP 1:

- Robot hardware integration.
- rosbag parsing.
- Real-time ROS graph introspection.
- Database storage.
- Required Docker setup.
- Full LLM-provider integration.

## 3. Current Phase

Phase 1: Documentation and architecture

## 4. Current Sub-Phase

Phase 1.3: Create ROS error taxonomy - complete

## 5. Completed Sub-Phases

- Phase 0.1: Defined project scope.
- Phase 0.2: Created initial repository structure.
- Phase 0.3: Created initial documentation.
- Phase 0.4: Improved and finalized the reusable project memory/progress structure.
- Phase 0.5: Prepared first GitHub checkpoint with `AGENTS.md`, final Phase 0 memory updates, local Git setup, GitHub remote setup, checkpoint commit, and release tag.
- Phase 1.1: Created a detailed ROS AI Debugger project plan.
- Phase 1.2: Created the ROS AI Debugger system architecture document.
- Phase 1.3: Created the MVP 1 ROS error taxonomy for rule-based analyzer implementation.

## 6. Pending Sub-Phases

- Phase 1.4: Review and finalize `AGENTS.md`.
- Phase 1.5: Finalize Phase 1, update memory file, commit, push, and tag.

## 7. Important Decisions

- MVP 1 will focus on text-based ROS debugging only.
- MVP 1 will support pasted terminal errors and uploaded ROS-related text files.
- MVP 1 will start with ROS 1 Noetic and ROS 2 Humble style error analysis.
- Backend will use Python and FastAPI.
- Frontend will default to React with Vite unless changed later.
- MVP 1 will not use a database.
- MVP 1 will begin with a rule-based ROS analyzer.
- An AI-provider abstraction will be included so an LLM provider can be added or changed later.
- Hardware integration is out of scope for MVP 1.
- rosbag parsing is out of scope for MVP 1.
- Docker is optional later and out of scope for the first MVP.
- Commit after each completed sub-phase.
- Push after meaningful milestones.
- Tag releases and major milestones.

## 8. Files/Folders Created

Folders:

- `backend/`
- `frontend/`
- `docs/`
- `examples/`
- `tests/`

Files:

- `README.md`
- `PLANS.md`
- `AGENTS.md`
- `backend/README.md`
- `frontend/README.md`
- `examples/README.md`
- `tests/README.md`
- `docs/project_memory.md`
- `docs/project_plan.md`
- `docs/mvp_scope.md`
- `docs/github_workflow.md`
- `docs/system_architecture.md`
- `docs/ros_error_taxonomy.md`

Files updated in Phase 1.1:

- `docs/project_plan.md`
- `docs/project_memory.md`

Files updated in Phase 1.2:

- `docs/system_architecture.md`
- `docs/project_memory.md`

Files updated in Phase 1.3:

- `docs/ros_error_taxonomy.md`
- `docs/project_memory.md`

## 9. GitHub Status

- Local Git repository initialized on branch `main`.
- Local Git identity configured for the authenticated GitHub account.
- GitHub remote configured as `origin`.
- GitHub repository: `https://github.com/Ghannesh22/ros-ai-debugger`.
- Repository visibility: private.
- First checkpoint commit message: `Phase 0 complete: planning, structure, documentation, and memory system`.
- First release-foundation tag created: `v0.1.0-project-foundation`.
- Branch `main` pushed to GitHub.
- Tag `v0.1.0-project-foundation` pushed to GitHub.
- Phase 0 checkpoint is available on GitHub.
- Phase 1.1 changes are committed locally.
- Phase 1.2 changes are committed locally.
- Phase 1.3 changes are committed locally.

## 10. Known Issues

- Backend and frontend contain placeholders only; no application code exists yet.
- No tests exist yet because implementation has not started.

## 11. Next Recommended Action

Proceed to Phase 1.4: review and finalize `AGENTS.md`.

## 12. Session Notes

- Phase 0.1 confirmed the repository started empty and defined the MVP scope.
- Phase 0.2 created the initial folder structure and placeholder README files.
- Phase 0.3 created initial beginner-friendly documentation and GitHub workflow notes.
- Phase 0.4 converted this memory file into a reusable progress system.
- Phase 0.5 created `AGENTS.md`, initialized Git, configured GitHub remote, and prepared the first checkpoint commit/tag.
- Phase 1.1 replaced the generic project plan with a specific beginner-friendly ROS AI Debugger plan covering vision, users, problem, solution, MVP scope, features, non-goals, success criteria, roadmap, and risks.
- Phase 1.2 created a beginner-friendly system architecture covering frontend, backend, input handling, parsing, analyzer pipeline, rule-based detection, optional AI abstraction, response formatting, API design, data structures, ROS-specific design, MVP constraints, scalability, and design decisions.
- Phase 1.3 created a backend-ready taxonomy for 16 MVP error categories, including detection clues, root causes, fixes, verification commands, confidence rules, examples, prioritization, and limitations.
- Backend implementation must not start until Phase 2.
- Frontend implementation must not start until Phase 3.
