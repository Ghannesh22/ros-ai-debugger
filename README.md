# ROS AI Debugger

ROS AI Debugger is a beginner-friendly tool for debugging ROS and ROS 2 systems.

The goal is to help robotics engineers understand errors faster by analyzing pasted terminal output and uploaded project files. The tool will explain what likely went wrong, why it matters, how to fix it, and how to verify the fix.

This project is software-first. You do not need robot hardware to use or develop the MVP. Development should stay friendly for Windows users, especially people building the project from a normal Windows machine while learning ROS debugging concepts.

## Project Status

- Phase 0: Complete
- Phase 1: Complete
- Phase 2: Complete
- Next: Frontend MVP (Phase 3)

Backend MVP implementation is complete. Frontend implementation has not started yet.

## MVP 1

MVP 1 focuses on text-based debugging for common ROS 1 Noetic and ROS 2 Humble errors.

Users should be able to:

- Paste ROS terminal errors.
- Upload ROS log files.
- Upload launch files.
- Upload `package.xml`.
- Upload `CMakeLists.txt`.
- Upload YAML, Python, and C++ files as text inputs.

The system should return:

- Detected issue.
- Likely root cause.
- Simple explanation.
- Suggested fix.
- Verification commands.
- Confidence level.
- Related ROS concepts.
- Next debugging steps.

MVP 1 will not require:

- Robot hardware.
- rosbag parsing.
- Real-time ROS graph introspection.
- Database storage.
- Docker.

## Planned Tech Stack

- Backend: Python and FastAPI.
- Frontend: React with Vite by default.
- Database: none for MVP 1.
- Storage: local files or JSON only if needed.
- AI layer: provider abstraction, starting with rule-based analysis.
- ROS support: text-based ROS 1 Noetic and ROS 2 Humble error analysis.

## How To Run

Backend setup and run commands are in [`backend/README.md`](backend/README.md).

Frontend setup and run commands are in [`frontend/README.md`](frontend/README.md).

For the current frontend skeleton, run:

```powershell
cd frontend
npm install
npm run dev
```

Then open:

```text
http://127.0.0.1:5173
```

To check that the frontend builds:

```powershell
npm run build
```

## Roadmap

### Phase 0: Planning And Repository Setup

- 0.1 Define project scope.
- 0.2 Create repository structure.
- 0.3 Create initial documentation.
- 0.4 Create memory/progress file.
- 0.5 Commit and prepare GitHub push.

### Phase 1: Documentation And Architecture

- 1.1 Create detailed project plan.
- 1.2 Create system architecture.
- 1.3 Create ROS error taxonomy.
- 1.4 Review and finalize `AGENTS.md`.
- 1.5 Finalize Phase 1, update memory file, commit, push, and tag.

### Phase 2: Backend MVP

- 2.1 Set up FastAPI backend.
- 2.2 Create health endpoint.
- 2.3 Create text analysis endpoint.
- 2.4 Create file analysis endpoint.
- 2.5 Create rule-based ROS analyzer.
- 2.6 Add structured JSON response.
- 2.7 Add backend tests.
- 2.8 Update memory file, commit, push, and tag.

### Phase 3: Frontend MVP

- 3.1 Create frontend skeleton.
- 3.2 Add text input area.
- 3.3 Add file upload area.
- 3.4 Connect frontend to backend.
- 3.5 Display diagnosis results.
- 3.6 Update memory file, commit, push, and tag.

### Phase 4: Examples And Testing

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
- Tag documented milestones and release points.
- Keep `docs/project_memory.md` updated before commits.
