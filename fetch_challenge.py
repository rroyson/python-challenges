import requests
import json

# Trying out requests api

res = requests.get("https://github.com/rroyson?tab=repositories")
response = res.json()

print(response)
