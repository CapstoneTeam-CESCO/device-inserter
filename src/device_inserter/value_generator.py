import random
from datetime import datetime, timedelta
from typing import List
from src.constants import myconstants


class valueGenerator:
    def getRandomDate(self) -> datetime:
        start_date = datetime(2010, 1, 1)
        end_date = datetime.now()

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        seconds_between_dates = time_between_dates.seconds
        random_num_of_secs = random.randrange(seconds_between_dates)
        random_num_of_days = random.randrange(days_between_dates)

        return start_date + \
            timedelta(days=random_num_of_days,
                      seconds=random_num_of_secs)

    def __make_2_digits(self, value: int) -> str:
        if value < 10:
            return '0' + str(value)
        return str(value)

    def setDeviceID(self, random_date: datetime, device_idx: int) -> str:
        types: List[str] = myconstants.DEVICE_TYPES
        deviceType = types[device_idx]

        time: str = ''
        time += self.__make_2_digits(random_date.year % 100)
        time += self.__make_2_digits(random_date.month)
        time += self.__make_2_digits(random_date.day)

        serial: str = ''
        for _ in range(4):
            serial += str(random.randrange(0, 10))

        return deviceType + time + serial

    def setRegion(self) -> str:
        regions: List[str] = myconstants.REGIONS
        return regions[random.randrange(len(regions))]

    def setLocation(self) -> str:
        locations: List[str] = myconstants.LOCATIONS
        return locations[random.randrange(len(locations))]

    def setDeviceName(self, device_idx: int) -> str:
        names: List[str] = myconstants.DEVICE_NAMES
        return names[device_idx]

    def setCreatedAt(self, random_date: datetime) -> str:
        year = str(random_date.year)
        month = self.__make_2_digits(random_date.month)
        day = self.__make_2_digits(random_date.day)
        hour = self.__make_2_digits(random_date.hour)
        minute = self.__make_2_digits(random_date.minute)
        second = self.__make_2_digits(random_date.second)

        return f'{year}-{month}-{day} {hour}:{minute}:{second}'
