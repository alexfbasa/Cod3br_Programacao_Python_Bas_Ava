with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            print(f"{registro}", file=saida)

# Fecha automaticamente
