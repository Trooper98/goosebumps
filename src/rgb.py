import RPi.GPIO as GPIO
import time
# setup the pins accrding to B+ board rather than BCM
GPIO.setmode(GPIO.BOARD)

redPin = 11  # GPIO 17
bluePin = 13  # GPIO 27
greenPin = 15  # GPIO 22
_rgb = [redPin, bluePin, greenPin]
switch_On = True
switch_Off = False

# setup the pins and switch on pins
for pin in _rgb:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, switch_On)

time.sleep(10)

# switch off leds
for pin in _rgb:
    GPIO.output(pin, switch_Off)
