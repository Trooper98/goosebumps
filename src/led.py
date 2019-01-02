import RPi.GPIO as GPIO
import time


class Led:
    """ this class defines the available pins """


redPin = 16  # GPIO 23
bluePin = 18  # GPIO 24
yellowPin = 22  # GPIO 25
greenPin = 32  # GPIO 12
switch_On = True
switch_Off = False


def __init__(self):
    setup_pins()
    # blink lights
    self.toggle_pins(switch_On)
    time.sleep(3)
    self.toggle_pins(switch_Off)


def setup_pins():
    # setup the pins accrding to B+ board rather than BCM
    GPIO.setmode(GPIO.BOARD)
    # setup the pins
    GPIO.setup(redPin, GPIO.OUT)
    GPIO.setup(bluePin, GPIO.OUT)
    GPIO.setup(yellowPin, GPIO.OUT)
    GPIO.setup(greenPin, GPIO.OUT)


def toggle_leds(switch):
    # light up the pins
    GPIO.output(redPin, switch)
    GPIO.output(bluePin, switch)
    GPIO.output(yellowPin, switch)
    GPIO.output(greenPin, switch)


def toggle(pin, switch):
    GPIO.output(pin, switch)
