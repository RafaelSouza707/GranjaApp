from marshmallow import Schema, fields, validate

class VendaOvosSchema(Schema):
    id = fields.Integer(dump_only=True)

    id_lote_frango = fields.Integer(required= True)

    data = fields.Date(required=True)

    valor = fields.Decimal(required=True, as_string=True, places=2)

    quantidade_ovos = fields.Integer(required=True)