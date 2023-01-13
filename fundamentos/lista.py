# Pode ser modificada, heterogenea
lista = []
type(lista)
dir(lista)
# help(list)
len(lista)
lista.append(1)
lista.append(5)
print(lista)
print(len(lista))

nova_lista = [1, 5, 'Ana', 'Bia']
print(nova_lista)
nova_lista.remove(5)
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

# %%
#        0  1      2          3       4 ou -1
lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista.index('Guilherme'))
# lista.index(42)
print(lista[2])
print(1 in lista)
print(f"{'Rebeca' in lista} Sim - Rebeca esta na lista")
print(f"{'Pedro' not in lista} Sim - Pedro nao esta na lista")
print(f"{lista[0]} primeiro elemento na lista")
print(f"{lista[4]} quarto elemento na lista")
# lista[5]
print(lista[-1])
print(lista[-5])

# %%
lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[1:3])
print(f"{lista[1:-1]} Vai do 1 ate -1, mas nao mostra o -1")
print(lista[1:])
print(f"{lista[:-1]} vai do zero ateh 0 -1 sem incluir o -1")
print(f"{lista[:]}")
print(lista[::2])
print(lista[::-1])
del lista[2]
print(lista)
del lista[1:]
print(lista)
