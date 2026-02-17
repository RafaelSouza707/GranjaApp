from flask_sqlalchemy import SQLAlchemy

from helpers.application import app

db = SQLAlchemy(app)