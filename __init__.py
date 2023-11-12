from requests import head

def init() -> None:
    """Checks for SpaceX API heartbeat"""

    alive = head("https://api.spacexdata.com/")
    if alive.status_code != 200:
        raise Exception("Cannot connect to SpaceX Capsule API!")

if __name__ == "__main__":
    init()