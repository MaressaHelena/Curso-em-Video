# Faça um programa que leia três números e mostre qual é o maior e qual é o menor


numero1 = float(input('Entre com o primeiro número: '))
numero2 = float(input('Entre com o segundo número: '))
numero3 = float(input('Entre com o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'O maior número é: {numero1}')
    if numero2 < numero3:
        print(f'O menor número é: {numero2}')
    else:
        print(f'O menor é: {numero3}')
elif numero2 > numero1 and numero2 > numero3:
    print(f'O maior número é {numero2}')
    if numero1 < numero3:
        print(f'O menor número é: {numero1}')
    else:
        print(f'O menor número é: {numero3}')
elif numero3 > numero1 and numero3 > numero2:
    print(f'O maior número é {numero3}')
    if numero1 < numero2:
        print(f'O menor número é: {numero1}')
    else:
        print(f'O menor número é: {numero2}')
print('Fim!!')


# outra forma 

lista = []
lista.append(float(input('Entre com o primeiro número: ')))
lista.append(float(input('Entre com o segundo número: ')))
lista.append(float(input('Entre com o terceiro número: ')))

print(f'O maior número da lista é: {max(lista)}\nO menor número é: {min(lista)}')