import mariadb
import os
import sys
from dotenv import load_dotenv


class dbConnector:
    def __init__(self) -> None:
        load_dotenv(verbose=True)

        try:
            conn = mariadb.connect(
                user=os.getenv('USERNAME'),
                password=os.getenv('PASSWORD'),
                host=os.getenv('HOST'),
                port=int(os.getenv('PORT')),
                database=os.getenv('DATABASE'),
                autocommit=True
            )
        except mariadb.Error as e:
            print(f'Error connecting to MariaDB Platform: {e}')
            sys.exit(1)

        self.cur = conn.cursor()
