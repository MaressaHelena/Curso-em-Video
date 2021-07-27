# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.


temperatura = float(input('Digite a temperatura em °C: '))
conversao_fahrenheit = (1.8*temperatura+32)
print(f'{temperatura} °C corresponde a {conversao_fahrenheit:.2f} °F')
print('Fim! 🌡️')