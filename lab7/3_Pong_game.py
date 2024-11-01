from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
speed = 0.4
score = 0
basket = [7,4]
up_down = -1

w = (0,0,0)
r = (255,0,0)
b = (0,0,255)

game_space = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,b,b,w,w,w]

def update_space(x, y, colour):
#index element from coordinate
    p = 8 * x + y
    game_space[p] = colour
    sense.set_pixels(game_space)

def left(event):
    if event.action == 'pressed':
    #the basket reached the left side
        if basket[0] - 1 == 0:
            pass
        #move basket one position left
        else:
            update_space(basket[0], basket[1], w)
            basket[1] -= 1
            update_space(basket[0], basket[1] - 1, b)

def right(event):
    if event.action == 'pressed':
    #the basket reached the right side
        if basket[1] + 1 == 8:
            pass
        #move basket one position left
        else:
            update_space(basket[0], basket[1] - 1, w)
            basket[1] += 1
            update_space(basket[0], basket[1], b)

sense.stick.direction_left = left
sense.stick.direction_right = right

sense.clear()
sense.set_pixels(game_space)
game_alive = True

x = 0
y = random.randint(0,7)
d = random.choice([-1, 1])

while game_alive:
    update_space(x, y, r)

    # while the ball is in the game space
    while True:
        sleep(speed)
        update_space(x, y, w)

        # ball is on the edge of x dimension
        if x == 7:
            if y == basket[1] - 1 or y == basket[1]:
                # ball is in the basket
                update_space(x, y, b)
                score += 1
                up_down = -1
            else:
                # ball is out of the space
                game_alive = False
                break

        # ball reached the right side of the space
        if y == 7 and d == 1: # and up_down == -1 és a másiknál fordítva
            d =-1

        # ball reached the left side of the space
        if y == 0 and d == -1:
            d = 1

        # ball reached the top side of the space
        if x == 0 and up_down == -1:
            up_down = 1

        y += d
        x += up_down
        update_space(x, y, r)

sense.clear()
sense.show_message("Game over!", scroll_speed=0.05, back_colour=w)
sense.show_message("Score: " + str(score), scroll_speed=0.05, back_colour=w)