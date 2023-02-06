import json

import requests

headers = {'content-type': 'application/x-www-form-urlencoded'}

body = """
query Ships {
  ships {
    model
    name
    type
    status
  }
}
"""
body1 = """
query Dragons {
  dragons {
    name
    first_flight
    diameter {
      feet
    }
    launch_payload_mass {
      lb
    }
  }
}
"""



b = json.dumps(body)

a = requests.post('https://spacex-production.up.railway.app/', json={'query': body1})
print()
