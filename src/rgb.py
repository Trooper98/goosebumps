import RPi.GPIO as GPIO
import time
import setup

switch_On = True
switch_Off = False


def __init__(self, redP, greenP, blueP):
    self.redP = redP
    self.greenP = greenP
    self.blueP = blueP
    self.rgb = [redP, greenP, blueP]
    # surpress warnings
    GPIO.setwarnings(False)
    # setup the pins accrding to B+ board rather than BCM
    GPIO.setmode(GPIO.BOARD)
    # set up main pins
    GPIO.setup(redP, GPIO.OUT)
    GPIO.setup(greenP, GPIO.OUT)
    GPIO.setup(blueP, GPIO.OUT)


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


def rainbow():
    for color in setup.allColors:
        setColor(color)
        time.sleep(.5)


rainbow()
lightsOut()
