# Recebe sequencia com valor padrao definido
def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante: Condição de parada
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 20 primeiros números da sequência
    # Recebeu so quantidade com input, sequencia ja esta padrao
    for fib in fibonacci(20):
        print(fib)