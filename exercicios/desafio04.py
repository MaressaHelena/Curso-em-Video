# O exercicio corresponde a aula 6 do CURSO EM VÍDEO.

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.



n = input('Digite algo: ')
print(f'Tipo primitivo: {type(n)}')
print(f'É númerico?: {n.isnumeric()}')
print(f'É alfa numérico?: {n.isalnum()}')
print(f'É alfa?: {n.isalpha()}')
print(f'Todas as letras são maiúsculas?: {n.isupper()}')
print('Fim!')