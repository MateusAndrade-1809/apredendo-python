def multiplicar(*args):
    total = 1
    for num in args:
        total *= num
    return total
                
multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)

def par_impar(num):
    mult_two = num % 2 == 0
    
    if mult_two:
        return f'{num} | par'
    
    return f'{num} | impar'

print(par_impar(12))
print(par_impar(15))
print(par_impar(23))
print(par_impar(60))