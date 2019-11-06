# Flask Import
from flask import Flask
# Project Import
from app import api_bp
from Model import db


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.register_blueprint(api_bp, url_prefix='/api')
    db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
