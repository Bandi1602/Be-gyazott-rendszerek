from sense_hat import SenseHat

P0 = 1013.25 #hPa

sense = SenseHat()
p = sense.get_pressure() #hPa

h = 44331 * (1 - ( (p / P0) ** (1 / 5.2558) ) )

print("You are ~{:.1f} meters above sea level".format(h))