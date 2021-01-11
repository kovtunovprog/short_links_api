from datetime import datetime, timedelta

from utils.db_api.models import ShortLinkModel


def get_default_url(short_url):
    short_link_obj = ShortLinkModel.query.filter_by(short_url=short_url).first()

    if not short_link_obj:
        return False
    if datetime.now() < (short_link_obj.time_update + timedelta(days=short_link_obj.days_actual)):
        return short_link_obj.default_url
    else:
        return False
