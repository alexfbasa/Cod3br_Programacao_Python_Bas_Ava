# ISO-8859-1
from urllib import request

import pandas

SITE = r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv'

with request.urlopen(SITE) as entrada:
    print('Baixando arquivo CSV.')
    dados = entrada.read().decode('latin-1')
    dados_formatados = pandas.read_csv(dados)
    print('Download completo.')
    origem = dados_formatados[dados_formatados['classe_ori'] == 'Centro']
    print(origem)

