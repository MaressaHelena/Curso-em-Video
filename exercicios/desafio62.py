# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos


termo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))

# contadores
primeiro = termo
contador = 1
total = 0
mais = 10 # vamos começar mostrando 10 termos

while mais != 0:
    total += mais
    while contador <= total:
        print(f'{primeiro}', end='')
        print(' ⇀ ' if contador < 10 else ' ', end=' ')
        primeiro += razao
        contador += 1
    print('\nPAUSA')
    mais = int(input('quantos termos você quer mostrar a mais?: '))
print('FIM')
