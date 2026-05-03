from fastapi.testclient import TestClient


def test_health_endpoint_returns_service_status(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "ros-ai-debugger-backend",
    }


def test_backend_allows_local_frontend_origin(client: TestClient) -> None:
    response = client.options(
        "/analyze/text",
        headers={
            "Origin": "http://127.0.0.1:5173",
            "Access-Control-Request-Method": "POST",
        },
    )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == (
        "http://127.0.0.1:5173"
    )
