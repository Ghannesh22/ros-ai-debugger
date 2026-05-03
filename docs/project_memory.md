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

Phase 3: Frontend MVP - in progress

## 4. Current Sub-Phase

Phase 3.5: Display diagnosis results - complete

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
- Phase 2.8: Finalized the Backend MVP checkpoint, updated project status docs, verified backend tests and compile checks, committed the Phase 2 checkpoint, pushed `main`, and tagged `v0.3.0-backend-mvp`.
- Phase 2: Complete. Backend MVP analyzer checkpoint is ready for Phase 3 frontend work.
- Phase 3.1: Created the React with Vite frontend skeleton with a clean static page, placeholder sections for text input, file upload, and results, beginner-friendly frontend run/build instructions, root README run links, and the permanent behavior documentation rule in `AGENTS.md`.
- Phase 3.2: Added the pasted ROS error text input UI with local state, optional filename, optional ROS version hint, an Analyze button, and the required local placeholder message without backend calls or API requests.
- Phase 3.3: Added the file upload UI with local state, multi-file selection, selected filename display, and supported file type guidance without backend calls, API requests, file reading, or real analysis behavior.
- Phase 3.4: Connected the frontend to the backend analysis API. Text input now calls `POST /analyze/text`, file-only input calls `POST /analyze/files`, loading and request error states are shown, raw structured JSON is displayed temporarily, Vite backend URL configuration was added, and local frontend CORS origins were enabled in the backend for integration.
- Phase 3.5: Replaced the temporary raw JSON display with beginner-friendly readable result sections for all structured response fields, copy-friendly verification command rows, confidence/ROS version metadata, and an optional `Show raw JSON` toggle.

## 6. Pending Sub-Phases

- Phase 3.6: Update memory file, commit, push, and tag.

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
- `.gitignore`
- `frontend/index.html`
- `frontend/package-lock.json`
- `frontend/package.json`
- `frontend/vite.config.js`
- `frontend/src/App.jsx`
- `frontend/src/main.jsx`
- `frontend/src/styles.css`

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

Files updated in Phase 2.8:

- `README.md`
- `PLANS.md`
- `backend/README.md`
- `docs/project_memory.md`

Files updated in Phase 3.1:

- `.gitignore`
- `AGENTS.md`
- `README.md`
- `frontend/README.md`
- `frontend/index.html`
- `frontend/package-lock.json`
- `frontend/package.json`
- `frontend/vite.config.js`
- `frontend/src/App.jsx`
- `frontend/src/main.jsx`
- `frontend/src/styles.css`
- `docs/project_memory.md`

Files updated in Phase 3.2:

- `frontend/README.md`
- `frontend/src/App.jsx`
- `frontend/src/styles.css`
- `docs/project_memory.md`

Files updated in Phase 3.3:

- `frontend/README.md`
- `frontend/src/App.jsx`
- `frontend/src/styles.css`
- `docs/project_memory.md`

Files updated in Phase 3.4:

- `README.md`
- `backend/README.md`
- `backend/app/main.py`
- `backend/tests/test_health.py`
- `frontend/README.md`
- `frontend/src/api.js`
- `frontend/src/App.jsx`
- `frontend/src/styles.css`
- `docs/project_memory.md`

Files updated in Phase 3.5:

- `README.md`
- `frontend/README.md`
- `frontend/src/App.jsx`
- `frontend/src/styles.css`
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
- Phase 2.8 commit message: `Phase 2 complete: backend MVP analyzer`.
- Phase 2 backend checkpoint pushed to GitHub on branch `main`.
- Phase 2 checkpoint tag created and pushed: `v0.3.0-backend-mvp`.
- Test status for Phase 2.8: `python -m pytest` passed with 25 tests, Python compile check passed, and `git diff --check` passed.
- Phase 3.1 commit message: `Phase 3.1: create frontend skeleton`.
- Test status for Phase 3.1: `npm run build` passed for the frontend skeleton and `git diff --check` passed.
- Phase 3.2 commit message: `Phase 3.2: add text input UI`.
- Test status for Phase 3.2: `npm run build` passed, `npm run` confirmed available frontend scripts, and `git diff --check` passed.
- Phase 3.3 commit message: `Phase 3.3: add file upload UI`.
- Test status for Phase 3.3: `npm run build` passed, `npm run` confirmed available frontend scripts, and `git diff --check` passed.
- Phase 3.4 commit message: `Phase 3.4: connect frontend to backend analysis API`.
- Test status for Phase 3.4: `npm run build` passed, backend `python -m pytest` passed with 26 tests, and `git diff --check` passed.
- Phase 3.5 commit message: `Phase 3.5: add readable analysis results UI`.
- Test status for Phase 3.5: `npm run build` passed and `git diff --check` passed.

## 10. Known Issues

- Backend MVP has a FastAPI app, health endpoint, text analysis endpoint, file analysis endpoint, and rule-based analyzer.
- Analyze text endpoint is connected to the first rule-based analyzer.
- Analyze files endpoint validates supported uploads, treats files as text only, and sends uploaded text to the first rule-based analyzer.
- Rule-based analyzer currently covers the first 9 requested MVP rules only.
- Analyzer confidence is now formalized as `high`, `medium`, or `low`.
- Rule-based analyzer is intentionally simple and may miss uncommon ROS error formats.
- Frontend now contains a React with Vite skeleton.
- Frontend text input UI now accepts pasted ROS terminal errors using local state only.
- Frontend filename and ROS version hint fields are local optional inputs only.
- Frontend Analyze button now calls the backend analysis API.
- Frontend file upload UI now allows selecting one or more files and shows selected filenames using local state only.
- Frontend supported file type guidance lists `.txt`, `.log`, `.launch`, `.xml`, `.yaml`, `.yml`, `.py`, `.cpp`, `CMakeLists.txt`, and `package.xml`.
- Frontend uses `VITE_BACKEND_URL` when set and defaults to `http://127.0.0.1:8000`.
- Frontend text analysis calls `POST /analyze/text`.
- Frontend file-only analysis calls `POST /analyze/files`.
- Frontend prefers text analysis when both pasted text and files are provided, and shows a note that combined analysis can be added later.
- Frontend now shows loading and request error states.
- Frontend now displays readable result sections for `summary`, `detected_errors`, `likely_root_causes`, `recommended_fixes`, `verification_commands`, `confidence`, `ros_version_guess`, `related_files`, and `next_debugging_steps`.
- Frontend keeps raw JSON hidden by default and exposes it with a `Show raw JSON` toggle for debugging.
- Frontend verification commands are displayed as copy-friendly command rows.
- Backend now allows local Vite frontend origins for CORS during development.
- Backend currently has health endpoint, endpoint validation, upload handling, analyzer rule coverage, unknown/no-match, multi-rule, and response structure consistency tests.
- No LLM behavior has been added.

## 11. Next Recommended Action

Proceed to Phase 3.6: update memory file, commit, push, and tag.

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
- Phase 2.8 finalized the backend MVP checkpoint. Route handlers remain thin, analyzer logic lives in services, uploaded files are treated as text only, no frontend or LLM logic was added, and verification passed with 25 backend tests, Python compile checks, and `git diff --check`.
- Phase 2 achievement summary: the project now has a working FastAPI backend MVP with `/health`, `/analyze/text`, `/analyze/files`, safe text-only upload handling, typed structured responses, an initial rule-based ROS analyzer, and focused backend tests.
- Phase 3.1 created a static React with Vite frontend skeleton in `frontend/`. The page includes the required title, subtitle, and placeholder sections for text input, file upload, and results. No backend connection or real analysis behavior was added.
- Phase 3.1 updated beginner-friendly commands in `frontend/README.md`, added root README run links, and updated `AGENTS.md` with the permanent behavior documentation rule.
- Phase 3.1 verification: `npm run build` passed in `frontend/`, and `git diff --check` passed from the repository root.
- Phase 3.2 added a real local text input form for pasted ROS errors, optional filename input, optional ROS version hint selector, and an Analyze button that only shows the required Phase 3.4 backend placeholder message. No backend connection, API request, file upload behavior, or real analysis behavior was added.
- Phase 3.2 updated `frontend/README.md` with beginner-friendly install, run, build, and manual verification steps for the text input UI.
- Phase 3.2 verification: `npm run build` passed in `frontend/`, `npm run` confirmed there is no separate frontend test script yet, and `git diff --check` passed from the repository root.
- Phase 3.3 added a local multi-file upload UI for ROS logs and project files, displayed selected filenames in the browser, and documented supported file types in the UI. No backend connection, API request, file reading, upload processing, or real analysis behavior was added.
- Phase 3.3 updated `frontend/README.md` with beginner-friendly install, run, build, and manual verification steps for the file upload UI.
- Phase 3.3 verification: `npm run build` passed in `frontend/`, `npm run` confirmed there is no separate frontend test script yet, and `git diff --check` passed from the repository root.
- Phase 3.4 added `frontend/src/api.js` for backend API configuration and request helpers. The default backend URL is `http://127.0.0.1:8000`, and it can be changed with `VITE_BACKEND_URL`.
- Phase 3.4 updated the frontend so pasted text calls `/analyze/text`, selected files call `/analyze/files` when no text is provided, both text and files prefer text analysis for now, and raw JSON responses are shown temporarily until Phase 3.5.
- Phase 3.4 added loading and request error states in the frontend.
- Phase 3.4 added local development CORS origins in the backend so the Vite frontend can call the FastAPI backend from `http://127.0.0.1:5173` or `http://localhost:5173`.
- Phase 3.4 updated `frontend/README.md`, `backend/README.md`, and `README.md` with beginner-friendly full-stack install, start, test, and verification commands.
- Phase 3.4 verification: `npm run build` passed in `frontend/`, backend `python -m pytest` passed with 26 tests, and `git diff --check` passed from the repository root.
- Phase 3.5 replaced temporary raw JSON display with readable diagnosis sections for every backend response field. Summary, detected errors, likely root causes, recommended fixes, verification commands, confidence, ROS version guess, related files, and next debugging steps now display in beginner-friendly sections.
- Phase 3.5 added a `Show raw JSON` / `Hide raw JSON` toggle so raw backend output is available for debugging but hidden by default.
- Phase 3.5 updated `frontend/README.md` and `README.md` with beginner-friendly manual verification steps for readable results and the raw JSON toggle.
- Phase 3.5 verification: `npm run build` passed in `frontend/`, and `git diff --check` passed from the repository root. Backend files were not changed, so backend tests were not required for this sub-phase.
