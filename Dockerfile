FROM python:3.12.0-slim as base

RUN apt-get update
RUN pip install poetry
RUN apt-get install -y -qq gcc python3-dev

FROM base AS app-install

WORKDIR /app

COPY poetry.lock .
COPY pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY server/ server/

FROM app-install as app_run

EXPOSE 8080

COPY env_vars.sh .
CMD ["/bin/bash", "-c", ". env_vars.sh && python -m server"]
