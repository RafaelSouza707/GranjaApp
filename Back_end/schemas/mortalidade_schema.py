from marshmallow import Schema, fields, validate


class MortalidadeSchema(schema):
    id = fields.Integer(dump_only=True)

    id_lote_frango = fields.Integer(required=True)

    data = fields.Date(required=True)

    quantidade_mortes = fields.Integer(required=True)

    lote_frango = fields.Integer(required=True)