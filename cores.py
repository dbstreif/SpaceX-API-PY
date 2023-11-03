from requests import get
from __init__ import init

def get_all_cores() -> dict:
    """Retreives current core information of all SpaceX cores"""

    init()
    jsondata = get("https://api.spacexdata.com/v4/cores").json()
    return jsondata

def get_core(core_id: str) -> dict:
    """Retreives information of specified SpaceX core"""

    init()
    jsondata = get(f"https://api.spacexdata.com/v4/cores/:{core_id}").json()
    return jsondata

def get_core_id() -> list[dict]:
    """Retreives the id and serial number of all current cores"""

    init()
    jsondata = get("https://api.spacexdata.com/v4/cores").json()
    idseriallist = []

    for data in jsondata:
        serialgrouping = {}
        serialgrouping["id"] = data["id"]
        serialgrouping["serial"] = data["serial"]
        idseriallist.append(serialgrouping)
    
    return idseriallist

print(get_core_id())