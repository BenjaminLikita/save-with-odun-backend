from flask_login import UserMixin
from . import db
from uuid import uuid4


def get_uuid():
    return uuid4().hex


class User(db.Model):
    id = db.Column(db.String(150), default=get_uuid, nullable=False, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    full_name = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)


    