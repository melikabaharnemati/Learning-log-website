FROM python:3.10.11-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apt-get update && apt-get install -y build-essential libpq-dev
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .