# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ARG DEFAULT_PORT=8080

# Volume anonimo garantindo que sempre minha aplicação terá acesso ao venv com as dependencias instaladas,
# mesmo que eu n tenha venv local
# VOLUME [ "/app/venv" ]
ENV PORT $DEFAULT_PORT 

EXPOSE $PORT

CMD [ "python", "run.py"] 