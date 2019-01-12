# File structure
src/
    |-main
    |-setup
    |-config [invisible]
    |- components/
        |- led [2 classes]
        |- weather_api [2 classes]

1. ```main.py``` this is the "main". I call the other files in here
2. ```setup.py``` this class stores configurations for the program
3. ```config.py``` stores my api keys. The reason it is invisible is t.gitignores which tell git not to record this file
4. _Components_
        - ```led.py``` is a controller. it controls the leds
        -  ```weather_api.py``` talks to the weather api (a big shoutout to the  [Darksky](https://darksky.net/poweredby/) __api__!)
        
