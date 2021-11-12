FROM python:3.9
MAINTAINER Robbe Van Herck <robbe@robbevanherck.be>

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY static/ /app/static
COPY templates/ /app/templates
COPY *.py /app/

RUN python init_db.py
ENTRYPOINT python jhdag2019.py
