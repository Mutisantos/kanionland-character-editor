# kanionland-character-editor

A Python-Flask solution for Roleplay automation for Kanionland Characters stats, jobs, equipment, etc.

The tech stack chosen for this project will be using Python-Flask-SQLite-MongoDB. Mixing both types of databases will allow handling structured records for reiterative and relational records and values, while saving information regarding characters from former sheets in mutable formats.

## Executing locally

1. Ensure you have Python installed on your system. You can download and install Python from the official website: https://www.python.org/downloads/
2. Execute the following commands to ensure that flask is enabled in your system.

```
pip install Flask
pip install pyinstaller
python run.py
```

The flask server will be running in https://localhost:5000

## Learning content

The Learning folder contains basic scripts and examples on how to properly use Python, providing guidance over concepts and best practices, with focus on data structures, libraries, modules, imports, collections, I/O operations, concurrency, algorithms, design patterns, Object-Oriented Programming concepts, and more.

This folder holds its own virtual environment, and can be executed using the following commands:

```
cd learning/basics
.\venv\Scripts\activate
```

After that, the scripts can be executed directly (if they were written with that purpose), showing a (venv) prefix in the console. Remember to activate the virtual environment every new console session.
