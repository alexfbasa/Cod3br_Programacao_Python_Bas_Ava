def tabuada(numero_multiplicar):
    for i in range(1, 11):
        print(f"{i}*{numero_multiplicar} = {i * numero_multiplicar}")


if __name__ == '__main__':
    for num in range(1, 11):
        tabuada(num)
