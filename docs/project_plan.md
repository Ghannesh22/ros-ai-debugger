# ROS AI Debugger Detailed Project Plan

## 1. Project Vision

ROS AI Debugger is a local web tool that helps people debug ROS and ROS 2 projects by turning confusing error text into clear explanations and practical fixes.

The product exists because ROS debugging is often difficult for beginners. A single problem can show up as a long terminal error, a failed launch file, a missing dependency, a broken build, or a node that silently does not start. New users often do not know whether the real issue is in `package.xml`, `CMakeLists.txt`, a launch file, an environment variable, a topic name, or a missing Python module.

ROS AI Debugger will help users answer three basic questions:

- What error was detected?
- What is the likely root cause?
- What should I do next to fix and verify it?

The first version is software-first. It does not require a robot, ROS hardware, sensors, or a live ROS runtime. It focuses on text that users can paste or upload from their existing ROS work.

## 2. Target Users

Primary users:

- Robotics students learning ROS or ROS 2.
- ROS beginners working through tutorials.
- Developers who understand Python or C++ but are new to ROS workspaces, launch files, and dependency management.

Primary user pain points:

- They see long terminal errors and do not know which line matters.
- They do not know the difference between a missing package, missing dependency, missing executable, and missing node.
- They copy commands from tutorials but cannot tell whether the issue is their workspace, environment setup, package name, or file permissions.
- They need beginner-friendly explanations instead of only raw error output.

Secondary users:

- Robotics engineers who want a quick second opinion.
- Startup teams building prototypes with ROS or ROS 2.
- Developers maintaining small robotics projects without a full robotics infrastructure team.

Secondary user pain points:

- They lose time scanning repeated build or launch errors.
- They need faster triage when switching between ROS 1 and ROS 2 projects.
- They want consistent debugging checklists for common problems.
- They may need to onboard junior engineers or interns.

## 3. Problem Statement

ROS debugging is difficult because errors often come from several layers at once:

- Workspace setup, such as forgetting to source `setup.bash`.
- Package metadata, such as missing dependencies in `package.xml`.
- Build files, such as incorrect `CMakeLists.txt` install or target rules.
- Launch files, such as invalid XML or wrong executable names.
- Runtime configuration, such as wrong topic names, missing parameters, or incorrect environment variables.
- ROS 2 middleware settings, such as DDS or domain ID mismatches.

Engineers lose time because the terminal output does not always explain the real cause in beginner language. A launch error may say a node cannot be found, but the fix might be to rebuild the workspace, source the workspace, mark a Python file executable, or correct the executable name in the launch file.

Real examples of debugging pain:

- A ROS 1 user runs `roslaunch` and gets `RLException: [talker] is neither a launch file in package...`. The actual issue may be a wrong package name or an unsourced workspace.
- A ROS 2 user runs `ros2 launch` and gets a package-not-found error after `colcon build`. The likely fix may be sourcing `install/setup.bash` or checking the package name.
- A Python node fails with `ModuleNotFoundError: No module named ...`. The real issue may be a missing dependency, wrong virtual environment, or missing package install rule.
- A robot visualization fails because `map` to `base_link` transform is missing. The user may need to inspect TF publishers, frame names, or launch order.
- Gazebo reports that a plugin cannot be loaded. The issue may be a missing plugin package, wrong library path, or incompatible plugin name.

## 4. Solution Overview

ROS AI Debugger solves the problem by accepting debugging evidence, analyzing it with a focused ROS error pipeline, and returning a structured diagnosis.

Input:

- Pasted terminal output.
- ROS log files.
- Launch files.
- `package.xml`.
- `CMakeLists.txt`.
- YAML configuration files.
- Python source files.
- C++ source files.

Processing:

- Detect likely ROS version from commands and error patterns.
- Scan text for known ROS, ROS 2, Gazebo, TF, build, package, and dependency error patterns.
- Match findings to a rule-based ROS error taxonomy.
- Identify related files when filenames or file contents are provided.
- Build a clear response with likely causes, fixes, verification commands, and next steps.
- Keep an AI-provider abstraction so an LLM can be added later without rewriting the analyzer interface.

Output:

- Short summary.
- Detected errors.
- Likely root causes.
- Recommended fixes.
- Verification commands.
- Confidence level.
- ROS version guess.
- Related files.
- Next debugging steps.

## 5. MVP 1 Scope

MVP 1 will be a small local web application for text-based ROS debugging.

What will be built:

- FastAPI backend.
- React with Vite frontend by default.
- Text input for pasted ROS terminal errors.
- File upload for supported text files.
- Rule-based analyzer for common ROS 1 Noetic and ROS 2 Humble errors.
- Structured JSON response.
- Beginner-friendly diagnosis display.
- Backend tests for common analyzer cases.
- Example input files for ROS 1, ROS 2, Gazebo, and TF/frame errors.
- Documentation that explains setup, usage, and project structure.

What will not be built in MVP 1:

- Real robot integration.
- Live ROS runtime debugging.
- Hardware support.
- rosbag analysis.
- VS Code plugin.
- Cloud/SaaS deployment.
- User accounts.
- Database persistence.
- Required Docker setup.
- Full LLM-provider integration.

MVP 1 should stay realistic: it should solve common text-based debugging problems well before adding live robotics features.

## 6. Core Features (MVP 1)

Error input:

- The user can paste ROS or ROS 2 terminal output into a text area.
- The backend receives the text and analyzes it without needing ROS installed.

File upload:

- The user can upload logs, launch files, `package.xml`, `CMakeLists.txt`, YAML, Python, and C++ files.
- MVP 1 treats uploads as text. It does not execute files.

Analysis:

- The analyzer detects known error categories such as missing package, missing dependency, node not found, launch syntax error, build failure, TF frame missing, Python import error, Gazebo plugin load error, `ROS_MASTER_URI` issue, and ROS 2 DDS/domain issue.
- The analyzer returns a confidence value so users know whether the result is strong or only a likely guess.

Fix suggestions:

- The tool explains the likely root cause in simple language.
- The tool recommends practical fixes, such as installing a dependency, rebuilding the workspace, sourcing setup files, correcting a package name, or checking file permissions.

Verification commands:

- The response includes commands the user can run to check whether the fix worked.
- Examples may include `roscd`, `rospack find`, `roslaunch`, `catkin_make`, `colcon build`, `ros2 pkg list`, `ros2 launch`, `ros2 topic list`, and TF inspection commands.

Diagnosis display:

- The frontend displays the diagnosis in sections so beginners can scan it easily.
- The result should not be a wall of text.

## 7. Non-Goals

MVP 1 does not include:

- Real robot integration.
- Live ROS runtime debugging.
- Hardware setup or hardware diagnostics.
- rosbag analysis yet.
- VS Code plugin yet.
- Automatic editing of project files.
- Automatic command execution.
- Cloud deployment.
- Multi-user accounts.
- Production monitoring.
- Guaranteed perfect diagnosis.

## 8. Success Criteria

MVP 1 is successful if:

- A user can paste a common ROS error and get a useful diagnosis.
- A user can upload a supported text file and get useful feedback.
- The response is understandable to a ROS beginner.
- The response includes a likely root cause, suggested fix, and verification command.
- The tool works for common ROS 1 and ROS 2 text errors.
- The backend returns the planned structured JSON response.
- The frontend clearly displays diagnosis results.
- The project can be developed on Windows without robot hardware.
- The documentation makes local setup and usage clear.

## 9. Future Roadmap

Future ideas after MVP 1:

- rosbag analysis for recorded runtime data.
- Simulation integration for Gazebo and other robotics simulators.
- VS Code extension for debugging inside a developer editor.
- LLM-backed explanations and deeper diagnosis.
- Workspace scanning for full ROS package folders.
- SaaS version for teams.
- Saved debugging reports.
- More ROS distributions beyond ROS 1 Noetic and ROS 2 Humble.

## 10. Risks And Challenges

Incorrect diagnosis:

- ROS errors can have several possible causes. The tool must avoid pretending it is certain when it is only guessing.
- Confidence levels and next debugging steps are important.

Complex ROS systems:

- Large workspaces may have many packages, launch files, parameters, and nodes.
- MVP 1 should focus on common isolated errors, not full-system diagnosis.

Variability in errors:

- Error messages differ between ROS 1, ROS 2, operating systems, shells, and package versions.
- The analyzer needs examples and tests so common patterns do not regress.

Beginner expectations:

- Users may expect the tool to fix everything automatically.
- The product should clearly explain that MVP 1 gives guidance and verification steps, not automatic repair.

Windows-friendly development:

- Many ROS tutorials assume Linux commands.
- The project itself should remain runnable from Windows development tools, even when some suggested ROS commands are Linux/ROS environment commands.
