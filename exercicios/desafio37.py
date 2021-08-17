# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal



numero = int(input('Digite um número inteiro: '))
bases = int(input('Ok, agora escolha a base para conversão: (1-binário), (2-octal), (3-hexadecimal): '))


# vou aplicar uma ideia de fatiamento de string nas variaveis BINARIO, OCTAL e HEXADECIMAL para que o python ignore
# o identificador das bases.
if bases == 1:
    binario = bin(numero) [2:]
    print(f'O número {numero} em BINÁRIO é: {binario}')
elif bases == 2:
    octal = oct(numero) [2:]
    print(f'O número {numero} em OCTAL é: {octal}')
elif bases == 3:
    hexadecimal = hex(numero) [2:]
    print(f'O número {numero} em HEXADECIMAL é: {hexadecimal}')
else:
    print('Você digitou um número inválido. Por favor,escolha a base para conversão: (1-binário), (2-octal), (3-hexadecimal) ')

# Também é possível fazer o programa da seguinte forma, utilizando 'caracteres' para remover a identificação

numero = int(input('Digite um número inteiro: '))
bases = int(input('Ok, agora escolha a base para conversão: (1-binário), (2-octal), (3-hexadecimal): '))


if bases == 1:
    print(f'O número {numero} em BINÁRIO é: {numero:b}')
elif bases == 2:
    print(f'O número {numero} em OCTAL é: {numero:o}')
elif bases == 3:
    print(f'O número {numero} em HEXADECIMAL é: {numero:x}') #:x para letras minusculas e :X para maiusculas
else:
    print('Você digitou um número inválido. Por favor,escolha a base para conversão: (1-binário), (2-octal), (3-hexadecimal)')