import random
from datetime import datetime
from .value_generator import valueGenerator


class deviceInserter:
    def __init__(self) -> None:
        self.vg = valueGenerator()

    def __make_insert_query(self, id: int) -> str:
        vg = self.vg
        random_date: datetime = vg.getRandomDate()
        device_idx: int = random.randrange(8)

        device_id: str = vg.setDeviceID(random_date, device_idx)
        region: str = vg.setRegion()
        location: str = vg.setLocation()
        device_name: str = vg.setDeviceName(device_idx)
        createdAt: str = vg.setCreatedAt(random_date)

        return f"INSERT INTO Devices VALUES ({id}, 1, '{device_id}', '{region}', '{location}', '{device_name}', False, False, '{createdAt}')"

    def run(self, cur, count: int = 1) -> None:
        for _ in range(count):
            cur.execute('select count(*) from Devices')
            (row_count,) = cur.fetchone()

            query: str = self.__make_insert_query(row_count + 1)

            cur.execute(query)
            print('Success: %s' % query)
