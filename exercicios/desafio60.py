# Faça um programa que leia o número qualquer e mostre o seu fatorial. Ex.: 5! = 5x4x3x2x1 = 120

numero = int(input('Digite um número: '))
c = numero #c vai receber o numero escolhido
f = 1

print(f'CALCULANDO O FATORIAL DE {numero}! = ', end='')
while c > 0: # maior que 0 pois o fatorial vai até o 1 
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='') # esse print é importante para remover o 'x' que aparece depois de 1
    f *= c
    c -= 1
print(f'{f}')