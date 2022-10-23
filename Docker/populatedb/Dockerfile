FROM alpine:latest

RUN apk update && apk add --no-cache python3 py3-pip && pip3 install neo4j
# Used for debugging
RUN apk add --no-cache bash 

WORKDIR /home/

COPY wait-for-it.sh /home/wait-for-it.sh
COPY populate_db.py /home/populate_db.py

EXPOSE 7474
EXPOSE 7687

ENTRYPOINT [ "./wait-for-it.sh", "0.0.0.0:7687", "--timeout=15", "--", "python3", "populate_db.py" ]
