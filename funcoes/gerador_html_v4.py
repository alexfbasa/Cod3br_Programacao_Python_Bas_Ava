def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'spam' if inline else 'div'
    return f"<{tag} class='{classe}'>{conteudo}</{tag}>"


def tag_list(*itens):
    # new_list = [new_item for item in list_item]
    lista = ''.join(f"<li>{item}</li>" for item in itens)
    return f"<ul>{lista}</ul>"


if __name__ == '__main__':
    testando_packing = tag_bloco(tag_list('Maradona', 'Xuxa', 'Pele'), inline=True)
    print(testando_packing)
    testando_packing_v2 = tag_bloco(("<ul><li>Maradona</li><li>Xuxa</li><li>Pele</li></ul>"), inline=True)
    '''#tag_bloco(("<ul><li>Maradona</li><li>Xuxa</li><li>Pele</li></ul>"), inline=True)'''
    print(testando_packing_v2)

# print(tag_list('Alexandre', 'Marcio', 'Luiz'))
