PALAVRAS_PROIBIDAS = ["futebol", "religiao", "politica"]

textos = ["Joao gosta de futebol e politica.",
          "A praia foi divertida."]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f"Esse texto nao eh permitido - pavra probida {palavra} encontrada")
            found = True
            break
        # if not found:
        #     print(f"Texto autorizado {texto}")
        else:
            print(f"Texto autorizado {texto}")
