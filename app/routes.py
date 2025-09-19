from flask import render_template, Blueprint

# Define the blueprint for routes
routes_blueprint = Blueprint('routes', __name__)

# Routes here (you could, instead, separate them into different modules)


@routes_blueprint.route('/')
def index():
    return render_template('home.html')


@routes_blueprint.route('/add_data')
def add_data():
    return render_template('addData.html')
