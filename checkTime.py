import time


# determines whether the current time is in between 7:00 am and 9:30 am

def checkTime():

    # These times do NOT take into account AM/PM
    openingHour = 7
    openingMinute = 0
    closingHour = 9
    closingMinute = 30

    timeOfDay = time.strftime("%p")
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))

    # open = True; closed = False; closing time = 3;
    # 3 is just used because in python True == 1 is true
    if timeOfDay == "AM":
        if hour > openingHour:
            if hour < closingHour:
                return True
            elif hour > closingHour:
                return False
            elif hour == closingHour and minute < closingMinute:
                return True
            # closing time
            elif hour == closingHour and minute == closingMinute:
                return 3
            else:
                return False
            # opening time
        elif hour == openingHour and minute == openingMinute:
            return True
        else:
            return False
    else:
        return False
