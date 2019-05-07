from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api

server = Flask(__name__)
api = Api(server)
