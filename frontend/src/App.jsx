const supportedFiles = [
  "logs",
  "launch files",
  "package.xml",
  "CMakeLists.txt",
  "YAML",
  "Python",
  "C++",
];

function App() {
  return (
    <main className="app-shell">
      <section className="hero" aria-labelledby="page-title">
        <p className="eyebrow">MVP 1 frontend skeleton</p>
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
            <span>Placeholder</span>
          </div>
          <textarea
            aria-label="ROS error text placeholder"
            placeholder="Paste ROS terminal output here in a later phase."
            disabled
          />
        </div>

        <div className="panel">
          <div className="panel-heading">
            <h2>File Upload</h2>
            <span>Placeholder</span>
          </div>
          <div className="upload-placeholder">
            <strong>Supported file area</strong>
            <p>{supportedFiles.join(", ")}</p>
          </div>
        </div>

        <div className="panel results-panel">
          <div className="panel-heading">
            <h2>Results</h2>
            <span>Placeholder</span>
          </div>
          <div className="results-placeholder">
            <p>Diagnosis results will appear here after frontend behavior is added.</p>
          </div>
        </div>
      </section>
    </main>
  );
}

export default App;
