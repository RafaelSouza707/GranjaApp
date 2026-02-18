from flask import request
from flask_restful import Resource
from helpers.database import db
from models.lote_racao import LoteRacao
from schemas.lote_racao_schema import LoteRacaoSchema

lote_schema = LoteRacaoSchema()
lotes_schema = LoteRacaoSchema(many=True)


class LoteRacaoResource(Resource):

    def get(self, id=None):
        if id:
            lote = LoteRacao.query.get_or_404(id)
            return lote_schema.dump(lote), 200

        lotes = LoteRacao.query.all()
        return lotes_schema.dump(lotes), 200
