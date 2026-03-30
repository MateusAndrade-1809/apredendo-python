''' CALCULADORA COM WHILE '''

while True:
    
    numero1 = input('digite um numero: ')
    numero2 = input('digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os numeros digitados sao invalidos.')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Digite um operador que esteja dentro do parentese (+-/*)')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador!!')
        continue
    
    print('Conta feita(Resultado abaixo)')
    
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)

    
    ##############
    sair = input ('quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break