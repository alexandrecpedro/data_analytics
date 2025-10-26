# KNOWLEDGE CONSOLIDATION - ASSESSMENT

## QUESTION 1

Você tem um DataFrame agregado chamado 'aprovados_curso'contendo nomes de cursos em uma coluna 'Curso' 
e contagens numa coluna 'Aprovado'. 
Como você cria um gráfico de pizza onde as fatias são rotuladas como nomes reais dos cursos?

- ✅ aprovados_curso.plot(kind='pie', y='Aprovado',labels=aprovados_curso['Curso'])
- ❌ aprovados_curso.plot(kind='pie', y='Aprovado',index='Curso')
- ❌ aprovados_curso.set_index('Curso').plot(kind='pie',y='Aprovado')
- ❌ aprovados_curso.plot(kind='pie', y='Aprovado',legend='Curso')

## QUESTION 2

Qual é a maneira mais direta de criar um gráfico de barras mostrando o número de alunos por curso usando a 
funcionalidade de plotagem integrada no Pandas?

- ❌ plt.bar(df['Curso'].unique(),df['Curso'].value_counts())
- ❌ df.groupby('Curso').plot(kind='bar')
- ✅ df['Curso'].value_counts().plot(kind='bar')
- ❌ df['Curso'].plot(kind='bar')

## QUESTION 3

Qual linha de código cria corretamente uma nova coluna booleana 'Aprovado' que é 'True' somente se 
'Nota' for pelo menos 7 e 'Presenca' for pelo menos 7,5?

- ❌ df['Aprovado']= (df['Nota'] >= 7) and (df['Presenca'] >= 7.5)
- ❌ df['Aprovado']= df.where((df['Nota'] >= 7) & (df['Presenca'] >= 7.5))
- ✅ df['Aprovado']= (df['Nota'] >= 7) & (df['Presenca'] >= 7.5)
- ❌ df.loc[(df['Nota']>= 7) & (df['Presenca'] >= 7.5), 'Aprovado'] = True

## QUESTION 4

Para remover permanentemente uma coluna chamada 'Projetos' de um DataFrame chamado 'df', qual comando está correto?

- ✅ df.drop('Projetos',axis=1, inplace=True)
- ❌ df.drop('Projetos',axis=0, inplace=True)
- ❌ new_df =df.drop('Projetos', axis=1)
- ❌ df.remove('Projetos', axis=1)

## QUESTION 5

Após usar 'groupby('Curso')', a coluna 'Curso' se torna o índice. Qual método é usado para converter esse índice 
de volta numa coluna padrão?

- ❌ .unstack()
- ❌ .reindex()
- ✅ .reset_index()
- ❌ .set_index()

## QUESTION 6

Se você tiver uma função Python 'classificacao(nota)' que retorna uma ‘string’ de categoria de desempenho, 
como criar uma coluna 'Desempenho' aplicando essa função a cada valor na coluna 'Nota'?

- ❌ df['Desempenho'] = df.apply(classificacao, column='Nota')
- ❌ df['Desempenho'] = df['Nota'].map(classificacao)
- ✅ df['Desempenho'] = df['Nota'].apply(classificacao)
- ❌ df['Desempenho'] = classificacao (df['Nota'])

## QUESTION 7


Ao carregar um arquivo CSV com o Pandas usando 'pd.read_csv()', qual parâmetro deve ser usado para analisar 
corretamente os dados em que as colunas são separadas por ponto e vírgula?

- ❌ separator=”;”
- ✅ sep=”;”
- ❌ delimiter=”;”
- ❌ col_sep=”;”

## QUESTION 8

Ao criar um gráfico de pizza com a função de plotagem do Matplotlib, qual parâmetro é usado para controlar 
o formato dos rótulos de porcentagem em cada fatia?

- ❌ pct_format
- ❌ legend
- ✅ autopct
- ❌ labels

## QUESTION 9

Para gerar um gráfico de linha de 'Nota' apenas para o curso 'Excel' de um DataFrame 'df', qual é a sintaxe correta?

- ❌ df.query('Curso== Excel').plot(kind='line', y='Nota')
- ❌ df.groupby('Curso')['Excel'].plot(kind='line',y='Nota')
- ✅ df[df['Curso']== 'Excel'].plot(kind='line', y='Nota')
- ❌ df.plot(kind='line',where='Curso'=='Excel', y='Nota')