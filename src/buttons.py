# HOLA
# This is just a basic template for manipulating the rgb LED.
# Try and switch things up to see how it works.

import RPi.GPIO as GPIO
import time

redPin = 11  # GPIO 17
greenPin = 13  # GPIO 22
bluePin = 15  # GPIO 27
button1 = 16  # GPIO 23
button2 = 18  # GPIO 24
switch_On = True
switch_Off = False

# all the color codes
red = [redPin]
green = [greenPin]
blue = [bluePin]
yellow = [redPin, greenPin]
puprle = [redPin, bluePin]
cyan = [green, blue]
white = [red, blue, green]
_rgb = [red, green, blue]
allColors = [red, green, blue, yellow, puprle, white]


def toggle(pin, switch):
    GPIO.output(pin, switch)


def lightsOut():
    for pin in _rgb:
        toggle(pin, switch_Off)


def setColor(colors):
    # switch off leds
    lightsOut()
    for color in colors:
        toggle(color, switch_On)


def rainbow():
    for color in allColors:
        setColor(color)
        time.sleep(.5)


# surpress warnings
GPIO.setwarnings(False)
# setup the pins accrding to B+ board rather than BCM
GPIO.setmode(GPIO.BOARD)
# set up RGB led pins
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
# set up buttons
GPIO.setup(button1, GPIO.OUT)
GPIO.setup(button2, GPIO.OUT)

# setup the pins and switch on the led
count = 0
for pin in _rgb:
    setColor(pin)
    if(count < 3):
        time.sleep(1)
        count = count + 1
        print(count)

# switch off leds
lightsOut()
time.sleep(3)

rainbow()
lightsOut()


# get the number of colors
colorWheel = len(allColors)
start = 1
end = colorWheel

current = 1
while True:
    setColor(current)
    if GPIO.input(button1):
        # get next color
        if(current == end):  # if the next number is greater than colorwheel
            current = start
        else:
            current += 1
    else if GPIO.input(button2):
        # get prev color
        if(current == start):  # if the next number is greater than colorwheel
            current = end
        else:
            current -= 1
