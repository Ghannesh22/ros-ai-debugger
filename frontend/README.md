# Frontend

This folder contains the React frontend for ROS AI Debugger.

Phase 3.4 connects the frontend to the backend analysis API. The page can send pasted ROS errors to `POST /analyze/text` and selected files to `POST /analyze/files`.

Full polished result display is planned for Phase 3.5. For now, the frontend shows the structured JSON response from the backend.

## Requirements

Install Node.js first. This project was verified with:

```powershell
node --version
npm --version
```

## Install Dependencies

Install backend dependencies from the repository root:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Open a second terminal, then install frontend dependencies from the repository root:

```powershell
cd frontend
npm install
```

## Start The Backend

From the `backend/` folder:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

The backend should be running at:

```text
http://127.0.0.1:8000
```

Check it in a browser:

```text
http://127.0.0.1:8000/health
```

## Start The Frontend

From the `frontend/` folder:

```powershell
npm run dev
```

The frontend will start locally, usually at:

```text
http://127.0.0.1:5173
```

Open that URL in a browser to see the frontend.

## Change The Backend URL

The frontend uses this backend URL by default:

```text
http://127.0.0.1:8000
```

To use a different backend URL, set `VITE_BACKEND_URL` before starting the frontend:

```powershell
cd frontend
$env:VITE_BACKEND_URL="http://127.0.0.1:8000"
npm run dev
```

## Test Text Analysis Manually

Start the backend in one terminal:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

Start the frontend in another terminal:

```powershell
cd frontend
npm run dev
```

Then open:

```text
http://127.0.0.1:5173
```

In the browser:

- Paste this ROS terminal error into the `ROS terminal error` box:

```text
Package 'demo_nodes_cpp' not found
```

- Optionally enter a filename such as `terminal.txt`.
- Optionally choose `ROS 1` or `ROS 2`.
- Click `Analyze`.

Expected result:

```json
{
  "detected_errors": ["Missing ROS package"],
  "confidence": "high"
}
```

The browser will show the full structured JSON response.

## Test File Analysis Manually

Create a small test file from the repository root:

```powershell
@'
Package 'demo_nodes_cpp' not found
'@ | Set-Content -Path .\sample-error.log
```

Start the backend in one terminal:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

Start the frontend in another terminal:

```powershell
cd frontend
npm run dev
```

In the browser:

- Find the `File Upload` section.
- Click the file picker.
- Select `sample-error.log`.
- Leave the text area empty.
- Click `Analyze`.
- Confirm the selected filenames appear under `Selected files`.

Expected result:

```json
{
  "detected_errors": ["Missing ROS package"],
  "related_files": ["sample-error.log"]
}
```

The browser will show the full structured JSON response.

Supported file types shown in the UI:

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

If both pasted text and files are provided, the frontend uses text analysis for now and shows a note that combined analysis can be added later.

## Build The Frontend

From the `frontend/` folder:

```powershell
npm run build
```

The production build is written to:

```text
frontend/dist/
```

## Preview The Production Build

After running `npm run build`, you can preview the built frontend:

```powershell
npm run preview
```

The preview server will print a local URL, usually:

```text
http://127.0.0.1:4173
```

## Run Checks Or Tests

Phase 3.4 does not add a frontend test suite yet. The available frontend check is the build:

```powershell
npm run build
```

If the command finishes without errors, the frontend builds successfully.

Backend tests can be run from the repository root:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -m pytest
```

## Current Status

- React with Vite is set up.
- The page has a clean text input UI for pasted ROS terminal errors.
- Filename and ROS version hint are local optional fields.
- The page has a local file upload UI for selecting one or more files.
- Selected filenames are shown in the UI.
- The Analyze button calls the backend.
- Pasted text is sent to `POST /analyze/text`.
- Selected files are sent to `POST /analyze/files` when the text area is empty.
- Temporary raw JSON response display is implemented.
- Loading and request error states are implemented.
- Full polished result display is not implemented yet.
