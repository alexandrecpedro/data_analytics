from database.database_conn import DBConnectionManager
from enums.log_level_enum import LogLevel
from log.logger import Logger

# Bloco SQL de criação e inserção das tabelas (Etapa 1 )
SQL_SCRIPT_FULL = """
-- Ajustado para compatibilidade com SQLite
DROP TABLE IF EXISTS vendas;
DROP TABLE IF EXISTS produtos;

CREATE TABLE produtos (
    id_produto INTEGER PRIMARY KEY,
    nome_produto TEXT,
    categoria TEXT,
    preco_unitario REAL
);

CREATE TABLE vendas (
    id_venda INTEGER PRIMARY KEY,
    id_produto INTEGER,
    quantidade INTEGER,
    data_venda DATE,
    desconto REAL
);

INSERT INTO produtos (id_produto, nome_produto, categoria, preco_unitario) VALUES
(1, 'Notebook Dell', 'Informática', 3500.00), (2, 'Mouse Logitech', 'Acessórios', 120.00), 
(3, 'Monitor LG 24"', 'Informática', 950.00), (4, 'Teclado Mecânico', 'Acessórios', 420.00),
(5, 'Headset Gamer', 'Acessórios', 480.00), (6, 'Impressora HP', 'Periféricos', 800.00), 
(7, 'Smartphone Samsung', 'Telefonia', 2900.00), (8, 'Cabo HDMI 2m', 'Acessórios', 40.00),
(9, 'Webcam Logitech', 'Acessórios', 310.00), (10, 'Roteador TP-Link', 'Redes', 250.00),
(11, 'SSD Kingston 480GB', 'Armazenamento', 380.00), (12, 'HD Externo 1TB', 'Armazenamento', 420.00),
(13, 'Tablet Lenovo', 'Informática', 1300.00), (14, 'Monitor Samsung 27"', 'Informática', NULL), 
(15, 'Caixa de Som JBL', NULL, 550.00); 

INSERT INTO vendas (id_venda, id_produto, quantidade, data_venda, desconto) VALUES
(1, 1, 3, '2025-10-01', 50.00), (2, 2, 5, '2025-10-02', 0.00), (3, 3, 2, '2025-10-03', NULL),
(4, 4, 1, '2025-10-04', 20.00), (5, 5, 4, '2025-10-05', 15.00), (6, 6, 2, '2025-10-06', 0.00),
(7, 7, 1, '2025-10-07', 200.00), (8, 8, 10, '2025-10-08', NULL), (9, 9, 3, '2025-10-09', 30.00),
(10, 10, 2, '2025-10-10', 10.00), (11, 11, 5, '2025-10-11', 0.00), (12, 12, 3, '2025-10-12', 25.00),
(13, 13, 1, '2025-10-13', 0.00), (14, 14, 2, '2025-10-14', 50.00), (15, 15, 6, '2025-10-15', NULL),
(16, 1, 1, '2025-10-16', 0.00), (17, 3, 4, '2025-10-17', 30.00), (18, 5, 2, '2025-10-18', NULL),
(19, 7, 2, '2025-10-19', 150.00), (20, 8, NULL, '2025-10-20', 0.00), (21, 9, 1, '2025-10-21', NULL),
(22, 10, 3, '2025-10-22', 0.00), (23, 11, NULL, '2025-10-23', 20.00), (24, 12, 2, '2025-10-24', 0.00),
(25, 13, 1, '2025-10-25', 10.00), (26, 14, NULL, '2025-10-26', NULL), (27, 15, 5, '2025-10-27', 0.00),
(28, NULL, 2, '2025-10-28', 0.00), (29, 6, 1, '2025-10-29', 0.00), (30, 2, 4, '2025-10-30', 10.00);
"""


def main():
    logger = Logger()
    logger.setup_config()

    logger.display("--- 🚀 Iniciando Processo de Análise de Vendas (SQLite In-Memory) ---")

    try:
        # 1. Conexão e Setup (Etapa 1)
        db_manager = DBConnectionManager()

        db_manager.execute_setup_script(SQL_SCRIPT_FULL)

        # 2. Extração de Dados (Etapa 2 e 3 )
        df_raw = db_manager.fetch_unified_data()

        if df_raw.empty:
            logger.display(
                level=LogLevel.ERROR,
                message="❌ Processo interrompido: DataFrame vazio após extração.",
                exc_info=True
            )
            return

        # 3. Análise (Etapa 4, 5, 6 e 7 )
        # O arquivo 'analysis_service.py' deve ser criado e importado do diretório raiz
        import analysis_service
        analyzer = analysis_service.SalesAnalyzer(df=df_raw, logger=logger)

        df_clean = analyzer.clean_data()  # Etapa 4 (Limpeza)

        if df_clean.empty:
            logger.display(
                level=LogLevel.ERROR,
                message="❌ Processo interrompido: DataFrame vazio após limpeza.",
                exc_info=True
            )
            return

        totals = analyzer.generate_indicators()  # Etapa 5 (Indicadores)
        analyzer.generate_visualizations()  # Etapa 6 (Gráficos)
        analyzer.generate_conclusions(totals)  # Etapa 7 (Conclusões)

    except ValueError as e:
        logger.display(level=LogLevel.ERROR, message=f"FATAL: Erro de configuração ou conexão DB: {e}", exc_info=True)
    except Exception as e:
        logger.display(level=LogLevel.ERROR, message=f"Ocorreu um erro inesperado: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()