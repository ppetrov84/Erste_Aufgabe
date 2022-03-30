from turtle import title
import requests

params = {"query": "Munich"}
headers = {"Content-Type": "application/json"}
result = requests.get(
    "https://www.metaweather.com/api/location/search/", params=params, headers=headers)

json = result.json()
print("JSON response: ", json)
