# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais


numero1 = int(input('Entre com o primeiro valor inteiro: '))
numero2 = int(input('Entre com o segundo valor inteiro: '))


if numero1 > numero2:
    print(f'O primeiro valor, {numero1}, é maior que o segundo valor, {numero2}')
elif numero2 > numero1:
    print(f'O segundo valor, {numero2}, é maior que o primeiro valor, {numero1}')
else:
    print(f'Não existe valor maior, os dois são iguais!')