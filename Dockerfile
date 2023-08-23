FROM nvidia/cuda:11.0-base
FROM python:3.10.9

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app/backend
WORKDIR /app/backend
COPY . /app/backend
RUN pip install --upgrade pip
RUN pip install git+https://github.com/suno-ai/bark.git
RUN pip install -r requirements.txt



EXPOSE 8000

