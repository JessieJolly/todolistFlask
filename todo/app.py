#using cd move to folder todo and run command 'python -m flask run' to launch website
from datetime import datetime 
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/flask_db'
app.config.update(
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:jess@localhost:5432/flask_db',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
db = SQLAlchemy(app)

"""Creating an Object for tasks"""
class Task(db.Model): 
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    note = db.Column(db.Unicode)
    creation_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
    """Creating a many to one relationship b/w tasks and user"""
    user = db.relationship("User", back_populates="tasks")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """On construction, set date of creation."""
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()

"""Creating an Object for User"""
class User(db.Model): 
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode, nullable=False)
    email = db.Column(db.Unicode, nullable=False)
    password = db.Column(db.Unicode, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False) 
    """Creating a many to one relationship b/w tasks and user"""
    tasks = db.relationship("Task", back_populates="user")

    def __init__(self, *args, **kwargs):
        """On construction, set date of joining."""
        super().__init__(*args, **kwargs)
        self.date_joined = datetime.now() 

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