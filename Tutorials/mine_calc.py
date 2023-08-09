#Calculator for solar mining



def consump_and_generation():
    gpu_list_wattage = [200, 225, 125, 185, 175]
    MH_second_list = [60, 50, 25, 28, 40]

    user_input = input("Chosse the number of one gpu > \n3060Ti(1)\nRX5700 XT(2)\nGTX 1660 Super(3)\nRadeon RX 580(4)\nRTX2070(5)\nnumber: ")
    user_input = int(user_input) -1

    #wattage consumption Wh and kWh per day
    gpu_wattage = gpu_list_wattage[user_input]
    watt_hours_day = gpu_wattage * 24
    kilo_watt_hours_day = watt_hours_day / 1000

    print("This GPU uses " + str(watt_hours_day) + " Wh and " + str(kilo_watt_hours_day) + " kWh per day!")
    print("The GPU generates " + str(MH_second_list[user_input]*1000) + "H/s and " + str(MH_second_list[user_input]) + "MH/s")

def panel_wattage_generation():
    panel_wattage_list = [40, 50, 60, 100, 150]
    user_input = input("Chosse the number of one gpu > \n40W(1)\n50W(2)\n60W(3)\n100W(4)\n150W(5)\nnumber: ")
    user_input = int(user_input) -1
    print (user_input)
    #wattage gerneration Wh and kWh per day / AVG 5hours sunlight and 0.85% eff
    wattage_per_day = panel_wattage_list[user_input] * 5 * 0.85
    print("The " + str(panel_wattage_list[user_input]) + "W panel generates " + str(wattage_per_day) + "Wh per day")
    panel_wattage_generation()
#executes
panel_wattage_generation()