from sense_hat import SenseHat
import time
import math
import matplotlib.pyplot as plt

calibration = True
sense = SenseHat()


def stop():
    global calibration
    calibration = False


def plot(filename):
    x_list = []
    y_list = []

    try:
        file = open(filename, "r")
        lines = file.readlines()
        for line in lines:
            values = line.split(",")
            x_list.append(float(values[0]))
            y_list.append(float(values[1]))

    finally:
        file.close()

    xmax = max(x_list)
    xmin = min(x_list)
    ymax = max(y_list)
    ymin = min(y_list)
    print("Max x:", xmax, "Min x:", xmin)
    print("Max y:", ymax, "Min y:", ymin)

    (line1,) = plt.plot(range(1, len(x_list) + 1), x_list, "r-", label="x")
    (line2,) = plt.plot(range(1, len(y_list) + 1), y_list, "b--", label="y")
    plt.xlabel("Measurements")
    plt.ylabel("Value")
    plt.legend(handles=[line1, line2])
    plt.show()
    return xmax, xmin, ymax, ymin


def main():
    filename = "compass.txt"

    sense.stick.direction_down = stop
    print("Start data acquisition…")

    file = open(filename, "w")

    try:
        # Calibration process
        while calibration:
            magnet = sense.get_compass_raw()
            x = magnet["x"]
            y = magnet["y"]
            file.write(str(x) + "," + str(y) + "\n")

    finally:
        file.close()

    xmax, xmin, ymax, ymin = plot(filename)

    while True:
        magnet = sense.get_compass_raw()
        x = magnet["x"]
        y = magnet["y"]

        # Range transform
        xz = -1 + ((1 - (-1)) / (xmax - xmin)) * (x - xmin)
        yz = -1 + ((1 - (-1)) / (ymax - ymin)) * (y - ymin)

        # Degree (a) calculation
        if xz == 0 and yz < 0:
            deg = 90
        elif xz == 0 and yz > 0:
            deg = 270
        elif yz < 0:
            deg = 360 + math.atan2(yz, xz) * (180 / math.pi)
        else:
            deg = math.atan2(yz, xz) * (180 / math.pi)

        # Cardinal points
        if 22.5 <= deg < 67.5:
            sense.show_message("NE")
        elif 67.5 <= deg < 112.5:
            sense.show_letter("E")
        elif 112.5 <= deg < 157.5:
            sense.show_message("SE")
        elif 157.5 <= deg < 202.5:
            sense.show_letter("S")
        elif 202.5 <= deg < 247.5:
            sense.show_message("SW")
        elif 247.5 <= deg < 292.5:
            sense.show_letter("W")
        elif 292.5 <= deg < 337.5:
            sense.show_message("NW")
        else:
            sense.show_letter("N")
        time.sleep(0.2)


if __name__ == "__main__":
    main()
