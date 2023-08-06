FROM ubuntu:22.04

ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && \
	apt install -y sudo python3 python3-distutils python3-pip

RUN pip3 install django gunicorn tzdata
RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /app
