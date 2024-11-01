from sense_hat import SenseHat
from random import randint
import time

def random_colour():
# randint - random integer between an interval
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)

s = SenseHat()
s.low_light = True

green = random_colour()
blue = random_colour()
red = random_colour()

green = (0, green[1], 0)
yellow = (255, 255, 0)
blue = (0, 0, blue[2])
red = (red[1], 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def trinket_logo():
    G = green
    O = yellow
    B = blue
    O = nothing
    logo = [
    O, G, O, O, O, B, O, O,
    O, G, O, O, B, O, B, O,
    O, G, O, B, O, O, O, B,
    O, G, O, B, O, O, O, B,
    O, G, O, B, B, B, B, B,
    O, G, O, B, O, O, O, B,
    O, G, O, B, O, O, O, B,
    O, G, O, B, O, O, O, B]
    return logo


images = [trinket_logo]
count = 0

while True: 
    s.set_pixels(images[0]())
    time.sleep(.75)
    count += 1