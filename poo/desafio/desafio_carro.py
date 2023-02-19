from poo.desafio.carro import Carro

if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.speed_up(10))

    for _ in range(25):
        print(c1.speed_down(10))
