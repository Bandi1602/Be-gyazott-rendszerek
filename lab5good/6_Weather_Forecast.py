from sense_emu import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
    
while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = 125 #round(h, 1) 

    #jelenleg
    P0 =  p * (1 - (0.0065 * h) / (t + 0.0065 * h + 273.15) ) ** -5.257 # atmospheric pressure
#   P0 = 1000
    most =p *(1 - (0.0065 * h) / (t + 0.0065 * h + 273.15) ) ** -5.257
#   most = P0- 1.6

    if ( (most <= P0 - 1.6) and (P0 <= 1050 and P0 >= 985)):
        Z = int(127 - 0.12 * P0)

        forecast_table = {
        1: "Settled Fine",
        2: "Fine Weather",
        3: "Fine, Becoming Less Settled",
        4: "Fairly Fine, Showery Later",
        5: "Showery, Becoming More Unsettled",
        6: "Unsettled, Rain Later",
        7: "Rain at Times, Worse Later",
        8: "Rain at Times, Becoming Very Unsettled",
        9: "Very Unsettled, Rain"}

        print(forecast_table[Z])
    #
    elif ( (most == P0) and (P0 <= 1033 and P0 >= 960)):

        Z = int(144 - 0.13 * P0)

        forecast_table = {
        10: "Settled Fine",
        11: "Fine Weather",
        12: "Fine, Possibly Showers",
        13: "Fairly Fine, Showers Likely",
        14: "Showery, Bright Intervals",
        15: "Changeable, Some Rain",
        16: "Rain at Frequent Intervals",
        17: "Rain at Times, Becoming Very Unsettled",
        18: "Very Unsettled, Rain"}

        print(forecast_table[Z])
    #

    elif(P0 <= 1033 and P0 >= 960):

        Z = int(185 - 0.16 * P0)

        forecast_table = {
        20: "Settled Fine",
        21: "Fine Weather",
        22: "Becoming Fine",
        23: "Fairly Fine, Improving",
        24: "Fairly Fine, Possibly Showers Early",
        25: "Showery Early, Improving",
        26: "Changeable, Mending",
        27: "Rather Unsettled, Clearing Later",
        28: "Unsettled, Probably Improving",
        29: "Unsettled, Short Fine Intervals",
        30: "Very Unsettled, Finer at Times",
        31: "Stormy, Possibly Improving",
        32: "Stormy, Much Rain"}

        print(forecast_table[Z])
    sleep(1)
        