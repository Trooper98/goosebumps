# rgb LED pins
redPin = 11  # GPIO 17
greenPin = 13  # GPIO 22
bluePin = 15  # GPIO 27
_rgb = [redPin, greenPin, bluePin]

# all the color codes
red = [redPin]
green = [greenPin]
blue = [bluePin]
yellow = [redPin, greenPin]
puprle = [redPin, bluePin]
cyan = [green, blue]
white = [red, blue, green]
allColors = [red, green, blue, yellow, puprle, white]

# buttons
leftB = 18  # GPIO 24 [left]
rightB = 16  # GPIO 23 [right]
