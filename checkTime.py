import time


# determines whether the current time is in between 7:00 am and 9:30 am

def checkTime():
    # These times do NOT take into account AM/PM
    openingHour = 7
    openingMinute = None
    closingHour = 9
    closingMinute = 30

    inTimeFrame = None
    timeOfDay = time.strftime("%p")
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))

    if timeOfDay == "AM":
        if hour > openingHour:
            if hour < closingHour:
                inTimeFrame = True
            elif hour > closingHour:
                inTimeFrame = False
            elif hour == closingHour and minute < closingMinute:
                inTimeFrame = True
            else:
                inTimeFrame = False
        else:
            inTimeFrame = False
    else:
        inTimeFrame = False
    return inTimeFrame
