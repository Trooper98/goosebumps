# encoding=utf8
# ^^^ VERY IMPORTANT THAT THIS IS NOT MOVED
# because sweden has special characters
# like "ö", "å" and "ä" that mess up the code and thus require the entire file to be encode
# link: https://markhneedham.com/blog/2015/05/21/python-unicodeencodeerror-ascii-codec-cant-encode-character-uxfc-in-position-11-ordinal-not-in-range128/
# anyways...
from datetime import datetime
import time
import requests
import json


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
        self.meta = self.getMetaData(self.rawData)

    def getQuery(self, location, api_key):
        query = "https://api.darksky.net/forecast/" + \
            api_key+"/"+location["lat"]+","+location["long"]+"?units=si"
        return query

    def getRawData(self):
        response = requests.get(self.query).json()
        return response

    def timestampInHour(self, timestamp):
        return int(datetime.utcfromtimestamp(timestamp).strftime("%H"))

    def getMetaData(self, rawData):
        data = rawData["hourly"]["data"]
        coldest = data[0]["temperature"]
        coldestFeel = data[0]["apparentTemperature"]
        hottest = data[0]["temperature"]
        hottestFeel = data[0]["apparentTemperature"]
        rainChance = data[0]["precipProbability"]
        wind = data[0]["windSpeed"]

        # Data model for meta
        meta = {
            "temp": self.data[0]["temperature"]["temp"],
            "coldest": coldest,
            "coldestFeel": coldestFeel,
            "hottest": hottest,
            "hottestFeel": hottestFeel,
            "rainChance": rainChance,
            "wind": wind
        }
        count = 0

        for unit in data:
            if unit["temperature"] < coldest:
                coldest = unit["temperature"]
            if unit["apparentTemperature"] < coldestFeel:
                coldestFeel = unit["apparentTemperature"]
            if unit["temperature"] > hottest:
                hottest = unit["temperature"]
            if unit["apparentTemperature"] < hottestFeel:
                hottestFeel = unit["apparentTemperature"]
            if unit["precipProbability"] > rainChance:
                rainChance = unit["precipProbability"]
            if unit["windSpeed"] > wind:
                wind = unit["windSpeed"]
            count += 1
            if(count == 12):
                break

        # avoid unecessary information
        if(hottest <= coldest or hottestFeel <= coldestFeel):
            meta = {
                "temp": self.data[0]["temperature"]["temp"],
                "coldest": coldest,
                "coldestFeel": coldestFeel,
                "rainChance": rainChance,
                "wind": wind
            }

        return meta

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
        self.rawData = self.getRawData()  # update raw data
        self.data = self.filterData(self.rawData)  # update overall data
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

            if data["precip"]["precipProb"] >= self.userPreference["willRain"]:
                self.rain = True
            else:
                self.rain = False

            if data["wind"]["windSpeed"] >= self.userPreference["badWind"]:
                self.wind = True
            else:
                self.wind = False
        self.meta = self.getMetaData(self.rawData)  # update meta data

    def toString(self):
        res = {"rain": self.rain, "wind": self.wind,
               "temp": self.temp, "currentData": self.meta}
        return json.dumps(res, indent=1)
