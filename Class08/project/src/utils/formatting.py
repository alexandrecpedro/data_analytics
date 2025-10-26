# formatted_currency = lambda currency_value: (
#     f'R$ {currency_value:,.2f}'.replace(".", "X").replace(",", ".").replace("X", ",")
# )
formatted_currency = lambda currency_value: f'R$ {currency_value:,.2f}'