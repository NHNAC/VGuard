FROM python:3.12-bookworm

# setting work directory
WORKDIR /usr/src/app

# env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install psycopg dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip pipenv
COPY Pipfile* ./
RUN pipenv install --system --ignore-pipfile

COPY . .
