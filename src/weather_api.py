# encoding=utf8
# ^^^ VERY IMPORTANT THAT THIS IS NOT MOVED
# because sweden has special characters
# like "ö", "å" and "ä" that mess up the code and thus require the entire file to be encode
# link: https://markhneedham.com/blog/2015/05/21/python-unicodeencodeerror-ascii-codec-cant-encode-character-uxfc-in-position-11-ordinal-not-in-range128/
# anyways...
import requests


def getQuery(location, option, api_key):
    # Option [1 = coordinates]
    # Option [2 = postal code]
    # Option [3 = city]
    query = ""
    if option == 1:
        query = "https://api.weatherbit.io/v2.0/forecast/hourly?lat=" + \
            location["lat"]+"&lon="+location["long"] + \
                "&key="+api_key+"&units=S"
        return query
    elif option == 2:
        query = "https://api.weatherbit.io/v2.0/forecast/hourly?postal_code=" + \
            location["postal-code"]+"&country=" + \
                location["country"]+"&key="+api_key+"&units=S"
        return query
    elif option == 3:
        query = "https://api.weatherbit.io/v2.0/forecast/hourly?city=" + \
            location["city"]+"&country=" + \
                location["country"]+"&key="+api_key+"&units=S"
        return query
    elif option == 4:
        query = "https://api.weatherbit.io/v2.0/forecast/daily?city=" + \
            location["city"]+"&country=" + \
                location["country"]+"&key="+api_key
        return query
    elif option == 5:
        query = "https://api.weatherbit.io/v2.0/forecast/current?postal_code=" + \
            location["postal-code"]+"&country=" + \
                location["country"]+"&key="+api_key+"&units=S"
        return query


def getUpdate(query):
    response = requests.get(query)
    data = response.json()
    return data


def getTemperature(data):
    tempList = []
    for unit in data:
        temp = {
            "name": unit["weather.description"],
            "temp": unit["temp"],
            "feelsLike": unit["app_temp"]
        }
        tempList.append(temp)
    return tempList


def getWind(data):
    windList = []
    for unit in data:
        wind = {
            "direction": unit["wind_cdir"],
            "speed": unit["wind_spd"],
            "gust": unit["wind_gust_spd"],
        }
        windList.append(wind)
    return windList


def getRain(data):
    rainPredictions = []
    for unit in data:
        rain = {
            "direction": unit["wind_cdir"],
            "speed": unit["wind_spd"],
            "gust": unit["wind_gust_spd"],
        }
        rainPredictions.append(rain)
    return rainPredictions
