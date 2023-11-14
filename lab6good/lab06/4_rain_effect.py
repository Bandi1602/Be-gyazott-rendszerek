from sense_hat import SenseHat
import random
import time

b = (0, 0, 255)
n = (0, 0, 0)

pixel_width = 8
pixel_height = 8

start = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]


sense = SenseHat()

while True:
    index = random.randint(0, pixel_width - 1) # [0, 7]

    for i in range(0, pixel_height):
        #print("DEBUG: {}".format(index + i * pixel_width))
        start[index + i * pixel_width] = b
        start[index + (i-1) * pixel_width] = n
        sense.set_pixels(start)
        time.sleep(0.5)
    
    start = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]