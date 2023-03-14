from school_schedule import registration_open, free_period

from datetime import datetime


class TestFreePeriod:
    def test_first_day(self):
        assert free_period(datetime(2022, 9, 7)) == "C"

    def test_known_day(self):
        assert free_period(datetime(2023, 3, 14)) == "G"


class TestRegistrationOpen:
    def test_early(self):
        assert registration_open(datetime(2023, 3, 14, 6, 0)) == False

    def test_late(self):
        assert registration_open(datetime(2023, 3, 14, 10, 0)) == False

    def test_wednesday(self):
        # registration is open late on wednesday
        assert registration_open(datetime(2023, 3, 15, 10, 0)) == True

    def test_ontime(self):
        assert registration_open(datetime(2023, 3, 14, 9, 37)) == True

    def test_weekend(self):
        assert registration_open(datetime(2023, 3, 12, 9, 37)) == False
