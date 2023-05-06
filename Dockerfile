FROM python:3

WORKDIR /app

COPY api /app

RUN pip install fastapi uvicorn gensim
# RUN pip --no-cache-dir install fastapi["all"] gensim
