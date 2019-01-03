import RPi.GPIO as GPIO
import time

leftB = 18  # GPIO 24 [left]
rightB = 16  # GPIO 23 [right]


def __init__(self, left, right):
    self.leftB = left
    self.rightB = right
    self.leftPressed = False
    self.rightPressed = False
    # surpress warnings
    GPIO.setwarnings(False)
    # setup the pins accrding to B+ board rather than BCM
    GPIO.setmode(GPIO.BOARD)
    # set up buttons
    GPIO.setup(leftB, GPIO.IN)
    GPIO.setup(rightB, GPIO.IN)


# toggles boolean and returns the new value after toggle
def toggle(self, button):
    if button == self.leftB:
        self.leftPressed = not self.leftPressed
        return self.leftPressed
    elif button == self.rightB:
        self.rightPressed = not self.rightPressed
        return self.rightPressed
