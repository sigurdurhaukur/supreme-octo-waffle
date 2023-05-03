FROM alpine:latest

RUN apk add --no-cache python3-dev \
    # && apk add --no-cache libexecinfo-dev \
    && apk add --no-cache build-base \
    && python3 -m ensurepip \
    && pip3 install --upgrade pip



WORKDIR /app

COPY api /app


# RUN apk add --no-cache musl-dev
# RUN apt-get -y install libc-dev
# RUN apt-get -y install build-essential
# RUN pip install -U pip

# RUN pip3 --no-cache-dir install -r requirements.txt
RUN pip3 --no-cache-dir install fastapi["all"]

# EXPOSE 5000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]