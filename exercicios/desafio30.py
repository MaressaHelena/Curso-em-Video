# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar


numero = int(input('Escolha um número inteiro: '))

if numero%2 == 0:
    print(f'{numero} é par!')
else:
    print(f'{numero} é ímpar!')