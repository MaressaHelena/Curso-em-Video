# O exercicio corresponde a aula 7 do CURSO EM VÍDEO.


# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Entre com o valor: '))
centimetro = metro/100
milimetro = metro/1000
print(f'{metro} em metros: {metro}')
print(f'{metro} em centímetros: {centimetro}')
print(f'{metro} em milímetros: {milimetro}')
print('FIM')