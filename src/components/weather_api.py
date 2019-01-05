# encoding=utf8
# ^^^ VERY IMPORTANT THAT THIS IS NOT MOVED
# because sweden has special characters
# like "ö", "å" and "ä" that mess up the code and thus require the entire file to be encode
# link: https://markhneedham.com/blog/2015/05/21/python-unicodeencodeerror-ascii-codec-cant-encode-character-uxfc-in-position-11-ordinal-not-in-range128/
# anyways...
import requests
from datetime import datetime
import time


class WeatherApi():
    """A Broker Class for Weather Api"""

    def __init__(self, location, api_key):
        query = self.getQuery(location, 1, api_key)
        dataSet = self.getUpdate(query)
        self.data = self.filterData(dataSet)

    def getQuery(self, location, option, api_key):
        # Option [1 = coordinates]
        # Option [2 = postal code]
        # Option [3 = city]
        query = ""
        if option == 1:
            query = "https://api.weatherbit.io/v2.0/forecast/hourly?lat=" + \
                location["lat"]+"&lon="+location["long"] + "&key="+api_key
        elif option == 2:
            query = "https://api.weatherbit.io/v2.0/forecast/hourly?postal_code=" + \
                location["postal-code"]+"&country=" +\
                location["country"]+"&key="+api_key
        elif option == 3:
            query = "https://api.weatherbit.io/v2.0/forecast/hourly?city=" +\
                location["city"]+"&country=" +\
                location["country"]+"&key="+api_key+"&units=S"
        elif option == 4:
            query = "https://api.weatherbit.io/v2.0/forecast/daily?city=" +\
                location["city"]+"&country=" +\
                location["country"]+"&key="+api_key
        elif option == 5:
            query = "https://api.weatherbit.io/v2.0/forecast/current?postal_code=" +\
                location["postal-code"]+"&country=" +\
                location["country"]+"&key="+api_key+"&units=S"
        return query

    def apiHour(self, timestamp):
        return int(datetime.utcfromtimestamp(timestamp).strftime("%H"))

    def filterData(self, dataSet):
        count = 0
        dataPoints = []
        currentHour = time.gmtime(time.time()).tm_hour

        for hour in dataSet["data"]:
            apihour = self.apiHour(hour["ts"])
            if(apihour >= currentHour):  # if unit has passed in time, then disregard it
                info = {
                    "location": dataSet["city_name"],
                    "country": dataSet["country_code"],
                    "time": hour["datetime"],
                    "temp": hour["temp"],
                    "tempFeel": hour["app_temp"],
                    "wind": hour["wind_spd"],
                    "wind_spd": hour["wind_gust_spd"],
                    "wind_dir": hour["wind_cdir"],
                    "descr": hour["weather"]["description"]
                }
                dataPoints.append(info)
                count += 1
                if(count == 12):
                    break
        return dataPoints

    def getAllData(self, dataSet):
        dataPoints = []

        for hour in dataSet["data"]:

            info = {
                "location": dataSet["city_name"],
                "country": dataSet["country_code"],
                "time": hour["datetime"],
                "temp": hour["temp"],
                "tempFeel": hour["app_temp"],
                "wind": hour["wind_spd"],
                "wind_spd": hour["wind_gust_spd"],
                "wind_dir": hour["wind_cdir"],
                "descr": hour["weather"]["description"]
            }
            dataPoints.append(info)
        return dataPoints

    def getUpdate(self, query):
        response = requests.get(query).json()
        return response
