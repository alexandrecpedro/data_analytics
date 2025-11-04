import sqlite3
import pandas as pd
from dotenv import load_dotenv

from enums.log_level_enum import LogLevel
from enums.sql_enum import SQLEnum
from log.logger import Logger


class DBConnectionManager:
    """
    Responsabilidade: Gerenciar a conexão in-memory com SQLite (Etapas 1, 2, 3),
    executar as etapas de setup e extração do banco.
    """

    def __init__(self):
        self.logger = Logger()
        # Opcional: carregar .env, embora as chaves não sejam mais usadas para DB
        load_dotenv()

        # Inicializa o banco de dados SQLite em memória
        self.conn = self._create_sqlite_connection()
        self._log(message="✅ Conexão SQLite in-memory inicializada com sucesso.")

    # ------------------------------------------------------------------
    # ⚙️ MÉTODOS DE CONEXÃO E SETUP (Etapas 1, 2, 3)
    # ------------------------------------------------------------------
    def _create_sqlite_connection(self):
        """Cria e retorna uma conexão SQLite in-memory."""
        try:
            # Usar ':memory:' cria um banco de dados temporário em RAM
            return sqlite3.connect(':memory:')
        except Exception as e:
            self._fail(message=f"Erro ao criar conexão SQLite: {e}")

    def execute_setup_script(self, sql_script: str):
        """
        Etapa 1: Executa o script DDL/DML no SQLite.
        """
        try:
            self._log(message="🔄 Executando script DDL/DML (DROP, CREATE, INSERT) no SQLite...")
            # executescript é ideal para múltiplos comandos separados por ';'
            self.conn.executescript(sql_script)
            self.conn.commit()
            self._log(message="✅ Tabelas criadas e dados inseridos no SQLite.")
        except Exception as e:
            self._fail(message=f"Erro na execução do script DDL/DML: {e}")

    def fetch_unified_data(self):
        """
        Etapa 2 & 3: Executa a consulta unificada e carrega no DataFrame.
        """
        sql_query_unified = f"""
        SELECT
            v.id_venda, v.data_venda, p.id_produto, p.nome_produto, p.categoria, p.preco_unitario, v.quantidade, v.desconto,
            -- Cálculo do valor_total: COALESCE(expr, 0.0) trata NULLs (descontos ausentes) como zero.
            (p.preco_unitario * v.quantidade) - COALESCE(v.desconto, 0.0) AS valor_total
        FROM
            {SQLEnum.SALES_TABLE_NAME.value} v
        LEFT JOIN 
            {SQLEnum.PRODUCTS_TABLE_NAME.value} p ON v.id_produto = p.id_produto;
        """

        try:
            self._log(message="🔄 Buscando dados da consulta unificada no SQLite...")
            # pd.read_sql_query funciona diretamente com a conexão sqlite3
            df = pd.read_sql_query(sql_query_unified, self.conn)
            self._log(message="✅ Dados carregados no DataFrame Pandas.")
            return df
        except Exception as e:
            self._fail(message=f"Erro ao carregar dados da consulta unificada: {e}")

    # ------------------------------------------------------------------
    # 🧭 UTILS
    # ------------------------------------------------------------------
    def _log(self, message: str, level=LogLevel.INFO):
        """Display structured log message."""
        self.logger.display(level=level, message=message)

    def _fail(self, message: str):
        """Log an error and raise immediately."""
        self._log(level=LogLevel.ERROR, message=message)
        raise ValueError(message)