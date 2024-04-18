FROM python:3.4
MAINTAINER OJ999 <7807@holbertonschool.com>

RUN git clone https://github.com/OJ999/AirBnB_clone_v3.git ~/AirBnB
WORKDIR /root/AirBnB
RUN pip3 install virtualenv
RUN pip install -r requirements.txt