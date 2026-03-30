nota = int(input('qual a sua nota: '))
mensalidade = int(input('quanto é a sua mensalidade: '))
desconto = mensalidade * 20 / 100
if nota >= 80:
    print('Voce é um aluno destaque e recebera 20 de desconto')
    print(f'Seu desconto é de {desconto}')
elif nota >= 60:
    print('Voce passou de ano')
else:
    print('Voce bombou de ano')