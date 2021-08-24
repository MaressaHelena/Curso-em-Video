# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos



kg = []

for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))
    kg.append(peso)
    maior = max(kg)
    menor = min(kg)
print(f'O maior peso foi: {maior}\nO menor peso foi {menor}')
print(kg)