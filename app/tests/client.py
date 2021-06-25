from fastapi import Header, HTTPException, status
from fastapi.testclient import TestClient

from app.dependencies import get_database
from app.main import app


def temp_db(f):
    def func(SessionLocal, *args, **kwargs):
        def override_get_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()

        app.dependency_overrides[get_database] = override_get_db
        f(*args, **kwargs)
        app.dependency_overrides[get_database] = get_database

    return func


client = TestClient(app)