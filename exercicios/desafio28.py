# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.


from time import sleep
import random

usuario = int(input('Escolha um número inteiro entre 0 e 5: '))
computador = random.randint(0, 5)
print('PROCESSANDO...')
sleep(3)
if usuario == computador:
    print(f'Parabéns, você descobriu o número! :)\nO número é: {computador}')
else:
    print(f'Vitória das máquinas! Você dançou!  \nO número correto é: {computador}')