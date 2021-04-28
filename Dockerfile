FROM python:3.8-alpine

ENV PORT=8000

ADD . /app
WORKDIR /app

RUN python3 -m pip install -r prod_requirements.txt

CMD gunicorn -w 4 --bind 0.0.0.0:$PORT app:app
