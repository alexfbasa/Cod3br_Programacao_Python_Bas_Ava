from poo.carro import Carro

c1 = Carro(180)

for _ in range(39):
    print(c1.acelerar())

for _ in range(30):
    print(c1.frear())
