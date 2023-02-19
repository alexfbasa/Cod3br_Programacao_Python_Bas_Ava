def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'spam' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f"<{tag} class='{classe}'>{html}</{tag}>"


def tag_list(*itens):
    lista = ''.join(f"<li>{item}</li>" for item in itens)
    return f"<ul>{lista}</ul>"


if __name__ == '__main__':
    # tag_bloco + um callable tag_lista
    print(tag_bloco(tag_list, 'Item01', 'Item02', classe='Info'))
    print(tag_bloco(tag_list('Item01', 'Item02'), classe='Warn'))
