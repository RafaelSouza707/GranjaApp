from flask import request
from flask_restful import Resource
from helpers.database import db
from models.postura import Postura
from schemas.postura_schema import PosturaSchema

postura_schema = PosturaSchema()
posturas_schema = PosturaSchema(many=True)


class PosturaResource(Resource):

    def get(self):
        posturas = Postura.query.all()
        return posturas_schema.dump(posturas), 200