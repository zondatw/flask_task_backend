from marshmallow import Schema, fields, validate

class TaskListSerializer(Schema):
    id = fields.Int()
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    status = fields.Int(default=0, validate=validate.Range(min=0, max=1))

class TaskDetailSerializer(Schema):
    id = fields.Int(required=True)
    name = fields.String(validate=validate.Length(min=1, max=100))
    status = fields.Int(validate=validate.Range(min=0, max=1))