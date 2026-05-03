# ROS AI Debugger Plans

This file tracks the project roadmap at a high level. Detailed planning lives in `docs/project_plan.md`, and current progress lives in `docs/project_memory.md`.

## Project Goal

Build an AI-assisted debugger for ROS systems that helps users understand errors from terminals, logs, launch files, package manifests, build files, and source/config files.

The project is software-first and does not require physical robotics hardware for MVP 1. It should remain friendly to Windows-based development.

## MVP 1 Definition

MVP 1 is a local web application with:

- A FastAPI backend.
- A React frontend.
- A rule-based ROS analyzer.
- A future-ready AI-provider abstraction.
- No required database.
- No required Docker setup.
- Text-based analysis for common ROS 1 Noetic and ROS 2 Humble errors.

MVP 1 input types:

- Pasted terminal errors.
- ROS log files.
- Launch files.
- `package.xml`.
- `CMakeLists.txt`.
- YAML files.
- Python files.
- C++ files.

MVP 1 output fields:

- `summary`
- `detected_errors`
- `likely_root_causes`
- `recommended_fixes`
- `verification_commands`
- `confidence`
- `ros_version_guess`
- `related_files`
- `next_debugging_steps`

## Current Milestone

- Phase 0: Complete.
- Phase 1: Complete.
- Phase 2: Complete.
- Phase 3: Complete.
- Next milestone: Phase 4 Examples And Testing.

## Phase Roadmap

### Phase 0: Planning And Repository Setup - Complete

- 0.1 Define project scope.
- 0.2 Create repository structure.
- 0.3 Create initial documentation.
- 0.4 Create memory/progress file.
- 0.5 Commit and prepare GitHub push.

### Phase 1: Documentation And Architecture - Complete

- 1.1 Create detailed project plan.
- 1.2 Create system architecture.
- 1.3 Create ROS error taxonomy.
- 1.4 Review and finalize `AGENTS.md`.
- 1.5 Finalize Phase 1, update memory file, commit, push, and tag.

### Phase 2: Backend MVP - Complete

- 2.1 Set up FastAPI backend.
- 2.2 Create health endpoint.
- 2.3 Create text analysis endpoint.
- 2.4 Create file analysis endpoint.
- 2.5 Create rule-based ROS analyzer.
- 2.6 Add structured JSON response.
- 2.7 Add backend tests.
- 2.8 Update memory file, commit, push, and tag.

### Phase 3: Frontend MVP - Complete

- 3.1 Create frontend skeleton.
- 3.2 Add text input area.
- 3.3 Add file upload area.
- 3.4 Connect frontend to backend.
- 3.5 Display diagnosis results.
- 3.6 Update memory file, commit, push, and tag.

### Phase 4: Examples And Testing - Next

- 4.1 Add example ROS 1 errors.
- 4.2 Add example ROS 2 errors.
- 4.3 Add Gazebo error examples.
- 4.4 Add TF/frame error examples.
- 4.5 Add test cases.
- 4.6 Update memory file, commit, push, and tag.

### Phase 5: First Release

- 5.1 Clean README.
- 5.2 Clean docs.
- 5.3 Verify setup instructions.
- 5.4 Run tests.
- 5.5 Push to GitHub.
- 5.6 Create first release tag.

## GitHub Workflow

- Commit after each completed sub-phase.
- Push after meaningful milestones.
- Tag release milestones.
- Update `docs/project_memory.md` before every commit.
- Keep commits focused and beginner-readable.
