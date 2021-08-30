# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma P.A, mostrando os 10 primeiros termos da
# progressão usando a estrutura WHILE


termo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))

primeiro = termo
contador = 1

while contador <= 10:
    print(f'{primeiro}', end='')
    print(' ⇀ ' if contador < 10 else ' ', end='')
    primeiro += razao
    contador += 1
print('\nFIM')
