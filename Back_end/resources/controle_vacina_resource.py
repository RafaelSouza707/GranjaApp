from flask import request
from flask_restful import Resource
from helpers.database import db
from models.controle_vacinas import ControleVacinas
from schemas.controle_vacina_schema import ControleVacinaSchema

Controle_Vacina = ControleVacinaSchema()
Controle_Vacina = ControleVacinaSchema(many=True)


class ControleVacinasResource(Resource):

    def get(self):
        lotes = ControleVacinas.query.all()
        return Controle_Vacina.dump(lotes), 200
    