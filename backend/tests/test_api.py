from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

def test_read_all_expenses():
    response = client.get("/expenses")
    assert response.status_code ==200


def test_create_expense():
    expense_data = {
        "title":"test lunch",
        "amount": 150,
        "category": "Food",
        "date": "2026-11-17",
        "notes": "Testing expense creation"

    }

    response = client.post("/expenses", json=expense_data)

    assert response.status_code ==200
    assert response.json()["title"] == "test lunch"
    assert response.json()["amount"] ==150


def test_read_expense_by_id():
    expense_data = {
        "title": "Test Dinner",
        "amount": 200,
        "category": "Food",
        "date": "2026-11-17",
        "notes": "Testing get by ID"
    }

    create_response = client.post("/expenses", json=expense_data)

    expense_id = create_response.json()["id"]

    response = client.get(f"/expenses/{expense_id}")

    assert response.status_code == 200
    assert response.json()["id"] == expense_id
    assert response.json()["title"] == "Test Dinner"


def test_update_expense():
    expense_data = {
        "title": "Old Lunch",
        "amount": 100,
        "category": "Food",
        "date": "2026-11-17",
        "notes": "Old notes"
    }

    create_response = client.post("/expenses", json=expense_data)
    expense_id = create_response.json()["id"]

    updated_data = {
        "title": "Updated Lunch",
        "amount": 250,
        "category": "Food",
        "date": "2026-11-17",
        "notes": "Updated notes"
    }

    response = client.put(
        f"/expenses/{expense_id}",
        json=updated_data
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Lunch"
    assert response.json()["amount"] == 250



def test_delete_expense():
    expense_data = {
        "title": "Temporary Expense",
        "amount": 100,
        "category": "Test",
        "date": "2026-11-17",
        "notes": "Testing deletion"
    }

    create_response = client.post("/expenses", json=expense_data)
    expense_id = create_response.json()["id"]

    response = client.delete(f"/expenses/{expense_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Expense deleted successfully!"

    get_response = client.get(f"/expenses/{expense_id}")
    assert get_response.status_code == 404