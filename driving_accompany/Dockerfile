FROM python:3.9
WORKDIR /driving_accompany

ADD . /driving_accompany

RUN pip install -r requirements.txt

CMD ["uwsgi","app.ini"]
