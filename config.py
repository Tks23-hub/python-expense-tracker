import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SQLite database file: expenses.db in your project folder
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'expenses.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Used by Flask (sessions, CSRF, etc.); override via env var if needed
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')
