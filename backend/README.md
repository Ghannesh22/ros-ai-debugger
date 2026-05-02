# Backend

This folder contains the FastAPI backend for ROS AI Debugger.

Phase 2 completes the backend MVP analyzer. The backend detects common ROS and ROS 2 error patterns from pasted text and uploaded text files, then returns a consistent JSON diagnosis. It does not use an LLM yet.

## Structure

```text
backend/
  app/
    main.py
    api/
      routes/
    core/
    services/
    models/
  tests/
  requirements.txt
  pyproject.toml
```

## Local Setup

From the repository root:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run The Backend

From the `backend/` folder:

```powershell
uvicorn app.main:app --reload
```

The backend will start locally, usually at:

```text
http://127.0.0.1:8000
```

## Check The Health Endpoint

After starting the backend, open this URL in a browser or send a request:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "ros-ai-debugger-backend"
}
```

## Try The Text Analysis Endpoint

The text analysis endpoint accepts pasted text and returns the planned structured response shape.

The endpoint now uses the first rule-based analyzer. If a known ROS error pattern is found, the response includes detected errors, likely causes, fixes, verification commands, confidence, and next steps.

Endpoint:

```text
POST http://127.0.0.1:8000/analyze/text
```

Example request body:

```json
{
  "text": "Resource not found: demo_nodes_cpp",
  "filename": "terminal.txt",
  "ros_version_hint": "ROS 2"
}
```

Example response:

```json
{
  "summary": "A ROS package appears to be missing or unavailable to the current environment.",
  "detected_errors": ["Missing ROS package"],
  "likely_root_causes": [
    "The package is not installed.",
    "The workspace was not built.",
    "The workspace setup file was not sourced.",
    "The package name may be misspelled.",
    "ROS 1 and ROS 2 commands or environments may be mixed."
  ],
  "recommended_fixes": [
    "Check the package name for spelling.",
    "Install the missing ROS package or dependency.",
    "Rebuild the workspace.",
    "Source the correct setup file for the workspace."
  ],
  "verification_commands": [
    "rospack find <package_name>",
    "roscd <package_name>",
    "ros2 pkg list",
    "ros2 pkg prefix <package_name>",
    "source devel/setup.bash",
    "source install/setup.bash"
  ],
  "confidence": "high",
  "ros_version_guess": "ROS 2",
  "related_files": ["terminal.txt"],
  "next_debugging_steps": [
    "Confirm whether the package should come from apt, source code, or another workspace.",
    "Check that the terminal is sourced for the right ROS distribution."
  ]
}
```

## Structured Analysis Response

Both analysis endpoints return the same JSON shape:

```json
{
  "summary": "Short explanation of the most likely issue.",
  "detected_errors": ["Detected ROS error category"],
  "likely_root_causes": ["Likely reason the issue happened"],
  "recommended_fixes": ["Practical fix the user can try"],
  "verification_commands": ["Command the user can run to verify"],
  "confidence": "high",
  "ros_version_guess": "ROS 1, ROS 2, or unknown",
  "related_files": ["filename.log"],
  "next_debugging_steps": ["What to inspect next"]
}
```

Field meanings:

- `summary`: Beginner-friendly explanation of the main issue.
- `detected_errors`: One or more detected ROS error categories.
- `likely_root_causes`: Practical reasons the error may have happened.
- `recommended_fixes`: Safe actions the user can try manually.
- `verification_commands`: Commands to run in the user's ROS environment.
- `confidence`: `high`, `medium`, or `low`.
- `ros_version_guess`: Best guess from user hint, command context, or matched rule.
- `related_files`: Uploaded or provided filenames related to the diagnosis.
- `next_debugging_steps`: Useful follow-up checks if the first fix does not work.

Confidence behavior:

- `high`: Strong exact pattern match, such as `Resource not found`, `ModuleNotFoundError`, or `Failed <<<`.
- `medium`: Partial or weaker match, such as text mentioning a missing executable without the exact ROS error line.
- `low`: Unknown input or no useful rule match.

Unknown input still returns the same JSON shape with beginner-friendly next steps.

## Try The File Analysis Endpoint

The file analysis endpoint accepts one or more uploaded ROS-related text files and returns the same planned structured response shape.

Uploaded files are treated as text only. The backend does not execute uploaded files.

The endpoint reads uploaded file content as text, passes it to the rule-based analyzer, and includes uploaded filenames in `related_files`.

Endpoint:

```text
POST http://127.0.0.1:8000/analyze/files
```

Supported files:

- `.txt`
- `.log`
- `.launch`
- `.xml`
- `.yaml`
- `.yml`
- `.py`
- `.cpp`
- `CMakeLists.txt`
- `package.xml`

Example PowerShell request:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/analyze/files" `
  -Method Post `
  -Form @{ files = Get-Item ".\error.log" }
```

Example response:

```json
{
  "summary": "A ROS package appears to be missing or unavailable to the current environment.",
  "detected_errors": ["Missing ROS package"],
  "likely_root_causes": [
    "The package is not installed.",
    "The workspace was not built.",
    "The workspace setup file was not sourced.",
    "The package name may be misspelled.",
    "ROS 1 and ROS 2 commands or environments may be mixed."
  ],
  "recommended_fixes": [
    "Check the package name for spelling.",
    "Install the missing ROS package or dependency.",
    "Rebuild the workspace.",
    "Source the correct setup file for the workspace."
  ],
  "verification_commands": [
    "rospack find <package_name>",
    "roscd <package_name>",
    "ros2 pkg list",
    "ros2 pkg prefix <package_name>",
    "source devel/setup.bash",
    "source install/setup.bash"
  ],
  "confidence": "high",
  "ros_version_guess": "unknown",
  "related_files": ["error.log"],
  "next_debugging_steps": [
    "Confirm whether the package should come from apt, source code, or another workspace.",
    "Check that the terminal is sourced for the right ROS distribution."
  ]
}
```

## Current Rule-Based Analyzer Coverage

The first rule-based analyzer detects these MVP rules:

- Missing ROS package
- Node/executable not found
- Python import error
- TF frame missing
- Gazebo plugin load error
- catkin_make build error
- colcon build error
- ROS_MASTER_URI issue
- ROS 2 DDS or ROS_DOMAIN_ID issue

Unknown input returns low confidence with practical next debugging steps.

## Run Backend Tests

From the `backend/` folder:

```powershell
python -m pytest
```

The tests cover:

- `GET /health`
- `POST /analyze/text`
- `POST /analyze/files`
- Upload validation
- Rule-based analyzer categories
- Unknown/no-match analyzer behavior
- Structured response schema consistency

To confirm Python files compile:

```powershell
python -m py_compile app\main.py app\api\routes\analyze.py app\api\routes\health.py app\services\ros_analyzer.py app\models\analysis.py
```

## Current Status

- FastAPI app entry point exists.
- API router exists.
- Health endpoint is implemented.
- Analyze text endpoint is connected to the first rule-based analyzer.
- Analyze files endpoint is connected to the first rule-based analyzer.
- Rule-based analyzer logic covers the first MVP error categories listed above.
- Structured responses are validated with typed Pydantic models.
- LLM-based analysis is not implemented yet.
