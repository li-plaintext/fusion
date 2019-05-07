from core.app import server
import hooks.cors
import routes

if __name__ == "__main__":
  server.run(debug=True)