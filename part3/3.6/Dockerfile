FROM node:alpine as build-stage
RUN apk add git && \
    git clone https://github.com/docker-hy/frontend-example-docker.git
WORKDIR /frontend-example-docker
RUN npm install && \
    npm run build

FROM node:alpine
COPY --from=build-stage /frontend-example-docker/dist /app/dist
RUN npm install -g serve
WORKDIR /app/dist
EXPOSE 5000
CMD serve -s -l 5000
