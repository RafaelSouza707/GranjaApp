
from flask import request
from flask_restful import Resource
from helpers.database import db
from models.venda_ovos import VendaOvos
from schemas.venda_ovos_schema import VendaOvosSchema

venda_ovos_schema = VendaOvosSchema()
vendas_ovos_schema = VendaOvosSchema(many=True)


class VendaOvosResource(Resource):

    def get(self):
        vendas_ovos = VendaOvos.query.all()
        return vendas_ovos_schema.dump(vendas_ovos), 200
