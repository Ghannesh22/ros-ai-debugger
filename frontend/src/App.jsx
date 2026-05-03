import { useState } from "react";

const supportedFileTypes = [
  ".txt",
  ".log",
  ".launch",
  ".xml",
  ".yaml",
  ".yml",
  ".py",
  ".cpp",
  "CMakeLists.txt",
  "package.xml",
];

function App() {
  const [errorText, setErrorText] = useState("");
  const [filename, setFilename] = useState("");
  const [rosVersionHint, setRosVersionHint] = useState("");
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [statusMessage, setStatusMessage] = useState("");

  function handleAnalyze(event) {
    event.preventDefault();
    setStatusMessage("Backend connection will be added in Phase 3.4.");
  }

  function handleFileSelection(event) {
    const filenames = Array.from(event.target.files, (file) => file.name);
    setSelectedFiles(filenames);
  }

  return (
    <main className="app-shell">
      <section className="hero" aria-labelledby="page-title">
        <p className="eyebrow">MVP 1 frontend</p>
        <h1 id="page-title">ROS AI Debugger</h1>
        <p className="subtitle">
          Analyze ROS errors, logs, and project files with beginner-friendly
          guidance for likely causes, fixes, and verification steps.
        </p>
      </section>

      <section className="workspace" aria-label="Debugger workspace">
        <div className="panel">
          <div className="panel-heading">
            <h2>Text Input</h2>
            <span>Local UI</span>
          </div>
          <form className="debug-form" onSubmit={handleAnalyze}>
            <label className="field">
              <span>ROS terminal error</span>
              <textarea
                aria-label="ROS terminal error"
                placeholder="Paste a ROS error here, for example: Resource not found: demo_nodes_cpp"
                value={errorText}
                onChange={(event) => setErrorText(event.target.value)}
              />
            </label>

            <div className="metadata-grid">
              <label className="field">
                <span>Filename optional</span>
                <input
                  aria-label="Optional filename"
                  placeholder="terminal.txt"
                  type="text"
                  value={filename}
                  onChange={(event) => setFilename(event.target.value)}
                />
              </label>

              <label className="field">
                <span>ROS version hint optional</span>
                <select
                  aria-label="Optional ROS version hint"
                  value={rosVersionHint}
                  onChange={(event) => setRosVersionHint(event.target.value)}
                >
                  <option value="">Not sure</option>
                  <option value="ROS 1">ROS 1</option>
                  <option value="ROS 2">ROS 2</option>
                </select>
              </label>
            </div>

            <button type="submit">Analyze</button>
          </form>
        </div>

        <div className="panel">
          <div className="panel-heading">
            <h2>File Upload</h2>
            <span>Local UI</span>
          </div>
          <div className="upload-area">
            <label className="field">
              <span>ROS logs and project files</span>
              <input
                aria-label="Select ROS log and project files"
                type="file"
                multiple
                accept=".txt,.log,.launch,.xml,.yaml,.yml,.py,.cpp"
                onChange={handleFileSelection}
              />
            </label>

            <div className="supported-types">
              <strong>Supported file types</strong>
              <ul>
                {supportedFileTypes.map((fileType) => (
                  <li key={fileType}>{fileType}</li>
                ))}
              </ul>
            </div>

            <div className="selected-files" aria-live="polite">
              <strong>Selected files</strong>
              {selectedFiles.length > 0 ? (
                <ul>
                  {selectedFiles.map((selectedFile, index) => (
                    <li key={`${selectedFile}-${index}`}>{selectedFile}</li>
                  ))}
                </ul>
              ) : (
                <p>No files selected yet.</p>
              )}
            </div>
          </div>
        </div>

        <div className="panel results-panel">
          <div className="panel-heading">
            <h2>Results</h2>
            <span>Placeholder</span>
          </div>
          <div className="results-placeholder">
            <p>
              {statusMessage ||
                "Diagnosis results will appear here after the backend is connected."}
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}

export default App;
