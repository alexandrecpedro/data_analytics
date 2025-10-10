FILEPATH_1 = 'assets/arquivo.txt'
FILEPATH_2 = 'assets/arquivo2.txt'

with open(FILEPATH_2, 'r', encoding='utf-8') as arq2:
  with open(FILEPATH_1, 'a', encoding='utf-8') as arq:
    for linha in arq2:
       arq.write(linha)