def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade.'
    elif idade in range(18, 64):
        return 'Adulto.'
    elif idade in range(65, 100):
        return 'Melhor idade.'
    elif idade >= 100:
        return 'Centenario.'
    else:
        return 'Idade Invalida'


if __name__ == '__main__':
    get_idade = int(input('Quantos anos voce tem? '))
    get_faixa_etaria = faixa_etaria(get_idade)
    print(get_faixa_etaria)
    idades = [17, 35, 87, 113, -2]
    for i in idades:
        idade_indice = faixa_etaria(i) # Otimizado, nao sera usado
        print(f"A idade de {i} eh considerada {faixa_etaria(i)} ")
