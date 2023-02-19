def podium(**kwargs):
    for posicao, piloto in kwargs.items():
        print(f'{posicao} --> {piloto}')


podium(primeiro='Alexandre',
       segundo='Sarlete',
       terceiro='Andrea')
