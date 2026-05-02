# ROS AI Debugger System Architecture

## 1. High-Level Architecture

ROS AI Debugger is a simple web application for analyzing ROS debugging text.

The basic flow is:

User -> Frontend -> Backend -> Analyzer -> Response -> Frontend

In plain language:

- The user pastes an error or uploads files in the frontend.
- The frontend sends the input to the backend.
- The backend prepares the input for analysis.
- The analyzer looks for ROS-specific error patterns.
- The backend formats the diagnosis as structured JSON.
- The frontend displays the result in beginner-friendly sections.

MVP 1 does not connect to a robot, run ROS commands, or inspect a live ROS system. It only analyzes text that the user provides.

## 2. System Components

### Frontend (UI)

The frontend is the user-facing part of the application.

It will provide:

- A text area for pasted ROS terminal errors.
- A file upload area for logs and ROS project files.
- A submit action to send the input to the backend.
- A results view that shows the diagnosis, likely causes, suggested fixes, verification commands, confidence, and next steps.

The frontend should be simple and readable. It should help beginners understand the result without needing to read raw JSON.

### Backend API (FastAPI)

The backend API receives requests from the frontend and returns structured diagnosis results.

FastAPI will provide:

- Clear HTTP endpoints.
- Request validation.
- Structured JSON responses.
- A simple health endpoint for checking that the backend is running.

The backend should not contain all analyzer logic directly inside route handlers. Routes should receive requests and pass the work to focused backend modules.

### Input Handler

The input handler prepares user input before analysis.

It will:

- Accept pasted text.
- Accept uploaded files.
- Track filenames when files are uploaded.
- Detect simple file types from filenames and extensions.
- Reject or ignore unsupported content when needed.

For MVP 1, input handling should stay conservative. It should treat uploads as text and should not execute uploaded files.

### File Parser

The file parser extracts useful text from supported files.

Supported MVP 1 file types include:

- ROS logs.
- Launch files.
- `package.xml`.
- `CMakeLists.txt`.
- YAML files.
- Python files.
- C++ files.

For MVP 1, parsing can be lightweight. The parser does not need to fully understand every file format. It should preserve useful text, file names, and simple metadata so the analyzer can make better decisions.

### ROS Analyzer Engine

The ROS analyzer engine coordinates the diagnosis process.

It receives normalized text and related file information, then runs the analyzer pipeline:

- Normalize input.
- Extract error patterns.
- Classify errors.
- Infer likely root causes.
- Generate fix suggestions.
- Generate verification commands.
- Produce a structured diagnosis.

This engine is the core ROS-specific part of the backend.

### Rule-Based Detector (MVP 1)

The rule-based detector is the first analyzer implementation.

It will look for known patterns such as:

- Missing package errors.
- Missing dependency errors.
- Node not found errors.
- Launch file syntax errors.
- `catkin_make` and `colcon` build errors.
- `package.xml` and `CMakeLists.txt` issues.
- TF frame missing errors.
- Gazebo plugin load errors.
- Python import errors.
- `ROS_MASTER_URI` problems.
- ROS 2 DDS or domain problems.

Rule-based detection is a good MVP choice because it is predictable, testable, and easy to explain.

### AI Analysis Layer (Abstracted, Optional For MVP)

The AI analysis layer is a future-facing abstraction.

In MVP 1, the main diagnosis should come from the rule-based detector. The AI layer can exist as an interface or placeholder so the project can later add an LLM provider without rewriting the backend.

Later, the AI layer may help with:

- Explaining errors in more natural language.
- Ranking possible root causes.
- Summarizing multiple files.
- Suggesting debugging plans for complex cases.

The analyzer should still work without an AI provider.

### Response Formatter

The response formatter converts analyzer results into the final response shape used by the frontend.

It should produce consistent fields:

- `summary`
- `detected_errors`
- `likely_root_causes`
- `recommended_fixes`
- `verification_commands`
- `confidence`
- `ros_version_guess`
- `related_files`
- `next_debugging_steps`

This keeps the frontend simple because it can always expect the same response format.

## 3. Data Flow

1. User submits input.

   The user pastes terminal output or uploads one or more supported text files.

2. Backend receives request.

   The frontend sends the request to the FastAPI backend using the text endpoint or file endpoint.

3. Input handler detects file types.

   The backend checks whether the input is pasted text or uploaded files. For files, it records file names and detects likely types such as log, launch, XML, CMake, YAML, Python, or C++.

4. Parser extracts useful information.

   The parser reads text from supported files and keeps useful context such as filenames, extensions, and recognizable ROS file content.

5. Analyzer processes errors.

   The analyzer receives normalized text plus file context and prepares it for ROS-specific detection.

6. Rule-based engine detects patterns.

   The MVP 1 detector scans for known error patterns and maps them to ROS error categories.

7. AI layer enhances reasoning.

   This is optional for MVP 1. If enabled later, it can improve explanations or reasoning, but the system should still work without it.

8. Response formatter structures output.

   The backend formats the result into the standard JSON response fields.

9. Frontend displays results.

   The frontend shows the diagnosis in readable sections so the user can understand the issue and try the suggested verification commands.

## 4. Analyzer Pipeline Design

### Input Normalization

Input normalization prepares raw user text for analysis.

It may:

- Normalize line endings.
- Trim very large empty sections.
- Preserve important file names and line references.
- Combine pasted text and file text into a consistent internal format.

The goal is to make analysis easier without losing useful debugging details.

### Pattern Extraction

Pattern extraction finds meaningful clues in the input.

Examples:

- Commands such as `roslaunch`, `ros2 launch`, `catkin_make`, or `colcon build`.
- Error phrases such as `package not found`, `No module named`, or `Could not load library`.
- File references such as `package.xml`, `CMakeLists.txt`, `.launch`, `.py`, or `.yaml`.
- ROS concepts such as node names, topic names, frame names, and parameters.

### Error Classification

Error classification maps extracted clues to known ROS error categories.

Example categories:

- Missing package.
- Missing dependency.
- Node not found.
- Launch file syntax error.
- Python import error.
- TF frame missing.
- Gazebo plugin load error.

Classification should stay transparent. If a rule matched, the backend should be able to explain why.

### Root Cause Inference

Root cause inference explains what probably caused the detected error.

For example:

- A package-not-found error after building may mean the workspace was not sourced.
- A Python import error may mean a missing dependency or wrong Python environment.
- A node-not-found error may mean the executable was not installed, built, or named correctly.

MVP 1 should use simple, practical reasoning rather than pretending to know the whole system.

### Fix Suggestion Generation

Fix suggestion generation turns the likely root cause into clear actions.

Examples:

- Source the workspace setup file.
- Install a missing dependency.
- Rebuild with `catkin_make` or `colcon build`.
- Check the package name.
- Check executable permissions.
- Correct a launch file node name.

Suggestions should be beginner-friendly and safe. The tool should not automatically edit files or run commands.

### Verification Command Generation

Verification commands help the user confirm whether a fix worked.

Examples:

- `rospack find <package_name>`
- `roscd <package_name>`
- `catkin_make`
- `source devel/setup.bash`
- `colcon build`
- `source install/setup.bash`
- `ros2 pkg list`
- `ros2 launch <package_name> <launch_file>`
- `ros2 topic list`

Commands may be Linux/ROS environment commands even though the project itself should remain Windows-development friendly.

## 5. Backend API Design

### `POST /analyze/text`

Analyzes pasted terminal output or copied error text.

Request behavior:

- Accepts text input from the frontend.
- May accept optional metadata such as a filename or ROS version hint later.
- Does not require uploaded files.

Response behavior:

- Returns the standard diagnosis JSON response.
- Returns a low-confidence or empty diagnosis if no known pattern is detected.

### `POST /analyze/files`

Analyzes one or more uploaded files.

Request behavior:

- Accepts supported text files.
- Reads file names and text content.
- Treats uploads as text only.
- Does not execute uploaded files.

Response behavior:

- Returns the standard diagnosis JSON response.
- Includes related files when file names help explain the diagnosis.

### `GET /health`

Checks whether the backend is running.

Response behavior:

- Returns a simple success response.
- Can be used by developers, tests, and the frontend to confirm backend availability.

## 6. Data Structures

The backend should return a consistent JSON response:

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

Field meanings:

- `summary`: A short explanation of the main issue.
- `detected_errors`: Specific errors or patterns found in the input.
- `likely_root_causes`: The most likely reasons the error happened.
- `recommended_fixes`: Practical steps the user can try.
- `verification_commands`: Commands the user can run to check the fix.
- `confidence`: A simple confidence level such as low, medium, or high.
- `ros_version_guess`: The analyzer's guess, such as ROS 1, ROS 2, or unknown.
- `related_files`: Files that appear relevant to the diagnosis.
- `next_debugging_steps`: What the user should inspect next if the first fix does not work.

## 7. ROS-Specific Design

### How ROS Errors Are Interpreted

ROS errors are interpreted by looking for commands, error phrases, filenames, and ROS concepts.

For example:

- `roslaunch` usually points to ROS 1.
- `ros2 launch` usually points to ROS 2.
- `catkin_make` usually points to a ROS 1 workspace.
- `colcon build` usually points to a ROS 2 workspace.
- TF errors often mention missing frame names.
- Package errors often mention package names that cannot be found.

The analyzer should combine these clues instead of relying on one word.

### How Logs And Launch Files Are Used

Logs can show runtime failures, missing nodes, crashes, plugin errors, or environment problems.

Launch files can show:

- Which package is being launched.
- Which node or executable name is expected.
- Which parameters are loaded.
- Which namespaces or remappings are used.

For MVP 1, launch files are analyzed as text. The system does not need a full launch interpreter.

### How `package.xml` Helps Debugging

`package.xml` helps identify package metadata and dependencies.

It can help answer:

- What is the package name?
- Are required dependencies declared?
- Is a missing dependency absent from the manifest?
- Does the package appear to be ROS 1 or ROS 2 style?

### How `CMakeLists.txt` Helps Debugging

`CMakeLists.txt` helps explain build and executable problems.

It can help answer:

- Are dependencies found with `find_package`?
- Are targets or executables defined?
- Are Python scripts installed correctly?
- Are libraries or plugins installed where ROS expects them?

For MVP 1, this analysis should be rule-based and limited to common patterns.

## 8. MVP Constraints

MVP 1 constraints:

- Rule-based first.
- No real-time ROS integration.
- No hardware dependency.
- No rosbag parsing yet.
- No automatic file editing.
- No automatic command execution.
- No database requirement.
- No required Docker setup.

These constraints keep the first version small, testable, and useful.

## 9. Scalability Plan

The architecture should allow the system to grow without rewriting the whole project.

Future growth paths:

- Add a plugin system for analyzers so ROS, ROS 2, Gazebo, TF, build, and dependency checks can evolve separately.
- Add ML or LLM integration later through the AI analysis abstraction.
- Add multi-file project analysis so users can upload a small package folder or selected project files.
- Add richer parsers for XML, YAML, CMake, Python, and C++ when needed.
- Add support for more ROS distributions.
- Add saved reports or shareable debugging summaries later.

MVP 1 should keep interfaces clean so these ideas remain possible later.

## 10. Design Decisions

### Why FastAPI

FastAPI is a good backend choice because:

- It is Python-based, which fits the ROS ecosystem.
- It supports clear JSON APIs.
- It has good request validation with Pydantic.
- It is simple to test.
- It is beginner-friendly compared with heavier backend frameworks.

### Why Rule-Based First

Rule-based analysis is the right first step because:

- Common ROS errors often have recognizable text patterns.
- Rules are easier to test than AI-only behavior.
- Beginners can understand why a result was returned.
- The project can work without API keys or paid LLM services.
- It creates a reliable baseline before adding AI.

### Why A Modular Pipeline

A modular pipeline keeps the system understandable.

Each part has a clear job:

- Input handling receives text and files.
- Parsing extracts useful content.
- Detection finds patterns.
- Analysis explains likely causes.
- Formatting creates the final response.

This makes the project easier to test, document, and extend without overengineering the MVP.
