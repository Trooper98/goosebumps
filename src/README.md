# File structure
src/
    |- buttons
    |-config [invisible]
    |-main
    |-rgb
    |-weather_api

1. ```buttons.py``` stores methods for the buttons that I can use to check out info
2. ```config.py``` stores my api keys. The reason it is invisible is t.gitignores which tell git not to record this file
2. ```main.py``` this is the "main". I call the other files in here
2. ```rgb.py``` is a controller. it sets the colors on the rpi
2. ```weather_api.py``` talks to the weather api (shoutout [weatherbit][https://www.weatherbit.io])

####### note
src/
    |-main
    |- components/
        |- buttons
        |-config [invisible]
        |-rgb
        |-weather_api

My original structure was ^ but given how constrained i was from importing python files (I searched countless of stackoverflow forums (e.g. "How to 
fix “Attempted relative import in non-package” even with __init__.py") with no success)
Also, its like 2:42 am so i figured ill frshen up the repo when im done zzzzzzzZZZZzzzZZzZz
