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
        data = request.get_json()

        errors = lote_schema.validate(data)
        if errors:
            return errors, 400

        novo_lote = LoteRacao(**data)

        db.session.add(novo_lote)
        db.session.commit()

        return lote_schema.dump(novo_lote), 201


    def put(self, id):
        lote = LoteRacao.query.get_or_404(id)

        data = request.get_json()
        errors = lote_schema.validate(data)
        if errors:
            return errors, 400

        for key, value in data.items():
            setattr(lote, key, value)

        db.session.commit()

        return lote_schema.dump(lote), 200


    def delete(self, id):
        lote = LoteRacao.query.get_or_404(id)

        db.session.delete(lote)
        db.session.commit()

        return {"message": "Lote removido com sucesso"}, 200