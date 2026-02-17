from marshmallow import Schema, fields, validate


class PosturaSchema(Schema):
    id = fields.Integer(dump_only=True)

    id_lote_frango = fields.Integer(required=True)

    data = fields.Date(required=True)

    quantidade_ovos = fields.Integer(required=True)
    
    ovo_descartados = fields.Integer(required=True)