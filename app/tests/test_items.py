from fastapi import status

from .client import client, temp_db


@temp_db
def test_items():
    response = client.get("/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 3

@temp_db
def test_item():
    item_id = "e7d35224-0f51-a62a-25af-4d5c930d9085"
    response = client.get(f"/items/{item_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json["name"] == "Item3"
