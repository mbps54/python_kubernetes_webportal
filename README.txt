It is a Python code and Dockerfile to make a ready container for WEB service.

1a. Build an image
docker build . -t web_doc_app:1.0

1b. Push container to hub (optional)
docker images | grep web_doc_app
docker tag 2f80d327e125 mbps54/web_doc_app:1.0
docker push mbps54/web_doc_app:1.0

2. Run a locally generated container

docker run -it \
-e SERVER_NAME_IP='0.0.0.0' \
-e SERVER_PORT='5000' \
-p 5000:5000 \
mbps54/web_doc_app:1.0


3. Run a container from hub.docker.com
docker run -it \
-e SERVER_NAME_IP='127.0.0.1' \
-e SERVER_PORT='5000' \
mbps54/web_doc_app:1.0

4. Local environments for Python app (launch not from container)
export SERVER_NAME_IP='127.0.0.1'
export SERVER_PORT='5000'
