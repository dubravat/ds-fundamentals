from core import db

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
    db.session.update(obj)
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
        return print(obj)

    @classmethod
    def delete(cls, row_id):
        """
        Delete record by id

        cls: class
        row_id: record id
        return: int (1 if deleted else 0)
        """
        obj = cls.query.filter_by(id=row_id).first()
        return 1 if obj else 0