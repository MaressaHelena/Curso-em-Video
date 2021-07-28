# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome


nome = str(input('Digite seu nome completo: ')).strip()
capitalizando = nome.title() #.title() para deixar as letras iniciais em Maiusculo
silva = 'Silva' in capitalizando
print(f'Tem Silva?: {silva}')