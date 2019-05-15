from core.app import server
from flask import jsonify

@server.after_request
def cors(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

@server.errorhandler(400)
def page_not_found(response):
    return jsonify({ 'code': 400})

@server.errorhandler(404)
def page_not_found(response):
    return jsonify({ 'code': 404})

@server.errorhandler(403)
def page_not_found(response):
    return jsonify({ 'code': '403'})


@server.errorhandler(500)
def internal_error(error):
    console
    return "500 error"