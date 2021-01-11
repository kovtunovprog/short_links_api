from _datetime import datetime

from loader import db


class ShortLinkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    default_url = db.Column(db.String(80), unique=True, nullable=False)
    short_url = db.Column(db.String(80), unique=True)
    time_update = db.Column(db.DateTime, unique=False, default=datetime.now(), nullable=False)
    days_actual = db.Column(db.Integer, unique=False, default=90, nullable=False)
