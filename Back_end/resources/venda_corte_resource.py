from flask import request
from flask_restful import Resource
from helpers.database import db
from models.venda_corte import VendaCorte
from schemas.venda_corte_schema import VendaCorteSchema

venda_corte_schema = VendaCorteSchema()
vendas_cortes_schema = VendaCorteSchema(many=True)


class VendaCorteResource(Resource):

    def get(self):
        vendas_cortes = VendaCorte.query.all()
        return vendas_cortes_schema.dump(vendas_cortes), 200