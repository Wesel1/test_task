from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_calculate_endpoint():
    response = client.post(
        "/calculate",
        json={
            "event_date": "2025-06-02"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["deadline"] == "2025-06-05"

    assert len(data["reminders"]) == 5

def test_response_contains_required_fields():
    response = client.post(
        "/calculate",
        json={
            "event_date": "2025-06-02"
        }
    )

    data = response.json()

    assert "deadline" in data
    assert "reminders" in data

def test_invalid_date():
    response = client.post(
        "/calculate",
        json={
            "event_date": "abracadabra"
        }
    )

    assert response.status_code == 422

def test_missing_event_date():
    response = client.post(
        "/calculate",
        json={}
    )

    assert response.status_code == 422