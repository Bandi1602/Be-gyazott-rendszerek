from sense_hat import SenseHat
import random
import time

sense = SenseHat()

def number_gen(event):
    if event.action == "pressed":
            
            val =randint(1,6)
            
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
            sleep(0.1)
            sense.clear()
            


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


dice = (Elso, Masodik,Harmadik,Negyedik,Otodik,Hatodik )
for i in range(0,30):
    choice = random.choice(dice)
    sense.set_pixels(choice)
    time.sleep(0.5)

val =randint(1,6)
sense.set_pixels(val)
    

