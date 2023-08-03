FROM python:3.9.15-slim-buster

COPY requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY . ./app

WORKDIR /app

ENTRYPOINT ["python", "app.py"]
