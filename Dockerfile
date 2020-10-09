FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y libgdal-dev && rm -fr /var/lib/apt/lists/*
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

ENTRYPOINT /code/docker/start.sh
