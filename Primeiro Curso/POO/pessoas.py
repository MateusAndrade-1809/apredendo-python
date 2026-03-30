class Pessoas:
    def __init__(self, parentesco, nome, idade, sexo):
        self.parentesco = parentesco
        self.nome = nome
        self.idade = idade
        self.sexo = sexo      
    def informaçoes(self):
        print(f'Essa pessoa é seu/sua {self.parentesco}')
        print(f'Esssa pessoa se chama {self.nome}')
        print(f'Tem {self.idade} anos')
        if self.idade >= 18:
            print('Essa pessoa é maior de idade')
        else:
            print('Essa pessoa é menor de idade')
        print(f'Essa pessoa é {self.sexo}')
    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f'Atualizando nova idade de {self.idade} para {nova_idade}')
        else:
            print('A nova idade tem que ser maior que a antiga')

print('\nPessoa1:')
pessoa1 = Pessoas('Mãe', 'Karla', 48, 'mulher')
pessoa1.informaçoes()
pessoa1.atualizar_idade(50)
print('\nPessoa2:')
pessoa2 = Pessoas('Pai', 'Rafael', 43, 'Homem')
pessoa2.informaçoes()
print('\nPessoa3:')
pessoa3 = Pessoas('Avô', 'Carlos', 67, 'Homem')
pessoa3.informaçoes()
print('\nPessoa4:')
pessoa4 = Pessoas('Avó', 'Rose', 70, 'Mulher')
pessoa4.informaçoes()