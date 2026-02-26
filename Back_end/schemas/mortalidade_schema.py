from marshmallow import Schema, fields


from schemas.lote_frango_schema import LoteFrangoSchema

class MortalidadeSchema(Schema):
    id = fields.Integer(dump_only=True)

    id_lote_frango = fields.Integer(required=True)
    data = fields.Date(required=True)
    quantidade_mortes = fields.Integer(required=True)

    lote_frango = fields.Nested(LoteFrangoSchema, dump_only=True)