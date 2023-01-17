# Versão com comprehension
# [ expressão for item in list ] e pode ter um if
dobros = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dobros)

# Versão normal
dobrado = {}

for i in range(10):
    if i % 2 == 0:
        dobrado['Numero'] = i

for i in dobrado:
    print(dobrado[i])
