import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from enums.log_level_enum import LogLevel
from log.logger import Logger

# Definir a localização e estilo
plt.rcParams['figure.dpi'] = 100
sns.set_theme(style="whitegrid")


class SalesAnalyzer:
    """
    Responsabilidade: Tratar, analisar, calcular indicadores, gerar visualizações
    e elaborar conclusões (Etapas 4, 5, 6, 7).
    """

    def __init__(self, df: pd.DataFrame, logger: Logger):
        self.df_raw = df
        self.logger = logger
        self.df_clean = pd.DataFrame()
        pd.set_option('display.max_columns', None)

    # --- ETAPA 4: TRATAMENTO DE DADOS (CLEANING) ---
    def clean_data(self):
        """Trata valores nulos (NaN) e garante tipos de dados corretos (Etapa 4 )."""
        self.logger.display("🔄 Iniciando Etapa 4: Tratamento de Dados...")
        df_clean = self.df_raw.copy()
        linhas_iniciais = len(df_clean)

        df_clean['data_venda'] = pd.to_datetime(df_clean['data_venda'])
        df_clean.dropna(subset=['data_venda'], inplace=True)
        df_clean['dia_da_semana'] = df_clean['data_venda'].dt.day_name(locale='pt_BR')

        # 1. Tratamento de Nulos de Produto (Categoria e Preço)
        df_clean['categoria'] = df_clean['categoria'].fillna('Desconhecida')
        # Imputação do Preço Unitário: Média da Categoria
        media_por_categoria = df_clean.groupby(by='categoria')['preco_unitario'].transform('mean')
        df_clean['preco_unitario'] = df_clean['preco_unitario'].fillna(media_por_categoria)

        # 2. Remoção de Nulos Críticos (Vendas sem Produto ou Quantidade)
        df_clean.dropna(subset=['id_produto', 'quantidade'], inplace=True)

        # 3. Desconto: Nulo em desconto significa 0.0
        df_clean['desconto'] = df_clean['desconto'].fillna(0.0)

        # 4. Recálculo dos Valores Totais (importante após a imputação de preço)
        df_clean['faturamento_bruto'] = df_clean['preco_unitario'] * df_clean['quantidade']
        df_clean['valor_total'] = df_clean['faturamento_bruto'] - df_clean['desconto']

        # 5. Conversão de tipos finais
        df_clean['quantidade'] = df_clean['quantidade'].astype(int)
        df_clean['id_produto'] = df_clean['id_produto'].astype(int)

        self.logger.display(message=f"✅ Etapa 4 concluída. Linhas Removidas: {linhas_iniciais - len(df_clean)}")
        self.df_clean = df_clean
        return self.df_clean

    # --- ETAPA 5: ANÁLISES E INDICADORES ---
    def generate_indicators(self):
        """Calcula e exibe as métricas chave (Etapa 5 )."""
        self.logger.display(message="🔄 Iniciando Etapa 5: Análises e Indicadores...")

        if self.df_clean.empty:
            self.logger.display(
                level=LogLevel.ERROR,
                message="❌ DataFrame vazio. Execute clean_data() primeiro.",
                exc_info=True
            )
            return None

        # Métricas Globais
        total_sales_qty = self.df_clean['quantidade'].sum()
        total_revenue = self.df_clean['valor_total'].sum()
        total_discount = self.df_clean['desconto'].sum()
        total_gross_revenue = self.df_clean['faturamento_bruto'].sum()

        # Tabela 1: Faturamento por Categoria
        df_category_revenue = self.df_clean.groupby(by='categoria').agg(
            faturamento_total=('valor_total', 'sum'),
            contagem_vendas=('id_venda', 'count'),
        ).reset_index()
        df_category_revenue['ticket_medio'] = df_category_revenue['faturamento_total'] / df_category_revenue[
            'contagem_vendas']
        self.df_category_revenue = df_category_revenue.sort_values(by='faturamento_total', ascending=False)

        # Tabela 2: Top 5 Produtos por Faturamento
        self.df_top_products = self.df_clean.groupby(by='nome_produto')['valor_total'].sum().reset_index()
        self.df_top_products = self.df_top_products.sort_values(by='valor_total', ascending=False).head(5)

        # Tabela 3: Vendas por Data
        self.df_sales_by_day = self.df_clean.groupby('data_venda').agg(
            faturamento=('valor_total', 'sum')
        ).reset_index().sort_values(by='faturamento', ascending=False)

        print("\n--- 📈 Resultados da Análise (Etapa 5) ---")
        print(f"* Faturamento Total (Líquido): R$ {total_revenue:,.2f}")
        print(f"* Faturamento Bruto: R$ {total_gross_revenue:,.2f}")
        print(f"* Desconto Total Concedido: R$ {total_discount:,.2f}")
        print(f"* Quantidade Total de Itens Vendidos: {total_sales_qty}")

        print("\n** Tabela 1: Faturamento e Ticket Médio por Categoria:**")
        print(self.df_category_revenue.to_markdown(index=False, floatfmt=".2f"))

        print("\n** Tabela 2: Top 5 Produtos por Faturamento:**")
        print(self.df_top_products.to_markdown(index=False, floatfmt=".2f"))

        print("\n** Tabela 3: Top 3 Dias com Maior Faturamento:**")
        print(self.df_sales_by_day.head(3).to_markdown(index=False, floatfmt=".2f"))

        self.logger.display(message="✅ Etapa 5 concluída.")
        return total_revenue, total_gross_revenue, total_discount

    # --- ETAPA 6: VISUALIZAÇÕES ---
    def generate_visualizations(self):
        """Gera os gráficos de análise (Etapa 6 )."""
        self.logger.display(message="🔄 Iniciando Etapa 6: Visualizações...")

        # 1. Gráfico de Barras: Faturamento por Categoria
        plt.figure(figsize=(10, 6))
        sns.barplot(
            x='faturamento_total',
            y='categoria',
            data=self.df_category_revenue,
            palette='viridis'
        )
        plt.title(label='1. Faturamento Total Líquido por Categoria')
        plt.xlabel(xlabel='Faturamento Total (R$)')
        plt.ylabel(ylabel='Categoria')
        plt.tight_layout()
        plt.show()

        # 2. Gráfico de Linha: Evolução do Faturamento por Data
        plt.figure(figsize=(12, 6))
        df_sales_by_day_sorted = self.df_sales_by_day.sort_values('data_venda')
        sns.lineplot(
            x='data_venda',
            y='faturamento',
            data=df_sales_by_day_sorted,
            marker='o',
            color='blue'
        )
        plt.title(label='2. Evolução Diária do Faturamento (Líquido)')
        plt.xlabel(xlabel='Data da Venda')
        plt.ylabel(ylabel='Faturamento (R$)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        self.logger.display("✅ Etapa 6 concluída.")

    # --- ETAPA 7: CONCLUSÕES ---
    def generate_conclusions(self, totals):
        """Elabora as conclusões finais (Etapa 7 )."""
        total_revenue, total_gross_revenue, total_discount = totals
        lider_cat = self.df_category_revenue.iloc[0]
        lider_dia = self.df_sales_by_day.iloc[0]

        print("\n--- 💡 Conclusões Finais (Etapa 7) ---")
        print(f"""
        **Relatório de Análise de Vendas (Outubro/2025)**

        **Resultados Financeiros:**
        * Faturamento Bruto: R$ {total_gross_revenue:,.2f}
        * Faturamento Líquido: **R$ {total_revenue:,.2f}**
        * Desconto Concedido: R$ {total_discount:,.2f}

        **1. Destaque por Categoria:**
        * A categoria **'{lider_cat['categoria']}'** é a líder absoluta, com o maior Faturamento Total e um Ticket Médio de R$ {lider_cat['ticket_medio']:,.2f}.

        **2. Performance Temporal:**
        * O pico de vendas (faturamento) foi registrado no dia **{lider_dia['data_venda'].strftime('%d/%m/%Y')}**.

        **3. Impacto do Desconto:**
        * O desconto total de R$ {total_discount:,.2f} foi concedido, o que deve ser monitorado para garantir margens saudáveis.
        """)
        self.logger.display(message="✅ Etapa 7 concluída: Conclusões elaboradas.")