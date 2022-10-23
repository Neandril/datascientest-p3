# Imports
from fastapi import FastAPI, HTTPException, Request
from funcs import *
import classes


# Tags for swagger
tags_metadata = [
    { 
        "name": "status",
        "description": "You can check weither the API is up or down here"
    },
    {
        "name": "marvel",
        "description": "Queries about Marvel super-heroes and super-vilains can be performed below"
    }
]

# API Init
api = FastAPI(
    title="Project 3",
    description="API Related to the Marvel Universe Network",
    version="1.0",
    openapi_tags=tags_metadata
)

# ====================

# Route Status
@api.get('/status', name='Get API Status', tags=['status'])
def get_status():
    """ 
    Status Route
    - Returns 1 if API is up, a 404 error otherwise
    """
    try:
        return { 'status': '1' }
    except IndexError:
        raise HTTPException(status_code=404, detail="Not Found")


@api.post('/mcu/comics_heroes', name='Comics from Heroes', tags=['marvel'])
def get_comics_from_heroes(
    hero: classes.Mcu,
    nb: classes.Nb_Results
):
    """
    Get all Comics where an Hero appears
    - **hero**: The Character requested
    - **nb**: Firsts results to display
    """
    result = get_comic_where_hero_appeared_in(hero, nb)

    if len(result) > 0:
        return { 'Heroes': result }
    else:
        return { 'Hero': 'No result' }


@api.post('/mcu/knows', name='Relationships', tags=['marvel'])
def get_knows(
    hero: classes.Mcu,
    nb: classes.Nb_Results
):
    """
    Get all relationship for the given hero
    - **hero**: The character requested
    - **nb**: Firsts results to display
    """
    result = get_who_knows_this_hero(hero, nb)
    if len(result) > 0:
        return { 'Knows': result }
    else:
        return { 'Knows': 'No result' }


@api.post('/mcu/heroes_comics', name='Heroes from Comics', tags=['marvel'])
def get_heroes_from_comics(
    comic: classes.Mcu,
    nb: classes.Nb_Results
):
    """
    Get all heroes who appear on a given comic
    - **comic**: The comic ref number
    - **nb**: Results to display
    """
    result = get_heroes_who_appears_in_comic(comic, nb)
    if len(result) > 0:
        return { 'Comic': result }
    else:
        return { 'Comic': 'No result' }

