FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN apt update
RUN apt install -y libpq-dev
RUN pip install fastapi[all] pytest alembic SQLAlchemy==1.3.24 sqlalchemy_utils psycopg2

COPY app/ /app
COPY docker/app/prestart.sh /app/prestart.sh
