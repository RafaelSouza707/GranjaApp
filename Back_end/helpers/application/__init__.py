from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://Databases@localhost:5432/TesteGranja"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # recomendado

api = Api(app)