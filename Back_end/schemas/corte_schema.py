from marshmallow import Schema, fields, validate


class CorteSchema(Schema):
    id = fields.Integer(dump_only=True)

    id_lote_frango = fields.Integer(required=True)

    data = fields.Date(required=True)

    peso = fields.Decimal(required=True, as_string=True, places=3)