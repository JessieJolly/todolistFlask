#using cd move to folder todo and run command 'python -m flask run' to launch website 
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config.update(
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jess@localhost:5432/flask_db',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
db = SQLAlchemy(app)

from models import Task, User

"""printing the list of api's provided on application"""
@app.route('/api/v1', methods=["GET"])
@app.route('/api/v1/', methods=["GET"])
def info_view():
    """List of routes for this API."""
    output = {
        'info': 'GET /api/v1',
        'register': 'POST /api/v1/accounts',
        'single profile detail': 'GET /api/v1/accounts/<username>',
        'edit profile': 'PUT /api/v1/accounts/<username>',
        'delete profile': 'DELETE /api/v1/accounts/<username>',
        'login': 'POST /api/v1/accounts/login',
        'logout': 'GET /api/v1/accounts/logout',
        "user's tasks": 'GET /api/v1/accounts/<username>/tasks',
        "create task": 'POST /api/v1/accounts/<username>/tasks',
        "task detail": 'GET /api/v1/accounts/<username>/tasks/<id>',
        "task update": 'PUT /api/v1/accounts/<username>/tasks/<id>',
        "delete task": 'DELETE /api/v1/accounts/<username>/tasks/<id>'
    }
    '''outpu is a dict which is converted to JSON format'''
    return jsonify(output)

"""The app.route decorator decorates the first view function; 
it can specify one of the routes used to access the application. """
@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'Hello, world!'