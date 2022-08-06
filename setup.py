from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='todo_flask',
    version='0.0',
    description='A To-Do List built with Flask',
    author='Jessica Jolly',
    author_email='jessicajolly.mec@gmail.com',
    keywords='web flask python',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)