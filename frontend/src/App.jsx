import { useState } from "react";
import { BACKEND_URL, analyzeFiles, analyzeText } from "./api.js";

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
  const [analysisResult, setAnalysisResult] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [statusMessage, setStatusMessage] = useState("");

  async function handleAnalyze(event) {
    event.preventDefault();
    const trimmedText = errorText.trim();
    const hasFiles = selectedFiles.length > 0;

    setAnalysisResult(null);
    setErrorMessage("");
    setStatusMessage("");

    if (!trimmedText && !hasFiles) {
      setErrorMessage("Paste ROS error text or select at least one file first.");
      return;
    }

    setIsLoading(true);

    try {
      if (trimmedText) {
        const response = await analyzeText({
          text: trimmedText,
          filename: filename.trim(),
          rosVersionHint,
        });
        setAnalysisResult(response);
        setStatusMessage(
          hasFiles
            ? "Text analysis was used. Combined text and file analysis can be added later."
            : "Text analysis complete.",
        );
      } else {
        const response = await analyzeFiles({
          files: selectedFiles,
          rosVersionHint,
        });
        setAnalysisResult(response);
        setStatusMessage("File analysis complete.");
      }
    } catch (error) {
      setErrorMessage(error.message);
    } finally {
      setIsLoading(false);
    }
  }

  function handleFileSelection(event) {
    setSelectedFiles(Array.from(event.target.files));
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
        <div className="api-banner">
          <strong>Backend API</strong>
          <span>{BACKEND_URL}</span>
        </div>

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

            <button type="submit" disabled={isLoading}>
              {isLoading ? "Analyzing..." : "Analyze"}
            </button>
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
                    <li key={`${selectedFile.name}-${index}`}>
                      {selectedFile.name}
                    </li>
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
            <span>{analysisResult ? "API Response" : "Waiting"}</span>
          </div>
          <div className="results-placeholder" aria-live="polite">
            {isLoading && <p>Analyzing input with the backend...</p>}

            {!isLoading && errorMessage && (
              <div className="message error-message">
                <strong>Request failed</strong>
                <p>{errorMessage}</p>
              </div>
            )}

            {!isLoading && statusMessage && !errorMessage && (
              <div className="message success-message">
                <strong>Status</strong>
                <p>{statusMessage}</p>
              </div>
            )}

            {!isLoading && analysisResult && (
              <pre>{JSON.stringify(analysisResult, null, 2)}</pre>
            )}

            {!isLoading && !errorMessage && !analysisResult && !statusMessage && (
              <p>
                Paste ROS error text or select files, then click Analyze to call
                the backend.
              </p>
            )}
          </div>
        </div>
      </section>
    </main>
  );
}

export default App;
