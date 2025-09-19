from flask import Flask


def create_app():
    app = Flask(__name__)

    # Import the routes (ensure the order of imports avoids circular
    # dependencies)
    from .home import home_blueprint
    from .addData import add_data_blueprint

    # Register the blueprints
    app.register_blueprint(home_blueprint)
    app.register_blueprint(add_data_blueprint)

    return app
