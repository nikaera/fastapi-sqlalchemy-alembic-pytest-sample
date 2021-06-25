from uuid import UUID
from typing import Optional
from sqlalchemy.orm import Session

from app import models
from app.dependencies import get_database
from fastapi import FastAPI, Depends

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_item(db: Session = Depends(get_database)):
    return db.query(models.Item).all()

@app.get("/items/{item_id}")
def read_item(item_id: UUID, db: Session = Depends(get_database)):
    return db.query(models.Item).get(item_id)

@app.get("/groups")
def read_group(db: Session = Depends(get_database)):
    return db.query(models.Group).all()

@app.get("/groups/{group_id}")
def read_group(group_id: UUID, db: Session = Depends(get_database)):
    return db.query(models.Group).get(group_id)

@app.get("/groups/{group_id}/items")
def read_group(group_id: UUID, db: Session = Depends(get_database)):
    return db.query(models.Group).get(group_id).items

@app.get("/group_items")
def read_group(db: Session = Depends(get_database)):
    return db.query(models.GroupItem).all()

@app.get("/group_items/{group_item_id}")
def read_group(group_item_id: UUID, db: Session = Depends(get_database)):
    return db.query(models.GroupItem).get(group_item_id)