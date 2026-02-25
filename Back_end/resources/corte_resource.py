from flask import request
from flask_restful import Resource
from helpers.database import db
from models.corte import Corte
from schemas.corte_schema import CorteSchema


corte_schema = CorteSchema()
cortes_schema = CorteSchema(many=True)


class CorteResource(Resource):

    def get(self, id=None):
        
        if id:
            corte = Corte.query.get(id)
            
            if not corte:
                return {"message": "Corte não encontrado"}, 404
            
            return corte_schema.dump(corte), 200
        
        cortes = Corte.query.all()
        return cortes_schema.dump(cortes), 200
    