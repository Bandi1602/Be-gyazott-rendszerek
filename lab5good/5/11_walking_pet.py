from sense_hat import SenseHat
from time import sleep
import math

p = (202, 30, 201)
g = (11, 102, 101)
y = (204, 202, 42)
b = (0, 0, 0)

pet_1 = [b, b, b, b, b, b, b, b,
         p, b, b, b, b, b, b, b,
         b, p, b, b, p, b, p, b,
         b, p, g, g, p, y, y, b,
         b, g, g, g, y, b, y, g,
         b, g, g, g, g, y, y, b,
         b, g, b, g, b, g, b, b,
         b, b, b, b, b, b, b, b]

pet_2 = [b, b, b, b, b, b, b, b,
         p, b, b, b, b, b, b, b,
         b, p, b, b, p, b, p, b,
         b, p, g, g, p, y, y, b,
         b, g, g, g, y, b, y, g,
         b, g, g, g, g, y, y, b,
         b, b, g, b, g, b, b, b,
         b, b, b, b, b, b, b, b]

def animated_walking():
    sense.set_pixels(pet_1)
    sleep(0.5)
    sense.set_pixels(pet_2)

sense = SenseHat()
sense.set_pixels(pet_1)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration["x"]
    y = acceleration["y"]
    z = acceleration["z"]

    F = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    #print(F)
    
    #TODO: Beállítani kb. egy jó értéket a kártyán
    if (F >= 1.10):
        animated_walking()