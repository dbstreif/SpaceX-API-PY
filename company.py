from requests import get
from __init__ import init

def get_company_info() -> dict:
    """Retrieves latest SpaceX company data"""

    init()
    jsondata = get("https://api.spacexdata.com/v4/company").json()
    return jsondata