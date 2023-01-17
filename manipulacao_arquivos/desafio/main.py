# ISO-8859-1
import csv
from urllib import request

SITE = r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv'


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando arquivo CSV.')
        dados = entrada.read().decode('latin-1')
        print('Download completo.')
        for linha in csv.reader(dados.splitlines()):
            print(f"{linha[8]}: {linha[3]}")


read(SITE)
