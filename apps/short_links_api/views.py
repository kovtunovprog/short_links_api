import json

from flask import make_response, request
from flask_restful import Resource, reqparse

from utils.db_api.short_links_api import add_short_link, get_instance_short_link, edit_instance_short_link, \
    delete_instance_short_link
from utils.short_links_api_utils import check_days_actual_value

FIELDS = {'link', 'days_actual'}


class CreateShortLinkView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        for f in FIELDS:
            parser.add_argument(str(f))

        args = parser.parse_args()
        default_url = args['link']
        days_actual = args['days_actual']

        headers = {
            'Access-Control-Allow-Origin': '*'
        }

        if not default_url:
            response = make_response(json.dumps({'Message': 'You have to pass link'}), 400)
            response.headers.extend(headers)
            return response

        if days_actual:
            check_days = check_days_actual_value(days_actual)
            if not check_days:
                response = make_response(json.dumps({'Message': 'days_actual must be between 1 and 366'}), 400)
                response.headers.extend(headers)
                return response

        short_link_data = add_short_link(default_url=default_url, days_actual=days_actual)
        if not short_link_data:
            response = make_response(json.dumps({'Message': 'This link already exists'}), 400)
            response.headers.extend(headers)
            return response

        response = make_response(json.dumps(short_link_data), 201)
        response.headers.extend(headers)
        return response


class ShortLinkInstanceView(Resource):
    def get(self, short_link_id):
        headers = {
            'Access-Control-Allow-Origin': '*'
        }

        if not short_link_id:
            response = make_response(json.dumps({'Message': 'You have to pass short link id'}), 400)
            response.headers.extend(headers)
            return response

        short_link_instance_data = get_instance_short_link(short_link_id=short_link_id)
        if not short_link_instance_data:
            response = make_response(json.dumps({'Message': 'Invalid instance id'}), 400)
            response.headers.extend(headers)
            return response

        response = make_response(json.dumps(short_link_instance_data), 200)
        response.headers.extend(headers)
        return response

    def put(self, short_link_id):
        parser = reqparse.RequestParser()
        for f in FIELDS:
            parser.add_argument(str(f))

        args = parser.parse_args()
        default_url = args['link']
        days_actual = args['days_actual']

        headers = {
            'Access-Control-Allow-Origin': '*'
        }

        if not short_link_id:
            response = make_response(json.dumps({'Message': 'You have to pass short link id'}), 400)
            response.headers.extend(headers)
            return response

        if days_actual:
            try:
                days_actual = int(days_actual)
            except ValueError:
                response = make_response(json.dumps({'Message': 'Invalid days value'}), 400)
                response.headers.extend(headers)
                return response
            check_days = check_days_actual_value(days_actual)
            if not check_days:
                response = make_response(json.dumps({'Message': 'days_actual must be between 1 and 366'}), 400)
                response.headers.extend(headers)
                return response

        short_link_instance_data = edit_instance_short_link(short_link_id=short_link_id, default_url=default_url,
                                                            days_actual=days_actual)
        if not short_link_instance_data:
            response = make_response(json.dumps({'Message': 'This link already exists'}), 400)
            response.headers.extend(headers)
            return response

        response = make_response({}, 204)
        response.headers.extend(headers)
        return response

    def delete(self, short_link_id):
        headers = {
            'Access-Control-Allow-Origin': '*'
        }

        if not short_link_id:
            response = make_response(json.dumps({'Message': 'You have to pass short link id'}), 400)
            response.headers.extend(headers)
            return response

        short_link_instance_data = delete_instance_short_link(short_link_id=short_link_id)
        if not short_link_instance_data:
            response = make_response(json.dumps({'Message': 'Object does not exists'}), 400)
            response.headers.extend(headers)
            return response

        response = make_response({}, 204)
        response.headers.extend(headers)
        return response