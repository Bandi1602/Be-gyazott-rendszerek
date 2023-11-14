





from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

nothing = (0,0,0) #no color
black = (0,0,255)


b = black
o = nothing
    
Elso = [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,b,b,o,o,o,
o,o,o,b,b,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o]

Masodik = [
b,b,o,o,o,o,o,o,
b,b,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,b,b,
o,o,o,o,o,o,b,b]

    
Harmadik = [
b,b,o,o,o,o,o,o,
b,b,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,b,b,o,o,o,
o,o,o,b,b,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,b,b,
o,o,o,o,o,o,b,b]

Negyedik = [
b,b,o,o,o,o,b,b,
b,b,o,o,o,o,b,b,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
b,b,o,o,o,o,b,b,
b,b,o,o,o,o,b,b]

Otodik = [
b,b,o,o,o,o,b,b,
b,b,o,o,o,o,b,b,
o,o,o,o,o,o,o,o,
o,o,o,b,b,o,o,o,
o,o,o,b,b,o,o,o,
o,o,o,o,o,o,o,o,
b,b,o,o,o,o,b,b,
b,b,o,o,o,o,b,b]

Hatodik = [
b,b,o,o,o,o,b,b,
b,b,o,o,o,o,b,b,
o,o,o,o,o,o,o,o,
b,b,o,o,o,o,b,b,
b,b,o,o,o,o,b,b,
o,o,o,o,o,o,o,o,
b,b,o,o,o,o,b,b,
b,b,o,o,o,o,b,b]

while True:
#go throw all joystick’s events
    for event in sense.stick.get_events():
        if event.action == "pressed":
            
            val =randint(1,6)
            time.sleep(1)
            
            if val == 1:
                sense.set_pixels(Elso)
            elif val == 2:
                sense.set_pixels(Masodik)
            elif val == 3:
                sense.set_pixels(Harmadik)
            elif val == 4:
                sense.set_pixels(Negyedik)
            elif val == 5:
                sense.set_pixels(Hatodik)
            elif val == 6:
                sense.set_pixels(Hatodik)
            time.sleep(2)
            sense.clear()
            
            
            
