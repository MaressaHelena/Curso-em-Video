# Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for


numero = int(input('Tabuada de: '))

for c in range(1, 11):
    tabuada = (f'{numero} x {c} = {numero*c}')
    print(tabuada)
print('FIM')