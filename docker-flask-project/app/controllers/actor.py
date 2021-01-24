from flask import jsonify, make_response
from datetime import datetime as dt
from ast import literal_eval
from models.actor import Actor
from models.movie import Movie
from models.relations import association
from settings.constants import ACTOR_FIELDS
# to make response pretty
from .parse_request import get_request_data

def get_all_actors():
    """
    Get list of all records
    """
    all_actors = Actor.query.all()
    actors = []
    for actor in all_actors:
        act = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        actors.append(act)
    return make_response(jsonify(actors), 200)

def get_actor_by_id():
    """
    Get record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        obj = Actor.query.filter_by(id=row_id).first()
        try:
            actor = {k: v for k, v in obj.__dict__.items() if k in ACTOR_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def add_actor():
    """
    Add new actor
    """
    data = get_request_data()
    ### YOUR CODE HERE ###

    # creating date
    cr_date = data['date_of_birth']
    cr_date = dt.strptime(cr_date, '%d.%m.%Y')
    cr_date = cr_date.strftime("%a, %d %b %Y %H:%M:%S" + " GMT")

    # use this for 200 response code
    new_record = Actor(name = data['name'], gender = data['gender'], date_of_birth = cr_date)
    new_actor = {k: v for k, v in new_record.__dict__.items() if k in ACTOR_FIELDS}

    return make_response(jsonify(new_actor), 200)
    ### END CODE HERE ###

def update_actor():
    """
    Update actor record by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        obj = Actor.query.filter_by(id=row_id).first()

        try:
            # creating date
            cr_date = data['date_of_birth']
            cr_date = dt.strptime(cr_date, '%d.%m.%Y')
            cr_date = cr_date.strftime("%a, %d %b %Y %H:%M:%S" + " GMT")

            actor = {k: v for k, v in obj.__dict__.items() if k in ACTOR_FIELDS}
            new_data = {'name': data['name'], 'gender': data['gender'], 'date_of_birth': cr_date}
            actor.update(new_data)

        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

    return make_response(jsonify(actor), 200)

    # use this for 200 response code
    # upd_record =
    # upd_actor = {k: v for k, v in upd_record.__dict__.items() if k in ACTOR_FIELDS}
    # return make_response(jsonify(upd_actor), 200)
    # ### END CODE HERE ###

def delete_actor():
    """
    Delete actor by id
    """
    data = get_request_data()
    all_actors = Actor.query.all()
    ### YOUR CODE HERE ###

    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        obj = Actor.query.filter_by(id=row_id).first()

        try:
            all_actors.remove(obj)
            msg = 'Record successfully deleted'
            # use this for 200 response code
            return make_response(jsonify(message=msg), 200)

        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

    ### END CODE HERE ###

def actor_add_relation():
    """
    Add a movie to actor's filmography
    """
    data = get_request_data()
    ### YOUR CODE HERE ###

    if 'id' in data.keys() and 'relation_id' in data.keys():
        try:
            row_id, row_relation_id = int(data['id']), int(data['relation_id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        actor, movie = Actor.query.filter_by(id=row_id).first(), Movie.query.filter_by(id=row_relation_id).first()

        actor_and_movies = []
        actor_and_movies.append(movie)

        try:
            # use this for 200 response code
            rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
            rel_actor['filmography'] = str(actor_and_movies) #str(actor.filmography)
            return make_response(jsonify(rel_actor), 200)
        except:
            err = 'Something goes wrong'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id either for movie or actor specified'
        return make_response(jsonify(error=err), 400)
    ### END CODE HERE ###

def actor_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        actor = Actor.query.filter_by(id=row_id).first()

        try:
            # use this for 200 response code
            # clear relations here
            rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
            rel_actor['filmography'] = str([]) # str(actor.filmography.clear())
            return make_response(jsonify(rel_actor), 200)

        except:
            err = 'Something goes wrong'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id for actor specified'
        return make_response(jsonify(error=err), 400)

    ### END CODE HERE ###