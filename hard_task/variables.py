
API = 'https://spacex-production.up.railway.app/'
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
ROCKETS = """
query Query {
  rockets {
    active
    boosters
    company
    cost_per_launch
    id
    stages
    success_rate_pct
    type
    wikipedia
  }
}
"""
MISSIONS = """
query Missions {
  missions {
    description
    id
    manufacturers
    name
    twitter
    website
    wikipedia
  }
}
"""