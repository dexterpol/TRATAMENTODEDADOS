import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# Carregando os dados
nome_arquivo = 'CARTAO.xlsx'
df = pd.read_excel(nome_arquivo)

# Verificando se o modelo já existe
if os.path.exists('modelo_naive_bayes.pkl'):
    print('ELE EXISTE')
    naive_bayes = joblib.load('modelo_naive_bayes.pkl')
else:
    # Criar um novo modelo se não existir
    naive_bayes = MultinomialNB()

# Adicionar uma nova coluna "CATEGORIA" no DataFrame
df['CATEGORIA'] = ''

# Pré-processamento
X = df['LOJA'].fillna('')  # Usaremos o nome da loja, preenchendo valores nulos com uma string vazia
y = df['CATEGORIA']  # A categoria será adicionada manualmente

# Vetorização do texto (nome da loja)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X).toarray()

# Solicitar a entrada da categoria para cada loja
for i, nome_loja in enumerate(df['LOJA']):
    if nome_loja.lower() == 'total' or nome_loja == "TOTAL":
        break  # Parar se o nome for "total"
    categoria = input(f'Digite a categoria para a loja "{nome_loja}": ')
    df.at[i, 'CATEGORIA'] = categoria

# Treinamento do modelo Naive Bayes
naive_bayes.fit(X, y)

# Salvar o modelo em um arquivo após o treinamento
joblib.dump(naive_bayes, 'modelo_naive_bayes.pkl')

# Solicitar a entrada do nome da loja para fazer previsões
nome_loja = input("Digite o nome da loja: ")

# Vetorizar o nome da loja
nome_loja_vetorizado = vectorizer.transform([nome_loja]).toarray()

# Fazer a previsão da categoria
categoria_prevista = naive_bayes.predict(nome_loja_vetorizado)

print(f'A categoria prevista para a loja é: {categoria_prevista[0]}')
