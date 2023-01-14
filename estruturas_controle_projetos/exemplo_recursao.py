def imprimir(maximo, inicial):
    # condição de parada!
    if inicial < maximo:
        print(inicial)
        # Chama si mesma
        imprimir(maximo, inicial + 10)


# imprimir(20, 1)
imprimir(200, 10)
