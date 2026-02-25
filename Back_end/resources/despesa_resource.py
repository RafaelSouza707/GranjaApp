from flask import request
from flask_restful import Resource
from helpers.database import db
from models.despesa import Despesa
from schemas.despesa_schema import DespesaSchema

despesa_schema = DespesaSchema()
despesa_schema = DespesaSchema(many=True)


class DespesaResource(Resource):

    def get(self):
        lotes = Despesa.query.all()
        return despesa_schema.dump(lotes), 200
    