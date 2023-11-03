from requests import get
from __init__ import init

def get_all_crew_members() -> dict:
    """Retreives current crew information on all crew members"""

    init()
    jsondata = get("https://api.spacexdata.com/v4/crew").json()
    return jsondata

def get_crew_member(crew_id: str) -> dict:
    """Retreives information of specified SpaceX crew member"""

    init()
    jsondata = get(f"https://api.spacexdata.com/v4/crew/:{crew_id}").json()
    return jsondata