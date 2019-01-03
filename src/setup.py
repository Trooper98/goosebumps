########################################################
# Hardware Pins
########################################################

# rgb LED pins
redPin = 11  # GPIO 17
greenPin = 13  # GPIO 22
bluePin = 15  # GPIO 27
_rgb = [redPin, greenPin, bluePin]

# buttons
rightB = 16  # GPIO 23 [right]
leftB = 18  # GPIO 24 [left]

########################################################
# Color Codes
########################################################
# NOTE: it refers to the hard ware RGB LED pins
# all the color codes
red = [redPin]
green = [greenPin]
blue = [bluePin]
yellow = [redPin, greenPin]
puprle = [redPin, bluePin]
cyan = [green, blue]
white = [red, blue, green]
allColors = [red, green, blue, yellow, puprle, white]

########################################################
# Timer
########################################################
# NOTE: all measumernets are done in seconds
sec = 60
mins = sec * 60
hour = mins * 60
day = hour * 24
