# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ex : Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1


numero = int(input('Entre com um valor: '))
unidade = numero // 1 % 10 #a divisão inteira de numero por 1 e o resto da sua divisão por 10 vai ser a unidade
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')