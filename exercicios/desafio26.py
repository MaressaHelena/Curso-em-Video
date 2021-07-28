# Faça um programa que leia uma frase pelo teclado e mostre:
# 1) quantas vezes aparece a letra 'A'
# 2) em que posição ela aparece a primeira vez 
# 3) em que posição ela aparece a ultima vez


frase = str(input('Entre com uma frase: ')).strip().lower()
letra_a = frase.count('a')
primeira_vez = frase.find('a')+1 # somar 1 pois é mais facil para nós interpretarmos algo começando do 1 ao invés do 0
ultima_vez = frase.rfind('a')+1 # usei rfind pois o programa vai começar a busca pelo lado direito da frase e somei 1 pelo mesmo motivo acima

print(f'Existem {letra_a} letras A em sua frase!')
print(f'A letra A aparece pela primeira vez na posição {primeira_vez}')
print(f'A letra A aparece pela última vez na posição {ultima_vez}')