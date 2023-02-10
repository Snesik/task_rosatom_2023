FROM python:3.10-slim as builder
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /app
RUN apt-get update && apt-get install -y \
	    python3-pip \
        libpq-dev
RUN apt-get autoclean
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY hard_task /app
CMD ["python3", "main.py"]

