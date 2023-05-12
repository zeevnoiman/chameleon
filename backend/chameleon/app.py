from flask import Flask
from flask_cors import CORS
from chameleon.routes.main import api_blueprint
from chameleon.services_init import db

app = Flask(__name__)
CORS(app)
app.register_blueprint(api_blueprint, url_prefix='/api')
db.connect()
db.create_tables()


if __name__ == '__main__':
    app.run()