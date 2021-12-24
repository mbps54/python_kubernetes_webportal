FROM ubuntu:20.04

RUN set -ex && apt-get update && apt-get install -y \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.6 \
    && apt-get clean && rm -rf /var/cache/apt

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY ./app/ /app/
RUN  chmod +x /app/app-exchange.py

WORKDIR /app

ENTRYPOINT ["python3", "app-exchange.py"]