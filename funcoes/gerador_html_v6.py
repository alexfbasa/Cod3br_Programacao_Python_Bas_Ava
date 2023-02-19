# Tag bloco e tag list vão receber uma série de parametro nomeados 'chave': 'valor'
def get_atrs(atrs_informados):
    # bloco_access_key= bloco_id= ul_id =
    return ' '.join(f'{k.split("_")[-1]}="{v}"' for k, v in atrs_informados.items())


def tag_bloco(conteudo, *args, classe='success', inline=False, **kwargs):
    tag = 'spam' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **kwargs)
    atributos = get_atrs(kwargs)
    # Vamos passar uma lista de parametros na tag
    return f"<{tag} {atributos}class='{classe}'>{html}</{tag}>"
    

def tag_list(*itens, **kwargs):
    # new_list = [new_item for item in list_item]
    lista = ''.join(f"<li>{item}</li>" for item in itens)
    # Vamos trabalhar nas tag ul
    return f"<ul {get_atrs(kwargs)}> {lista}</ul>"


if __name__ == '__main__':
    print(tag_bloco(tag_list, 'Sem_parenteses', 'callable', 'ainda_posicional', 'outro_posicional',
                    classe='Fim_posicional', bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))
