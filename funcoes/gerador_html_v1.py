def tag_bloco(texto, classe='success'):
    return f"<div class='{classe}'>{texto}</div>"



if __name__ == '__main__':
    primeiro_commit = tag_bloco('Alexandre', 'deu_bom')
    print(primeiro_commit)
    assert tag_bloco('Alexandre') == "<div class='success'>Alexandre</div>"
