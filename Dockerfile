FROM ubuntu:20.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update; apt install -y sudo python3 python3-distutils python3-pip vim nginx
RUN pip3 install django gunicorn
RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /app
