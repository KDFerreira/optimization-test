FROM python:3.6.6-stretch

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y build-essential g++ libgl1-mesa-glx libx11-6

RUN pip install --no-cache-dir -r requirements.txt