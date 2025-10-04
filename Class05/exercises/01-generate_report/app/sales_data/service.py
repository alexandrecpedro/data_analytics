import logging
from typing import List, Tuple
from common.constants import SalesFields, SEPARATOR
from sales_data.models import SalesRecord
from sales_data.repository import SalesFileRepository

class SalesService:
    """Handles the business logic: parsing, validation, and total calculation."""

    # O logger agora é tipado como logging.Logger
    def __init__(self, repository: SalesFileRepository, logger: logging.Logger):
        # Dependency Injection: O serviço depende do repositório e do logger
        self._repository = repository
        self._logger = logger

    def get_processed_sales(self) -> Tuple[List[SalesRecord], float]:
        """
        Reads raw data, processes it into SalesRecord objects, and computes the grand total.

        :return: A tuple containing the list of SalesRecord objects and the grand total sales value (float).
        """
        self._logger.info(msg=f"Processing sales data")
        # 1. Access data via Repository (decoupling I/O from business logic)
        raw_lines = self._repository.get_raw_lines()

        if raw_lines is None:
            # File not found error was already logged by repository.
            return [], 0.0

        sales_list: List[SalesRecord] = []
        total_sales_value: float = 0.0

        # 2. Process raw data (Business Logic)
        for line in raw_lines:
            parts = line.strip().split(SEPARATOR)

            if len(parts) == 3:
                try:
                    # Use Enum to access parts by field index for better readability
                    name = parts[SalesFields.NAME.value].strip()
                    department = parts[SalesFields.DEPARTMENT.value].strip()

                    # Convert and validate sales value
                    sales_value = float(parts[SalesFields.SALES_VALUE.value].strip())
                    total_sales_value += sales_value

                    # Create Model object (SalesRecord)
                    sales_list.append(SalesRecord(name, department, sales_value))

                except ValueError:
                    # Usamos o logger injetado
                    self._logger.error(msg=f'Invalid sales value in line ignored: {line.strip()}!')

            else:
                # Usamos o logger injetado
                self._logger.warning(msg=f'Skipping malformed line: {line.strip()}')

        if not sales_list:
            # Usamos o logger injetado
            self._logger.warning(msg=f'No valid sales data was processed!')

        return sales_list, total_sales_value