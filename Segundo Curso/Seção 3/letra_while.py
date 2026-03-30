frase = 'Mateus comprou pao na casa do Joao'\
    'Lucas comprou pao na casa do Joao'\
    'Guilherme comprou pao na casa do Joao'

i = 0
m_vezes = 0
letra_m_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    m_vezes_atual = frase.count(letra_atual)

    if m_vezes < m_vezes_atual:
        m_vezes = m_vezes_atual
        letra_m_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_m_vezes}" que apareceu '
    f'{m_vezes}x'
)