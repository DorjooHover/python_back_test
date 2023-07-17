from datetime import datetime
def serializeDict(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"],
        "timestamp": datetime[item["timestamp"]]
    }

def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i == '_id'}, **{i:a[i] for i in a if i != '_id'}}

def serializeList(a) -> list:
    return [serializeDict(i) for i in a]