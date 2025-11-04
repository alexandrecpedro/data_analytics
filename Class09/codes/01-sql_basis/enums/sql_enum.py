from enum import Enum


class SQLEnum(Enum):
    SUBSCRIPTIONS_TABLE_NAME = 'subscriptions'
    SUBSCRIPTIONS_SCHEMA = [
        {"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"},
        {"name": "name", "type": "TEXT NOT NULL"},
        {"name": "email", "type": "TEXT UNIQUE NOT NULL"},
        {"name": "course", "type": "TEXT NOT NULL"},
        {"name": "age", "type": "INTEGER"}
    ]