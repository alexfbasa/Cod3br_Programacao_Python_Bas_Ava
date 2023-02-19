class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, fator=5):
        maxima = self.velocidade_maxima
        nova = self.velocidade_atual + fator
        self.velocidade_atual = nova if nova <= self.velocidade_maxima else maxima
        return self.velocidade_atual

    def frear(self, fator=20):
        nova = self.velocidade_atual - fator
        self.velocidade_atual = nova if nova >= 0 else 0
        return self.velocidade_atual
