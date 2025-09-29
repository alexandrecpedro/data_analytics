from prettytable import PrettyTable

"""
FUNCTION SPLIT:
    (a) Definition
        Splits a string into a list of strings after breaking
        the given string by the specified separator

    (b) Syntax: str.split(separator, maxsplit)

INSTRUCTION:
    Write a program that reads a string containing three integers separated by spaces
    Split them into individual integers, calculate their sum, and display the result on the screen

TEST CASES:
    Entry = 26 128 44 (separated by white space)
    Exit:
        n1 = 26
        n2 = 128
        n3 = 44
        Sum = 198
"""

def validate_and_get_numbers(input_str: str):
    """
    Valida a entrada do usuário para garantir exatamente 3 números inteiros.

    Usa early return para sair assim que um erro é encontrado.
    Retorna: (lista_de_ints) ou (None, mensagem_de_erro)
    """
    input_values_list = input_str.strip().split(sep=' ')

    if len(input_values_list) != 3:
        return None, f"ERROR: You entered {len(input_values_list)} values. Please enter exactly 3 numbers."

    final_numbers = []
    for item in input_values_list:
        try:
            final_numbers.append(int(item))
        except ValueError:
            return None, f"ERROR: You entered {item} which is not an integer."

    return final_numbers, None

def main():
    while True:
        input_values_str = input('Enter 3 integer numbers separated by space: ')

        numbers, error_message = validate_and_get_numbers(input_str=input_values_str)
        if not error_message:
            final_numbers = numbers
            break

        print(error_message)

    table_field_names = ['Description', 'Value']
    table = PrettyTable(field_names=table_field_names)
    table.add_row(['Numbers received', final_numbers])
    table.add_row(['Quantity of numbers', len(final_numbers)])
    table.add_row(['Sum', sum(final_numbers)])
    print(table)

if __name__ == '__main__':
    main()