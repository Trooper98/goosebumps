########################################################
# Temperature
########################################################
# NOTE: these units are in celsius
# how things work = data gois into a list. The list can have a maximum
# of 2 data points for low and high that act as a threshold
# also, the values in the list should not exceed the absolute value of 100
cold = [-100, 5]
hot = [26, 100]

########################################################
# Hardware Pins
########################################################

# multi-color LED pins
red_pin = 33  # GPIO 13
green_pin = 31  # GPIO 6

# multi-color LED pins
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
# Current Location
########################################################
# NOTE: the structure and naming is important
gothenburg = {
    "lat": "57.696991",
    "long": "11.986500",
    "postal-code": "411 06",
    "country": "SE",
    "city": "Gothenburg"
}
lindholmen = {
    "lat": "57.706970",
    "long": "11.938020",
    "postal-code": "417 56",
    "country": "SE",
    "city": "Gothenburg"
}
