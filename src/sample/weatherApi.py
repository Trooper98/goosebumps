import config
import requests

apiKey = config.apiKey
query = "https://api.weatherbit.io/v2.0/forecast/hourly?lat=57.705644&lon=11.9368388&key="
response = requests.get(query+apiKey)
data = response.json()
print(data["city_name"])
