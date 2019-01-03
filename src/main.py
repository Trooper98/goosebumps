# import rgb
import setup
from buttons import Button
import weather_api

data = weather_api.getUpdate()
leftButton = Button(setup.leftB)
print(leftButton.toggle())
