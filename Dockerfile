FROM ubuntu:22.04

ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && \
    apt install -y sudo python3 python3-distutils python3-pip

COPY requirements.txt /app/requirements.txt
WORKDIR /app

#RUN pip3 install django gunicorn tzdata
RUN pip3 install -r requirements.txt
RUN ln -s /usr/bin/python3 /usr/bin/python
