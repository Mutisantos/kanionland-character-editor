from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Route to serve the index.html file


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/add_data')
def add_data_page():
    return render_template('addData.html')


# Define the path to the SQLite database file
db_path = os.path.join(os.path.dirname(__file__), 'database.db')

# Function to create the SQLite database table (you can define your
# entities here)


def create_table():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS example_entity (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            value INTEGER
                          )''')


# Initialize the database table
create_table()

# Sample route to add data to the database


@app.route('/add_data', methods=['POST'])
def add_data():
    print(request.get_json())
    data = request.get_json()
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO example_entity (name, value) VALUES (?, ?)",
            (data['name'],
             data['value']))
        conn.commit()
    return jsonify({'message': 'Data added successfully!'})

# Sample route to fetch data from the database


@app.route('/get_data', methods=['GET'])
def get_data():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM example_entity")
        data = cursor.fetchall()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
