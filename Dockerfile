FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /Shuba_back
WORKDIR /Shuba_back
COPY requirements.txt /Shuba_back/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /Shuba_back/