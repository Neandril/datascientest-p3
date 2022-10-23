from neo4j import GraphDatabase



# Init variables
protocol = "neo4j"
url = "172.17.0.1"
port = "7687"
username = "neo4j"
password = "s3cr3t"

# Create Neo4J driver
driver = GraphDatabase.driver(
    '{protocol}://{url}:{port}'.format(protocol=protocol, url=url, port=port),
    auth=(username, password)
)

# List of queries that populate the db
queries = (
    """
    CALL apoc.schema.assert(
    {},
    {Comic:['name'],Hero:['name']});
    """,

    """
    LOAD CSV WITH HEADERS FROM "file:///var/lib/neo4j/import/edges.csv" as row
    CALL 
    {
        WITH row
        MERGE (h:Hero {name: row.hero})
        MERGE (c:Comic {name: row.comic})
        MERGE (h)-[:APPEARED_IN]->(c)
    }
    """,

    """
    LOAD CSV WITH HEADERS FROM "file:///var/lib/neo4j/import/hero-network.csv" as row
    CALL 
    {
        WITH row
        MERGE (h1:Hero {name: row.hero1})
        MERGE (h2:Hero {name: row.hero2})
        MERGE (h1)-[:KNOWS]->(h2)
    }
    """
)

# Run queries
for query in queries:
    with driver.session() as session:
        session.run(query).data()


# Db populated
print("=================================")
print("Database successfully populated")
print("Address: localhost:7474")
print("=================================")
