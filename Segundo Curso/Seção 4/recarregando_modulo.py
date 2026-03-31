import importlib

import recarregando_modulo_m

print(recarregando_modulo_m.variavel)

for i in range(10):
    importlib.reload(recarregando_modulo_m)
    print(i)

print('Fim')