from requests import get
from __init__ import init

def get_all_capsules() -> dict:
    """Retreives current capsule information of all SpaceX capsules"""

    init()
    jsondata = get("https://api.spacexdata.com/v4/capsules").json()
    print(jsondata)
    return jsondata

def get_capsule(capsule_id: str) -> dict:
    """Retreives information of specified SpaceX capsule"""

    init()
    jsondata = get(f"https://api.spacexdata.com/v4/capsules/:{capsule_id}").json()
    return jsondata

def get_all_capsule_id() -> list[dict]:
    """Retrieves ID and type of all current capsules"""

    init()
    jsondata = get("https://api.spacexdata.com/v4/capsules").json()
    typeidlist = []

    for data in jsondata:
        typegrouping = {}
        typegrouping["id"] = data["id"]
        typegrouping["type"] = data["type"]
        typeidlist.append(typegrouping)
    
    return typeidlist