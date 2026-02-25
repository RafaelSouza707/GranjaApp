from flask import request
from flask_restful import Resource
from helpers.database import db
from models.mortalidade import Mortalidade
from schemas.mortalidade_schema import MortalidadeSchema

mortalidade_schema = MortalidadeSchema()
mortalidades_schema = MortalidadeSchema(many=True)


class MortalidadeResource(Resource):

    def get(self):
        mortalidades = Mortalidade.query.all()
        return mortalidades_schema.dump(mortalidades), 200