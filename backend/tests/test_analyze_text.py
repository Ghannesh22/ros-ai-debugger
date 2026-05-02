from fastapi.testclient import TestClient

from app.main import app


def test_analyze_text_accepts_valid_text_input() -> None:
    client = TestClient(app)

    response = client.post(
        "/analyze/text",
        json={
            "text": "Package 'demo_nodes_cpp' not found",
            "filename": "terminal.txt",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["detected_errors"] == ["Missing ROS package"]
    assert body["confidence"] == "high"
    assert body["related_files"] == ["terminal.txt"]


def test_analyze_text_rejects_empty_text() -> None:
    client = TestClient(app)

    response = client.post("/analyze/text", json={"text": ""})

    assert response.status_code == 422


def test_analyze_text_uses_ros_version_hint_when_provided() -> None:
    client = TestClient(app)

    response = client.post(
        "/analyze/text",
        json={
            "text": "The robot is not moving.",
            "ros_version_hint": "ROS 2",
        },
    )

    assert response.status_code == 200
    assert response.json()["ros_version_guess"] == "ROS 2"
