class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor
        self.quartos = quartos
        self.banheiros = banheiros
        
    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')
    def mostrar_quartos(self):
        print(f'Esta casa tem {self.quartos} quartos')
    def mostrar_banheiros(self):
        print(f'e {self.banheiros} banheiros')
    def adicionar_quartos(self):
        self.quartos += 1
        print(f'Esta casa tem {self.quartos} quartos')
    def pintar_casa(self, nova_cor):
        print(f'Pintando nova casa de {self.cor} para {nova_cor}')

casa1 = Casa('Azul', 4, 3)
casa2 = Casa('Vermelho', 5, 3)
casa3 = Casa('Laranja', 3, 2)
print('\nCasa 1: ')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quartos()
casa1.pintar_casa('Vermelho')
print('\nCasa 2: ')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
print('\nCasa 3: ')
casa3.mostrar_cor()
casa3.mostrar_quartos()
casa3.mostrar_banheiros()