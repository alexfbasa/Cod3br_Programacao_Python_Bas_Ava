def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'spam' if inline else 'div'
    return f"<{tag} class='{classe}'>{conteudo}</{tag}>"


def tag_list(*itens):
    lista = ''.join(f"<li>{item}</li>" for item in itens)
    return f"<ul>{lista}</ul>"



if __name__ == '__main__':
    testando_packing = tag_bloco(tag_list('Maradona', 'Xuxa', 'Pele'), inline=True)
    print(testando_packing)

print(tag_list('Alexandre', 'Marcio', 'Luiz'))
