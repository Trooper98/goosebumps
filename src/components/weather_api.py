# encoding=utf8
# ^^^ VERY IMPORTANT THAT THIS IS NOT MOVED
# because sweden has special characters
# like "ö", "å" and "ä" that mess up the code and thus require the entire file to be encode
# link: https://markhneedham.com/blog/2015/05/21/python-unicodeencodeerror-ascii-codec-cant-encode-character-uxfc-in-position-11-ordinal-not-in-range128/
# anyways...
from datetime import datetime
import time
import requests


class darkSky_api():
    """A Broker Class for the Dark Sky Api"""

    def __init__(self, location, api_key, userPreference):
        self.rain = False
        self.wind = False
        self.temp = False
        self.userPreference = userPreference
        self.query = self.getQuery(location, api_key)
        self.rawData = self.getRawData()
        self.data = self.filterData(self.rawData)

    def getQuery(self, location, api_key):
        query = "https://api.darksky.net/forecast/" + \
            api_key+"/"+location["lat"]+","+location["long"]+"?units=si"
        return query

    def getRawData(self):
        response = requests.get(self.query).json()
        return response

    def timestampInHour(self, timestamp):
        return int(datetime.utcfromtimestamp(timestamp).strftime("%H"))

    def filterData(self, rawData):
        data = rawData["hourly"]["data"]
        dataset = []
        count = 0
        for point in data:
            unit = {
                "time": self.timestampInHour(point["time"]),
                "description": point["summary"],
                "temperature": {
                    "temp": point["temperature"],
                    "tempFeel": point["apparentTemperature"]
                },
                "precip": {
                    "precipProb": point["precipProbability"],
                    # "precipType": point["precipType"]
                },
                "wind": {
                    "windSpeed": point["windSpeed"],
                    "windDirection": point["windBearing"]
                }
            }
            dataset.append(unit)
            count += 1
            if(count == 5):  # i want five data points at most
                break
        return dataset

    def update(self):
        self.data = self.filterData(self.getRawData())
        for data in self.data:
            if data["temperature"]["temp"] < self.userPreference["temp"]["cold"]:
                self.temp = True
            elif data["temperature"]["temp"] > self.userPreference["temp"]["hot"]:
                self.temp = True
            else:
                self.temp = False

            if data["temperature"]["tempFeel"] < self.userPreference["temp"]["cold"]:
                self.temp = True
            elif data["temperature"]["tempFeel"] > self.userPreference["temp"]["hot"]:
                self.temp = True
            else:
                self.temp = False

            if data["precip"]["precipProb"] > self.userPreference["willRain"]:
                self.rain = True
            else:
                self.rain = False

            if data["wind"]["windSpeed"] > self.userPreference["badWind"]:
                self.wind = True
            else:
                self.wind = False

    def toString(self):
        return {"rain": self.rain, "wind": self.wind, "temp": self.temp, "currentData": {self.data}, "userPreference": self.userPreference}


class weatherIO():
    """A Broker Class for WeatherIO Api"""

    def __init__(self, location, api_key):
        self.query = self.getQuery(location, 1, api_key)
        self.rawData = self.getData(self.query)
        self.data = self.filterData(self.rawData)

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

    def filterData(self, rawData):
        count = 0
        dataPoints = []
        currentHour = time.gmtime(time.time()).tm_hour

        for hour in rawData["data"]:
            apihour = self.apiHour(hour["ts"])
            if(apihour >= currentHour):  # if unit has passed in time, then disregard it
                info = {
                    "location": rawData["city_name"],
                    "country": rawData["country_code"],
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

    def getAllData(self, rawData):
        dataPoints = []

        for hour in rawData["data"]:

            info = {
                "location": rawData["city_name"],
                "country": rawData["country_code"],
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

    def getData(self, query):
        response = requests.get(query).json()
        return response
