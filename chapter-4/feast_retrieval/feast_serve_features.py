import requests
import json

res = requests.post(
    url="http://127.0.0.1:6566/get-online-features", 
    json={
        "features": [
            "demographic:Sex"
        ],
        "entities": {
            "user_id": ["9f2ac416-06e1-44a0-87bd-d4787c85bf66"]
        }
    }
)

print(res.json())

