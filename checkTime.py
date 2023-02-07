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

    # 2 and 3 are just used because in python True == 1 is true
    if timeOfDay == "AM":
        if hour > openingHour:
            if hour < closingHour:
                return True
            elif hour > closingHour:
                return False
            elif hour == closingHour and minute < closingMinute:
                return True
            elif hour == closingHour and minute == closingMinute:
                return 3
            else:
                return False
        elif hour == openingHour and minute == openingMinute:
            return 2
        else:
            return False
    else:
        return False