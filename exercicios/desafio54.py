# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
# considerar 21 como maioridade



for c in range(0, 7):
    ano = int(input(f'Ano de nascimento da pessoa {c+1}: '))
    idade = ano - 2021
if idade >= 21:
    print(f'Você tem {idade} anos. Você já é maior de idade!')
else:
    print(f'Você tem {idade} anos. Você ainda é menor de idade!')    