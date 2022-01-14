## Web App for automatic documents generation (docx and pdf)
Status:<br><img src="https://github.com/mbps54/web_doc_app/actions/workflows/ci-process.yaml/badge.svg"><br>
### Description
Python web application allows users to fill in a form ang got a ready document in .docx and .pdf formats, based in input parameters.

### Release notes
In 1.1.2 a proper crontab job is added  to docker container. It clears generated files (remove "/app/files") directiry each 4 hour.
Version 1.1.1 contains crontab job files, but it does not work.
In 1.3.1 only calc is left.

### This git direcory contains:
1. Python and html codes
2. Dockerfile to make a Docker container
3. Kubernetes Deployment, Service and Ingress manifests to get up the service

Docker images are also available on Docker Hub
<br />[web-app](https://hub.docker.com/r/mbps54/app-web)
<br />[web-exchange](https://hub.docker.com/r/mbps54/app-exchange)

### Usage options:
1. Python and Bash scripts in TMUX sessions on linux machine (for tests)
```
apt-get update && apt-get install -y \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.6 \
    libreoffice=1:6.4.7-0ubuntu0.20.04.2 \
    unoconv=0.7-2 \
    iputils-ping=3:20190709-3 \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.6 \
    cron=3.0pl1-136ubuntu1 \
    ntp=1:4.2.8p12+dfsg-3ubuntu4.20.04.1 \
    python3-dev=3.8.2-0ubuntu2 \
    libldap2-dev=2.4.49+dfsg-2ubuntu1.8 \
    libsasl2-dev=2.1.27+dfsg-2 \
    libssl-dev=1.1.1f-1ubuntu2.10\
    tmux

export SERVER_NAME_IP='0.0.0.0' (optional)

tmux new-session -t app-web
python3 ./app-web/app/app-web.py

```

2. Run Docuer containes on Linux machine
- Build images (optional)
```
cd app-web
docker build . -t mbps54/app-web:1.3.1

cd app-exchange
docker build . -t mbps54/app-exchange:1.1.2
```
- Push Docker images to hub (optional)
```
docker push mbps54/app-web:1.3.1
docker push mbps54/app-exchange:1.1.2
```

- Run Docker containers
```
docker network create -d bridge multi-host-network
docker run -d \
           -p 6379:6379 \
           --network=multi-host-network \
           --name app-redis \
           redis:latest
docker run -d \
           -e DB_NAME_IP='app-redis' \
           -e API_KEY='Nu2Em4s1cB' \
           -e CRON_SCHEDULE='0 9 1 X X' \
           --network=multi-host-network \
           --name app-exchange \
           mbps54/app-exchange:1.1.2
docker run -d \
           -p 80:8000 \
           -e DB_NAME_IP='app-redis' \
           --network=multi-host-network \
           --name app-web \
           mbps54/app-web:1.3.1

```

3. Run Docker containes on Kubernetes cluster
```
cd Kubernetes
kubectl apply -f Service.yaml
kubectl apply -f Ingress.yaml
kubectl apply -f Deployment_db.yaml
kubectl apply -f Job.yaml
kubectl apply -f Deployment.yaml
kubectl apply -f CronJob.yaml
```

### Info
Detailed K8S info in /Diagram/web-portal.pdf
```
tree -a -I ".git"

├── .github
├── .gitignore
├── Diagram
│   ├── web-portal.pdf
│   └── web-portal.vsdx
├── Kubernetes
│   ├── CronJob.yaml
│   ├── Deployment.yaml
│   ├── Deployment_db.yaml
│   ├── Ingress.yaml
│   ├── Job.yaml
│   └── Service.yaml
├── README.md
├── app-exchange
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── app
│   │   ├── app_exchange_cbtr.py
│   │   ├── old
│   │   │   ├── old_app_exchange_cbrf.py
│   │   │   ├── old_app_exchange_manual.py
│   │   │   └── old_app_exchange_stock.py
│   │   └── start.sh
│   └── requirements.txt
└── app-web
    ├── .dockerignore
    ├── Dockerfile
    ├── app
    │   ├── app-web.py
    │   ├── functions
    │   │   ├── app_email_sender.py
    │   │   ├── check_functions.py
    │   │   ├── create_doc_2_pdf.py
    │   │   ├── data_validations.py
    │   │   ├── documents_functions.py
    │   │   └── zp.py
    │   ├── start.sh
    │   ├── static
    │   │   └── hf.css
    │   └── templates
    │       ├── base.html
    │       ├── doc2.html
    │       └── results2.html
    ├── crontab
    └── requirements.txt

11 directories, 34 files

```
