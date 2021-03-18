import os

from flask import Flask

from config import SQLALCHEMY_DATABASE_URI


def create_app(config_filename):
    app = Flask(__name__)

    app.config.from_object(config_filename)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = app.config['SECRET_KEY']
    app.config['APPLICATION_PATH'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
    app.config['PROPAGATE_EXCEPTIONS'] = True

    from app.models import db

    db.init_app(app)

    from app.views.main import main_view
    from app.views.pokemonView import pokemon_view
    from app.views.teamsView import teams_view

    app.register_blueprint(blueprint=main_view, url_prefix="/")
    app.register_blueprint(blueprint=pokemon_view, url_prefix="/pokemon")
    app.register_blueprint(blueprint=teams_view, url_prefix="/team")

    return app
