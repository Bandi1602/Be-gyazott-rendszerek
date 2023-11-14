from sense_hat import SenseHat
import time
import random

sense = SenseHat()

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
n = (0, 0, 0)

score = 0
speed = 0.5

walls = [b, b, b, b, b, b, b, b,
         b, n, n, n, n, n, n, b,
         b, n, n, n, n, n, n, b,
         b, n, n, n, n, n, n, b,
         b, n, n, n, n, n, n, b,
         b, n, n, n, n, n, n, b,
         b, n, n, n, n, n, n, b,
         b, b, b, b, b, b, b, b]

def grow_snake():
    snakePosX.append(0)
    snakePosY.append(0)

def generate_food():
    global foodPosX, foodPosY
    isFreePos = False
    while not isFreePos:
        foodPosX = random.randint(1, 6)
        foodPosY = random.randint(1, 6)
        isFreePos = True
        for x, y in zip(snakePosX, snakePosY):
            if x == foodPosX and y == foodPosY:
                isFreePos = False
                break

# set default snake starting position (values are just chosen by preference):
snakePosX = [3]
snakePosY = [6]

foodPosX = 3
foodPosY = 3

# snake movement vector
movementX = 0
movementY = -1

sense.clear()

snakeBitesItself = False

while True:
    # snake eats food:
    if foodPosX == snakePosX[0] and foodPosY == snakePosY[0]:
        grow_snake()
        generate_food()
        score += 1

    # snake bites itself:
    for i in range(1, len(snakePosX)):
        if snakePosX[i] == snakePosX[0] and snakePosY[i] == snakePosY[0]:
            snakeBitesItself = True

    if snakeBitesItself:
        break

    # joy events:
    events = sense.stick.get_events()
    for event in events:
        if event.direction == "left" and movementX != 1:
            movementX = -1
            movementY = 0
        elif event.direction == "right" and movementX != -1:
            movementX = 1
            movementY = 0
        elif event.direction == "up" and movementY != 1:
            movementY = -1
            movementX = 0
        elif event.direction == "down" and movementY != -1:
            movementY = 1
            movementX = 0

    # move snake:
    for i in range((len(snakePosX) - 1), 0, -1):
        snakePosX[i] = snakePosX[i - 1]
        snakePosY[i] = snakePosY[i - 1]

    # move head by vector
    snakePosX[0] += movementX
    snakePosY[0] += movementY

    # check game borders:
    if snakePosX[0] == 0 or snakePosX[0] == 7:
        break
    
    if snakePosY[0] == 0 or snakePosY[0] == 7:
        break

    # update matrix:
    sense.clear()
    sense.set_pixels(walls)
    sense.set_pixel(foodPosX, foodPosY, r)
    for x, y in zip(snakePosX, snakePosY):
        sense.set_pixel(x, y, g)

    time.sleep(speed)

# Game over
sense.show_message("Score: " + str(score), text_colour=g, scroll_speed=0.05)
sense.clear()