
class Mago():
    def falar(self):
        print('Eu uso um mago que usa magias')

class Arqueiro():
    def falar(self):
        print('Eu sou um arqueiro com uma otima mira')

class Gigante():
    def falar(self):
        print('Eu sou um gigante forte e lento')

personagens = [Mago(), Arqueiro(), Gigante()]

for p in personagens:
    p.falar()