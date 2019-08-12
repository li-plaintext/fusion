from flask import Flask, Blueprint
from flask_restful import Api
from http import HTTPStatus

from werkzeug.exceptions import NotFound, MethodNotAllowed, InternalServerError, Unauthorized, BadRequest

url_prefix = '/api/v1'

server = Flask(__name__)
blueprint = Blueprint(None, __name__)



HTTP_ERROR_MAP = {
        NotFound.__name__: {
            'message': "The requested resource does not exist",
            'status': HTTPStatus.NOT_FOUND
        },
        MethodNotAllowed.__name__:{
            'message': "Method not allowed",
            'status': HTTPStatus.METHOD_NOT_ALLOWED
        },
        InternalServerError.__name__:{
            'message': 'Internal API error',
            'status': HTTPStatus.INTERNAL_SERVER_ERROR
        },
        Unauthorized.__name__:{
            'message': 'Invalid API key',
            'status': HTTPStatus.UNAUTHORIZED
        },
        BadRequest.__name__:{
            'message': 'Bad request',
            'status': HTTPStatus.BAD_REQUEST
        }
}

api = Api(server, errors=HTTP_ERROR_MAP, catch_all_404s=True)

server.register_blueprint(blueprint, url_prefix=url_prefix)



