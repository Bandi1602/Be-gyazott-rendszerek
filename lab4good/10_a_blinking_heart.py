from sense_hat import SenseHat
import time

s = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)


G = green
Y = yellow
B = blue
O = nothing
w = white
r = red
    
Elso = [
w, w, w, w, w, w, w, w,
w, r, r, w, w, r, r, w,
r, r, r, r, r, r, r, r,
r, r, r, r, r, r, r, r,
w, r, r, r, r, r, r, w,
w, w, r, r, r, r, w, w,
w, w, w, r, r, w, w, w,
w, w, w, w, w, w, w, w,
]

Masodik = [
w, w, w, w, w, w, w, w,
w, w, r, w, w, r, w, w,
w, r, r, r, r, r, r, w,
w, r, r, r, r, r, r, w,
w, w, r, r, r, r, w, w,
w, w, w, r, r, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
]

Harmadik = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, r, r, w, w, r, r, w,
w, r, r, r, r, r, r, w,
w, w, r, r, r, r, w, w,
w, w, w, r, r, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
]

Negyedik = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, r, w, w, r, w, w,
w, w, r, r, r, r, w, w,
w, w, w, r, r, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
]

    
Otodik = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, r, r, r, r, w, w,
w, w, w, r, r, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
]

Hatodik = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, r, w, w, r, w, w,
w, w, w, r, r, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
]
    
Hetedik = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, r, r, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
]
    
Nyolcadik = [
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, r, r, w, w, w,
w, w, w, w, w, w, w, w,
w, w, w, w, w, w, w, w,
]
def Anim():
    sense.set_pixels(Elso)
    time.sleep(0.5)
    sense.set_pixels(Masodik)
    time.sleep(0.5)
    sense.set_pixels(Harmadik)
    time.sleep(0.5)
    sense.set_pixels(Negyedik)
    time.sleep(0.5)
    sense.set_pixels(Otodik)
    time.sleep(0.5)
    sense.set_pixels(Hatodik)
    time.sleep(0.5)
    sense.set_pixels(Hetedik)
    time.sleep(0.5)
    sense.set_pixels(Nyolcadik)
    time.sleep(0.5)


sense = SenseHat()

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            Anim()
