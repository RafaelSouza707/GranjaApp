from flask import request
from flask_restful import Resource
from helpers.database import db
from models.lote_frangos import LoteFrango
from schemas.lote_frango_schema import LoteFrangoSchema

lote_frango_schema = LoteFrangoSchema()
lotes_frangos_schema = LoteFrangoSchema(many=True)


class LoteFrangoResource(Resource):
    
    def get(self, int=None):
        if id:
            lote_frango = LoteFrango.query.get_or_404(id)
            return lotes_frangos_schema.dump(lote_frango), 200
        
        lotes = LoteFrango.query.all()
        return lotes_frangos_schema.dump(lotes), 200
    
    def post(self):
        json_data = request.get_json()
        data = lotes_frangos_schema.load(json_data)

        novo_lote = LoteFrango(**data)
        db.session.add(novo_lote)
        db.session.commit()

        return lote_frango_schema.dump(novo_lote), 201
    
    def put(self, id):
        lote = LoteFrango.query.get_or_404(id)
        json_data = request.get_json()
        data = lote_frango_schema.load(json_data)

        lote.quantidade_inicial = data["quantidade_inicial"]
        lote.data_entrada_aves = data["data_entrada_aves"]
        lote.data_ninhada = data["data_ninhada"]
        lote.fornecedor = data["fornecedor"]
        lote.tipo_lote = data["tipo_lote"]
        lote.galpao = data["galpao"]
        lote.status = data["status"]
        lote.peso_medio = data["peso_medio"]

        db.session.commit()

        return lote_frango_schema.dump(lote), 200
    
    def delete(self, id):
        lote = LoteFrango.query.get_or_404(id)
        db.session.delete(lote)
        db.session.commit()

        return {"message": "Lote de frangos removido com sucesso!"}