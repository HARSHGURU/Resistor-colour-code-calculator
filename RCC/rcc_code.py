import os
significant_figures = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7,
                       "grey": 8, "white": 9, "gold": 0, "silver": 0, "none": 0}

multiply = {"black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000, "green": 100000, "blue": 1000000,
            "violet": 10000000, "grey": 100000000, "white": 1000000000, "gold": 0.1, "silver": 0.01, "none": 0}

tolerance = {"black": "", "brown": 1, "red": 2, "orange": "", "yellow": "", "green": 0.5, "blue": 0.25, "violet": 0.1,
             "grey": 0.05, "white": "", "gold": 5, "silver": 10, "none": "20"}

temp_coeff = {"black": 250, "brown": 100, "red": 50, "orange": 15, "yellow": 25, "green": 20, "blue": 10, "violet": 5,
              "grey": 1, "white": 0, "gold": 0, "silver": 0, "none": 0}

#******************************************Three band ********************************************
def three_band():
    band = []
    for i in range(1 , 4):
        band_color = input(f"Enter {i} band colour: ")
        if band_color not in significant_figures:
            print("Invalid input !!!!!!!!!!!!!!")
            return
        elif i == 3:
            band.append(multiply[band_color])
        else:
             band.append(significant_figures[band_color])
    resistor_value = ((band[0]*10) + (band[1])) * band[2]

    print("Resistor value : ")
    print(f"{resistor_value} ohms")
    print(f"{resistor_value/1000} Kohms")
    print(f"{resistor_value/1000000} Mohms")
    print(f"tolerance: {tolerance['none']}%")

#*******************************************Four band************************************************
def four_band():
    band = []
    for i in range(1, 5):
        band_color = input(f"Enter {i} band colour: ")
        if band_color not in significant_figures:
            print("Invalid input !!!!!!!!!!!!!!")
            return
        elif i == 3:
            band.append(multiply[band_color])
        elif i == 4:
            band.append(tolerance[band_color])
        else:
            band.append(significant_figures[band_color])
    resistor_value = ((band[0] * 10) + (band[1])) * band[2]

    print("Resistor value : ")
    print(f"{resistor_value} ohms")
    print(f"{resistor_value / 1000} Kohms")
    print(f"{resistor_value / 1000000} Mohms")
    print(f"tolerance: {band[3]}%")


#*******************************************Five band************************************************
def five_band():
    band = []
    for i in range(1, 6):
        band_color = input(f"Enter {i} band colour: ")
        if band_color not in significant_figures:
            print("Invalid input !!!!!!!!!!!!!!")
            return
        elif i == 4:
            band.append(multiply[band_color])
        elif i == 5:
            band.append(tolerance[band_color])
        else:
            band.append(significant_figures[band_color])
    resistor_value = ((band[0] * 100) + ((band[1])*10) +(band[2])) * band[3]

    print("Resistor value : ")
    print(f"{resistor_value} ohms")
    print(f"{resistor_value / 1000} Kohms")
    print(f"{resistor_value / 1000000} Mohms")
    print(f"tolerance: {band[4]}%")

#*******************************************six band************************************************
def six_band():
    band = []
    for i in range(1, 7):
        band_color = input(f"Enter {i} band colour: ")
        if band_color not in significant_figures:
            print("Invalid input !!!!!!!!!!!!!!")
            return
        elif i == 4:
            band.append(multiply[band_color])
        elif i == 5:
            band.append(tolerance[band_color])
        elif i == 6:
            band.append(temp_coeff[band_color])
        else:
            band.append(significant_figures[band_color])
    resistor_value = ((band[0] * 100) + ((band[1]) * 10) + (band[2])) * band[3]

    print("Resistor value : ")
    print(f"{resistor_value} ohms")
    print(f"{resistor_value / 1000} Kohms")
    print(f"{resistor_value / 1000000} Mohms")
    print(f"tolerance: {band[4]}%")
    print(f"Temp.Coeff: {band[5]}ppm/K")


#*****************************************Start game function******************************
def start_game():
    band = input("Enter the total number of bands (three , four , five , six): ").lower()
    if band == "three":
        three_band()
    elif band == "four":
        four_band()
    elif band == "five":
        five_band()
    elif band == "six":
        six_band()
    else:
        print("Invalid Input !!!!!")

#************************************Main function******************************************
chalo = True
while chalo:
    start = input("Enter Start/STOP: ").upper()
    if start == "START":
        fuc = "START"
        game = True
        while game:
            if start == fuc:
                # print("calling function")
                start_game()
            print("\n")
            cont = int(input("Want to continue press 1(YES) or 0(NO): "))
            if cont == 1:
                start = "START"
                fuc = "START"
            elif cont == 0:
                exit(0)
            else:
                print("Invalid input Enter again")
                start = "START"
                fuc = "No"

    elif start == "STOP":
        chalo = False
    else:
        print("Invalid input. Enter again")

