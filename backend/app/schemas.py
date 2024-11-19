from marshmallow import Schema, fields, validate

class TitanicPassengerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    sex = fields.Str(required=True, validate=validate.OneOf(["male", "female"]))
    age = fields.Int(required=True, validate=validate.Range(min=0))