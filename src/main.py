import rgb
import setup
from buttons import Button
import weather_api

data = weather_api.getUpdate()
#leftButton = Button(setup.leftB, "left")
#rightButton = Button(setup.rightB, "right")
#print("{} has a pressed value of {} and a pin number of {}".format(
#    leftButton.name, leftButton.pressed, leftButton.pin))
print(data["city_name"])
