# Versao basica
arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()
print(dados)

for registro in dados.splitlines():
    nome = registro.split(',')[0]
    idade = registro.split(',')[-1]

    print(f"O nome eh {nome}")
    print(f"A idade eh {idade}")

print(dados.strip().split(','))
