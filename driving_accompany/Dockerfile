FROM python:3.9
WORKDIR /Driving_accompany/driving_accompany

ADD . /Driving_accompany/driving_accompany

RUN pip install -r requirements.txt

CMD ["uwsgi","app.ini"]
