
def calculo_imposto(preco_produto, porcentagem_imposto, frete):
    imposto = preco_produto * porcentagem_imposto / 100
    (print(f'O valor do imposto é de {imposto}'))
    print(f'O valor total do produto é de {preco_produto + imposto + frete}') 
