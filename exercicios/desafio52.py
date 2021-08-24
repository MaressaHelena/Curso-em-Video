# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo


numero = int(input('Digite um número: '))
divisivel = 0

for c in range(1, numero + 1):
    if numero%c == 0:
        divisivel += 1


if divisivel == 2:
    print(f'O número {numero} foi dividido {divisivel} vezes. Ele é PRIMO!')
else:
    print(f'O número {numero} foi dividido {divisivel} vez(es). Ele NÃO É PRIMO!')