from core.app import server
import hooks.cors
import routes
from waitress import serve

if __name__ == "__main__":
  server.run(debug=True)
  # serve(server, host='localhost', port=5000)


