from fastapi.testclient import TestClient

from app.main import app


def test_analyze_files_accepts_valid_single_file_upload() -> None:
    client = TestClient(app)

    response = client.post(
        "/analyze/files",
        files={
            "files": (
                "error.log",
                b"Package 'demo_nodes_cpp' not found",
                "text/plain",
            )
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["detected_errors"] == ["Missing ROS package"]
    assert body["confidence"] == "high"
    assert body["related_files"] == ["error.log"]


def test_analyze_files_accepts_valid_multiple_file_uploads() -> None:
    client = TestClient(app)

    response = client.post(
        "/analyze/files",
        files=[
            (
                "files",
                ("terminal.txt", b"roslaunch my_robot bringup.launch", "text/plain"),
            ),
            (
                "files",
                (
                    "package.xml",
                    b"<package><name>my_robot</name></package>",
                    "text/xml",
                ),
            ),
            (
                "files",
                ("CMakeLists.txt", b"find_package(catkin REQUIRED)", "text/plain"),
            ),
        ],
    )

    assert response.status_code == 200
    assert response.json()["related_files"] == [
        "terminal.txt",
        "package.xml",
        "CMakeLists.txt",
    ]


def test_analyze_files_rejects_unsupported_file_type() -> None:
    client = TestClient(app)

    response = client.post(
        "/analyze/files",
        files={"files": ("notes.md", b"# Not supported yet", "text/markdown")},
    )

    assert response.status_code == 400
    assert "Unsupported file type: notes.md" in response.json()["detail"]


def test_analyze_files_rejects_empty_upload_list() -> None:
    client = TestClient(app)

    response = client.post("/analyze/files")

    assert response.status_code == 400
    assert response.json()["detail"] == "At least one file must be uploaded."
