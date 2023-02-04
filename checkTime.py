import time

# determines whether the current time is in between 6:00 am and 9:30 am 
def checkTime():
    # times do NOT take into account AM/PM
    openingHour = 6
    openingMinute = None
    closingHour = 9
    closingMinute = 30
    # time.strftime("%A, %d. %B %Y %I:%M:%S %p")
    #year = int(time.strftime("%Y"))
    #month = time.strftime("%B")
    #day = int(time.strftime("%d"))
    inTimeFrame = None
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    timeOfDay = time.strftime("%p")
    if timeOfDay == "AM":
        if hour > openingHour:
            if hour > closingHour:
                inTimeFrame = False
            elif hour < closingHour:
                inTimeFrame = True
            elif hour == closingHour and minute < closingMinute:
                inTimeFrame = True
        else:
            inTimeFrame = False
    else:
        inTimeFrame = False
    return inTimeFrame