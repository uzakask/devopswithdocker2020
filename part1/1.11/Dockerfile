FROM ubuntu:16.04
WORKDIR /backend-example-docker
RUN apt-get update && apt-get install -y curl
RUN apt install -y git
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt-get install -y nodejs
RUN git clone  https://github.com/docker-hy/backend-example-docker .
RUN npm install
EXPOSE 8000
ENTRYPOINT ["npm"]
CMD ["start"]
