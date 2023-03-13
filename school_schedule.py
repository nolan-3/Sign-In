"""Tools for working with the school schedule.

This module handles the internal representation of the school schedule,
handling vacations, registration times and the current free period.
"""

from pytz import timezone
from datetime import time, datetime
import numpy as np
import logging

# Print a warning for dates outside this range:
VALID_START = datetime(2022, 9, 26)
VALID_END = datetime(2023, 5, 29)

# Holidays and schedule information
#   FREE_PATTERN[0] should correspond to FIRST_DAY
#   holiday format: "YYYY-MM-DD"
FIRST_DAY = datetime(2022, 9, 7)
FREE_PATTERN = ["C", "G", "D", "A", "E", "B", "F"]
HOLIDAYS = ['2022-09-26',
            '2022-10-05', '2022-10-21',
            '2022-11-14', '2022-11-23', '2022-11-24', '2022-11-25',
            '2022-12-19', '2022-12-20', '2022-12-21', '2022-12-22', '2022-12-23', '2022-12-26', '2022-12-27', '2022-12-28', '2022-12-29', '2022-12-30',
            '2023-01-02', '2023-01-16',
            '2023-02-17', '2023-02-20',
            '2023-03-17', '2023-03-24', '2023-03-27', '2023-03-28', '2023-03-29', '2023-03-30', '2023-03-31',
            '2023-04-07',
            '2023-05-01', '2023-05-29']

# Registration times
OPEN_TIME = time(7, 0)
CLOSE_TIME = time(9, 45)
WEDNESDAY_CLOSE_TIME = time(10, 15)


def registration_open(query=datetime.now()):
    """Check whether registration is open at a given datetime."""
    logging.info(f"Checking registration at {query}.")
    _validate_datetime(query)

    # Registration is closed on holidays
    if _is_holiday(query): 
        return False

    # Wednesday has a separate schedule
    if query.strftime("%A") == "Wednesday":
        return (OPEN_TIME <= query.time()) and (query.time() <= WEDNESDAY_CLOSE_TIME)
    
    return (OPEN_TIME <= query.time()) and (query.time() <= CLOSE_TIME)


def free_period(query=datetime.now()):
    """Determine the free period on a given day."""
    logging.info(f"Checking free period for {query}.")
    # Free periods rotate according to FREE_PATTERN, but only on school days
    school_days = np.busday_count(
        FIRST_DAY.strftime("%Y-%m-%d"), query.strftime("%Y-%m-%d"), holidays=HOLIDAYS)

    return FREE_PATTERN[school_days % 7]


def _validate_datetime(query):
    """Print a warning if the datetime is outside of the expected range."""
    if query < VALID_START or query > VALID_END:
        logging.warning(
            f"The given datetime '{query}' is outside the valid"
            f" range ({VALID_START} to {VALID_END}), this may lead to unexpected behaviour.")

def _is_holiday(query):
    """Check whether a given date is a holiday"""
    _validate_datetime(query)
    return not np.is_busday(query.strftime("%Y-%m-%d"), holidays=HOLIDAYS)
