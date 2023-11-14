from sense_hat import SenseHat
import time

delay_val = 1.0

def delay(event):
    global delay_val
    if event.action == "pressed":

        if event.direction == "middle":

            if event.action == 'pressed':
                delay_val = 0.2
            elif event.action == 'released':
                delay_val = 1.0

        elif event.direction == "up":

            if event.action == 'pressed':
                delay_val = 0.4
            elif event.action == 'released':
                delay_val = 2.0

        elif event.direction == "down":

            if event.action == 'pressed':
                delay_val = 0.8
            elif event.action == 'released':
                delay_val = 4.0

        elif event.direction == "left":

            if event.action == 'pressed':
                delay_val = 0.16
            elif event.action == 'released':
                delay_val = 8.0

        else:
            if event.action == 'pressed':
                delay_val = 0.32
            elif event.action == 'released':
                delay_val = 16.0

sense = SenseHat()

sense.stick.direction_middle = delay
sense.stick.direction_up = delay
sense.stick.direction_down = delay
sense.stick.direction_right = delay
sense.stick.direction_left = delay

w = (255,255,255)
n = (0,0,0)

on = [
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w
 ]

off = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]

while True:
    sense.set_pixels(on)
    time.sleep(delay_val)
    sense.set_pixels(off)
    time.sleep(delay_val)
    