from flask.templating import render_template_string

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class BaseModel:
    def add_object(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print('DATABASE ERROR', e)
            raise

    def delete_object(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            print('DATABASE ERROR', e)
            raise

    def update_object(self):
        try:
            db.session.commit()
        except Exception as e:
            print('DATABASE ERROR', e)
            raise


class Soda(BaseModel, db.Model):
    __tablename__ = 'soda'
    TYPES = {'cola': 'Cola', 'lemon_lime': 'Lemon Lime', 'root_beer': 'Root Beer', }
    soda_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(31))
    type = db.Column(db.String(11))

    def serialize(self):
        return {key: getattr(self, key) for key in ('soda_id', 'name', 'type')}
    