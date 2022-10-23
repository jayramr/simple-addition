FROM ubuntu:latest
RUN apt-get update && apt-get install python3-pip python3 -y
ADD ./requirements.txt /opt/webapp/
WORKDIR /opt/webapp
RUN pip3 install -r requirements.txt
ADD . /opt/webapp
EXPOSE 8080
CMD python3 /opt/webapp/app.py
