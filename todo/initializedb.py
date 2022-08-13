'''in command prompt, enter: 'psql -U postgres' to view database'''
'''\l: lists all databases'''
'''\c flask_db: connects to database'''
'''\dt: lists all tables in database'''
from app import db
import os

if bool(os.environ.get('DEBUG', '')):
    db.drop_all()
db.create_all()