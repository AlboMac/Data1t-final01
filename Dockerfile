FROM python:3.9-slim-buster

WORKDIR /app

ADD . /app

ENTRYPOINT ["python", "app.py"]
