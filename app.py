import requests #import request library the standard for making http request with Python
import json # Import library used to work with JSON

response = requests.get("http://api.open-notify.org/iss-now.json") #send GET request to API enpoint
json_response = response.json() #store the json response in a variable named json_reponse
longitude = json_response["iss_position"]["longitude"] #extract the longitude from the JSON response object
latitude = json_response["iss_position"]["latitude"] #extract the latitide from the JSON repsonse object

print(latitude,longitude) #print to the console the latitide and longitude of the international space station