from flask import request
from flask_restful import Resource
from helpers.database import db
from models.consumo_lote_diaria import ConsumoLoteDiaria
from schemas.consumo_lote_diaria_schema import ConsumoLoteDiariaSchema

consumo_lote_schema = ConsumoLoteDiariaSchema()
consumo_lote_schema = ConsumoLoteDiariaSchema(many=True)


class ConsumoLoteDiariaResource(Resource):

    def get(self):
        lotes = ConsumoLoteDiaria.query.all()
        return consumo_lote_schema.dump(lotes), 200
    