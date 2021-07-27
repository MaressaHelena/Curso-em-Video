# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.


# utilizando o módulo hypot

from math import hypot


cateto_a = float(input('Digite o valor do cateto a: '))
cateto_b = float(input('Digite o valor do cateto b: '))
print(f'A hipotenusa equivale a {hypot(cateto_a, cateto_b):.2f}')

# sem biblioteca

cateto_a = float(input('Digite o valor do cateto a: '))
cateto_b = float(input('Digite o valor do cateto b: '))
print(f'A hipotenusa equivale a {((cateto_a**2) + (cateto_b**2))**0.5}')