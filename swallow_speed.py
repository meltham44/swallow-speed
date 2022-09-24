#!/usr/bin/env python3

global count, mph_list, kph_list


def average(a):
    return sum(a) / len(a)


def reading_input():
    global count, mph_list, kph_list

    print("Swallow Speed Analysis: Version 1.0")
    print("")
    kph_list = []
    mph_list = []
    i = 0
    count = 0
    while i == 0:
        reading = input("Enter the Next Reading: ").upper()
        if reading == "":
            i = 1
            if len(mph_list) > 0:
                reading_output()
            else:
                print("No readings entered. Nothing to do.")
        elif reading[0] != "E" and reading[0] != "U" or reading[1].isdigit() != True:
            i = 1
            print("Incorrect data entered.")
        elif reading[0] == "E":
            reading = float(reading[1:])
            kph_list.append(reading)
            mph_list.append(reading/1.61)
            print("Reading saved.")
        elif reading[0] == "U":
            reading = float(reading[1:])
            mph_list.append(reading)
            kph_list.append(reading*1.61)
            print("Reading saved.")


def reading_output():
    print("")
    print("Results Summary")
    print("")
    if len(mph_list) == 1:
        print(len(mph_list), "Reading Analysed.")
    else:
        print(len(mph_list), "Readings Analysed.")
    print("")
    print("Max Speed:", round(max(mph_list), 1), "MPH,", round(max(kph_list), 1), "KPH.")
    print("Min Speed:", round(min(mph_list), 1), "MPH,", round(min(kph_list), 1), "KPH.")
    print("Avg Speed:", round(average(mph_list), 1), "MPH,", round(average(kph_list), 1), "KPH.")


if __name__ == '__main__':
    reading_input()
