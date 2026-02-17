from marshmallow import Schema, fields, validate


class ControleVacina(Schema):
    id = fields.Integer(dump_only=True)

    id_lote_frango = fields.Integer(required=True)

    medicamento_aplicado = fields.String(required=True, validate=validate.Length(max=100))

    data = fields.Date(required=True)

    responsavel_aplicacao = fields.String(required=True, validate=validate.Length(max=100))