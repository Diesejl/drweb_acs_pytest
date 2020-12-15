FROM python:3.7-slim

WORKDIR /drweb_acs_pytest

COPY requirements.txt /drweb_acs_pytest/
RUN pip install -r /drweb_acs_pytest/requirements.txt
COPY . /drweb_acs_pytest/

CMD pytest smoke_test.py
