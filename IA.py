import pandas as pd
from db import Categoria, DBSession


nome_arquivo = 'CARTAO.xlsx'

df = pd.read_excel(nome_arquivo)
session = DBSession()

palavras_chave = {
    'posto': 'Posto de Combustível',
    'fruta': 'Comida',
    
}

for loja in df['LOJA']:
    print(f"Descrição da Loja: {loja}")
    categoria = ""

    loja = loja.lower()
    for palavra, cat in palavras_chave.items():
        if palavra in loja:
            categoria = cat
            break

    if not categoria:
        categoria = input("Digite a categoria para esta loja: ")

    
    nova_categoria = Categoria(nome=categoria)
    categoria_existente = session.query(Categoria).filter_by(nome=categoria).first()

    if not categoria_existente:
        session.add(nova_categoria)
        session.commit()
        print(f"Categoria '{categoria}' foi salva no banco de dados.")
    else:
        print(f"A categoria '{categoria}' já existe no banco de dados.")
