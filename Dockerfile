FROM python3.6:alpine

RUN apt-get install nginx

RUN pip install rasa

COPY . /usr/share/nginx/html

RUN rasa run -m models --enable-api --cors "*" --debug