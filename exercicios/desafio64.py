# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

numero = contador = soma = 0 #assim economiza linhas
numero = int(input('Digite um número [999 para parar]: ')) # essa é uma maneira de desconsiderar o flag 
while numero != 999:
    contador +=1
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
else:
    print(f'Você digitou {contador} vezes antes de parar!')
    print(f'A soma é {soma}')