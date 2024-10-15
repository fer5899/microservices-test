FROM python:3

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client netcat-openbsd \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY src .
RUN pip install --no-cache-dir -r requirements.txt
