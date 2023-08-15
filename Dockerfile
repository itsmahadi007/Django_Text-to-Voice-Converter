FROM python:3.10.9

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app/backend
WORKDIR /app/backend
COPY . /app/backend
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN #pip install git+https://github.com/suno-ai/bark.git


EXPOSE 5020

