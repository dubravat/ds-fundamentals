from core import db
from settings.constants import ACTOR_FIELDS
from settings.constants import MOVIE_FIELDS

def commit(obj):
    """
    Function for convenient commit
    """
    db.session.add(obj)
    db.session.commit()
    db.session.refresh(obj)
    return obj

def update(obj):
    """
    Function for convenient update
    """
    db.session.commit()
    return obj

def delete(obj):
    """
    Function for convenient delete
    """
    db.session.delete(obj)
    db.session.commit()
    return obj


class Model(object):
    @classmethod
    def create(cls, **kwargs):
        """
        Create new record

        cls: class
        kwargs: dict with object parameters
        """
        obj = cls(**kwargs)
        return commit(obj)

    @classmethod
    def update(cls, row_id, **kwargs):
        """
        Update record by id

        cls: class
        row_id: record id
        kwargs: dict with object parameters
        """
        obj = cls.query.filter_by(id=row_id)
        obj.update(kwargs.items())

        return update(obj)

    @classmethod
    def delete(cls, row_id):
        """
        Delete record by id

        cls: class
        row_id: record id
        return: int (1 if deleted else 0)
        """
        obj = cls.query.filter_by(id=row_id).first()
        return 1 if obj else 0 #to delete use return 1 if delete(obj) else 0

    @classmethod
    def add_relation(cls, row_id, rel_obj):
        """
        Add relation to object

        cls: class
        row_id: record id
        rel_obj: related object
        """

        obj = cls.query.filter_by(id=row_id).first()

        if cls.__name__ == 'Actor':
            rel_actor = {k: v for k, v in obj.__dict__.items() if k in ACTOR_FIELDS}
            rel_actor['filmography'] = str(rel_obj)

        elif cls.__name__ == 'Movie':
            rel_movie = {k: v for k, v in obj.__dict__.items() if k in MOVIE_FIELDS}
            rel_movie['cast'] = str(rel_obj)

        return commit(obj)