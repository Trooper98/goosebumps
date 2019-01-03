import RPi.GPIO as GPIO
import time
import setup

class Led:

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
        self.rainbow(setup.allColors)
        print("led is set up")
        print(setup.allColors)
    
    @staticmethod
    def toggle(pin, switch):
        GPIO.output(pin, switch)

    @staticmethod
    def lightsOut(colors):
        for pin in colors:
            toggle(pin, switch_Off)

    @staticmethod
    def setColor(colors):
        # switch off leds
        lightsOut()
        for color in colors:
            toggle(color, switch_On)

    @staticmethod
    def rainbow(colors):
        for color in colors:
            setColor(color)
            time.sleep(.5)


led = Led(setup.redPin, setup.greenPin, setup.bluePin)
red = setup.red
print(red)
led.setColor(red)
led.rainbow(setup.allColors)
led.lightsOut(setup._rgb)
