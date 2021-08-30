# Melhore o jogo do DESAFIO 28 onde o computador vai pensar em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

c = 0


usuario = int(input('Escolha um número inteiro entre 0 e 10: '))
computador = random.randint(0, 10)

while usuario != computador:
    usuario = int(input('Escolha um número inteiro entre 0 e 10: '))
    computador = random.randint(0, 10)
    c += 1
else:

    print(f'Você finalmente conseguiu! Você tentou {c} vez(es)! ')