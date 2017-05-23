import mongoengine

host = "ds149431.mlab.com"
port = 49431
db_name = "laujilao-account"
user_name = "admin"
password = "341607"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())