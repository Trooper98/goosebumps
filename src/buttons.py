import RPi.GPIO as GPIO
import time

leftB = 18  # GPIO 24 [left]
rightB = 16  # GPIO 23 [right]


class Button:
    def __init__(self, button):
        self.button = button
        self.buttonPressed = False
        # surpress warnings
        GPIO.setwarnings(False)
        # setup the pins accrding to B+ board rather than BCM
        GPIO.setmode(GPIO.BOARD)
        # set up buttons
        GPIO.setup(button, GPIO.IN)

    def toggle(self):
        # toggles boolean and returns the new value after toggle
        self.button = not self.button
        return self.button


b = Button(leftB)

print(b.toggle())
