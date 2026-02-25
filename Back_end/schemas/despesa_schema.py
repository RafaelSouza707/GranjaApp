from marshmallow import Schema, fields


class DespesaSchema(Schema):
    id = fields.Integer(dump_only=True)

    id_tipo_despesa = fields.Integer(required=True)

    data = fields.Date(required=True)

    valor = fields.Decimal(required=True, as_string=True, places=2)