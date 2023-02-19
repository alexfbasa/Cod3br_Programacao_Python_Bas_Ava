class Data:
    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 19
d1.mes = 2
d1.ano = 2023

print(d1.to_str())
