class Familia:
    def __init__(self, nome, grau, idade):
        self.nome = nome
        self.idade = idade
        self.grau = grau
    def apresentação(self):
        print(f'Me chamo {self.nome}, sou {self.grau} do Mateus e tenho {self.idade} anos')
    
class Funcionario(Familia):
    def __init__(self, nome, grau, idade, anos_serviço):
        super().__init__(nome, grau, idade)
        self.anos_serviço = anos_serviço
    def tempo_trabalho(self):
        print(f'Trabalha na empresa há {self.anos_serviço} anos')

class Cliente(Familia):
    def __init__(self, nome, grau, idade, saldo):
        super().__init__(nome, grau, idade)
        self.saldo = saldo
    def compra(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f'A sua compra de {valor_compra} foi aprovada! Seu saldo é de: {self.saldo}')
        else:
            print(f'Saldo insuficiente')

print('\nPessoa 1:')
p1 = Familia('Karla', 'Mãe', 47)
p1.apresentação()
print('\nPessoa 2:')
p2 = Familia('Rafael', 'Pai', 42)
p2.apresentação()

print('\nPessoa 3:')
p3 = Funcionario('Jhonathan', 'Atendente', 32, 5)
p3.apresentação()
p3.tempo_trabalho()

print('\nPessoa4:')
p4 = Funcionario('Marco', 'Gestor', 66, 12)
p4.apresentação()
p4.tempo_trabalho()

print('\nPessoa 5:')
p5 = Cliente('Joao', 'Cliente', 50, 6000)
p5.apresentação()
p5.compra(3560)

