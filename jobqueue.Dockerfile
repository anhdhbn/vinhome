FROM python:3.6-alpine

LABEL Author="Anh DH"
LABEL Version="1.0"

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apk update
RUN apk upgrade
RUN apk add bash


CMD [ "/bin/sh", "-c" , "./wait-for-it.sh redis:6379 -t 0 -- celery -A jobqueue.tasks worker -E" ]