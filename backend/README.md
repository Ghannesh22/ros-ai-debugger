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

## Current Status

- FastAPI app entry point exists.
- API router placeholder exists.
- Health endpoint is not implemented yet.
- Analyze text endpoint is not implemented yet.
- Analyze files endpoint is not implemented yet.
- Rule-based analyzer logic is not implemented yet.

