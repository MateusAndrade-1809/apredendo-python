#Sistema de Faculdade
class Escola():
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status
    def apresentar(self):
        print(f'Meu nome é {self.nome}, tenho {self.idade} anos')
    def verificar_status(self):
        print(f'Status: {"ATIVO" if self.status else "INATIVO"}')
class Aluno(Escola):
    def __init__(self, nome, idade, status, ano):
        super().__init__(nome, idade, status)
        self.ano = ano
    def apresentar(self):
        print(f'Meu nome é {self.nome}, tenho {self.idade} de idade e estou no {self.ano} ano')
    

class Professor(Escola):
    def __init__(self, nome, idade, status, materia):
        super().__init__(nome, idade, status)
        self.materia = materia
        
class Assistente(Escola):
    def __init__(self, nome, idade, status, bloco):
        super().__init__(nome, idade, status)
        self.bloco = bloco

a1 = Aluno('Marcos', 12, True, 8)
a1.apresentar()
p1 = Professor('Augusto', 56, True, 'Geometria')
p1.apresentar()
p1.verificar_status()
as1 = Assistente('Mariana', 18, False, 'B')
