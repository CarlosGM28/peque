import secrets
from flask import Flask
from routes import register_routes
from config.init_db import init_db

app = Flask(__name__)
register_routes(app)

app.secret_key = secrets.token_hex(32)

init_db()

if __name__ == "__main__":
    app.run(debug=True)
