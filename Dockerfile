FROM python:3.8-slim

# set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR 1
ENV PIP_IGNORE_INSTALLED 1
ENV VENV_PATH=/opt/env
ENV PATH="$VENV_PATH/bin:$PATH"

WORKDIR /opt/invoicing

COPY . .
# upgrade pip
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && python -m venv ENV_DIR $VENV_PATH \
    && pip install -U pip \
    && pip install -e . \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
