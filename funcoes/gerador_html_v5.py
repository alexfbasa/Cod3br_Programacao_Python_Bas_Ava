def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'spam' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f"<{tag} class='{classe}'>{html}</{tag}>"


def tag_list(*itens):
    # new_list = [new_item for item in list_item]
    lista = ''.join(f"<li>{item}</li>" for item in itens)
    return f"<ul>{lista}</ul>"


if __name__ == '__main__':
    testando_packing = tag_bloco(tag_list('Maradona', 'Xuxa', 'Pele'), inline=True)
    print(testando_packing)
    # O conteudo vem da tag_lista
    print(tag_bloco(tag_list('Alexandre', 'Sarlete', 'Andrea')), False)
    print(tag_bloco(tag_list('Alexandre', 'Sarlete', 'Andrea'), classe='info'), False)
