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
    assert response.json() == {
        "summary": "Text received for analysis. Analyzer logic will be added in Phase 2.5.",
        "detected_errors": [],
        "likely_root_causes": [],
        "recommended_fixes": [],
        "verification_commands": [],
        "confidence": "low",
        "ros_version_guess": "unknown",
        "related_files": ["terminal.txt"],
        "next_debugging_steps": [],
    }


def test_analyze_text_rejects_empty_text() -> None:
    client = TestClient(app)

    response = client.post("/analyze/text", json={"text": ""})

    assert response.status_code == 422


def test_analyze_text_uses_ros_version_hint_when_provided() -> None:
    client = TestClient(app)

    response = client.post(
        "/analyze/text",
        json={
            "text": "ros2 launch demo_nodes_cpp talker_listener.launch.py",
            "ros_version_hint": "ROS 2",
        },
    )

    assert response.status_code == 200
    assert response.json()["ros_version_guess"] == "ROS 2"
