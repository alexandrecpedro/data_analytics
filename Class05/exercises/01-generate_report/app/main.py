import logging
import os
import sys
from sales_data.repository import SalesFileRepository
from sales_data.service import SalesService
from sales_report.generator import SalesReportGenerator
from common.constants import ENCODING, FILEPATH, MODE  # Import constants from the common module

# ===============================================================================
# 2. SET LOGGING
# ===============================================================================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ===============================================================================
# 3. MAIN FUNCTION (Controller/Orchestration)
# ===============================================================================
def main():
    """
    Main function to execute the sales report generation process.

    This function acts as the Controller, coordinating the Data Access (Repository),
    Business Logic (Service), and Presentation (Generator) layers.
    """
    logger.info("Starting Sales Report Generation program...")

    current_dir = os.path.dirname(__file__)
    absolute_filepath = os.path.join(current_dir, FILEPATH)

    # 1. Initialize Repository (Data Access Layer)
    repository = SalesFileRepository(logger=logger, filepath=absolute_filepath, mode=MODE, encoding=ENCODING)

    # 2. Initialize Service (Business Logic Layer)
    service = SalesService(repository=repository, logger=logger)

    # 3. Execute Service Logic
    sales_data, total_sales_value = service.get_processed_sales()

    if not sales_data:
        logger.error(msg=f'No valid sales data was processed! Check file path: {absolute_filepath}.')
        return

    # 4. Initialize and Generate Report (Presentation Layer)
    generator = SalesReportGenerator(logger=logger)
    report_output = generator.generate_report(sales_data=sales_data, total_sales_value=total_sales_value)

    sys.stdout.flush()

    print(f'\n{report_output}')
    logger.info('End of program')

if __name__ == '__main__':
    main()
