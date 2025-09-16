# PRESCRIPTIVE ANALYTICS

## 1. INTRODUCTION

A análise prescritiva vai além da previsão e recomenda a melhor ação a ser tomada 
Responde à pergunta: `O que devemos fazer?` combinando insights de todos os outros tipos de análise

### 1.1. CARACTERÍSTICAS PRINCIPAIS

- Combina dados, algoritmos e regras de negócio
- Fornece recomendações específicas de ação
- Utiliza inteligência artificial e otimização matemática
- Maior complexidade e valor estratégico

### 1.2. FERRAMENTAS RECOMENDADAS

- Python (Pulp, Gurobi), R (OptimR), MATLAB
- IBM Decision Optimization, SAS, Oracle Advanced Analytics

### 1.3. MÉTODOS UTILIZADOS

- Modelos matemáticos para otimização de processos
- Simulações para prever impactos de decisões
- Inteligência artificial para sugerir estratégias de negócio
- Algoritmos de otimização multiobjetivo

### 1.4. QUANDO USAR

- Otimização de rotas de entrega para reduzir custos logísticos
- Precificação dinâmica baseada em demanda e concorrência
- Alocação otimizada de orçamento de marketing entre canais
- Gestão automatizada de inventário

## 2. CASOS DE USO - EXEMPLOS

### 2.1. EXEMPLO 1 - CADEIA DE SUPRIMENTOS E REDUÇÃO DE CUSTOS OPERACIONAIS

Análise na cadeia de suprimentos para determinar as melhores rotas de entrega, horários de abastecimento e níveis de
estoque para reduzir custos operacionais

### 2.2. EXEMPLO 2 - OTIMIZAÇÃO DE MIX DE PRODUTOS

Foco: Otimizar mix de produtos baseado em perfil demográfico local, sazonalidade e histórico de vendas
Passos para resolução:

#### 2.2.1. COLETA E INTEGRAÇÃO DE DADOS

(1) Fontes principais

- Histórico de vendas (ERP, PDV, e-commerce)
- Perfil demográfico (IBGE, geolocalização, cadastro de clientes)
- Sazonalidade (datas comemorativas, clima, ciclos de doenças)

(2) Exemplo

Extrair vendas dos últimos 3 anos, vincular com idade/gênero/bairro dos clientes e mapear períodos de pico
(ex.: aumento de antigripais no inverno)

#### 2.2.2. ANÁLISE DIAGNÓSTICA

Descobrir por que certos produtos vendem mais/menos:
    
- Promoções influenciam picos?
- Estoque insuficiente em certas épocas?
- Concorrência local? 

#### 2.2.3. ANÁLISE EXPLORATÓRIA (EDA)

Identificar padrões básicos:
- Produtos mais vendidos por região/faixa etária
- Correlação entre doenças (ex.: clientes com diabetes compram também medicamentos para hipertensão)
- Tendências sazonais (ex.: aumento de repelentes no verão)

Ferramentas:
- Pandas
- SQL
- Power BI
- Tableau

#### 2.2.4. MODELAGEM PREDITIVA

Usar `Machine Learning/Estatística` para prever demanda futura:

- *Entradas*:
    - Histórico de vendas + perfil local + sazonalidade

- *Saída*:
    - Previsão de vendas por produto/região/período

#### 2.2.5. ANÁLISE PRESCRITIVA (OTIMIZAÇÃO DO MIX)

(1) Após prever a demanda, aplicar `otimização` para decidir:

- Quais produtos manter em estoque
- Em que quantidade comprar
- Como alocar em diferentes lojas/regiões

(2) Técnicas

- Programação Linear (ex.: PuLP, ortools)
- Algoritmos de otimização multiobjetivo (maximizar lucro + minimizar falta de estoque)

#### 2.2.6. IMPLEMENTAÇÃO E MONITORAMENTO

(1) Criar `dashboards dinâmicos` (Power BI, Tableau ou Streamlit) com:

- Mix ideal por região
- Alertas de estoque crítico
- Previsões de vendas futuras

(2) Rodar a análise periodicamente (ex.: mensal)

----
```plaintext
Resumindo...

- Coleta: histórico de vendas de metformina e losartana em determinada região

- EDA: identificar que 60% dos clientes que compram metformina também compram 
    medicamentos de pressão
    
- Previsão: prever demanda de ambos os medicamentos no próximo trimestre 
    (considerando sazonalidade e perfil etário)

- Otimização: definir estoque mínimo de cada produto para atender à correlação 
    de compras
```

## 3. BIBLIOGRAPHICAL REFERENCES

- [01] [What is Prescriptive Analytics?](https://www.qlik.com/us/augmented-analytics/prescriptive-analytics#:~:text=Prescriptive%20analytics%20is%20the%20use,%E2%80%9CWhat%20should%20we%20do%3F%E2%80%9D)
- [02] [What Is Prescriptive Analytics? 6 Examples](https://online.hbs.edu/blog/post/prescriptive-analytics)
- [03] [What is Prescriptive Analytics in Data Science?](https://www.geeksforgeeks.org/data-science/what-is-prescriptive-analytics-in-data-science/)
- [04] [O que é análise de dados prescritiva?](https://www.ibm.com/br-pt/think/topics/prescriptive-analytics)