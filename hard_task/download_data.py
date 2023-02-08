import json

import requests

from variables import LAUNCHES, MISSIONS, ROCKETS, API
from models import RocketsModel


def get_data_api(api_requests: list, href: str) -> dict:
    """
    :param api_requests: list query
    :param href: str url

    """
    results = {}
    for query in api_requests:
        response = requests.post(href, json={'query': query}, timeout=20).text
        results.update(json.loads(response)['data'])
    return results


data = get_data_api([LAUNCHES, MISSIONS, ROCKETS], API)
