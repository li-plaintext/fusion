from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
 
class Users(Resource):
  def get(self): 
    return {
      'method': 'GET'
    }

  def post(self):
    return {
      'method': 'POST'
    }

  def put(self):
    return {
      'method': 'PUT'
    }
  
  def delete(self):
    return {
      'method': 'DELETE'
    }

api.add_resource(Users, "/")

if __name__ == "__main__":
  app.run(debug=True)