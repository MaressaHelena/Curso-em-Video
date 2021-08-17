# Crie um programa que faça o computador jogar Jokenpô com você
# pedra ganha de tesoura, tesoura ganha de papel e papel ganha de pedra


import random


entrada = str(input('Digite sua escolha (PEDRA), (PAPEL), (TESOURA): ')).lower()
jokenpo = ['pedra', 'papel', 'tesoura']
computador = random.choice(jokenpo)

if entrada == computador:
    print(f'Houve EMPATE!\nSua escolha: {entrada}\nEscolha do computador: {computador}')
elif entrada == 'pedra' and computador == 'tesoura':
    print(f'Você VENCEU!\nSua escolha: {entrada}\nEscolha do computador: {computador}')
elif entrada == 'tesoura' and computador == 'papel':
    print(f'Você VENCEU!\nSua escolha: {entrada}\nEscolha do computador: {computador}')
elif entrada == 'papel' and computador == 'pedra':
    print(f'Você VENCEU!\nSua escolha: {entrada}\nEscolha do computador: {computador}')
else:
    print(f'Você PERDEU!\nSua escolha: {entrada}\nEscolha do computador: {computador}')