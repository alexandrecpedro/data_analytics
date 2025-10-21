# KNOWLEDGE CONSOLIDATION - ASSESSMENT

## QUESTION 1

Para salvar um DataFrame chamado 'selecao' em um arquivo chamado 'export.csv', sem incluir a coluna de índice e 
usando ponto e vírgula como separador, qual comando é o correto?

- ❌ selecao.to_csv('export.csv', index=None, delimiter=',')
- ❌ selecao.write_csv('export.csv', index=False, sep=';')
- ✅ selecao.to_csv('export.csv', index=False, sep=';')
- ❌ selecao.save_csv('export.csv', no_index=True, separator=';')

## QUESTION 2

No início do projeto, qual comando é utilizado para importar a biblioteca pandas com o alias 'pd', que é uma 
convenção comum?

- ✅ import pandas as pd
- ❌ load library pandas as pd
- ❌ import pd from pandas
- ❌ require('pandas').as('pd')

## QUESTION 3

Qual é a sintaxe correta para selecionar apenas as colunas 'modelo' e 'montadora' de um DataFrame chamado 'dados'?

- ❌ dados.select('modelo' , 'montadora')
- ❌ dados['modelo', 'montadora']
- ✅ dados[['modelo', 'montadora']]
- ❌ dados.select('modelo' e 'montadora')

## QUESTION 4

Qual função do pandas é usada para ler dados de um arquivo CSV a partir de uma URL ou de um caminho local 
e carregá-los em um DataFrame?

- ✅ pd.read_csv()
- ❌ pd.get_csv()
- ❌ pd.open_csv()
- ❌ pd.load_csv()

## QUESTION 5

Como você filtraria o DataFrame 'dados' para mostrar apenas os carros onde o 'ano_fabricacao' é maior que 2020, 
usando o método `.query()`?

- ✅ dados.query('ano_fabricacao > 2020')
- ❌ dados.filter(ano_fabricacao > 2020)
- ❌ dados.where('ano_fabricacao > 2020')
- ❌ dados.query(dados['ano_fabricacao'] > 2020)

## QUESTION 6

Para obter a frequência de cada montadora como um percentual do total, qual método e parâmetro devem ser usados 
na coluna 'montadora'?

- ✅ .value_counts(normalize=True)
- ❌ .value_counts(percentage=True)
- ❌ .count(percentage=True)
- ❌ .unique(normalize=True)

## QUESTION 7

Qual método fornece um resumo conciso de um DataFrame, incluindo o tipo de dados de cada coluna e 
o número de valores não nulos?

- ❌ .shape()
- ❌ .columns()
- ✅ .info()
- ❌ .describe()

## QUESTION 8

Para calcular o valor médio de mercado ('valor_mercado') agrupado por cada fabricante ('montadora'), 
qual é a sintaxe correta?

- ❌ dados.group('montadora').mean()
- ✅ dados.groupby('montadora')['valor_mercado'].mean()
- ❌ dados.mean('valor_mercado').by('montadora')
- ❌ dados.select('montadora', 'valor_mercado').mean()

## QUESTION 9

Qual método fornece um resumo conciso de um DataFrame, incluindo o tipo de dados de cada coluna e 
o número de valores não nulos?

- ❌ Primeiro `dados.sum_nulls()` e depois `dados.fill(0)`
- ❌ Primeiro `dados.fillna(0)` e depois `dados.isnull().sum()`
- ✅ Primeiro `dados.isnull().sum()` e depois `dados = dados.fillna(0)`
- ❌ Primeiro `dados.hasnull()` e depois `dados.replace(null, 0)`

## QUESTION 10

Para inspecionar rapidamente as primeiras e as últimas linhas de um DataFrame chamado 'dados', 
quais são os dois métodos corretos a serem utilizados?

- ✅ .head() e .tail()
- ❌ .first() e .last()
- ❌ .start() e .end()
- ❌ .top() e .bottom()