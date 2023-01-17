def tag_bloco(texto, classe='success', inline=False):
    tag = 'spam' if inline else 'div'
    return f"<{tag} class='{classe}'>{texto}</{tag}>"


if __name__ == '__main__':
    segundo_commit = tag_bloco('Kuene-nagel', inline=True)
    print(segundo_commit)
    terceiro_commit = tag_bloco('Kuene-nagel', inline=False)
    print(terceiro_commit)
    quarto_commit = tag_bloco('Testando', classe='error', inline=True)
    print(quarto_commit)
