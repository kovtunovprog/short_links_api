from flask import request
from sqlalchemy.exc import IntegrityError

from loader import db
from utils.db_api.models import ShortLinkModel
from utils.generate_link import generate_short_link


def add_short_link(default_url, days_actual=None):
    """
    Create new short link in database
    :param default_url:
    :param days_actual:
    :return: new short link data
    """
    if days_actual is None:
        days_actual = 90
    try:
        short_link_obj = ShortLinkModel(default_url=default_url, days_actual=days_actual)
        db.session.add(short_link_obj)
        db.session.commit()
        short_link_id = short_link_obj.id
        short_url = generate_short_link(short_link_id)
        short_link_obj.short_url = short_url
        db.session.commit()
    except IntegrityError:
        return False
    return {'id': short_link_obj.id, 'default_url': short_link_obj.default_url, 'short_url': str(request.host_url) +
            short_link_obj.short_url, 'days_actual': short_link_obj.days_actual}


def get_instance_short_link(short_link_id):
    """
    Get instance short link from database
    :param short_link_id:
    :return: instance short link data
    """
    short_link_id = int(short_link_id)
    short_link_obj = ShortLinkModel.query.filter_by(id=short_link_id).first()
    if short_link_obj is None:
        return False
    return {'id': short_link_obj.id, 'default_url': short_link_obj.default_url, 'short_url': short_link_obj.short_url,
            'days_actual': short_link_obj.days_actual}


def edit_instance_short_link(short_link_id, default_url=None, days_actual=None):
    """
    Edit short link instance
    :param short_link_id:
    :param default_url:
    :param days_actual:
    :return: bool
    """
    short_link_id = int(short_link_id)
    short_link_obj = ShortLinkModel.query.filter_by(id=short_link_id).first()
    if short_link_obj is None:
        return False
    if default_url:
        short_link_check = ShortLinkModel.query.filter_by(default_url=default_url).first()
        if short_link_check:
            return False
        short_link_obj.default_url = default_url
    if days_actual:
        short_link_obj.days_actual = days_actual
    db.session.commit()
    return True


def delete_instance_short_link(short_link_id):
    """
    Delete short link instance
    :param short_link_id:
    :return: bool
    """
    short_link_id = int(short_link_id)
    short_link_obj = ShortLinkModel.query.filter_by(id=short_link_id).first()
    if short_link_obj is None:
        return False
    db.session.delete(short_link_obj)
    db.session.commit()
    return True
