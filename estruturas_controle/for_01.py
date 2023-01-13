def repet_to_end(number_final):
    for i in range(1, number_final):
        print(f"Eu vou imprimir ate o numero {number_final}, comecando por {i}")
        if i >= 30:
            print('Estou ficando cansado de imprimir a mesma coisa')
        else:
            print('Ainda ta legal imprimir. :) ')


if __name__ == '__main__':
    get_numero = int(input('Insira o numero final: '))
    repet_to_end(get_numero)
