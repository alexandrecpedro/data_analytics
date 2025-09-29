from enum import Enum

class ExceptionMessages(Enum):
    INVALID_COST_INPUT_EXCEPTION = "Invalid cost input! Please enter a valid number"
    INVALID_OPTION_EXCEPTION = "Error: Invalid choice. Please enter '0' for No or '1' for Yes!"
    INVALID_VALUE_EXCEPTION = "Error: Please enter a valid value!"
    NEGATIVE_VALUE_EXCEPTION = "Error: Negative values are not allowed for this input!"
    PRODUCT_CODE_EXCEPTION = "Error: Invalid product code. Please enter a valid numeric product code!"