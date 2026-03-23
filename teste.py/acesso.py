acesso = int(input('Qual a sua idade? '))
autorizacao_pais = input('autorizacao dos pais?(s/n): ')
if acesso >= 18:
    print('Acesso permitido!!')
elif acesso >= 16 and autorizacao_pais == 's':
    print('acesso autorizado com a permissão dos pais')
else:
    print('acesso negado')