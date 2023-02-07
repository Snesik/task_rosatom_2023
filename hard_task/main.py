import requests


LAUNCHES = """
query Launches {
  launches {
    id
    details
    is_tentative
    launch_date_local
    launch_date_utc
  launch_date_unix
    mission_id
    mission_name
  }
}
"""
body1 = """
query Query {
  missions {
    id
  }
}
"""



#b = json.dumps(body)

a = requests.post('https://spacex-production.up.railway.app/',  json={'query': LAUNCHES}).json()
print()
