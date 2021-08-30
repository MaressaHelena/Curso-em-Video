# Crie um programa que leia dois valores e mostre o menu na tela:
# - [1] somar
# - [2] multiplicar
# - [3] maior
# - [4] novos números
# - [5] sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso


valor1 = float(input('Entre com o valor 1: '))
valor2 = float(input('Entre com o valor 2: '))
escolha = 0


while escolha != 5:
    escolha = int(input('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA : '))
    if escolha == 1:
        print(f'A soma entre os dois números é: {valor1 +valor2}')
    elif escolha == 2:
        print(f'A multiplicação entre os dois números é: {valor1*valor2}')
    elif escolha == 3:
        print(f'O maior número é {max(valor1, valor2)}')
    elif escolha == 4:
        valor1 = float(input('Entre com o valor 1: '))
        valor2 = float(input('Entre com o valor 2: '))
    else:
        print('Obrigada!')