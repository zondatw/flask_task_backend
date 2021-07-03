from .extensions import db

# Alias common SQLAlchemy names
Column = db.Column

basestring = (str, bytes)

class CRUDMixin:
    """CRUDMixin

    Mixin that adds convenience methods for CRUD (create, read, update, delete) operations
    """

    @classmethod
    def create(cls, **kwargs):
        """create

        Create a new record and save it the database
        """
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """update

        Update specific fields of a record
        """
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            return self.save()
        return self

    def save(self, commit=True):
        """save

        Save the record
        """
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """delete

        Remove the record from the database
        """
        db.session.delete(self)
        if commit:
            return db.session.commit()
        return


class Model(CRUDMixin, db.Model):
    """Model

    Base model class that includes CRUD convenience methods
    """

    __abstract__ = True

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.id}>"


class PkModel(Model):
    """PkModel

    Base model class that includes CRUD convenience methods, plus adds a 'primary key' column named ``id``
    """

    __abstract__ = True
    id = Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, record_id):
        """get_by_id

        Get record by ID.
        """
        if any(
            (
                isinstance(record_id, basestring) and record_id.isdigit(),
                isinstance(record_id, (int, float)),
            )
        ):
            return cls.query.get(int(record_id))
        return None