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

    def toggle(self):
        self.switch = not self.switch
        GPIO.output(self.pin, self.switch)

    def manualToggle(self, switch):
        GPIO.output(self.pin, switch)
        self.switch = switch

    def lightsOn(self):
        self.manualToggle(switch_On)
        self.switch = True

    def lightsOut(self):
        self.manualToggle(switch_Off)
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

    def manualToggle(self, pin, switch):
        GPIO.output(pin, switch)
        self.switch = switch

    def lightsOn(self):
        self.manualToggle(self.red, switch_On)
        self.manualToggle(self.green, switch_On)
        self.manualToggle(self.blue, switch_On)
        self.switch = True

    def lightsOut(self):
        self.manualToggle(self.red, switch_Off)
        self.manualToggle(self.green, switch_Off)
        self.manualToggle(self.blue, switch_Off)
        self.switch = False

    def setColor(self, colors):
        self.lightsOut()
        for color in colors:
            self.manualToggle(color, switch_On)

    def rainbow(self):
        self.setColor(self.allColors)
        self.switch = True
        time.sleep(.5)

    def toString(self):
        return {"name": self.name, "switch": self.switch, "redPin": self.red, "greenPin": self.green, "bluePin": self.blue}
