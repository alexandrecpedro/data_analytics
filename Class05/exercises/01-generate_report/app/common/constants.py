from enum import Enum
from typing import Final

# ===============================================================================
# 1. APPLICATION CONFIGURATION CONSTANTS
# ===============================================================================
# Final type hint is used to signify that these variables are constants and should not be reassigned.
FILEPATH: Final[str] = '../assets/vendas.txt'
ENCODING: Final[str] = 'utf-8'
SEPARATOR: Final[str] = ';'
MODE: Final[str] = 'r'

# ===============================================================================
# 2. REPORT LAYOUT CONSTANTS
# ===============================================================================
# Dimensions and fixed strings for the report layout.
REPORT_WIDTH: Final[int] = 52
COL_DEPT_WIDTH: Final[int] = 15
COL_NAME_WIDTH: Final[int] = 20
# Calculate remaining width dynamically to ensure REPORT_WIDTH is always maintained.
COL_SALES_WIDTH: Final[int] = REPORT_WIDTH - COL_NAME_WIDTH - COL_DEPT_WIDTH
HEADER_TEXT: Final[str] = ' SALES REPORT '

# ===============================================================================
# 3. ENUMERATION (DATA INDEX MAPPING)
# ===============================================================================
class SalesFields(Enum):
    """Maps the column index to the field name in the input file."""
    NAME = 0
    DEPARTMENT = 1
    SALES_VALUE = 2