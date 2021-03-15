FROM nginx:alpine

RUN rasa run -m models --enable-api --cors "*" --debug
COPY . /usr/share/nginx/html