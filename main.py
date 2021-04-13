from src.db_connector.db_connector import dbConnector
from src.device_inserter.device_inserter import deviceInserter


def main() -> None:
    count = int(input('Type number of devices you want to insert: '))
    db_conn = dbConnector()
    deviceInserter().run(db_conn.cur, count)


if __name__ == "__main__":
    main()
