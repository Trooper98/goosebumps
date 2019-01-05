########################################################
# Hardware Pins
########################################################
# single-color LED pins
single_redPin = 31  # GPIO 13
single_greenPin = 33  # GPIO 6

# multi-color LED pins
multi_redPin = 11  # GPIO 17
multi_greenPin = 13  # GPIO 22
multi_bluePin = 15  # GPIO 27

# buttons
rightB = 16  # GPIO 23 [right]
leftB = 18  # GPIO 24 [left]

# Button
leftButton = {
    "name": "left",
    "pin": leftB,
    "switch": False
}

rightButton = {
    "name": "right",
    "pin": rightB,
    "switch": False
}

# Led
multi_led = {
    "red": multi_redPin,
    "green": multi_greenPin,
    "blue": multi_bluePin
}

########################################################
# Color Codes
########################################################
# NOTE: it refers to the hard ware RGB LED pins
# all the color codes
red = [multi_led["red"]]
green = [multi_led["green"]]
blue = [multi_led["blue"]]
yellow = [red, green]
puprle = [red, blue]
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
