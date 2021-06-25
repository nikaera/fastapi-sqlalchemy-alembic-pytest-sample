import os

import alembic.config
import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database

from .seed import items, groups, group_items


def migrate_in_memory(migrations_path, alembic_ini_path='alembic.ini', connection=None, revision="head"):
    config = alembic.config.Config(alembic_ini_path)
    config.set_main_option('script_location', migrations_path)
    if connection is not None:
        config.attributes['connection'] = connection
    alembic.command.upgrade(config, revision)


@pytest.fixture(scope="session", autouse=True)
def SessionLocal():
    test_sqlalchemy_database_url = os.environ['DATABASE_URL']
    engine = create_engine(test_sqlalchemy_database_url)

    if database_exists(test_sqlalchemy_database_url):
        drop_database(test_sqlalchemy_database_url)

    create_database(test_sqlalchemy_database_url)

    with engine.begin() as connection:
        migrate_in_memory("migration", 'alembic.ini', connection)

    Base = declarative_base()
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db_session = SessionLocal()

    for group in groups:
        db_session.add(group)

    for item in items:
        db_session.add(item)
    db_session.commit()

    for group_item in group_items:
        db_session.add(group_item)
    db_session.commit()

    db_session.close()

    yield SessionLocal

    drop_database(test_sqlalchemy_database_url)
    engine.dispose()
