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

G = green
R = red
O = yellow
b = blue
O = nothing
w = white
    
logo = [w, w, w, w, w, w, w, w,
        w, R, R, w, w, R, R, w,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        w, R, R, R, R, R, R, w,
        w, w, R, R, R, R, w, w,
        w, w, w, R, R, w, w, w,
        w, w, w, w, w, w, w, w]

s.set_pixels(logo)


