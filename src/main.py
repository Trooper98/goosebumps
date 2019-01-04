import RPi.GPIO as GPIO
import json
from datetime import datetime
import time
import setup
import weather_api as api
import config

# Button
leftButton = {
    "name": "left",
    "pin": setup.leftB,
    "switch": False
}

rightButton = {
    "name": "right",
    "pin": setup.rightB,
    "switch": False
}

# Led
multi_led = {
    "red": setup.redPin,
    "green": setup.greenPin,
    "blue": setup.bluePin
}

green_led = [setup.green_pin, False]
red_led = [setup.red_pin, False]

switch_On = True
switch_Off = False

# API
apiKey = config.apiKey
location = setup.lindholmen

option = 1
query = api.getQuery(location, option, apiKey)
response = api.getUpdate(query)
data = response["data"]
dataPoints = []

currentDate = time.gmtime(time.time())
currentHour = currentDate.tm_hour

count = 0


def toggle(pin, switch):
    GPIO.output(pin, switch)


def lightsOut():
    for pin in setup._rgb:
        toggle(pin, switch_Off)


def setColor(colors):
    # switch off leds
    lightsOut()
    for color in colors:
        toggle(color, switch_On)


def rainbow(colors):
    for color in colors:
        setColor(color)
        time.sleep(.5)


def apiHour(timestamp):
    return int(datetime.utcfromtimestamp(timestamp).strftime("%H"))


def refillData(data):
    for hour in data:
        apihour = apiHour(hour["ts"])
        if(apihour >= currentHour):  # if unit has passed in time, then disregard it
            info = {
                "location": response["city_name"],
                "country": response["country_code"],
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


# Setting Up
# surpress warnings
GPIO.setwarnings(False)
# setup the pins accrding to B+ board rather than BCM
GPIO.setmode(GPIO.BOARD)

# set up multi-color LED #
GPIO.setup(multi_led["red"], GPIO.OUT)
GPIO.setup(multi_led["green"], GPIO.OUT)
GPIO.setup(multi_led["blue"], GPIO.OUT)

# set up LED #
GPIO.setup(green_led[0], GPIO.OUT)
GPIO.setup(red_led[0], GPIO.OUT)

# set up buttons #
# Set button pin to be an input pin and set initial value to be pulled low (off)
GPIO.setup(leftButton["pin"], GPIO.IN)
GPIO.setup(rightButton["pin"], GPIO.IN)

print(multi_led)
print(rightButton)
print(leftButton)


rainbow(setup.allColors)
setColor(setup.white)
toggle(red_led[0], switch_On)
toggle(green_led[0], switch_On)
time.sleep(3)
lightsOut()
toggle(red_led[0], switch_Off)
toggle(green_led[0], switch_Off)

try:
    while True:
        if GPIO.input(rightButton["pin"]) == 0:
            print("right")
            toggle(red_led[0], red_led[1])
            red_led[1] = not red_led[1]
            time.sleep(.5)
        elif GPIO.input(leftButton["pin"]) == 0:
            print("left")
            toggle(green_led[0], green_led[1])
            green_led[1] = not green_led[1]
            time.sleep(.5)
        else:
            setColor(setup.puprle)
finally:
    lightsOut()
