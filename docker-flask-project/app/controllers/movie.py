from flask import jsonify, make_response
from datetime import datetime as dt
from ast import literal_eval
from models.actor import Actor
from models.movie import Movie
from settings.constants import MOVIE_FIELDS
# to make response pretty
from .parse_request import get_request_data


def get_all_movies():
    """
    Get list of all records
    """
    all_movies = Movie.query.all()
    movies = []
    for movie in all_movies:
        mov = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        movies.append(mov)
    return make_response(jsonify(movies), 200)