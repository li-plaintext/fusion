from flask_restful import Resource, request
from utils.utils import sum_users
from flask import abort
import dummy

class Users(Resource):
  def get(self): 
    params = [ key for key in request.args.keys()]
    users = dummy.users
    
    if len(users): 
      for key in params: 
        users = [ user for user in users if key in user and user[key] == request.args[key]]
    
    return users


class User(Resource):
  def get(self, id): 
    found_users = [user for user in dummy.users if user['id'] == id]
    found_user = next(iter(found_users), {})

    return found_user