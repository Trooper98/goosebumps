import RPi.GPIO as GPIO
import time

switch_On = True
switch_Off = False


class Single_Led():
    """A class for single color LED's """

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.switch = False

    def toggle(self, switch):
        GPIO.output(self.pin, switch)
        self.switch = not switch

    def lightsOn(self):
        self.toggle(switch_On)
        self.switch = True

    def lightsOut(self):
        self.toggle(switch_Off)
        self.switch = False

    def toString(self):
        return {"name": self.name, "switch": self.switch, "pin": self.pin}


class Multi_Led(Single_Led):
    """A class for Multi-Color LED's"""

    def __init__(self, name, redPin, greenPin, bluePin):
        self.name = name
        self.switch = False
        self.red = redPin
        self.green = greenPin
        self.blue = bluePin
        self.yellow = [redPin, greenPin]
        self.puprle = [redPin, bluePin]
        self.cyan = [greenPin, bluePin]
        self.white = [redPin, greenPin, bluePin]
        self.allColors = [redPin, greenPin, bluePin,
                          self.yellow, self.puprle, self.cyan, self.white]

    def toggle(self, pin, switch):
        GPIO.output(pin, switch)

    def lightsOn(self):
        self.toggle(self.red, switch_On)
        self.toggle(self.green, switch_On)
        self.toggle(self.blue, switch_On)
        self.switch = True

    def lightsOut(self):
        self.toggle(self.red, switch_Off)
        self.toggle(self.green, switch_Off)
        self.toggle(self.blue, switch_Off)
        self.switch = False

    def setColor(self, colors):
        self.lightsOut()
        for color in colors:
            self.toggle(color, switch_On)

    def rainbow(self):
        self.setColor(self.allColors)
        time.sleep(.5)

    def toString(self):
        return {"name": self.name, "switch": self.switch, "redPin": self.red, "greenPin": self.green, "bluePin": self.blue}
