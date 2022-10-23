FROM neo4j

WORKDIR /var/lib/neo4j/

COPY neo4j.conf conf/
COPY *.csv import/
COPY apoc-4.4.0.9-all.jar plugins/

EXPOSE 7474
EXPOSE 7687

ENV NEO4JLABS_PLUGINS=\[\"apoc\"\]
ENV NEO4J_AUTH=neo4j/s3cr3t

CMD [ "neo4j", "-p 7474:7474", "-p 7687:7687" ]