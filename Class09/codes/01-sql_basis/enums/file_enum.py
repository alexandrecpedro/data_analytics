from enum import Enum


class FileEnum(Enum):
    DATABASE_FILE = 'database/sqlite_database.db'
    DATA_FILE = 'assets/files/data_colab.txt'
    RANDOM_DATA_FILE = 'assets/files/subscriptions_random.txt'
    ENCODING = 'utf-8'
    SEPARATOR = ','