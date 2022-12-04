FROM python:3.11

RUN apt-get update
RUN apt-get install apt-file -y
RUN apt-file update
RUN apt-get install vim -y

COPY docker/requirements.txt /tmp/requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /tmp/requirements.txt

ENV HISTCONTROL=ignoreboth:erasedups
