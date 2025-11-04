import sqlite3
from contextlib import contextmanager

from enums.log_level_enum import LogLevel
from log.logger import Logger


class SQLConnection:
    """
    SQLite connection handler with basic CRUD operations,
    automatic rollback on failure, and referential integrity enabled.
    """
    def __init__(self, db_name: str):
        self.logger = Logger()
        self.db_name = db_name
        self.conn = None
        self._connect()
        self._enable_foreign_keys()

    # -------------------------------------------------------------
    # 🔗 Connection Management
    # -------------------------------------------------------------
    def _connect(self, timeout: int = 60):
        """Connect to the SQLite database file."""
        if getattr(self, "conn", None):
            # Já conectado
            self.logger.display(message=f"Already connected to database: {self.db_name}")
            return self.conn

        self.logger.display(message=f"Connecting to database: {self.db_name}")
        try:
            self.conn = sqlite3.connect(database=self.db_name, timeout=timeout)
            self.conn.row_factory = sqlite3.Row # Rows as dict-like objects
            self.logger.display(message=f"Connected to database: {self.db_name}")
            return self.conn
        except sqlite3.DatabaseError:
            self.logger.display(
                level=LogLevel.ERROR,
                message="Error connecting to SQLite database",
                exc_info=True
            )
            raise

    def _enable_foreign_keys(self):
        """Ensure foreign key constraints are enforced."""
        if not getattr(self, "conn", None):
            self.logger.display(level=LogLevel.WARNING, message="No active connection to enable foreign keys")
            return

        self.logger.display(message="Enabling foreign key constraints")
        try:
            self.conn.execute("PRAGMA foreign_keys = ON;")
            self.logger.display(message="Foreign key constraints enabled")
        except sqlite3.DatabaseError as e:
            self.logger.display(
                level=LogLevel.WARNING,
                message=f"Could not enable foreign keys: {e}",
                exc_info=True
            )

    def close(self):
        """Close the database connection."""
        if not getattr(self, "conn", None):
            self.logger.display(message="No active connection to close")
            return

        self.logger.display(message="Closing database connection")
        try:
            self.conn.close()
            self.conn = None
            self.logger.display(message="Database connection closed successfully")
        except sqlite3.Error:
            self.logger.display(
                level=LogLevel.ERROR,
                message="Could not close database connection",
                exc_info=True
            )

    # -------------------------------------------------------------
    # ⚙️ Context Manager for Safe Transactions
    # -------------------------------------------------------------
    @contextmanager
    def _transaction(self):
        """
        Context manager that commits on success and rollbacks on failure.
        Usage:
            with self._transaction():
                self.conn.execute("INSERT ...")
        """
        # self.logger.display(message="Starting database transaction")
        try:
            yield
            self.conn.commit()
        except sqlite3.DatabaseError:
            self.conn.rollback()
            self.logger.display(
                level=LogLevel.ERROR,
                message="Transaction failed. Rolled back",
                exc_info=True
            )
            raise

    # -------------------------------------------------------------
    # Helper: Execute SQL with transaction and logging
    # -------------------------------------------------------------
    def _execute(self, query: str, values=None, fetch: bool = False, message: str = None, many: bool = False):
        """
        Executes SQL within a transaction and handles errors.
        Shows the query with actual values for debugging.

        :param query:
        :param values:
        :param fetch:
        :param message: Message to display
        :param many: se True, 'values' é uma lista de tuplas para executemany
        :return:
        """
        values = values or ()
        message = message or f"Failed executing query: {query}"

        try:
            with self._transaction():
                execute_fn = self.conn.executemany if many else self.conn.execute
                cursor = execute_fn(query, values)

                result = [dict(row) for row in cursor.fetchall()] if fetch else cursor
                cursor.close()
                return result
        except sqlite3.DatabaseError:
            self.logger.display(level=LogLevel.ERROR, message=message, exc_info=True)
            raise

    # -------------------------------------------------------------
    # 🧱 Table Management
    # -------------------------------------------------------------
    def create_table(self, table_name: str, fields: list[dict[str, str]]):
        """
        Create a table if it does not exist, and automatically add missing columns
        if new fields are introduced later.

        :param table_name: name of the table
        :param fields: list of dictionaries describing the fields to be added
            e.g.
            [
                {"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"},
                {"name": "username", "type": "TEXT NOT NULL"},
                {"name": "email", "type": "TEXT UNIQUE"}
            ]
        :return: None
        """
        # Checa se a tabela já existe
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?;"
        values = (table_name,)
        cursor = self._execute(query=query, values=values, fetch=True)
        table_exists = bool(cursor)

        self.logger.display(message=f"Creating table '{table_name}'")
        # Query de criação da tabela
        columns_def = ', '.join([f"{field['name']} {field['type']}" for field in fields])
        create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def});"
        error_message = f"Error creating or updating table '{table_name}'"
        self._execute(query=create_query, message=error_message)

        # Mensagens conforme estado da tabela
        messages = {
            True: f"Table '{table_name}' already exists",
            False: f"Table '{table_name}' created successfully"
        }

        self.logger.display(message=messages[table_exists])

        self._add_missing_columns(table_name=table_name, fields=fields)

    def _add_missing_columns(self, table_name: str, fields: list[dict[str, str]]):
        """
        Add columns that are in 'fields' but missing in the table.
        Makes new columns nullable if NOT NULL without DEFAULT.

        :param table_name: name of the table
        :param fields: list of dictionaries describing the fields to be added
            e.g.
            [
                {"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"},
                {"name": "username", "type": "TEXT NOT NULL"},
                {"name": "email", "type": "TEXT UNIQUE"}
            ]
        :return: None
        """
        # self.logger.display(message=f"Checking for missing columns in '{table_name}'")
        cursor_query = f"PRAGMA table_info({table_name});"
        error_message = f"Error adding missing columns to table '{table_name}'"
        existing_columns = [row["name"] for row in self._execute(query=cursor_query, fetch=True, message=error_message)]

        for field in fields:
            col_name = field["name"]
            col_type = field["type"].strip().upper()

            if col_name not in existing_columns:
                # Impede erro se for NOT NULL sem DEFAULT
                safe_col_type = col_type
                if "NOT NULL" in col_type and "DEFAULT" not in col_type:
                    safe_col_type = col_type.replace("NOT NULL", "").strip()
                    self.logger.display(
                        level=LogLevel.WARNING,
                        message=(
                            f"Column '{col_name}' in '{table_name}' defined as NOT NULL without DEFAULT. "
                            f"Automatically made nullable to avoid SQLite error."
                        )
                    )

                alter_query = f"ALTER TABLE {table_name} ADD COLUMN {col_name} {safe_col_type};"
                alter_query_error_message = f"Failed adding column '{col_name}' to '{table_name}'"
                self._execute(query=alter_query, message=alter_query_error_message)
                self.logger.display(
                    level=LogLevel.WARNING,
                    message=f"Added new column '{col_name}' ({safe_col_type}) to table '{table_name}'"
                )

    # -------------------------------------------------------------
    # 🧩 CRUD Operations
    # -------------------------------------------------------------
    def insert(self, table_name: str, data_list: list[dict], unique_field: str = None):
        """
        Insert one or multiple records into the table.
        Skips insert if unique_field already exists.

        :param table_name: Name of the table
        :param data_list: List of dictionaries (multiple records) with column names and values
        :param unique_field: Optional unique column name to check before inserting
        :return: None
        """
        if not data_list:
            self.logger.display(message=f"Insert data list is empty")
            return

        if not isinstance(data_list, list) or not all(isinstance(row, dict) for row in data_list):
            self.logger.display(
                level=LogLevel.ERROR,
                message="Data must be a list of dictionaries",
                exc_info=True
            )
            raise ValueError("Data must be a list of dictionaries")

        # Filtrar registros que já existem se unique_field for informado
        if unique_field:
            unique_values = [row[unique_field] for row in data_list if unique_field in row]
            if unique_values:
                placeholders = ','.join(['?'] * len(unique_values))
                query = f"SELECT {unique_field} FROM {table_name} WHERE {unique_field} IN ({placeholders})"
                existing_records = self._execute(query=query, values=unique_values, fetch=True)
                existing_values = {r[unique_field] for r in existing_records}
                data_list = [row for row in data_list if row.get(unique_field) not in existing_values]

        if not data_list:
            self.logger.display(level=LogLevel.WARNING, message="No new records to insert")
            return

        columns = ', '.join(data_list[0].keys())
        placeholders = ', '.join(['?'] * len(data_list[0]))
        values = [tuple(row.values()) for row in data_list]
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        error_message = f"Failed to insert record(s) into '{table_name}'"
        self._execute(query=query, values=values, message=error_message, many=True)
        self.logger.display(message=f"{len(data_list)} record(s) inserted into '{table_name}' successfully")

    def read(
            self,
            table_name: str,
            fields: list = None,
            where: dict = None,
            order_by: str = None,
            limit: int = None,
            offset: int = None
    ):
        """
        Read records from the table with optional WHERE, LIMIT, and OFFSET.

        :param table_name: Name of the table
        :param fields: Optional list of columns to select. Default is all (*)
        :param where: Optional filter conditions, e.g. {"username": "Alice"}
        :param order_by: Optional ordering conditions, e.g. "id DESC"
        :param limit: Optional limit for pagination
        :param offset: Optional offset for pagination
        :return: List of rows as dictionaries
        """
        query_fields = ', '.join(fields) if fields else '*'
        values = []

        query = f"SELECT {query_fields} FROM {table_name}"

        if where:
            conditions = ' AND '.join([f'{key}=?' for key in where])
            query += f' WHERE {conditions}'
            values.extend(where.values())

        if order_by:
            query += f' ORDER BY {order_by}'

        if limit is not None:
            query += f' LIMIT ?'
            values.append(limit)

        if offset is not None:
            query += f' OFFSET ?'
            values.append(offset)

        error_message = f"Error reading data from '{table_name}'"
        result = self._execute(query=query, values=values, fetch=True, message=error_message)
        return result


    def update(self, table_name: str, data_list: list[dict], where_list: list[dict]):
        """
        Update one or multiple records in a table.

        :param table_name: Name of the table
        :param data_list: List of dictionaries with column names and values
        :param where_list: List of dictionaries with filter conditions, e.g. [{"username": "Alice"}]
        :return: None
        """
        if not data_list or not where_list:
            self.logger.display(level=LogLevel.WARNING, message=f"No data or conditions provided for update")
            return

        if not isinstance(data_list, list) or not all(isinstance(row, dict) for row in data_list):
            self.logger.display(
                level=LogLevel.ERROR,
                message="Data must be a list of dictionaries",
                exc_info=True
            )
            raise ValueError("Data must be a list of dictionaries")


        set_clause = ', '.join([f'{k}=?' for k in data_keys])
        where_clause = ' AND '.join([f'{k}=?' for k in where_keys])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"

        values = [
             tuple(d[k] for k in data_keys) + tuple(w[k] for k in where_keys)
             for d, w in zip(data_list, where_list)
        ]

        # Executar todas
        error_message = f"Failed to update record in '{table_name}'"
        cursor_result = self._execute(query=query, values=values, many=True, message=error_message)
        self.logger.display(message=f"{cursor_result.rowcount} record(s) updated in '{table_name}' successfully")

    def delete(self, table_name: str, where_list: list[dict]):
        """
        Delete one or multiple records from a table

        :param table_name: Name of the table
        :param where_list: List of dictionaries with filter conditions, e.g. [{"username": "Alice"}]
        :return: None
        """
        if not where_list:
            self.logger.display(level=LogLevel.WARNING, message="No conditions provided for delete")
            return

        keys = where_list[0].keys()
        where_clause = ' AND '.join([f'{k}=?' for k in keys])
        query = f'DELETE FROM {table_name} WHERE {where_clause}'
        values = [tuple(w[k] for k in keys) for w in where_list]

        error_message = f"Error deleting from '{table_name}'"
        cursor_result = self._execute(query=query, values=values, many=True, message=error_message)

        self.logger.display(message=f"{cursor_result.rowcount} record(s) deleted from '{table_name}' successfully")