FROM python:3.7-buster

RUN pip install flask sqlalchemy psycopg2

WORKDIR app/

COPY . .

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

ENV FLASK_DEBUG 1

CMD ["flask", "run"]
