from flask_restful import Resource, request
from utils.utils import sum_users
from flask import abort
import dummy
import uuid

class Users(Resource):
  def get(self): 
    params = [ key for key in request.args.keys()]
    users = dummy.users

    if len(users): 
      for key in params: 
        users = [ user for user in users if key in user and user[key] == request.args[key]]
    return users

  def post(self):
    created_user = request.get_json().copy();
    created_user['id'] = str(uuid.uuid4());
    dummy.users.append(created_user)

    return created_user
    
  
class User(Resource):
  def get(self, id): 
    found_users = [user for user in dummy.users if user['id'] == id]
    found_user = next(iter(found_users), {})

    return found_user
  
  def put(self, id):
    found_users = [user for user in dummy.users if user['id'] == id]
    found_user = next(iter(found_users), {})

    updated_user = {**found_user, **request.get_json()}

    return updated_user