########################################################
# Temperature and stuff
########################################################
# NOTE: the temperature unit is in degrees Celsius

# I once went to rome during its peak (32) and id rather not get close to that again
hot = 27
cold = 4

badWind = 5.5  # more than this exceeds my comfort
willRain = 0.2  # more than this percentage and you better get a rain coat

preference = {
    "temp": {
        "hot": hot,
        "cold": cold
    },
    "badWind": badWind,
    "willRain": willRain
}

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
