from app import db
from datetime import datetime 

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