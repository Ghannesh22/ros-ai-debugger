from fastapi.testclient import TestClient

from tests.helpers import assert_analysis_response_shape


def test_analyze_text_accepts_valid_text_input(client: TestClient) -> None:
    response = client.post(
        "/analyze/text",
        json={
            "text": "Package 'demo_nodes_cpp' not found",
            "filename": "terminal.txt",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert_analysis_response_shape(body)
    assert body["detected_errors"] == ["Missing ROS package"]
    assert body["confidence"] == "high"
    assert body["related_files"] == ["terminal.txt"]


def test_analyze_text_rejects_empty_text(client: TestClient) -> None:
    response = client.post("/analyze/text", json={"text": ""})

    assert response.status_code == 422


def test_analyze_text_uses_ros_version_hint_when_provided(client: TestClient) -> None:
    response = client.post(
        "/analyze/text",
        json={
            "text": "The robot is not moving.",
            "ros_version_hint": "ROS 2",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert_analysis_response_shape(body)
    assert body["confidence"] == "low"
    assert body["ros_version_guess"] == "ROS 2"


def test_analyze_text_unknown_input_returns_useful_low_confidence_response(
    client: TestClient,
) -> None:
    response = client.post(
        "/analyze/text",
        json={"text": "The robot behaves strangely after startup."},
    )

    assert response.status_code == 200
    body = response.json()
    assert_analysis_response_shape(body)
    assert body["summary"] == "No known ROS error pattern was detected."
    assert body["detected_errors"] == []
    assert body["confidence"] == "low"
    assert body["recommended_fixes"]
    assert body["next_debugging_steps"]
