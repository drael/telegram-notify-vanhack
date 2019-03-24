FROM python:alpine3.6

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt
WORKDIR /app/app

ENTRYPOINT gunicorn --bind 0.0.0.0:8000 --timeout 160 wsgi:application