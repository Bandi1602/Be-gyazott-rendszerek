from sense_hat import SenseHat
import math

# Initialize the Sense HAT
sense = SenseHat()


# Function to calculate cardinal direction based on X and Y values
def get_cardinal_direction(x, y):
    angle = math.atan2(y, x)
    angle_degrees = math.degrees(angle)

    if angle_degrees < 0:
        angle_degrees += 360

    if 45 <= angle_degrees < 135:
        return "E"
    elif 135 <= angle_degrees < 225:
        return "S"
    elif 225 <= angle_degrees < 315:
        return "W"
    else:
        return "N"


try:
    while True:
        # Read accelerometer data
        acceleration = sense.get_accelerometer_raw()
        x = acceleration["x"]
        y = acceleration["y"]

        # Get cardinal direction
        direction = get_cardinal_direction(x, y)

        # Display the direction on the Sense HAT LED matrix
        sense.show_letter(direction)
except KeyboardInterrupt:
    # Exit the program when Ctrl+C is pressed
    sense.clear()
