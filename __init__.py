from requests import head

def init() -> None:
    """Checks for SpaceX API heartbeat"""

    alive = head("https://api.spacexdata.com/v4/capsules")
    if alive.status_code != 200:
        raise Exception("Cannot connect to SpaceX Capsule API!")