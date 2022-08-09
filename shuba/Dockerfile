FROM python:3.8-slim-buster

RUN apt-get -y update && apt-get -y install netcat

WORKDIR /app/shuba

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

