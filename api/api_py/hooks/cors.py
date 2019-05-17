from core.app import server, api
from flask import jsonify
import werkzeug

@server.after_request
def cors(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

@server.errorhandler(werkzeug.exceptions.NotFound)
def page_not_found(e):
  print('400 exception');
  return jsonify({ 'code': 400})

@server.errorhandler(werkzeug.exceptions.MethodNotAllowed)
def page_not_found(e):
  print('405 exception');
  return jsonify({ 'code': '405'})

@api.handler_error(werkzeug.exceptions.MethodNotAllowed)
def page_not_found(e):
  print('405 exception');
  return jsonify({ 'code': '405'})

@server.errorhandler(Exception)
def page_not_found(e):
  print('500 exception');
  return jsonify({ 'code': '500'})
