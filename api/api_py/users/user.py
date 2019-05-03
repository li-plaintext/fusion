from flask_restful import Resource
from utils.utils import sum_users

class Users(Resource):
  def get(self): 
    return {
      'method': 'GET',
      'size': sum_users([1,2,3])
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
