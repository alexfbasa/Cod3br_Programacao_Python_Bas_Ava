def nota_conceito(valor):
    nota = float(valor)
    if nota > 10:
        return 'Nota invalida'
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    else:
        return 'Nota invalida'


if __name__ == '__main__':
    is_on = True
    while is_on:
        get_nota = input('Insira a nota do aluno:')
        conceito = nota_conceito(get_nota)
        print(conceito)
        if conceito == 'A':
            print('Parabens, voce esta indo muito bem.')
        elif conceito == 'B':
            print('Voce tem um grande potencial.')
        should_continue= input("Deseja ver outra nota? (S)im, (N)ao: ").lower()
        if should_continue == 'sim':
            pass
        else:
            is_on = False
