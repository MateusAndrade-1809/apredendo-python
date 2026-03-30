ano_nascimento = int(input('Em que ano voce nasceu: '))
mes_nascimento = int(input('Mes de nascimento: '))
mes_atual = int(input('Em que mes estamos: '))
ano = 2026 - ano_nascimento - 1
idade = mes_atual - mes_nascimento
print(f'voce tem {ano} anos e {idade} meses')

