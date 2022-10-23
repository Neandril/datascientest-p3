from neo4j import GraphDatabase

# Neo4j Driver
driver = GraphDatabase.driver(
    'neo4j://172.19.0.2:7687',
    auth=('neo4j', 's3cr3t')
)


def get_comic_where_hero_appeared_in(hero, nb):
    """
    Get comics where an hero appears
    """
    # Don't limit the result if nb is set to All
    if nb != 'All':
        query = """
        MATCH (h:Hero)
        MATCH (c:Comic)
        WHERE h.name =~ toUpper('.*{hero}.*')
        MATCH (h)-[r:APPEARED_IN]->(c)
        RETURN h.name as Hero, type(r) as Relation, c.name as Comic
        LIMIT {n}
        """.format(hero=hero, n=nb)
    else:
        query = """
        MATCH (h:Hero)
        MATCH (c:Comic)
        WHERE h.name =~ toUpper('.*{hero}.*')
        MATCH (h)-[r:APPEARED_IN]->(c)
        RETURN h.name as Hero, type(r) as Relation, c.name as Comic
        """.format(hero=hero)

    with driver.session() as session:
        result = session.run(query).data()

    # Init dictionary
    heroes = {}

    # Add all comics to the list
    for r in result:
        heroes.setdefault(r['Hero'], [])
        heroes[r['Hero']].append(r['Comic'])
    

    # Return the list
    return heroes

def get_who_knows_this_hero(hero, nb):
    """
    Get all other heroes / vilains known by the requested Hero
    """
    # Don't limit the result if nb is set to All
    if nb != 'All':
        query = """
        MATCH (h1:Hero)
        MATCH (h2:Hero)
        WHERE h1.name =~ toUpper('.*{hero}.*')
        MATCH (h1)-[r:KNOWS]->(h2)
        RETURN h1.name as HeroName, type(r) as Relation, h2.name as Hero2
        LIMIT {n}
        """.format(hero=hero, n=nb)
    else:
        query = """
        MATCH (h1:Hero)
        MATCH (h2:Hero)
        WHERE h1.name =~ toUpper('.*{hero}.*')
        MATCH (h1)-[r:KNOWS]->(h2)
        RETURN h1.name as HeroName, type(r) as Relation, h2.name as Hero2
        """.format(hero=hero)


    with driver.session() as session:
        result = session.run(query).data()

    # Empty dict
    knows = {}

    # Add all Heroes (hero nickname / hero character) to the list
    for r in result:
        knows.setdefault(r['HeroName'], [])
        knows[r['HeroName']].append(r['Hero2'])

    return knows

def get_heroes_who_appears_in_comic(comic, nb):
    """
    Get all comics where an Hero appears
    """
    # Don't limit the result if nb is set to All
    if nb != 'All':
        query = """
        MATCH (c:Comic)
        MATCH (h:Hero)
        WHERE c.name =~ toUpper('.*{comic}.*')
        MATCH (c)<-[r:APPEARED_IN]-(h)
        RETURN h.name as Hero, type(r) as Relation, c.name as Comic
        LIMIT 10
        """.format(comic=comic, n=nb)
    else:
        query = """
        MATCH (c:Comic)
        MATCH (h:Hero)
        WHERE c.name =~ toUpper('.*{comic}.*')
        MATCH (c)<-[r:APPEARED_IN]-(h)
        RETURN h.name as Hero, type(r) as Relation, c.name as Comic
        """.format(comic=comic)

    with driver.session() as session:
        result = session.run(query).data()

    # Init dict
    appears = {}

    for r in result:
        appears.setdefault(r['Comic'], [])
        appears[r['Comic']].append(r['Hero'])

    return appears
