FROM node:10-alpine
RUN apk add --no-cache git &&\
    git clone https://github.com/docker-hy/frontend-example-docker.git && \
    apk del git && \
    adduser -D app && \
    chown -R app /frontend-example-docker
USER app
WORKDIR /frontend-example-docker
RUN npm install && \
    rm -rf /app/.git
EXPOSE 5000
ENV API_URL=http://localhost:8000
CMD npm start
