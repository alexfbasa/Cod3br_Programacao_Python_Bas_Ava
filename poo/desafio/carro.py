class Carro:
    def __init__(self, velo_max):
        self.velox_max = velo_max
        self.velocidade = 0

    def ligar_carro(self):
        return True

    def desligar_carro(self):
        print('Carro desligado.')
        return True

    def speed_up(self, fator_acelerar=10):
        while self.velocidade < self.velox_max:
            self.velocidade += fator_acelerar
            return self.velocidade
        print('Carro não pode acelerar mais')

    def speed_down(self, fator_frear=20):
        while self.velocidade >= 0:
            self.velocidade -= fator_frear
            if self.velocidade < 0:
                self.velocidade = 0
            return self.velocidade
        print('Carro não pode frear mais')
