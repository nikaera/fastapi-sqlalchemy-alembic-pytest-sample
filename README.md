# fastapi-sqlalchemy-alembic-pytest-sample
Sample project using [alembic](https://github.com/alembic/alembic) in [FastAPI](https://github.com/tiangolo/fastapi) + [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) project at pytest runtime.

## Getting Started 💨

The environment variables required at runtime are listed below, if you want to use [Docker Compose](https://docs.docker.jp/compose/toc.html), you don't need to use it because it already has its own [`.env` file](https://github.com/nikaera/fastapi-sqlalchemy-alembic-pytest-sample/blob/main/docker/.env).

```bash
# .envrc
export POSTGRES_USER=fastapi_pytest
export POSTGRES_PASSWORD=fastapi_pytest
export POSTGRES_DB=fastapi_pytest_development

export DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:5432/${POSTGRES_DB}
```

When running locally, execute the following command on the PostgreSQL server you want to connect to beforehand, but not when running Docker.
```sql
# psql -h localhost postgres
CREATE USER fastapi_pytest WITH PASSWORD 'fastapi_pytest';
ALTER ROLE fastapi_pytest CREATEDB;
CREATE DATABASE fastapi_pytest_development;
```

If you want to quickly verify the operation with Docker Compose, please refer to the following.

```bash
# Checking the operation with docker-compose
docker compose up --abort-on-container-exit --exit-code-from app

# clean up after docker-compose
docker compose down --rmi all --volumes --remove-orphans
```


