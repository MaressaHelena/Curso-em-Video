# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# ex: digite um número: 6.127 | o número 6.127 tem a parte inteira 6.

# utilizando módulo trunc

from math import trunc


numero = float(input('Digite um número real qualquer: '))
inteiro = trunc(numero)
print("\n**************************\n")
print(f'A porção inteira de {numero} é {inteiro} !!')


# sem utilizar módulo

numero = float(input('Digite um número real qualquer: '))
print("\n**************************\n")
print(f'A porção inteira de {numero} é {numero:.0f} !!')