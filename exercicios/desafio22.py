# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1) o nome com todas as letras maiusculas
# 2) o nome com todas as letras minusculas
# 3) quantas letras ao todo (sem considerar espaços)
# 4) quantas letras tem o primeiro nome


nome = str(input('Entre com o nome completo: ')).strip() #.strip() só remove espaço do lado esquerdo e direito, fazendo importante o uso da situação em 'total'
maiuscula = nome.upper()
minuscula = nome.lower()
total = len(nome) - nome.count(' ') # o nome.count(' ') é importante para remover os espaços que ainda são contados
dividido = nome.split()
primeiro_nome = len(dividido[0])


print(f'Letra maiúscula: {maiuscula}')
print(f'Letra minúscula: {minuscula}')
print(f'Total de letra: {total}')
print(f'Letras totais do primeiro nome: {primeiro_nome}')