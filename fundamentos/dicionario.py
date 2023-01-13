
pessoa = {'nome': 'Prof(a). Ana', 'idade': 38,
          'cursos': ['Inglês', 'Português']}
type(pessoa)
dir(dict)
len(pessoa)

print(pessoa)
print(pessoa['nome'])
print(f"{pessoa['idade']} pessoa['idade']")
print(pessoa['cursos'])
print(pessoa['cursos'][1])
# print(pessoa['tags'])
print(f"{pessoa.keys()} keys")
print(f"{pessoa.values()} values")
print(f"{pessoa.items()} pessoas.items()")
print(f"{pessoa.get('idade')} pessoa.get('idade')")

print(pessoa.get('tags'))
print(pessoa.get('tags', "retorna valor default #aqui"))
#
# # %%
pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')

print(pessoa)

print(pessoa.pop('idade'))
print(pessoa)

pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)