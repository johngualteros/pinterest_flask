from flask import Flask
from api.data import db_session
from api.config.constants import DATABASE_ENGINE, DATABASE_NAME
from api.routes import init_routes


def create_app():
    app: Flask = Flask(__name__)
    db_session.global_init(DATABASE_ENGINE, f'api/db/{DATABASE_NAME}')
    init_routes(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
