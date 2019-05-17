from core.app import api
from users.user import Users, User

api.add_resource(Users, "/users")
api.add_resource(User, "/users/<id>")
