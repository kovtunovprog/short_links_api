from loader import db
from utils.db_api.models import *


def db_startup():
    db.create_all()