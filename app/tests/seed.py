from app.models import Group, GroupItem, Item


def datas_to_models(model, datas):
    models = list()
    for data in datas:
        models.append(model(**data))
    return models

_groups = [{
    "id": "7d60e1d4-a6af-fc52-6355-67c3094479ab",
    "name": "Group1",
    "description": "Group1 description"
}, {
    "id": "218587ed-d548-bd06-d278-43583021c1a9",
    "name": "Group2",
    "description": "Group2 description"
}]

_items = [{
    "id": "555425c2-4aeb-4713-3ef9-d03dc2a837a1",
    "name": "Item1",
}, {
    "id": "9ab921a1-d177-7691-0bb4-b66ef823d9b4",
    "name": "Item2",
}, {
    "id": "e7d35224-0f51-a62a-25af-4d5c930d9085",
    "name": "Item3",
}]

_group_items = [{
    "id": "20062627-ba92-f2da-4ebc-3d73642ac88a",
    "group_id": _groups[0]["id"],
    "item_id": _items[0]["id"]
}, {
    "id": "988092bf-1d2a-46e5-26cc-3868b09ef698",
    "group_id": _groups[0]["id"],
    "item_id": _items[1]["id"]
}, {
    "id": "821aff31-f932-b651-22fe-7e57cebf05ab",
    "group_id": _groups[1]["id"],
    "item_id": _items[2]["id"]
}]

groups = datas_to_models(Group, _groups)
items = datas_to_models(Item, _items)
group_items = datas_to_models(GroupItem, _group_items)