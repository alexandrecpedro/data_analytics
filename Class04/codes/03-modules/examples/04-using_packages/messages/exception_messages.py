from enum import Enum

class ExceptionMessages(Enum):
    INVALID_OPTION_EXCEPTION = "Error: Invalid choice. Please enter '0' for No or '1' for Yes!"
    INVALID_VALUE_EXCEPTION = "Error: Please enter a valid value!"
    NEGATIVE_VALUE_EXCEPTION = "Error: Please enter a non-negative value!"