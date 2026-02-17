from marshmallow import Schema, fields, validate


class VendaCorte(Schema):
    id = fields.Integer(dump_only=True)

    id_lote_frango = fields.Integer(required=True)

    data = fields.Date(required=True)

    valor = fields.Decimal(required=True, as_string=True, places=2)

    quilos = fields.Decimal(required=True, as_string=True, places=3)