a = {1, 2, 3}
type(a)
# a[0]
a = set('coddddd3r')  # Nao aceita repeticao
print(a)
print('3' in a, 4 not in a)
print({1, 2, 3} == {3, 2, 1, 3})

# operacoes
c1 = {1, 2}
c2 = {2, 3}
c1.union(c2)
c1.intersection(c2)
c1.update(c2)
print(c1)
print(c2 <= c1)
print(c1 >= c2)
c1 -= {2}
