class Numeros:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def total_calculos(self):
        print(f'soma: {self.n1 + self.n2}')
        print(f'subtracao: {self.n1 - self.n2}')
        print(f'multiplicacao: {self.n1 * self.n2}')
        print(f'elevado: {self.n1 ** self.n2}')
        print(f'divisao: {self.n1 / self.n2}')

print('\nCalculo 1:')        
c1 = Numeros(2, 5)
c1.total_calculos()
print('\nCalculo 2:')        
c2 = Numeros(8, 6)
c2.total_calculos()
print('\nCalculo 3:')
c2 = Numeros(5, 2)
c2.total_calculos()
print('\nCalculo 4:')
c3 = Numeros(12, 18)
c3.total_calculos()