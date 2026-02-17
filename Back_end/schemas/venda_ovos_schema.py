from marshmallow import Schema, fields, validate

class VendaOvosSchema(Schema):
    id = fields.integer(dump_only=True)

    id_lote_frango = fields.integer(required= True)

    data = fields.Date(required=True)

    valor = fields.Decimal(required=True, as_string=True, places=2)

    quantidade_ovos = fields.integer(required=True)