from flask import Flask, request
from flask import current_app as app
from controllers.actor import *
from controllers.movie import *
from core import db

@app.route('/api/actors', methods=['GET'])
def actors():
    """
    Get all actors in db
    """
    return get_all_actors()

@app.route('/api/movies', methods=['GET'])
def movies():
    """
    Get all movies in db
    """
    return get_all_movies()

@app.route('/api/actor', methods=['GET'])
def actor():
    """
    Get actor by id
    """
    return get_actor_by_id()

@app.route('/api/movie', methods=['GET'])
def movie():
    """
    Get movie by id
    """
    return get_movie_by_id()

@app.route('/api/actor', methods=['POST'])
def actor1():
    """
    Add new actor
    """
    return add_actor()

@app.route('/api/movie', methods=['POST'])
def movie1():
    """
    Add new movie
    """
    return add_movie()

@app.route('/api/actor', methods=['PUT'])
def actor2():
    """
    Add new movie
    """
    return update_actor()

@app.route('/api/movie', methods=['PUT'])
def movie2():
    """
    Add new movie
    """
    return update_movie()

@app.route('/api/actor', methods=['DELETE'])
def actor3():
    """
    Add new movie
    """
    return delete_actor()

@app.route('/api/movie', methods=['DELETE'])
def movie3():
    """
    Add new movie
    """
    return delete_movie()

@app.route('/api/actor-relations', methods=['PUT'])
def actor4():
    """
    Add new movie
    """
    return actor_add_relation()

@app.route('/api/movie-relations', methods=['PUT'])
def movie4():
    """
    Add new movie
    """
    return movie_add_relation()

@app.route('/api/actor-relations', methods=['DELETE'])
def actor5():
    """
    Add new movie
    """
    return actor_clear_relations()

@app.route('/api/movie-relations', methods=['DELETE'])
def movie5():
    """
    Add new movie
    """
    return movie_clear_relations()