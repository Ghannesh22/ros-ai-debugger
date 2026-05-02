# MVP Scope

MVP 1 is the first usable version of ROS AI Debugger.

It is intentionally limited to text-based debugging so the project can be built and tested without robotics hardware. A user should be able to run the tool on a normal development machine, including Windows.

## In Scope

- Pasted ROS terminal errors.
- Uploaded ROS log files.
- Uploaded launch files.
- Uploaded `package.xml`.
- Uploaded `CMakeLists.txt`.
- Uploaded YAML files.
- Uploaded Python files.
- Uploaded C++ files.
- Rule-based analysis for common ROS 1 Noetic errors.
- Rule-based analysis for common ROS 2 Humble errors.
- Structured diagnosis output.
- Beginner-friendly explanations and next steps.
- FastAPI backend.
- React frontend.
- AI-provider abstraction for future LLM support.

## Out Of Scope

- Robot hardware integration.
- Live ROS graph introspection.
- rosbag parsing.
- Simulation data parsing beyond text-based Gazebo errors.
- Database persistence.
- User accounts.
- Cloud deployment.
- Docker as a required setup path.
- Full LLM-provider integration.

## Initial Error Categories

- Missing package.
- Missing dependency.
- Node not found.
- Wrong topic name.
- Launch file syntax error.
- Missing executable permission.
- `catkin_make` build error.
- `colcon` build error.
- `CMakeLists.txt` issue.
- `package.xml` dependency issue.
- TF frame missing.
- Parameter not found.
- Gazebo plugin load error.
- Python import error.
- `ROS_MASTER_URI` issue.
- ROS 2 DDS/domain issue.

## MVP 1 Success Criteria

- A user can paste terminal output and receive a structured diagnosis.
- A user can upload supported text files and receive a structured diagnosis.
- The diagnosis includes likely causes, suggested fixes, verification commands, confidence, related files, and next debugging steps.
- Setup and usage instructions are clear enough for beginners.
- The project can be developed on Windows without robot hardware.

