from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_calculate_endpoint_returns_deadline_and_reminders():
    response = client.post("/calculate", json={"event_date": "2025-06-02"})

    assert response.status_code == 200
    assert response.json() == {
        "deadline": "2025-06-05",
        "reminders": [
            "2025-06-04",
            "2025-06-02",
            "2025-05-27",
            "2025-05-16",
            "2025-04-18",
        ],
    }


def test_calculate_endpoint_skips_weekends_and_russian_holidays():
    response = client.post("/calculate", json={"event_date": "2025-06-10"})

    assert response.status_code == 200
    assert response.json()["deadline"] == "2025-06-17"


def test_calculate_endpoint_rejects_invalid_date():
    response = client.post("/calculate", json={"event_date": "abracadabra"})

    assert response.status_code == 422


def test_calculate_endpoint_requires_event_date():
    response = client.post("/calculate", json={})

    assert response.status_code == 422
