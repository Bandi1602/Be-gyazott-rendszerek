# from sense_hat import SenseHat
from sense_hat import SenseHat
import time

sense = SenseHat()

r = (255,0,0)
n = (0,0,0)

light_len = 4
p = [light_len-1 , 3]
space_size = 8

space_first = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n]


def shift_right():
    for e in range (0,light_len):
        space_first[p[1] * 8 + p[0] - e] = r
    
    sense.set_pixels(space_first)
    space_first[p[1] * 8 + p[0] - light_len + 1] = n
    p[0] = p[0]+1

def shift_left():
    for e in range (0,light_len):
        space_first[p[1] * 8 + p[0] - e] = r
        
    sense.set_pixels(space_first)
    
    space_first[p[1] * 8 + p[0]] = n
    p[0] = p[0]-1

def main():
    while True:

        while True:
          shift_right()
          time.sleep(0.5)
          if p[0] == space_size-1: break
        
        while True:
          shift_left()
          time.sleep(0.5)
          if p[0] == light_len-1: break
if __name__ == "__main__":
    main()
