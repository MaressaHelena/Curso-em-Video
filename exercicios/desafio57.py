# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Informe uma codição válidan [M/F]: ')).strip().upper()[0] # [0]: para que pegue apenas a primeira letra
while sexo not in 'MF':
    sexo = str(input('Por favor, uma condição válida [M/F]: ')).strip().upper()[0]
else:
    print(f'Sexo [{sexo}] registrado!')