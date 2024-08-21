from flask import Blueprint, render_template

add_data_blueprint = Blueprint('add_data', __name__)

@add_data_blueprint.route('/add_data')
def add_data_page():
    return render_template('add_data.html')
