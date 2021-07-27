# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse ângulo.

# utilizando módulo: sin, cos, tan, radians


from math import sin, cos, tan, radians


angulo = float(input('Digite o ângulo: '))
conversao = radians(angulo)
print(f'Seno: {sin(conversao):.2f} \nCosseno: {cos(conversao):.2f} \nTangente: {tan(conversao):.2f}')
