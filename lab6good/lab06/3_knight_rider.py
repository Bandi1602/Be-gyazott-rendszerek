from sense_hat import SenseHat
import time

sense = SenseHat()
p = [2, 3]
light_len = 3
space_size = 8
speed = 1/7

r = (255, 0, 0)
n = (0, 0, 0)

space = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    r, r, r, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]

def shift_right():
    space[p[1] * space_size + p[0] - light_len] = n
    space[p[1] * space_size + p[0]] = r
    p[0] += 1
    sense.set_pixels(space)

def shift_left():
    space[p[1] * space_size + p[0] - light_len] = r
    space[p[1] * space_size + p[0]] = n
    p[0] -= 1
    sense.set_pixels(space)

def main():
    global p
    while True:
        while True:
            shift_right()
            time.sleep(speed)
            if p[0] == space_size: break
        
        while True:
            shift_left()
            time.sleep(speed)
            if p[0] == light_len - 1: break


main()