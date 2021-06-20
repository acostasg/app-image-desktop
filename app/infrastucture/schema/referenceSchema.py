from marshmallow import Schema, fields, post_load
from app.dominio.entity.reference import Reference


class ReferenceSchema(Schema):
    id = fields.Int()
    campaign_id = fields.Int()
    name = fields.Str()
    details = fields.Str()
    created = fields.DateTime()
    modified = fields.DateTime()

    @post_load
    def make_expense(self, data, **kwargs):
        return Reference(**data)
