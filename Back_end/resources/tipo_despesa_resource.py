from flask import request
from flask_restful import Resource
from helpers.database import db
from models.tipo_despesa import TipoDespesa
from schemas.tipo_despesa_schema import TipoDespesaSchema

tipo_despesa_schema = TipoDespesaSchema()
tipos_despesas_schema = TipoDespesaSchema(many=True)


class TipoDespesaResource(Resource):

    def get(self, id = None):
        if id:
            tipo_despesa = TipoDespesa.query.get_or_404(id)
            return tipo_despesa_schema.dump(tipo_despesa), 200
        
        tipos_despesas = TipoDespesa.query.all()
        return tipos_despesas_schema.dump(tipos_despesas), 200
    
    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {"message": "Nenhum dado enviado."}, 400
        
        data = tipo_despesa_schema.load(json_data)

        novo_tipo = TipoDespesa(**data)
        db.session.add(novo_tipo)
        db.session.commit()

        return tipo_despesa_schema.dump(novo_tipo), 201
    
    def put(self, id):
        tipo = TipoDespesa.query.get_or_404(id)
        json_data = request.get_json()
        data = tipo_despesa_schema.load(json_data)

        tipo.nome = data["nome"]

        db.session.commit()

        return tipo_despesa_schema.dump(tipo), 200
    
    def delete(self, id):
        tipo = TipoDespesa.query.get_or_404(id)
        db.session.delete(tipo)
        db.session.commit()

        return {"message": "Tipo de despesa excluído com sucesso!"}, 200