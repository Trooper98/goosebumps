import config
import requests

apiKey = config.apiKey
dataQuery = "https://api.weatherbit.io/v2.0/forecast/hourly?lat=57.705644&lon=11.9368388&key="
data = requests.get(dataQuery+apiKey)
print(data.city_name)
