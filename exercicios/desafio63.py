# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
# de uma sequencia de Fibonacci. Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8


n = int(input('Quantos termos você quer mostrar?: '))
termo1 = 0
termo2 = 1
print(f'{termo1} ⇀ {termo2}', end=' ')
contador = 3 # o contador recebe 3 porque o termo1 e termo2 já foi mostrado

while contador <= n:
    termo3 = termo1 + termo2
    print(f' ⇀ {termo3}', end='')
    termo1 = termo2 # essa forma é para ir substitunindo os valores e ir somando entre si. Isso também porque ja printei o t3 = t1 + t2
    termo2 = termo3
    contador += 1
print('\nFIM')
