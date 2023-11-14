from sense_hat import SenseHat
import time
import math

s = SenseHat()


G = (0, 255, 0)
Y = (255, 255, 0)
N = (0,0,0)
P = (255,105, 180)
    
Anim_elso = [
N, N, N, N, N, N, N, N,
P, N, N, N, N, N, N, N,
N, P, N, N, P, N, P, N,
N, P, G, G, P, Y, Y, N,
N, G, G, G, Y, N, Y, G,
N, G, G, G, G, Y, Y, N,
N, G, N, G, N, G, N, N,
N, N, N, N, N, N, N, N,]

    
Anim_masodik = [
N, N, N, N, N, N, N, N,
P, N, N, N, N, N, N, N,
N, P, N, N, P, N, P, N,
N, P, G, G, P, Y, Y, N,
N, G, G, G, Y, N, Y, G,
N, G, G, G, G, Y, Y, N,
N, N, G, N, G, N, N, N,
N, N, N, N, N, N, N, N,]

while True:
    acceleration = s.get_accelerometer_raw()
    x = acceleration["x"]
    y = acceleration["y"]
    z = acceleration["z"]

    F = math.sqrt(x ** 2 + y ** 2 + z ** 2)

    if (F >= 1.5):
        s.set_pixels(Anim_elso)
        time.sleep(2)
        s.set_pixels(Anim_masodik)
        time.sleep(2)
        s.clear()
