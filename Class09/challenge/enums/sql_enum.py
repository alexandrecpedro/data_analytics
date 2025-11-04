from enum import Enum


class SQLEnum(Enum):
    PRODUCTS_TABLE_NAME = 'produtos'
    PRODUCTS_SCHEMA = [
        {"name": "id_produto", "type": "INTEGER PRIMARY KEY"},
        {"name": "nome_produto", "type": "TEXT"},
        {"name": "categoria", "type": "TEXT"},
        {"name": "preco_unitario", "type": "FLOAT"},
    ]

    SALES_TABLE_NAME = 'vendas'
    SALES_SCHEMA = [
        {"name": "id_venda", "type": "INTEGER PRIMARY KEY"},
        {"name": "id_produto", "type": "INTEGER"},
        {"name": "quantidade", "type": "INTEGER"},
        {"name": "data_venda", "type": "DATE"},
        {"name": "desconto", "type": "FLOAT"},
    ]