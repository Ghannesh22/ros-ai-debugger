const DEFAULT_BACKEND_URL = "http://127.0.0.1:8000";

export const BACKEND_URL = (
  import.meta.env.VITE_BACKEND_URL || DEFAULT_BACKEND_URL
).replace(/\/$/, "");

async function parseApiResponse(response) {
  const responseBody = await response.json().catch(() => null);

  if (!response.ok) {
    const detail = responseBody?.detail;
    const message =
      typeof detail === "string"
        ? detail
        : "The backend request failed. Check that the backend is running.";
    throw new Error(message);
  }

  return responseBody;
}

export async function analyzeText({ text, filename, rosVersionHint }) {
  const response = await fetch(`${BACKEND_URL}/analyze/text`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text,
      filename: filename || null,
      ros_version_hint: rosVersionHint || null,
    }),
  });

  return parseApiResponse(response);
}

export async function analyzeFiles({ files, rosVersionHint }) {
  const formData = new FormData();

  files.forEach((file) => {
    formData.append("files", file);
  });

  if (rosVersionHint) {
    formData.append("ros_version_hint", rosVersionHint);
  }

  const response = await fetch(`${BACKEND_URL}/analyze/files`, {
    method: "POST",
    body: formData,
  });

  return parseApiResponse(response);
}
