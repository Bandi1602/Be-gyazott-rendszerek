from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def Left():
    G = green
    Y = yellow
    B = blue
    O = nothing
    W = white
    R = red
    
    L = [
    W, W, W, W, W, W, W, W,
    W, W, W, R, W, W, W, W,
    W, W, R, W, W, W, W, W,
    W, R, W, W, W, W, W, W,
    R, R, R, R, R, R, R, R,
    W, R, W, W, W, W, W, W,
    W, W, R, W, W, W, W, W,
    W, W, W, R, W, W, W, W,
    ]
    return L

def Right():
    G = green
    R = red
    O = nothing
    W = white
    
    R = [
    W, W, W, W, W, W, W, W,
    W, W, W, W, R, W, W, W,
    W, W, W, W, W, R, W, W,
    W, W, W, W, W, W, R, W,
    R, R, R, R, R, R, R, R,
    W, W, W, W, W, W, R, W,
    W, W, W, W, W, R, W, W,
    W, W, W, W, R, W, W, W,
    ]
    return R

def Up():
    G = green
    R = red
    O = nothing
    W = white
    
    U = [
    W, W, W, R, W, W, W, W,
    W, W, R, R, R, W, W, W,
    W, R, W, R, W, R, W, W,
    R, W, W, R, W, W, R, W,
    W, W, W, R, W, W, W, W,
    W, W, W, R, W, W, W, W,
    W, W, W, R, W, W, W, W,
    W, W, W, R, W, W, W, W,
    ]
    return U

def Down():
    G = green
    R = red
    O = nothing
    W = white
    
    D = [
    W, W, W, R, W, W, W, W,
    W, W, W, R, W, W, W, W,
    W, W, W, R, W, W, W, W,
    W, W, W, R, W, W, W, W,
    R, W, W, R, W, W, R, W,
    W, R, W, R, W, R, W, W,
    W, W, R, R, R, W, W, W,
    W, W, W, R, W, W, W, W,
    ]
    return D

images = [Right, Left, Up, Down]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(2)
    count += 1