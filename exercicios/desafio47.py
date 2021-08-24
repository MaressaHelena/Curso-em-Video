# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50


lista = []

for c in range(1, 51):
    
    if c%2 == 0:
        lista.append(c)

print(f'Os números pares são: {lista}')
