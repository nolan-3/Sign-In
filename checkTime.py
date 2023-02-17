# Determines whether the current time is between 7:00am and 9:30am EST (inclusive).

from datetime import datetime, time
from pytz import timezone

# All times are localized and interpreted in this timezone.
TIMEZONE = timezone("US/Eastern")

OPEN_TIME = time(7, 0)
CLOSE_TIME = time(9, 30)

# TODO(braid): Remove special close condition
# open = True; closed = False; closing time = 3;
# 3 is just used because in python True == 1 is true
def checkTime():
    timeNow = TIMEZONE.localize(datetime.now()).time()

    if timeNow == CLOSE_TIME:
        return 3

    return (OPEN_TIME <= timeNow) and (timeNow <= CLOSE_TIME)
