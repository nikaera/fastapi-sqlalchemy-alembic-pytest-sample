from fastapi import status

from .client import client, temp_db


@temp_db
def test_groups():
    response = client.get("/groups")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group():
    group_id = "218587ed-d548-bd06-d278-43583021c1a9"
    response = client.get(f"/groups/{group_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json["name"] == "Group2"
    assert json["description"] == "Group2 description"

@temp_db
def test_group_items_1():
    group_id = "7d60e1d4-a6af-fc52-6355-67c3094479ab"
    response = client.get(f"/groups/{group_id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group_items_2():
    group_id = "218587ed-d548-bd06-d278-43583021c1a9"
    response = client.get(f"/groups/{group_id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 1

