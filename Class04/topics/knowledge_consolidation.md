# KNOWLEDGE CONSOLIDATION - ASSESSMENT

## QUESTION 1

Em um exercício para encontrar o preço de um produto em um dicionário chamado precos, 
qual é a forma correta de verificar se uma variável produto existe como chave antes de imprimir seu valor?

- ❌ if precos.keys(produto):
- ❌ if precos[produto]:
- ✅ if produto in precos:
- ❌ if produto in precos.values():

## QUESTION 2

Qual é a principal diferença entre os métodos de lista .append() e .insert()?

- ❌ .insert() substitui um item existente, enquanto .append() adiciona um novo item.
- ❌ .append() só pode adicionar um item por vez, enquanto .insert() pode adicionar vários.
- ✅ .append() adiciona um item no final da lista, enquanto .insert() adiciona em uma posição específica
- ❌ .append() é usado para listas de números e .insert() para listas de strings.

## QUESTION 3

Considere a tupla `dados = (10, 'SP', ['Rio', 'Bahia'])`. Qual das seguintes operações é VÁLIDA?

- ❌ dados[0] = 20
- ❌ dados.append['Novo Item]
- ✅ dados[2].append['Pernambuco']
- ❌ dados[1] = "RJ"

## QUESTION 4

Qual será o resultado do fatiamento (slice) na lista anos = [2001, 2002, 2004, 2010, 2050] usando o comando print(anos[1:4])?

- ✅ [2002,2004,2010]
- ❌ [2001,2002,2004]
- ❌ '2002,2004,2010'
- ❌ [2002,2004,2010,2050]

## QUESTION 5

Dado o código linha = ['Ivan', [1970, 1994, 2002], 'Fábio'], como você acessaria o ano de 1994?

- ✅ linha[1][1]
- ❌ linha[2][1]
- ❌ linha[1]
- ❌ linha[1,1]

## QUESTION 6

Considere a lista `dados = [100, 200, 300, 400]`. Qual comando acessa o penúltimo elemento da lista (o valor 300)?

- ❌ dados[300]
- ✅ dados[-2]
- ✅ dados[2]
- ❌ dados[-1]

## QUESTION 7

Qual é a principal característica que diferencia uma tupla de uma lista em Python?

- ❌ Tuplas só podem armazenar números, enquanto listas podem armazenar qualquer tipo de dado
- ❌ O acesso aos elementos de uma tupla é mais lento do que em uma lista.
- ✅ Uma tupla é imutável, enquanto uma lista é mutável.
- ❌ Tuplas são definidas por colchetes [ ] e listas por parênteses ( )

## QUESTION 8

Qual comando inverte a ordem de uma lista numeros = [1, 2, 3, 4] resultando em [4, 3, 2, 1]?

- ✅ sorted(numeros,reverse=True)
- ❌ numeros[-1]
- ✅ numeros.reverse()
- ✅ numeros[::-1]

## QUESTION 9

O que acontece se você tentar adicionar uma chave que já existe em um dicionário?

- ❌ A nova atribuição é ignorada e o valor original é mantido.
- ❌ A nova chave e valor são adicionados, e o dicionário fica com duas chaves iguais.
- ✅ O valor associado à chave existente é substituído pelo novo valor.
- ❌ O Python gera um erro de 'chave duplicada'.

## QUESTION 10

No Python básico, sem usar bibliotecas externas, qual é a maneira correta de calcular a média de uma lista numérica chamada numeros?

- ❌ average(numeros)
- ❌ mean(numeros)
- ✅ sum(numeros) / len(numeros)
- ❌ numeros.media()

## QUESTION 11

Qual comando usa o método split para transformar a string `registro = 001;Silvio Santos;1250` em uma lista de três elementos?

- ❌ registro.split(',')
- ✅ registro.split(';')
- ❌ registro.slice(';')
- ❌ split(registro,';')

## QUESTION 12

Se você precisa usar apenas a função `randint` de um módulo chamado `random`, qual é a forma de importação mais direta que permite chamar a função sem o prefixo do módulo?

- ❌ import randint from random
- ❌ import random.randint
- ✅ from random inport randint
- ❌ import random