from sense_hat import SenseHat
from random import randint
import time

def random_colour():
# randint - random integer between an interval
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)

sense = SenseHat()

szin = random_colour()

sense.show_letter("I", szin)
time.sleep(1)
sense.show_letter("A", szin)