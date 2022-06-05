FROM python:3.10-slim-buster

RUN apt update && apt upgrade -y

RUN apt install python3-pip -y

RUN apt install ffmpeg -y

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -

RUN apt-get install -y nodejs

RUN npm i -g npm

RUN mkdir /app/

COPY . /app

WORKDIR /app

RUN pip3 install --upgrade pip


WORKDIR /app

RUN apt-get -y update

RUN apt-get -y install git gcc python3-dev

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]
