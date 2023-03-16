import json


class CreateJson(object):
    def dict2json(self, data):
        if data:
            return json.dumps(data)
        return None

    def object2json(self, data):
        if data is not None:
            data = data.__dict__
            return json.dumps(obj=data)
        return None

    def json2dict(self, data):
        if data is not None:
            return json.loads(s=data)
        return None
