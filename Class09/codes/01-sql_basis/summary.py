import os
import sys
import time

from Class09.codes.sql_basis.database.sql import SQLConnection
from Class09.codes.sql_basis.enums.file_enum import FileEnum
from Class09.codes.sql_basis.enums.sql_enum import SQLEnum
from Class09.codes.sql_basis.log.logger import Logger, LogLevel
from Class09.codes.sql_basis.report.report import Report

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def clean_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def read_file_data(filepath: str, encoding: str, logger: Logger):
    """Read data from file and return it as a list of dicts"""
    try:
        raw_data = [line.strip().split(sep=FileEnum.SEPARATOR.value) for line in open(file=filepath, mode='r', encoding=encoding)][1:]
        data = [{"name": col[0], "email": col[1], "course": col[2], "age": col[3]} for col in raw_data]
        return data
    except FileNotFoundError:
        logger.display(
            level=LogLevel.ERROR,
            message=f"File {filepath} not found.",
            exc_info=True
        )
        raise

def insert_data_into_table(table: str, sql_conn: SQLConnection, data: list, existing_emails: set, logger: Logger):
    """Insert new records into a SQL table, avoiding duplicates based on email"""
    try:
        file_insert_data = []
        inserted_emails = set(existing_emails)

        for row in data:
            email = row["email"]
            if email not in inserted_emails:
                file_insert_data.append(row)
                inserted_emails.add(email)

        sql_conn.insert(table_name=SQLEnum.SUBSCRIPTIONS_TABLE_NAME.value, data_list=file_insert_data)
        subscriptions = sql_conn.read(table_name=SQLEnum.SUBSCRIPTIONS_TABLE_NAME.value)
        return subscriptions

    except Exception as e:
        logger.display(
            level=LogLevel.ERROR,
            message=f"Error inserting data into table {table}: {e}",
            exc_info=True
        )
        raise

def main():
    logger = Logger()
    # Conexão com o banco de dados
    sql_conn = SQLConnection(db_name=FileEnum.DATABASE_FILE.value)

    # Criação da tabela (se não existir)
    sql_conn.create_table(
        table_name=SQLEnum.SUBSCRIPTIONS_TABLE_NAME.value,
        fields=SQLEnum.SUBSCRIPTIONS_SCHEMA.value
    )

    # Leitura de todos os registros
    subscriptions_before_insert = sql_conn.read(table_name=SQLEnum.SUBSCRIPTIONS_TABLE_NAME.value)
    print(subscriptions_before_insert)
    print('=' * 50)

    # # Inserção condicional
    insert_data = [
        {"name": "Ivan", "email": "ivan@gmail.com", "course": "Java", "age": 50},
        {"name": "Denise", "email": "denise@gmail.com", "course": "Java", "age": 45},
        {"name": "Carlos", "email": "carlos@gmail.com", "course": "Python", "age": 35},
        {"name": "Joana", "email": "joana@gmail.com", "course": "Java", "age": 24},
        {"name": "Silvio", "email": "silvio@gmail.com", "course": "Dados", "age": 67},
    ]

    existing_emails = {row['email'] for row in subscriptions_before_insert}
    new_insert_data = [row for row in insert_data if row['email'] not in existing_emails]

    if new_insert_data:
        subscriptions = insert_data_into_table(
            table=SQLEnum.SUBSCRIPTIONS_TABLE_NAME.value,
            sql_conn=sql_conn,
            data=new_insert_data,
            existing_emails=existing_emails,
            logger=logger
        )
        print(subscriptions)
        print('=' * 50)

    # # Read new data from file
    # encoding = FileEnum.ENCODING.value
    # data_file = FileEnum.DATA_FILE.value
    # file_data = read_file_data(filepath=data_file, logger=logger, encoding=encoding)
    #
    # # Insert only new data
    # subscriptions_after_data_file = insert_data_into_table(
    #     table=SQLEnum.SUBSCRIPTIONS_TABLE_NAME.value,
    #     sql_conn=sql_conn,
    #     data=file_data,
    #     existing_emails=existing_emails,
    #     logger=logger
    # )
    #
    # print(subscriptions_after_data_file)
    # print('=' * 50)
    # time.sleep(5)
    # clean_screen()

    encoding = FileEnum.ENCODING.value
    random_data_filepath = FileEnum.RANDOM_DATA_FILE.value
    random_file_data = read_file_data(filepath=random_data_filepath, logger=logger, encoding=encoding)
    subscriptions_random_data_file = insert_data_into_table(
        table=SQLEnum.SUBSCRIPTIONS_TABLE_NAME.value,
        sql_conn=sql_conn,
        data=random_file_data,
        existing_emails=existing_emails,
        logger=logger
    )

    print(subscriptions_random_data_file)
    print('=' * 50)
    time.sleep(10)
    clean_screen()

    report = Report(data=subscriptions_random_data_file)
    report.display()

if __name__ == '__main__':
    main()