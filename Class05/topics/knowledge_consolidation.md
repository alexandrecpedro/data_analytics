# KNOWLEDGE CONSOLIDATION - ASSESSMENT

## QUESTION 1

Para documentar uma função em Python, fornecendo descrições sobre seus parâmetros e o que ela faz, 
qual é a convenção utilizada?

- ❌ Usar a função `print()` dentro da função para exibir a documentação quando ela for chamada
- ❌ Declarar variáveis no início da função com nomes descritivos como 'descricao_parametro_1'
- ❌ Usar comentários de linha única com '#' antes de cada linha de descrição
- ✅ Colocar aspas duplas triplas (""") ou aspas simples triplas (''') logo após a linha de definição da função

## QUESTION 2

No contexto de tratamento de exceções em Python, qual bloco de código é utilizado para envolver uma operação que pode 
potencialmente causar um erro?

- ❌ if error
- ✅ try
- ❌ finnaly
- ❌ on error

## QUESTION 3

No exemplo de cálculo de juros compostos, a função `calculo` recebe capital, taxa e meses e depois utiliza a 
instrução `return`. Qual é a finalidade principal do `return` nesse contexto?

- ✅ Encerrar a execução da função e enviar o valor calculado de volta para onde a função foi chamada
- ❌ Armazenar o resultado do cálculo em uma variável global
- ❌ Imprimir o resultado do cálculo diretamente no terminal.
- ❌ Verificar se o cálculo foi executado com sucesso, retornando `True` ou `False`

## QUESTION 4

Um desenvolvedor precisa adicionar registros a um arquivo de log. Se o arquivo não existir, ele deve ser criado. 
Se já existir, os novos registros devem ser adicionados ao final, sem apagar os anteriores. Qual modo de abertura 
de arquivo é o mais apropriado?

- ❌ w+
- ✅ a
- ❌ r+
- ❌ w

## QUESTION 5

Em Python, qual é a consequência de abrir um arquivo existente que já contém dados, utilizando o modo de abertura 
'w' (write)?

- ✅ O conteúdo existente no arquivo é completamente apagado antes que qualquer nova escrita ocorra.
- ❌ O novo conteúdo é adicionado ao final do arquivo, preservando os dados existentes.
- ❌ O conteúdo do arquivo é lido para a memória e depois sobrescrito, permitindo uma operação de leitura e escrita.
- ❌ O programa gera um erro, pois o modo 'w' só pode ser usado para criar novos arquivos.

## QUESTION 6

Qual é a sintaxe correta para definir uma função em Python que pode aceitar um número variável de argumentos 
posicionais?

- ❌ def minha_funcao(list args):
- ✅ def minha_funcao(*args):
- ❌ def minha_funcao(args[]):
- ❌ def minha_funcao(**kwargs):

## QUESTION 7

Ao ler um arquivo de texto linha por linha com um laço "for", as linhas frequentemente incluem caracteres de nova linha 
("\n") no final. Qual método de string é mais específico para remover apenas os espaços em branco (incluindo "\n") 
do final da string?

- ✅ rstrip()
- ❌ strip()
- ❌ lstrip()
- ❌ remove('\n')

## QUESTION 8

Na definição de uma função em Python, qual é o propósito da sintaxe `parametro: int`?

- ✅ Fornece uma 'dica de tipo' (type hint) indicando que o parâmetro 'parametro' deve ser um inteiro.
- ❌ Converte automaticamente qualquer valor passado para o parâmetro em um número inteiro
- ❌ Gera um erro se um valor que não seja um inteiro for passado para o parâmetro
- ❌ É uma forma de comentário que o interpretador Python ignora completamente

## QUESTION 9

Se você precisa abrir um arquivo de imagem (como um .png) para ler seu conteúdo bruto em bytes, qual combinação de 
modo de abertura você deve usar?

- ❌ r
- ❌ b
- ✅ rb
- ❌ rt

## QUESTION 10

Qual função da biblioteca 'os' é comumente usada para verificar se um arquivo já existe em um determinado caminho antes 
de tentar abri-lo?

- ❌ os.find(caminho)
- ❌ os.path.isfile(caminho)
- ✅ os.path.exists(caminho)
- ❌ os.path.open(caminho)