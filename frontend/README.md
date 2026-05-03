# Frontend

This folder contains the React frontend for ROS AI Debugger.

Phase 3.1 creates the frontend skeleton only. The page shows the project title, a short description, and placeholder sections for text input, file upload, and results. It does not connect to the backend yet and does not perform real analysis yet.

## Requirements

Install Node.js first. This project was verified with:

```powershell
node --version
npm --version
```

## Install Dependencies

From the repository root:

```powershell
cd frontend
npm install
```

## Start The Development Server

From the `frontend/` folder:

```powershell
npm run dev
```

The frontend will start locally, usually at:

```text
http://127.0.0.1:5173
```

Open that URL in a browser to see the frontend skeleton.

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

Phase 3.1 does not add a frontend test suite yet. The available frontend check is the build:

```powershell
npm run build
```

If the command finishes without errors, the frontend skeleton builds successfully.

## Current Status

- React with Vite is set up.
- The page has a clean static skeleton.
- Text input, file upload, and results are placeholders only.
- Backend calls are not implemented yet.
- Real analysis UI behavior is not implemented yet.
