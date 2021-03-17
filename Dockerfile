FROM python:3.6-alpine

WORKDIR /app

RUN apk add  --update  nginx
RUN apk --update add --no-cache \ 
    lapack-dev \ 
    gcc \
    freetype-dev 
RUN apk add --no-cache --virtual .build-deps \
    gfortran \
    musl-dev \
    g++
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip install rasa

COPY . /app

COPY /app/index.html /usr/share/nginx/html
RUN nohup rasa run actions &
RUN rasa run -m models --enable-api --cors "*" --debug