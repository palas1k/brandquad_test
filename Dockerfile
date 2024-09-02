FROM python:3.12-alpine

COPY requirements.txt /temp/requirements.txt

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password brnduser
COPY . /brandquad
WORKDIR /brandquad
EXPOSE 8000

USER brnduser