# from sense_hat import SenseHat
from sense_hat import SenseHat
import time
import random

sense = SenseHat()

raindrop_color = (0, 0, 255)

sense.clear()

while True:

    sor = random.randint(0, 7)

    sense.set_pixel(sor, 0, raindrop_color)

    time.sleep(0.5)

    for sor in range(7, 0, -1):

        for oszlop in range(0, 8, 1):

            pixel = sense.get_pixel(oszlop, sor - 1)
            sense.set_pixel(oszlop, sor, pixel)

    for sor in range(8):
        sense.set_pixel(sor, 0, (0, 0, 0))
