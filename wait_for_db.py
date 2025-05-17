import time
import psycopg2
from psycopg2 import OperationalError


def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname="reading_analytics",
                user="reading_admin",
                password="securepass123",
                host="postgres",  # Имя сервиса PostgreSQL
                port="5432",
            )
            conn.close()
            print("Database is ready.")
            break
        except OperationalError:
            print("Waiting for database...")
            time.sleep(2)


if __name__ == "__main__":
    wait_for_db()
