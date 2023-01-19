# ISO-8859-1
from urllib import request

import pandas

SITE = r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv'


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando arquivo CSV.')
        dados = entrada.read().decode('latin-1')
        dados_formatados = pandas.read_csv(dados)
        print('Download completo.')
        print(dados_formatados['classe_ori'])


read(SITE)
