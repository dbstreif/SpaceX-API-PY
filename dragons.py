from requests import get
from __init__ import init

def get_all_dragons() -> dict:
    """Retreives current dragon information on all dragons"""

    init()
    jsondata = get("https://api.spacexdata.com/v4/dragons").json()
    return jsondata

def get_crew_member(dragon_id: str) -> dict:
    """Retreives information of specified SpaceX dragon"""

    init()
    jsondata = get(f"https://api.spacexdata.com/v4/dragons/:{dragon_id}").json()
    return jsondata