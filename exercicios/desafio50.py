# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o

n = 0
s = 0
for c in range(1, 7):
    n += 1
    numero = int(input(f'Digite o numero {n}: '))
    if numero%2 == 0:
        s += numero
print(f'A soma entre todos os números pares é: {s}')
print('fim')
