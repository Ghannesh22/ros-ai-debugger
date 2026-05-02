# Backend

This folder contains the FastAPI backend skeleton for ROS AI Debugger.

Phase 2.1 creates only the backend foundation. Analyzer logic and API endpoint behavior will be added in later Phase 2 sub-phases.

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

Analyzer logic is not implemented yet. Until Phase 2.5, this endpoint returns a placeholder response.

Endpoint:

```text
POST http://127.0.0.1:8000/analyze/text
```

Example request body:

```json
{
  "text": "Package 'demo_nodes_cpp' not found",
  "filename": "terminal.txt",
  "ros_version_hint": "ROS 2"
}
```

Example placeholder response:

```json
{
  "summary": "Text received for analysis. Analyzer logic will be added in Phase 2.5.",
  "detected_errors": [],
  "likely_root_causes": [],
  "recommended_fixes": [],
  "verification_commands": [],
  "confidence": "low",
  "ros_version_guess": "ROS 2",
  "related_files": ["terminal.txt"],
  "next_debugging_steps": []
}
```

## Try The File Analysis Endpoint

The file analysis endpoint accepts one or more uploaded ROS-related text files and returns the same planned structured response shape.

Uploaded files are treated as text only. The backend does not execute uploaded files.

Analyzer logic is not implemented yet. Until Phase 2.5, this endpoint returns a placeholder response and includes uploaded filenames in `related_files`.

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

Example placeholder response:

```json
{
  "summary": "Files received for analysis. Analyzer logic will be added in Phase 2.5.",
  "detected_errors": [],
  "likely_root_causes": [],
  "recommended_fixes": [],
  "verification_commands": [],
  "confidence": "low",
  "ros_version_guess": "unknown",
  "related_files": ["error.log"],
  "next_debugging_steps": []
}
```

## Run Backend Tests

From the `backend/` folder:

```powershell
pytest
```

## Current Status

- FastAPI app entry point exists.
- API router exists.
- Health endpoint is implemented.
- Analyze text endpoint skeleton is implemented with placeholder response.
- Analyze files endpoint skeleton is implemented with placeholder response.
- Rule-based analyzer logic is not implemented yet.
