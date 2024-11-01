from sense_hat import SenseHat
import time

sense = SenseHat()

r = (255, 0, 0)
w = (255,255,255)
    
L = [
w, w, w, w, w, w, w, w,
w, w, w, r, w, w, w, w,
w, w, r, w, w, w, w, w,
w, r, w, w, w, w, w, w,
r, r, r, r, r, r, r, r,
w, r, w, w, w, w, w, w,
w, w, r, w, w, w, w, w,
w, w, w, r, w, w, w, w]
    
R = [
w, w, w, w, w, w, w, w,
w, w, w, w, r, w, w, w,
w, w, w, w, w, r, w, w,
w, w, w, w, w, w, r, w,
r, r, r, r, r, r, r, r,
w, w, w, w, w, w, r, w,
w, w, w, w, w, r, w, w,
w, w, w, w, r, w, w, w]

    
U = [
w, w, w, r, w, w, w, w,
w, w, r, r, r, w, w, w,
w, r, w, r, w, r, w, w,
r, w, w, r, w, w, r, w,
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w]

D = [
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w,
r, w, w, r, w, w, r, w,
w, r, w, r, w, r, w, w,
w, w, r, r, r, w, w, w,
w, w, w, r, w, w, w, w]

#images = [right, Left, Up, Down]
count = 0

while True:
#go throw all joystick’s events
    for event in sense.stick.get_events():
        if event.action == "pressed":
 # Check which direction
            if event.direction == "up":
                sense.set_pixels(U) # Up arrow
            elif event.direction == "down":
                sense.set_pixels(D) # Down arrow
            elif event.direction == "left":
                sense.set_pixels(L) # Left arrow
            elif event.direction == "right":
                sense.set_pixels(R) # right arrow

 # wait a while and then clear the screen
            time.sleep(0.5)
            sense.clear()

