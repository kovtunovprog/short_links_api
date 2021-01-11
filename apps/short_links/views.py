import json

from flask import redirect, make_response

from loader import app
from utils.db_api.short_links import get_default_url


@app.route('/<string:link>', methods=["GET", "POST"])
def redirect_to_pages(link):
    if not link:
        return {}
    default_url = get_default_url(link)
    if not default_url:
        response = make_response(json.dumps({'Message': 'Invalid or expired url'}), 400)
        return response
    return redirect(default_url, code=302)


