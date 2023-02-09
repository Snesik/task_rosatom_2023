import requests
import json

from graphql_query import Operation, Query

API = 'https://spacex-production.up.railway.app/'
launches = Query(
    name='launches', fields=[
        'id', 'details', 'is_tentative',
        'launch_date_local', 'launch_date_utc',
        'mission_name', 'launch_success', 'launch_year',
        'static_fire_date_utc', 'tentative_max_precision',
        'upcoming'
    ]
)
rockets = Query(
    name='rockets', fields=[
        'id', 'active', 'boosters',
        'cost_per_launch', 'stages',
        'success_rate_pct', 'type', 'wikipedia'
    ]
)

missions = Query(
    name='missions', fields=[
        'id', 'description', 'manufacturers',
        'name', 'twitter', 'website', 'wikipedia'
    ]
)

operation = Operation(type='query', queries=[launches, rockets, missions])


def get_data_api(query: Operation, href: str) -> dict:
    results = {}
    response = requests.post(href, json={'query': query.render()}, timeout=20).text
    results.update(json.loads(response)['data'])
    return results



