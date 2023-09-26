FROM alpine

RUN apk add --no-cache python3 py3-pip socat

RUN pip3 install --upgrade pip

RUN mkdir -p /chal
WORKDIR /chal

COPY . .

RUN chmod +x ./docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]