from flask import Flask, Blueprint
from flask_restful import Api

url_prefix = '/api/v1'

server = Flask(__name__)
blueprint = Blueprint(None, __name__)
api = Api(blueprint)

server.register_blueprint(blueprint, url_prefix=url_prefix)
