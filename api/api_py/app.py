from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api

from users.user import Users


server = Flask(__name__)
api = Api(server)

api.add_resource(Users, "/")

import cors
