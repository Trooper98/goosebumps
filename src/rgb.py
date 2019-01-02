import RPi.GPIO as GPIO
import time

redPin = 11  # GPIO 17
greenPin = 13  # GPIO 22
bluePin = 15  # GPIO 27
switch_On = True
switch_Off = False

# all the color codes
red = [redPin]
green = [greenPin]
blue = [bluePin]
yellow = [redPin, greenPin]
puprle = [redPin, bluePin]
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


# surpress warnings
GPIO.setwarnings(False)
# setup the pins accrding to B+ board rather than BCM
GPIO.setmode(GPIO.BOARD)
# set up main pins
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)


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

for color in allColors:
    setColor(color)
    time.sleep(.5)

# setColor(red)
# time.sleep(5)
# setColor(green)
# time.sleep(5)
# setColor(blue)
