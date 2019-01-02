import RPi.GPIO as GPIO
Class 
redPin = 16 #GPIO 23
bluePin = 18 #GPIO 24
yellowPin = 22 #GPIO 25
greenPin = 32 #GPIO 12
switch_On = True 
switch_Off = False
# setup the pins accrding to B+ board rather than BCM
GPIO.setmode(GPIO.BOARD)

# setup the pins
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)
GPIO.setup(yellowPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)

# light up the pins
GPIO.output(redPin, switch_On)
GPIO.output(bluePin, switch_On)
GPIO.output(yellowPin, switch_On)
GPIO.output(greenPin, switch_On)

