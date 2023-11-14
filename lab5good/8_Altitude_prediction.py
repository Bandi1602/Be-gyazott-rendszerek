from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1) 

    #jelenleg
    P0 = p * (1 - (0.0065 * h) / (t + 0.0065 * h + 273.15) ) ** -5.257

    h = 44331 * (1 - ( (p / P0) ** (1/5.2558) ) )
    print(h)
    sleep(1)
