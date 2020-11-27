FROM python:3.9

COPY docker/requirements.txt /tmp/requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /tmp/requirements.txt
