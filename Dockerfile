FROM python:3

WORKDIR /app

COPY api /app

RUN pip install fastapi sentence-transformers uvicorn gensim