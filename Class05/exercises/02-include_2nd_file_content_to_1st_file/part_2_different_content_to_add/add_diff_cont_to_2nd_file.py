FILEPATH_1 = 'assets/arquivo.txt'
FILEPATH_2 = 'assets/arquivo2.txt'

with open(FILEPATH_1, 'r', encoding='utf-8') as arq:
    set1 = set(linha.strip() for linha in arq)
with open(FILEPATH_2, 'r', encoding='utf-8') as arq2:
    set2 = set(linha.strip() for linha in arq2)

novas = set2 - set1
print(novas)

if novas:
    with open('arquivo.txt', 'a', encoding='utf-8') as arq:
        for linha in novas:
            arq.write('\n' + linha)