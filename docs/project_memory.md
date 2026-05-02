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

Phase 2: Backend MVP

## 4. Current Sub-Phase

Phase 2.7: Add backend tests - complete

## 5. Completed Sub-Phases

- Phase 0.1: Defined project scope.
- Phase 0.2: Created initial repository structure.
- Phase 0.3: Created initial documentation.
- Phase 0.4: Improved and finalized the reusable project memory/progress structure.
- Phase 0.5: Prepared first GitHub checkpoint with `AGENTS.md`, final Phase 0 memory updates, local Git setup, GitHub remote setup, checkpoint commit, and release tag.
- Phase 1.1: Created a detailed ROS AI Debugger project plan.
- Phase 1.2: Created the ROS AI Debugger system architecture document.
- Phase 1.3: Created the MVP 1 ROS error taxonomy for rule-based analyzer implementation.
- Phase 1.4: Refined `AGENTS.md` with project identity, global rules, agent roles, coding rules, Git rules, safety rules, and memory rules.
- Phase 1.5: Finalized Phase 1, updated status documentation, prepared GitHub checkpoint, and created the Phase 1 release tag.
- Phase 2.1: Set up the FastAPI backend skeleton without analyzer or endpoint logic.
- Phase 2.2: Added the backend `GET /health` endpoint and a focused health endpoint test.
- Phase 2.3: Added the `POST /analyze/text` endpoint skeleton with request/response models and placeholder response behavior.
- Phase 2.4: Added the `POST /analyze/files` endpoint skeleton with safe text-only upload handling, supported filename validation, placeholder response behavior, and file upload tests.
- Phase 2.5: Implemented the first rule-based ROS analyzer and connected it to text and file analysis endpoints.
- Phase 2.6: Formalized structured analyzer responses with documented Pydantic fields, constrained confidence values, consistent response tests, and high/medium/low confidence behavior.
- Phase 2.7: Strengthened backend tests with shared fixtures/helpers, endpoint schema assertions, analyzer category coverage, unknown/no-match checks, and multi-rule response checks.

## 6. Pending Sub-Phases

- Phase 2.8: Update memory file, commit, push, and tag.

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
- `backend/app/__init__.py`
- `backend/app/main.py`
- `backend/app/api/__init__.py`
- `backend/app/api/routes/__init__.py`
- `backend/app/api/routes/analyze.py`
- `backend/app/api/routes/health.py`
- `backend/app/core/__init__.py`
- `backend/app/services/__init__.py`
- `backend/app/services/ros_analyzer.py`
- `backend/app/models/__init__.py`
- `backend/app/models/analysis.py`
- `backend/tests/__init__.py`
- `backend/tests/conftest.py`
- `backend/tests/helpers.py`
- `backend/tests/test_health.py`
- `backend/tests/test_analyze_text.py`
- `backend/tests/test_analyze_files.py`
- `backend/tests/test_ros_analyzer.py`
- `backend/requirements.txt`
- `backend/pyproject.toml`

Files updated in Phase 1.1:

- `docs/project_plan.md`
- `docs/project_memory.md`

Files updated in Phase 1.2:

- `docs/system_architecture.md`
- `docs/project_memory.md`

Files updated in Phase 1.3:

- `docs/ros_error_taxonomy.md`
- `docs/project_memory.md`

Files updated in Phase 1.4:

- `AGENTS.md`
- `docs/project_memory.md`

Files updated in Phase 1.5:

- `README.md`
- `PLANS.md`
- `docs/project_memory.md`

Files updated in Phase 2.1:

- `backend/README.md`
- `backend/app/__init__.py`
- `backend/app/main.py`
- `backend/app/api/__init__.py`
- `backend/app/api/routes/__init__.py`
- `backend/app/core/__init__.py`
- `backend/app/services/__init__.py`
- `backend/app/models/__init__.py`
- `backend/tests/__init__.py`
- `backend/requirements.txt`
- `backend/pyproject.toml`
- `docs/project_memory.md`

Files updated in Phase 2.2:

- `backend/app/api/routes/__init__.py`
- `backend/app/api/routes/health.py`
- `backend/tests/test_health.py`
- `backend/README.md`
- `docs/project_memory.md`

Files updated in Phase 2.3:

- `backend/app/api/routes/__init__.py`
- `backend/app/api/routes/analyze.py`
- `backend/app/models/__init__.py`
- `backend/app/models/analysis.py`
- `backend/tests/test_analyze_text.py`
- `backend/README.md`
- `docs/project_memory.md`

Files updated in Phase 2.4:

- `backend/app/api/routes/analyze.py`
- `backend/tests/test_analyze_files.py`
- `backend/requirements.txt`
- `backend/README.md`
- `docs/project_memory.md`

Files updated in Phase 2.5:

- `backend/app/api/routes/analyze.py`
- `backend/app/services/__init__.py`
- `backend/app/services/ros_analyzer.py`
- `backend/tests/test_analyze_text.py`
- `backend/tests/test_analyze_files.py`
- `backend/tests/test_ros_analyzer.py`
- `backend/README.md`
- `docs/project_memory.md`

Files updated in Phase 2.6:

- `backend/app/models/__init__.py`
- `backend/app/models/analysis.py`
- `backend/app/services/ros_analyzer.py`
- `backend/tests/test_ros_analyzer.py`
- `backend/README.md`
- `docs/project_memory.md`

Files updated in Phase 2.7:

- `backend/tests/conftest.py`
- `backend/tests/helpers.py`
- `backend/tests/test_health.py`
- `backend/tests/test_analyze_text.py`
- `backend/tests/test_analyze_files.py`
- `backend/tests/test_ros_analyzer.py`
- `backend/README.md`
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
- Phase 1.4 changes are committed locally.
- Phase 1.5 commit message: `Phase 1 complete: planning, architecture, and ROS taxonomy`.
- Phase 1 checkpoint tag created: `v0.2.0-phase-1-complete`.
- Phase 1 commits pushed to GitHub.
- Tag `v0.2.0-phase-1-complete` pushed to GitHub.
- Phase 2.1 changes are committed locally.
- Phase 2.2 changes are committed locally.
- Phase 2.3 changes are committed locally.
- Phase 2.4 changes are committed locally with message `Phase 2.4: add file analysis endpoint skeleton`.
- Phase 2.5 changes are committed locally with message `Phase 2.5: implement initial rule-based ROS analyzer`.
- Phase 2.6 changes are committed locally with message `Phase 2.6: formalize structured analyzer responses`.
- Phase 2.7 changes are committed locally with message `Phase 2.7: strengthen backend analyzer tests`.

## 10. Known Issues

- Backend has a FastAPI skeleton and health endpoint.
- Analyze text endpoint is connected to the first rule-based analyzer.
- Analyze files endpoint validates supported uploads, treats files as text only, and sends uploaded text to the first rule-based analyzer.
- Rule-based analyzer currently covers the first 9 requested MVP rules only.
- Analyzer confidence is now formalized as `high`, `medium`, or `low`.
- Rule-based analyzer is intentionally simple and may miss uncommon ROS error formats.
- Frontend contains placeholders only; no frontend application code exists yet.
- Backend currently has health endpoint, endpoint validation, upload handling, analyzer rule coverage, unknown/no-match, multi-rule, and response structure consistency tests.

## 11. Next Recommended Action

Proceed to Phase 2.8: update memory file, commit, push, and tag the backend MVP checkpoint.

## 12. Session Notes

- Phase 0.1 confirmed the repository started empty and defined the MVP scope.
- Phase 0.2 created the initial folder structure and placeholder README files.
- Phase 0.3 created initial beginner-friendly documentation and GitHub workflow notes.
- Phase 0.4 converted this memory file into a reusable progress system.
- Phase 0.5 created `AGENTS.md`, initialized Git, configured GitHub remote, and prepared the first checkpoint commit/tag.
- Phase 1.1 replaced the generic project plan with a specific beginner-friendly ROS AI Debugger plan covering vision, users, problem, solution, MVP scope, features, non-goals, success criteria, roadmap, and risks.
- Phase 1.2 created a beginner-friendly system architecture covering frontend, backend, input handling, parsing, analyzer pipeline, rule-based detection, optional AI abstraction, response formatting, API design, data structures, ROS-specific design, MVP constraints, scalability, and design decisions.
- Phase 1.3 created a backend-ready taxonomy for 16 MVP error categories, including detection clues, root causes, fixes, verification commands, confidence rules, examples, prioritization, and limitations.
- Phase 1.4 converted `AGENTS.md` into a project-specific operating guide for safe, phased, beginner-friendly work across planning, architecture, taxonomy, backend, frontend, testing, documentation, and GitHub/release tasks.
- Phase 1.5 finalized the documentation and architecture phase, updated project status docs, prepared the Phase 1 GitHub checkpoint, and tagged `v0.2.0-phase-1-complete`.
- Phase 1 achievement summary: the project now has a detailed product plan, system architecture, ROS error taxonomy, agent operating rules, MVP scope, GitHub workflow, and memory system ready for Backend MVP implementation.
- Phase 2.1 created a minimal FastAPI app entry point, empty API router, backend package structure, dependency list, pytest configuration, and backend run instructions.
- Phase 2.2 added `GET /health`, documented how to call it, added a test, installed backend requirements in the local environment for verification, ran backend tests, and confirmed Python files compile.
- Phase 2.3 added shared analysis request/response models, `POST /analyze/text`, placeholder response behavior, endpoint documentation, and tests for valid input, empty input validation, and ROS version hints.
- Phase 2.4 added `POST /analyze/files`, safe text-only upload reading, supported filename validation, clear errors for unsupported or missing uploads, documentation for the upload endpoint, and tests for single file, multiple files, unsupported files, and empty uploads.
- Phase 2.5 added `backend/app/services/ros_analyzer.py` with rule-based detection for missing packages, missing nodes/executables, Python imports, TF frames, Gazebo plugins, catkin builds, colcon builds, ROS_MASTER_URI, and ROS 2 DDS/domain issues. Both analysis endpoints now call the analyzer service, and tests cover every required MVP rule plus unknown input.
- Phase 2.6 documented and constrained the response model, added medium confidence partial-match behavior, kept unknown results beginner-friendly, documented the final JSON schema in `backend/README.md`, and added tests for consistent response fields.
- Phase 2.7 added shared test fixtures and response schema helpers, strengthened endpoint tests for text and file analysis, verified all MVP analyzer categories are represented, checked multi-rule output deduplication, and documented backend test commands.
- Frontend implementation must not start until Phase 3.
