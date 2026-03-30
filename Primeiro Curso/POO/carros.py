class Carros:
    def __init__(self, cor, motor, novousado, ano):
        self.cor = cor
        self.motor = motor
        self.novousado = novousado
        self.ano = ano
    
    def informaçoes(self):
        print(f'A cor do carro é {self.cor}')
        print(f'O motor do carro é {self.motor}')
        print(f'O carro é {self.novousado}')
        print(f'O carro é de {self.ano}')

mustang = Carros('Azul', 'V8', 'novo', 2025)
print('\nmustang: ')
mustang.informaçoes()

camaro = Carros('Amarelo', 'V12', 'novo', 2026)
print('\nCamaro: ')
camaro.informaçoes()

porshe = Carros('Preto', 'V8', 'usado', 2023)
print('\nPorshe Panamera: ')
porshe.informaçoes()
