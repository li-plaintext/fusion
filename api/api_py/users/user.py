from flask_restful import Resource

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
