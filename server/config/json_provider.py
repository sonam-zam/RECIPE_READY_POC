import json

from flask.json.provider import JSONProvider

from server.config.json_encoder import CustomJSONEncoder


class CustomJSONProvider(JSONProvider):

    def dumps(self, obj, **kwargs):
        return json.dumps(cls=CustomJSONEncoder, obj=obj)

    def loads(self, s: str | bytes, **kwargs):
        return json.loads(s, **kwargs)
