class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie
    def apresentar(self):
        print(f'Eu sou o {self.especie} chamado {self.nome} da cor {self.cor}')
        
class Cachorro(Animal):
    def emitir_som(self):
        print('AuAu!')

class Cavalo(Animal):
    pass

cachorro1 = Cachorro('Bob', 'Branco', 'Pastor Alemão')
cachorro1.apresentar()
cachorro1.emitir_som()

cachorro2 = Cachorro('Maia', 'Marrom', 'Yorkshine')
cachorro2.apresentar()
cachorro2.emitir_som()

cavalo1 = Cavalo('Douglas', 'Marrom', 'Mustangue')
cavalo1.apresentar()