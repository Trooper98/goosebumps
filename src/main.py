import RPi.GPIO as GPIO
import json
import time
import setup
import weather_api as api

######
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
led = {
    "red": setup.redPin,
    "green": setup.greenPin,
    "blue": setup.bluePin
}
switch_On = True
switch_Off = False
#############


#############
# Setting Up
# surpress warnings
GPIO.setwarnings(False)
# setup the pins accrding to B+ board rather than BCM
GPIO.setmode(GPIO.BOARD)

# set up led #
GPIO.setup(led["red"], GPIO.OUT)
GPIO.setup(led["green"], GPIO.OUT)
GPIO.setup(led["blue"], GPIO.OUT)

# set up buttons #
GPIO.setup(leftButton["pin"], GPIO.IN)
GPIO.setup(rightButton["pin"], GPIO.IN)
#############


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


print(led)
print(rightButton)
print(leftButton)

rainbow(setup.allColors)
setColor(setup.white)
while True:
    print("current is {}".format(current))
    if GPIO.input(rightButton["pin"]) == 0:
        # will it rain
        time.sleep(180)
    elif GPIO.input(leftButton["pin"]) == 0:
        # windy?
        time.sleep(180)
    elif (False == True):
        # this is meant to be the case that closes program
    else:
        # is the temparature good
