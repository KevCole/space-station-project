import requests
import json

response = requests.get("http://api.open-notify.org/iss-now.json")
json_response = response.json()
longitude = json_response["iss_position"]["longitude"]
latitude = json_response["iss_position"]["latitude"]

print(latitude,longitude)