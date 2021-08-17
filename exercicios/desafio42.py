# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero = todos os lados iguais
# - Isósceles = dois lados iguais
# - Escaleno = todos os lados diferentes

a = float(input('Digite o comprimento da reta a: '))
b = float(input('Digite o comprimento da reta b: '))
c = float(input('Digite o comprimento da reta c: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Você formou um triângulo!')
    if a == b and b == c:
        print(f'Este triângulo é EQUILÁTERO!')
    elif a == b and a != c or b == c and b != a or c == a and c != b:
        print('Você formou um triângulo ISÓSCELES!')
    elif a != b and a != c and b != c:
        print('Você formou um triângulo ESCALENO!')
else:
    print('Não é possível formar um triângulo!')