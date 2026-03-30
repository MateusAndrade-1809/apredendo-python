def desconto(preço, porcentagem):
    return preço - (preço * porcentagem / 100)
valor = desconto(706, 7.95)
print(f'O valor com desconto é R${valor:.2f}')