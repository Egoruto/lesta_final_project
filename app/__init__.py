from flask import Flask
from app.models import db
from app.routes import bp
import os
from dotenv import load_dotenv

load_dotenv()


def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(flask_app)
    flask_app.register_blueprint(bp)

    with flask_app.app_context():
        db.create_all()

    return flask_app
