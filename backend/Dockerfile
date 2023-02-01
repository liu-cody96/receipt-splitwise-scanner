FROM python:3.11.0-slim-bullseye
MAINTAINER Cody Liu <liu.cody@gmail.com>

ENV INSTALL_PATH /receiptscanner
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "receiptscanner.app:main_app"
