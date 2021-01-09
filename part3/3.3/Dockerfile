FROM docker:dind

WORKDIR /builder

RUN apk update && apk add git \
&& rm -rf /var/lib/apt/lists/* 

COPY script.sh /usr/local/bin/

ENTRYPOINT ["script.sh"]
