## Web App for automatic documents generation (docx and pdf)
Status:<br><img src="https://github.com/mbps54/web_doc_app/actions/workflows/ci-process.yaml/badge.svg"><br>
### Description
Python web application allows users to fill in a form ang got a ready document in .docx and .pdf formats, based in input parameters.

### This git direcory contains:
1. Python and html codes
2. Dockerfile to make a Docker container
3. Kubernetes Deployment, Service and Ingress manifests to get up the service

Docker image is also available on [Docker Hub](https://hub.docker.com/r/mbps54/web_doc_app)

### Usage options:
1. Python and Bash scripts in TMUX sessions on linux machine
```
apt-get update && apt-get install -y \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.6 \
    libreoffice=1:6.4.7-0ubuntu0.20.04.2 \
    unoconv=0.7-2 \
    tmux
export SERVER_NAME_IP='0.0.0.0' (optional)
export POST_SCHEDULE='0, 9,11,13,15,17, X X 1-5' (optional)

tmux app-web
python3 ./app-web/app/app-web.py
tmux app-exchange
/bin/sh ./app-exchange/start.sh

```

2. Run Docuer containes on Linux machine
- Build images (optional)
```
cd app-web
docker build . -t mbps54/app-web:latest

cd app-exchange
docker build . -t mbps54/app-exchange:latest
```
- Push Docker images to hub (optional)
```
docker push mbps54/app-web:latest
docker push mbps54/app-exchange:latest
```

- Run Docker containers
```
docker network create -d bridge multi-host-network
docker run -d \
           -p 6379:6379 \
           --network=multi-host-network \
           redis:latest
docker run -d \
           --env DB_NAME_IP='redis' \
           --env CRON_SCHEDULE='0 9,11,13,15,17 X X 1-5' \
           --network=multi-host-network \
           mbps54/app-exchange:latest
docker run -d \
           -e DB_NAME_IP='redis' \
           -p 8000:8000 \
           --network=multi-host-network \
           mbps54/app-web:latest
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
```
tree -a -I ".git"
.
├── .github
│   └── workflows
│       └── ci-process.yaml
├── .gitignore
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
│   │   ├── app-exchange.py
│   │   └── start.sh
│   └── requirements.txt
└── app-web
    ├── .dockerignore
    ├── Dockerfile
    ├── app
    │   ├── app-web.py
    │   ├── data
    │   │   ├── test0.yaml
    │   │   ├── test1.yaml
    │   │   ├── test2.yaml
    │   │   ├── test3.yaml
    │   │   └── test4.yaml
    │   ├── functions
    │   │   ├── check_functions.py
    │   │   ├── create_doc_1_doc.py
    │   │   ├── create_doc_1_pdf.py
    │   │   ├── data_validations.py
    │   │   ├── documents_functions.py
    │   │   └── zp.py
    │   ├── static
    │   │   └── hf.css
    │   └── templates
    │       ├── base.html
    │       ├── doc1.html
    │       ├── doc2.html
    │       ├── entry.html
    │       ├── results1.html
    │       └── results2.html
    └── requirements.txt

11 directories, 36 files

```