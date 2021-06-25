from fastapi import status

from .client import client, temp_db


@temp_db
def test_group_items():
    response = client.get("/group_items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 3

@temp_db
def test_group_item():
    group_id = "988092bf-1d2a-46e5-26cc-3868b09ef698"
    response = client.get(f"/group_items/{group_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json["group_id"] == "7d60e1d4-a6af-fc52-6355-67c3094479ab"
    assert json["item_id"] == "9ab921a1-d177-7691-0bb4-b66ef823d9b4"
