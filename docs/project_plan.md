# Project Plan

ROS AI Debugger will help robotics engineers debug ROS and ROS 2 systems by turning confusing error output into practical next steps.

The project starts with a text-based MVP. It will not connect to robot hardware, run ROS nodes, or parse rosbag data in MVP 1. This keeps the first version easier to build, test, and run on Windows development machines.

## MVP 1 Goals

MVP 1 should let a user:

- Paste ROS terminal output.
- Upload ROS log files.
- Upload launch files.
- Upload `package.xml` and `CMakeLists.txt`.
- Upload YAML, Python, and C++ files as text.
- Receive a structured diagnosis with suggested fixes and verification commands.

## MVP 1 Response Shape

The backend should eventually return this structure:

```json
{
  "summary": "",
  "detected_errors": [],
  "likely_root_causes": [],
  "recommended_fixes": [],
  "verification_commands": [],
  "confidence": "",
  "ros_version_guess": "",
  "related_files": [],
  "next_debugging_steps": []
}
```

## Phase Roadmap

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

## Development Rules

- Keep the project beginner-friendly.
- Keep Windows development in mind.
- Update `docs/project_memory.md` after each phase and sub-phase.
- Do not add backend or frontend implementation before the relevant phase.
- Commit after each completed sub-phase.
- Push after meaningful milestones.
- Tag releases and major milestones.
