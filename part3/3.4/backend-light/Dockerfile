FROM ubuntu:16.04
RUN apt-get update && apt-get install -y curl git \
&& curl -sL https://deb.nodesource.com/setup_10.x | bash \
&& git clone  https://github.com/docker-hy/backend-example-docker.git \
&& apt install -y nodejs \
&& apt-get purge -y --auto-remove curl git \
&& rm -rf /var/lib/apt/lists/* \
&& useradd -m app \
&& chown -R app /backend-example-docker
USER app
WORKDIR /backend-example-docker
RUN npm install \
&& rm -rf /app/.git \
EXPOSE 8000
ENV FRONT_URL=http://localhost:5000
CMD npm start
