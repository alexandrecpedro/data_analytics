import locale
from enum import Enum
from prettytable import PrettyTable

"""
PRODUCT CATALOGUE
"""

# ========== PART 1 - ENUMS ==========
class ErrorMessage(Enum):
    INVALID_TYPE = 'Invalid item type!'
    NOT_FOUND = 'Item not found!'

class Color(Enum):
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    GREEN = "\033[32m"
    MAGENTA = "\033[35m"
    RED = "\033[31m"
    RESET = "\033[0m"
    YELLOW = "\033[33m"

# ========== PART 2 - CONSTANTS ==========
FIELD_NAMES = ['Description', 'Value']
ITEM_CATALOG = {
    'tv': 1500,
    'radio': 200,
    'microwave-oven': 500,
    'fridge': 3500,
    'oven': 900
}

# ========== PART 3 - LOCALE ADAPTATIONS ==========
locale.setlocale(category=locale.LC_ALL, locale='pt_BR.UTF-8')

# ========== PART 4 - FUNCTIONS ==========
def display_all_products(catalog: dict[str, int], table: PrettyTable) -> PrettyTable:
    """Builds a table with all catalog items"""
    for name, value in catalog.items():
        formatted_value = format_currency(value=value)
        table.add_row([name, formatted_value])
    return table

def display_catalog_and_choice(product_name: str, catalog: dict[str, int], table_field_names: list[str]) -> PrettyTable:
    """Displays the full catalog and highlights the chosen product"""
    table = generate_table(table_field_names=table_field_names)
    display_all_products(catalog=catalog, table=table)

    item_value = catalog.get(product_name, ErrorMessage.NOT_FOUND.value)
    formatted_item_value = format_currency(value=item_value) if isinstance(item_value, (int, float)) else item_value

    table.add_rows([
        ['=========', '========='],
        [highlight(text=product_name), highlight(text=formatted_item_value)]
    ])

    return table

def format_currency(value: int | float) -> str:
    """Converts a number into local currency format using locale"""
    try:
        return locale.currency(val=value, grouping=True)
    except (ValueError, TypeError):
        return ErrorMessage.INVALID_TYPE.value

def generate_table(table_field_names: list[str]) -> PrettyTable:
    """Generates a table to display the results"""
    return PrettyTable(field_names=table_field_names, border=True, header=True)

def get_user_choice() -> str:
    """Reads the product choice from the user"""
    return input('Enter product name (or type "all" to list all): ').strip().lower()

def highlight(text: str, color: Color = Color.BLUE) -> str:
    """
    Highlights text using ANSI color constants.
    Default color is green.
    """
    return f"{color.value}{text}{Color.RESET.value}"

def main():
    choice = get_user_choice()
    table = display_catalog_and_choice(product_name=choice, catalog=ITEM_CATALOG, table_field_names=FIELD_NAMES)
    print(table)

if __name__ == '__main__':
    main()