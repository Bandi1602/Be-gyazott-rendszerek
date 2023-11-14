from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

h = 121 # altitude of Debrecen in meters

the_pressure_is = ""
Z = 0
forecast_table = ("Error",
                  "Settled Fine",
                  "Fine Weather",
                  "Fine, Becoming Less Settled",
                  "Fairly Fine, Showery Later",
                  "Showery, Becoming More Unsettled",
                  "Unsettled, Rain Later",
                  "Rain at Times, Worse Later",
                  "Rain at Times, Becoming Very Unsettled",
                  "Very Unsettled, Rain",
                  "Settled Fine",
                  "Fine Weather",
                  "Fine, Possibly Showers",
                  "Fairly Fine, Showers Likely",
                  "Showery, Bright Intervals",
                  "Changeable, Some Rain",
                  "Unsettled, Rain at Times",
                  "Rain at Frequent Intervals",
                  "Very Unsettled, Rain",
                  "Settled Fine",
                  "Fine Weather",
                  "Becoming Fine",
                  "Fairly Fine, Improving",
                  "Fairly Fine, Possibly Showers Early",
                  "Showery Early, Improving",
                  "Changeable, Mending",
                  "Rather Unsettled, Clearing Later",
                  "Unsettled, Probably Improving",
                  "Unsettled, Short Fine Intervals",
                  "Very Unsettled, Finer at Times",
                  "Stormy, Possibly Improving",
                  "Stormy, Much Rain"
                  )

while True:
    p = sense.get_pressure()
    t = sense.get_temperature()
    p_rel_0 = p * ((1 - (0.0065 * h) / (t + 0.0065 * h + 273.15)) ** (-5.257))

    # 3 hours | change to demonstrate
    sleep(3 * 60 * 60)

    p = sense.get_pressure()
    t = sense.get_temperature()
    p_rel_1 = p * ((1 - (0.0065 * h) / (t + 0.0065 * h + 273.15)) ** (-5.257))

    # 1.6 mBar = 1.6 hPa
    if (p_rel_0 - p_rel_1) >= 1.6:
        the_pressure_is = "falling"
    elif (p_rel_0 - p_rel_1) <= -1.6:
        the_pressure_is = "rising"
    else:
        the_pressure_is = "steady"

    if the_pressure_is == "falling" and p_rel_1 >= 985 and p_rel_1 <= 1050:
        Z = round(127 - 0.12 * p_rel_1)
    elif the_pressure_is == "steady" and p_rel_1 >= 960 and p_rel_1 <= 1033:
        Z = round(144 - 0.13 * p_rel_1)
    elif the_pressure_is == "rising" and p_rel_1 >= 947 and p_rel_1 <= 1030:
        Z = round(185 - 0.16 * p_rel_1)

    print(forecast_table[Z])
