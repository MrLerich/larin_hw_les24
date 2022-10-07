from typing import Iterable, Dict

from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_PARAMS: Iterable = ('filter', 'sort', 'map', 'unique', 'limit', 'regex')  # regex for 24hw


class RequestParams(Schema):
    cmd = fields.String(required=True)
    value = fields.String(required=True)

    @validates_schema
    def validates_cmd_params(self, values: Dict[str, str], *args: Any, **kwargs: Any) -> Dict[str, str]:
        if values['cmd'] not in VALID_CMD_PARAMS:
            raise ValidationError('Invalid: "cmd" contains invalid value')


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)  # не понимаю почему подсвечивается pycharm???
    # Nested-умеет хранить в себе др схему(как раз для спсиска словарей норм)
