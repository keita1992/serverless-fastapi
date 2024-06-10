FROM python:3.9-slim

COPY ./src/Pipfile /app/Pipfile
COPY ./src/Pipfile.lock /app/Pipfile.lock

RUN pip install --no-cache-dir pipenv
RUN cd /app && pipenv sync

WORKDIR /app