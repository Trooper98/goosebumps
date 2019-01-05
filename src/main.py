import RPi.GPIO as GPIO
from datetime import datetime
import time
import setup
import config
from components.led import Single_Led
from components.led import Multi_Led
from components.weather_api import darkSky_api as API

# API
apiKey = config.darksky_key
location = setup.lindholmen
api = API(location, apiKey, setup.preference)

# LEDS
multiLed = Multi_Led(
    "multi led", setup.multi_led["red"], setup.multi_led["green"], setup.multi_led["blue"])
greenLed = Single_Led("green", setup.single_greenPin)
redLed = Single_Led("red", setup.single_redPin)

switch_On = True
switch_Off = False

# Setting Up
# surpress warnings
GPIO.setwarnings(False)
# setup the pins accrding to B+ board rather than BCM
GPIO.setmode(GPIO.BOARD)

# set up multi-color LED #
GPIO.setup(multiLed.red, GPIO.OUT)
GPIO.setup(multiLed.green, GPIO.OUT)
GPIO.setup(multiLed.blue, GPIO.OUT)

# set up LED #
GPIO.setup(greenLed.pin, GPIO.OUT)
GPIO.setup(redLed.pin, GPIO.OUT)

# set up buttons #
# Set button pin to be an input pin and set initial value to be pulled low (off)
GPIO.setup(setup.leftButton["pin"], GPIO.IN)
GPIO.setup(setup.rightButton["pin"], GPIO.IN)

print(setup.multi_led)
print(setup.rightButton)
print(setup.leftButton)

multiLed.rainbow()
redLed.lightsOn()
greenLed.lightsOn()
time.sleep(3)
multiLed.lightsOut()
redLed.lightsOut()
greenLed.lightsOut()
print("{} led switch is {}".format(redLed.name, redLed.switch))
print("{} led switch is {}".format(greenLed.name, greenLed.switch))
print("{} led switch is {}".format(multiLed.name, multiLed.switch))

try:
    currentHour = datetime.now().hour  # get the current hour
    halfHour = 30  # keep track of half hour
    api.update()
    while True:
        currentMinute = datetime.now().minute
        hourStamp = datetime.now().hour

        if GPIO.input(setup.rightButton["pin"]) == 0:  # wind
            print("right")
            if(api.wind):
                multiLed.setColor(multiLed.white)
            else:
                multiLed.setColor(multiLed.red)
            print("current wind speeds are {} in the {} direction".format(
                api.data[0]["wind"]["windSpeed"], api.data[0]["wind"]["windDirection"]))
            print("weather description: {}".format(
                api.data[0]["description"]))
            time.sleep(.5)
            multiLed.setColor(multiLed.puprle)
            time.sleep(1)
            multiLed.lightsOut()
        elif GPIO.input(setup.leftButton["pin"]) == 0:  # rain
            print("left")
            if(api.wind):
                multiLed.setColor(multiLed.blue)
            else:
                multiLed.setColor(multiLed.red)
            print("current rain predictions are {}".format(
                api.data[0]["precip"]["precipProb"]))
            print("weather description: {}".format(
                api.data[0]["description"]))
            time.sleep(.5)
            multiLed.setColor(multiLed.puprle)
            time.sleep(1)
            multiLed.lightsOut()
        else:
            if(api.temp):  # if its gonna get cold
                greenLed.lightsOut()
                redLed.lightsOn()
            else:
                redLed.lightsOut()
                greenLed.lightsOn()

        if(currentMinute == halfHour):
            multiLed.rainbowLoop(1)
            if(api.wind):
                multiLed.setColor(multiLed.white)
                time.sleep(1)
                multiLed.setColor(multiLed.puprle)
            if(api.rain):
                multiLed.setColor(multiLed.blue)
                time.sleep(1)
                multiLed.setColor(multiLed.puprle)
            multiLed.setColor(multiLed.puprle)
            time.sleep(1)
            multiLed.lightsOut()

        if(hourStamp == currentHour):
            api.update()
            multiLed.rainbowLoop(2)
            if hourStamp == 23:
                currentHour = 0
            else:
                currentHour += 1
            multiLed.lightsOut()

finally:
    multiLed.lightsOut()
    greenLed.lightsOut()
    redLed.lightsOut()
