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

    def post(self):
        json_data = request.get_json()
        data = lote_schema.load(json_data)

        novo_lote = LoteRacao(**data)
        db.session.add(novo_lote)
        db.session.commit()

        return lote_schema.dump(novo_lote), 201
    
    def put(self, id):
        lote = LoteRacao.query.get_or_404(id)
        json_data = request.get_json()
        data = lote_schema.load(json_data)

        lote.tipo_racao = data["tipo_racao"]
        lote.fornecedor = data["fornecedor"]
        lote.data_compra = data["data_compra"]
        lote.quilos = data["quilos"]
        lote.valor = data["valor"]

        db.session.commit()

        return lote_schema.dump(lote), 200
    
    def delete(self, id):
        lote = LoteRacao.query.get_or_404(id)
        db.session.delete(lote)
        db.session.commit()

        return {"message": "Lote de ração removido com sucesso!"}, 200