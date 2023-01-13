# while True:
#     print('Vai demorar muitooooo')

from random import randint

numero_informado = -1  # Iniciado com -1 pq o rando nao ira negativo, poderia ser 11
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    # Modifica o status da variavel numero_informado, ateh que seja True
    numero_informado = int(input('Informe o número: '))

print('Número secreto {} foi encontrado!'.format(numero_secreto))
