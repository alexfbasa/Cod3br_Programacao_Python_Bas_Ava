# Versão com comprehension
# [ expressão for item in list ] e pode ter um if
dobros = [i * 2 for i in range(10)]
print(dobros)

# Versão normal
dobrado = []

for i in range(10):
    dobrado.append(i * 2)

print(dobrado)