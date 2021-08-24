# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão


termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))

n = 0
progressao_aritmetica = []

for c in range(1, 11):
    n += 1
    progressao_aritmetica.append(termo + (n-1)*razao)

print(f'Os 10 primeiros números da P.A são: {progressao_aritmetica}')
