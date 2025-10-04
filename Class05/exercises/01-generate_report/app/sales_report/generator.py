import logging
from typing import List
from common.constants import (
    REPORT_WIDTH, COL_NAME_WIDTH, COL_DEPT_WIDTH, COL_SALES_WIDTH, HEADER_TEXT, SalesFields
)
from sales_data.models import SalesRecord

class SalesReportGenerator:
    """Handles the formatting and generation of the final sales report."""

    def __init__(self, logger: logging.Logger):
        self._logger = logger

    @staticmethod
    def _format_sales_value(value: float) -> str:
        """
        Formats a float value into the R$ X,XXX.XX string format (US locale formatting with R$ symbol).

        :param value: The sales value (float) to be formatted.
        :return: A formatted string including 'R$ ' prefix and US localization for numbers.
        """
        # Uses US locale formatting (comma for thousands, period for decimals)
        # R$ symbol is added manually.
        return f'R$ {value:12,.2f}'

    def generate_report(self, sales_data: List[SalesRecord], total_sales_value: float) -> str:
        """
        Generates a precisely aligned text report based on the processed sales data.

        :param sales_data: A list of SalesRecord objects.
        :param total_sales_value: The calculated grand total of all sales.
        :return: A formatted string representing the final sales report.
        """
        self._logger.info(msg=f"Generating report for sales data...")
        report: List[str] = []

        # 1. Header
        header_text_centered = HEADER_TEXT.center(REPORT_WIDTH, '=')
        report.append(header_text_centered)

        # 2. Column Headers
        header_line = (
                "Name".ljust(COL_NAME_WIDTH) +
                "Department".ljust(COL_DEPT_WIDTH) +
                "Total Sales Value".rjust(COL_SALES_WIDTH)
        )
        report.append(header_line)

        # 3. Separator line
        report.append('-' * REPORT_WIDTH)

        # 4. Data Lines
        for entry in sales_data:
            sales_value = entry.sales_value

            # Format value using the helper function
            formatted_sales_value = self._format_sales_value(sales_value)

            data_line = (
                    entry.name.ljust(COL_NAME_WIDTH) +
                    entry.department.ljust(COL_DEPT_WIDTH) +
                    formatted_sales_value.rjust(COL_SALES_WIDTH)
            )
            report.append(data_line)

        # 5. Bottom separator line
        report.append('-' * REPORT_WIDTH)

        # 6. Grand Total
        formatted_total = self._format_sales_value(total_sales_value)

        # TOTAL GENERAL is left-aligned across the Name/Department columns and the value is right-aligned
        total_line = (
                "TOTAL GENERAL".ljust(COL_NAME_WIDTH + COL_DEPT_WIDTH) +  # Align the label
                formatted_total.rjust(COL_SALES_WIDTH)  # Align the value
        )
        report.append(total_line)

        # 7. Footer
        report.append("=" * REPORT_WIDTH)

        self._logger.info("Sales report successfully generated.")

        return "\n".join(report)
