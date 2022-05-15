import requests
import json

res = requests.get("https://github.com/rroyson?tab=repositories")
response = res.json()

print(response)
