# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

resposta = 'S'
soma = contador = maior = menor = 0

while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    resposta = str(input('CONTINUAR? [S/N]: ')).upper().strip()[0] # para considerar só primeira letra
    contador += 1
    soma += numero
    if contador ==1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f'media {soma/contador:.2f}\nMAIOR: {maior}\nMENOR: {menor}')
