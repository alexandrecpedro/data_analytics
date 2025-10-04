"""
INSTRUCTIONS:
    Write a programme that reads an input file and generate a report as the following image:

    ======================= SALES REPORT =======================
    Name                Department            Total Sales Value
    ------------------------------------------------------------
    Helena              Logistic              R$   17,019.12
    Sergio              HR                    R$   12,212.26
    Tatiane             HR                    R$    1,467.60
    Vinicius            Sales                 R$   17,008.33
    ...
    Eduardo             Sales                 R$   13,561.92
    Nicolas             Marketing             R$    3,243.97
    Juliana             Sales                 R$   11,859.78
    Karen               IT                    R$    9,822.86
    Vinicius            Logistic              R$   12,327.84
    ------------------------------------------------------------
    TOTAL GENERAL                             R$  189,897.60
"""

import logging
from enum import Enum
from typing import Dict, List, Tuple, Union

# ===============================================================================
# 1. CONSTANTS
# ===============================================================================
FILEPATH = 'assets/vendas.txt'
MODE = 'r'
ENCODING = 'utf-8'
FORMAT_SPEC_2f = '2f'
SEPARATOR = ';'
HEADER_TEXT = ' SALES REPORT '

# Total width and column widths for precise alignment
REPORT_WIDTH = 52
COL_DEPT_WIDTH = 15
COL_NAME_WIDTH = 20
COL_SALES_WIDTH = REPORT_WIDTH - COL_NAME_WIDTH - COL_DEPT_WIDTH

class SalesFields(Enum):
    """Represents the expected fields (keys) in the sales data dictionary."""
    NAME = 0
    DEPARTMENT = 1
    SALES_VALUE = 2

SalesEntry = Dict[SalesFields, Union[str, float]]

# ===============================================================================
# 2. SET LOGGING
# ===============================================================================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ===============================================================================
# 3. HELPER FUNCTIONS
# ===============================================================================
def read_sales_data(filepath: str, separator: str) -> Tuple[List[SalesEntry], float]:
    """
    Reads the sales data from a file and converts sales values to float, and calculates the grand total.
    :param filepath: The path to the input file (e.g., 'assets/vendas.txt').
    :param separator: The delimiter used in the file (e.g., ';').
    :return: A tuple containing the list of sales dictionaries and the grand total sales value (float).
    """
    sales_list: List[SalesEntry] = []
    total_sales_value: float = 0.0

    try:
        with open(file=filepath, mode=MODE, encoding=ENCODING) as file:
            try:
                # Skip header line
                next(file)
            except StopIteration:
                logger.warning(msg=f'The file {filepath} is empty!')
                return [], 0.0

            for line in file:
                parts = line.strip().split(separator)
                if len(parts) == 3:
                    name = parts[0].strip()
                    department = parts[1].strip()
                    try:
                        # Converts the sales string to float (using '.' as decimal)
                        sales_value = float(parts[2].strip())
                        total_sales_value += sales_value

                        sales_list.append({
                            SalesFields.NAME: name,
                            SalesFields.DEPARTMENT: department,
                            SalesFields.SALES_VALUE: sales_value,
                        })
                    except ValueError:
                        logger.error(msg=f'Invalid sales value in line ignored: {line.strip()}!')
        return sales_list, total_sales_value
    except FileNotFoundError:
        return [], 0.0

def generate_report(sales_data: List[SalesEntry], total_sales_value: float) -> str:
    """
    Generates a report for the sales data.
    :param sales_data: A list of SalesEntry dictionaries containing the parsed sales records.
    :param total_sales_value: The calculated grand total of all sales (float).
    :return: A formatted string representing the final sales report.
    """
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
        name = entry.get(SalesFields.NAME, '')
        department = entry.get(SalesFields.DEPARTMENT, '')
        sales_value = entry.get(SalesFields.SALES_VALUE, 0.0)

        # Formatting the sales value for display (R$ X,XXX.XX)
        formatted_sales_value = f'R$ {sales_value:12,.2f}'

        data_line = (
            name.ljust(COL_NAME_WIDTH) +
            department.ljust(COL_DEPT_WIDTH) +
            formatted_sales_value.rjust(COL_SALES_WIDTH)
        )
        report.append(data_line)

    # 5. Bottom separator line
    report.append('-' * REPORT_WIDTH)

    # 6. Grand Total
    # formatted_total = format_currency(value=total_sales_value)
    formatted_total = f'R$ {total_sales_value:12,.2f}'

    # GRAND TOTAL is left-aligned across the Name/Department columns and the value is right-aligned
    total_line = (
        "GRAND TOTAL".ljust(COL_NAME_WIDTH + COL_DEPT_WIDTH) + # Align the label
        formatted_total.rjust(COL_SALES_WIDTH)                 # Align the value
    )
    report.append(total_line)

    # 7. Footer
    report.append("=" * REPORT_WIDTH)

    return "\n".join(report)

# ===============================================================================
# 4. MAIN FUNCTION
# ===============================================================================
def main():
    print("Starting Sales Report Generation program...")

    sales_data, total_sales_value = read_sales_data(filepath=FILEPATH, separator=SEPARATOR)
    if not sales_data:
        logger.error(msg=f'No valid sales data was processed!')
        return

    report_output = generate_report(sales_data=sales_data, total_sales_value=total_sales_value)
    print(f'\n{report_output}')
    print('\nEnd of program')


if __name__ == '__main__':
    main()