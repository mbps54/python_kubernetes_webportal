## Web App for automatic documents generation (docx and pdf)
### Description
Python web application allows users to fill in a form ang got a ready document in .docx and .pdf formats, based in input parameters.

### This git direcory contains:
1. Python and html codes
2. Dockerfile to make a Docker container
3. Kubernetes Deployment, Service and Ingress manifests to get up the service

Docker image available on [Docker Hub](https://hub.docker.com/r/mbps54/web_doc_app)

### Usage:
1. Python
```
apt-get update && apt-get install -y \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.6 \
    libreoffice=1:6.4.7-0ubuntu0.20.04.2 \
    unoconv=0.7-2
export SERVER_NAME_IP='0.0.0.0' (optional)
cd ./app
python3 app.py
```

2. Create Docker image
- Build an image
```
docker build . -t mbps54/web_doc_app
```
- Push container to hub (optional)
```
docker push mbps54/web_doc_app
```

3. Run locally created Docker imange
-  Run a locally generated container
```
docker run -it -p 5000:5000 web_doc_app
```
or
```
docker run -it -e SERVER_NAME_IP='0.0.0.0' -p 5000:5000
```

4. Run Docker imange from hub.docker.com
```
docker run -it -p 5000:5000 mbps54/web_doc_app
```
or
```
docker run -it -e SERVER_NAME_IP='0.0.0.0' -p 5000:5000 mbps54/web_doc_app
```
