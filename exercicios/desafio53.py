# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços


palindromo = str(input('Digite a frase: ')).strip().upper()
palavra = palindromo.split()
junto = ''.join(palavra)
inverso = ''

for c in range(len(junto) -1, -1, -1): # aqui eu pego o final da string até o inicio da string (como uma contagem regressiva)
    inverso += junto[c] # aqui ocorre a concatenação de string
if inverso == junto:
    print(f'{junto} e {inverso} formam um PALÍNDROMO!')
else:
    print(f'{junto} e {inverso} NÃO formam um PALÍNDROMO!')