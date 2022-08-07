#using cd move to folder todo and run command 'python -m flask run' to launch website
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost:5432/flask_db'
db = SQLAlchemy(app)

"""The app.route decorator decorates the first view function; 
it can specify one of the routes used to access the application. """
@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'Hello, world!'