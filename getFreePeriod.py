from datetime import date
import time
import math


def daysOff(year, month, day):
    happyDays = 0
    # format [year,month,day]
    daysOff = [[2022, 9, 26], [2022, 10, 5], [2022, 10, 21], [2022, 11, 14], [2022, 11, 23], [2022, 11, 24],
               [2022, 11, 25], [2022, 12, 19], [2022, 12, 20], [
                   2022, 12, 21], [2022, 12, 22], [2022, 12, 23],
               [2022, 12, 26], [2022, 12, 27], [2022, 12, 28], [
        2022, 12, 29], [2022, 12, 30],
        [2023, 1, 2], [2023, 1, 16], [2023, 2, 17], [2023, 2, 20], [2023, 3, 17],
        [2023, 3, 24], [2023, 3, 27], [2023, 3, 28], [
            2023, 3, 29], [2023, 3, 30],
        [2023, 3, 31], [2023, 4, 7], [2023, 5, 1], [2023, 5, 29]]

    # Find how many days off we've had so far, yes it is chronological but lets not rely on that
    for i in range(0, len(daysOff)):
        if year > daysOff[i][0]:
            happyDays += 1
        elif year == daysOff[i][0]:
            if month > daysOff[i][1]:
                happyDays += 1
            elif month == daysOff[i][1]:
                if day > daysOff[i][2]:
                    happyDays += 1
    return happyDays


def dayOfWeek():
    dayOfWeek = time.strftime("%A")
    # switch case requires version 3.10 or newer, occidam serpentem
    if dayOfWeek == "Monday":
        return 1
    elif dayOfWeek == "Tuesday":
        return 2
    elif dayOfWeek == "Wednesday":
        return 3
    elif dayOfWeek == "Thursday":
        return 4
    elif dayOfWeek == "Friday":
        return 5
    else:
        return 0


def getFreePeriod():
    # number of school days since the start of school*4 module 7 is the current first period free
    # Or simply the number of school days modulo 7 corresponds to this pattern
    pattern = ["A", "E", "B", "F", "C", "G", "D"]

    # start of school if we started on a sunday because the school is into masochism
    # add 3 days so that wednesday - friday of the first week of school are included
    firstSunday = date(2022, 9, 11)
    days = 3

    year = int(time.strftime("%Y"))
    month = time.strftime("%B")
    month = time.strptime(month, '%B').tm_mon
    day = int(time.strftime("%d"))
    current = date(year, month, day)

    deltaT = current - firstSunday
    deltaDays = deltaT.days
    fullWeeks = math.floor(deltaDays/7)
    days += fullWeeks * 5
    days += dayOfWeek()

    # seriously local variable takese precedence over function, bruh
    daysMissed = daysOff(year, month, day)

    schoolDays = (days - daysMissed) + 3
    index = schoolDays % 7
    freePeriod = pattern[index]
    return freePeriod
