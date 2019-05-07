from core.app import api
from users.user import Users

api.add_resource(Users, "/")