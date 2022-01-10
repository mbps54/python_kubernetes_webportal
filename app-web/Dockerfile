FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN set -ex && apt-get update && apt-get install -y \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.6 \
    libreoffice=1:6.4.7-0ubuntu0.20.04.2 \
    unoconv=0.7-2 \
    python3-dev=3.8.2-0ubuntu2 \
    libldap2-dev=2.4.49+dfsg-2ubuntu1.8 \
    libsasl2-dev=2.1.27+dfsg-2 \
    libssl-dev=1.1.1f-1ubuntu2.10 \
    cron=3.0pl1-136ubuntu1 \
    && apt-get clean && rm -rf /var/cache/apt

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY ./app/ /app/
RUN  chmod +x /app/app-web.py
RUN  chmod +x /app/start.sh

ADD crontab /etc/cron.d/cron1
RUN chmod 0644 /etc/cron.d/cron1

WORKDIR /app
EXPOSE 8000

ENTRYPOINT ["/bin/bash", "start.sh"]