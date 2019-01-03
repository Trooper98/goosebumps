import RPi.GPIO as GPIO
import time

leftB = 18  # GPIO 24 [left]
rightB = 16  # GPIO 23 [right]


class Button:
    def __init__(self, pin, name):
        self.name = name
        self.pin = pin
        self.pressed = False
        # surpress warnings
        GPIO.setwarnings(False)
        # setup the pins accrding to B+ board rather than BCM
        GPIO.setmode(GPIO.BOARD)
        # set up buttons
        GPIO.setup(self.pin, GPIO.IN)

    def toggle(self):
        # toggles boolean and returns the new value after toggle
        self.pressed = not self.pressed
        return self.pressed


b = Button(leftB, "left")

print(b.toggle())
