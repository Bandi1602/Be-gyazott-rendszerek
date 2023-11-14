from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

nothing = (0,0,0) #no color
black = (0,0,255)


def Elso():
    b = black
    o = nothing
    
    E = [
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    ]
    return E

def Masodik():
    b = black
    o = nothing
    
    M = [
    b,b,o,o,o,o,o,o,
    b,b,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,b,b,
    o,o,o,o,o,o,b,b
    ]
    return M

def Harmadik():
    b = black
    o = nothing

    
    H = [
    b,b,o,o,o,o,o,o,
    b,b,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,b,b,
    o,o,o,o,o,o,b,b
    ]
    return H

def Negyedik():
    b = black
    o = nothing
    
    N = [
    b,b,o,o,o,o,b,b,
    b,b,o,o,o,o,b,b,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    b,b,o,o,o,o,b,b,
    b,b,o,o,o,o,b,b
    ]
    return N
def Otodik():
    b = black
    o = nothing
   
    Ot = [
    b,b,o,o,o,o,b,b,
    b,b,o,o,o,o,b,b,
    o,o,o,o,o,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,o,o,o,o,o,
    b,b,o,o,o,o,b,b,
    b,b,o,o,o,o,b,b
    ]
    return Ot
def Hatodik():
    b = black
    o = nothing
    
    Ha = [
    b,b,o,o,o,o,b,b,
    b,b,o,o,o,o,b,b,
    o,o,o,o,o,o,o,o,
    b,b,o,o,o,o,b,b,
    b,b,o,o,o,o,b,b,
    o,o,o,o,o,o,o,o,
    b,b,o,o,o,o,b,b,
    b,b,o,o,o,o,b,b
    ]
    return Ha


images = [Elso, Masodik, Harmadik, Negyedik, Otodik, Hatodik]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(0.75)
    count += 1

