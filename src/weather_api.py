# encoding=utf8
# ^^^ VERY IMPORTANT THAT THIS IS NOT MOVED
# because sweden has special characters
# like "ö", "å" and "ä" that mess up the code and thus require the entire file to be encode
# link: https://markhneedham.com/blog/2015/05/21/python-unicodeencodeerror-ascii-codec-cant-encode-character-uxfc-in-position-11-ordinal-not-in-range128/
# anyways...
import config
import requests

apiKey = config.apiKey
query = "https://api.weatherbit.io/v2.0/forecast/hourly?lat=57.705644&lon=11.9368388&key="


def getUpdate():
    response = requests.get(query+apiKey)
    data = response.json()
    return data
