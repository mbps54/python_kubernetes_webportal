FROM ubuntu:20.04

RUN ln -snf /usr/share/zoneinfo/Europe/Moscow /etc/localtime && echo Europe/Moscow > /etc/timezone

RUN set -ex && apt-get update && apt-get install -y \
    iputils-ping=3:20190709-3 \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.6 \
    cron=3.0pl1-136ubuntu1 \
    ntp=1:4.2.8p12+dfsg-3ubuntu4.20.04.1 \
    && apt-get clean && rm -rf /var/cache/apt

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY ./app/ /app/
RUN  chmod +x /app/app_exchange_cbtr.py /app/start.sh

ENTRYPOINT ["/bin/bash", "/app/start.sh"]