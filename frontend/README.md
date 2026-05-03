# Frontend

This folder contains the React frontend for ROS AI Debugger.

Phase 3.2 adds the pasted ROS error text input UI. The page has a text area, optional filename field, optional ROS version hint, and an Analyze button. The button only shows a local placeholder message for now.

The frontend does not connect to the backend yet, does not send API requests yet, and does not implement file upload yet.

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

Open that URL in a browser to see the frontend.

## Verify The Text Input UI

Start the development server:

```powershell
cd frontend
npm run dev
```

Then open:

```text
http://127.0.0.1:5173
```

In the browser:

- Paste a ROS terminal error into the `ROS terminal error` box.
- Optionally enter a filename such as `terminal.txt`.
- Optionally choose `ROS 1` or `ROS 2`.
- Click `Analyze`.

Expected result:

```text
Backend connection will be added in Phase 3.4.
```

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

Phase 3.2 does not add a frontend test suite yet. The available frontend check is the build:

```powershell
npm run build
```

If the command finishes without errors, the frontend skeleton builds successfully.

## Current Status

- React with Vite is set up.
- The page has a clean text input UI for pasted ROS terminal errors.
- Filename and ROS version hint are local optional fields.
- The Analyze button shows a local placeholder message.
- File upload is still a placeholder only.
- Backend calls are not implemented yet.
- Real analysis behavior is not implemented yet.
