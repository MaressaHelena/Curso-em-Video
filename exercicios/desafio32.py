# Faça um programa que leia um ano qualquer e mostre se ele é bissexto


ano = int(input('Insira um ano qualquer: '))
unidade = str(ano // 1 % 10) #transformação de um inteiro em string para ser concatenado
dezena = str(ano // 10 % 10) #transformação de um inteiro em string para ser concatenado
decada = int(dezena + unidade) # transformação em inteiro de uma concatenação

if decada%4 == 0 and decada != 00:
    print(f'{ano} é um ano bissexto')

elif ano%400 == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um bissexto')