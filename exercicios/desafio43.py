# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, 
# de acordo com a tabela abaixo:
# - Abaixo de 18.5 = abaixo do peso
# - Entre 18.5 e 25 = peso ideal
# - 25 até 30 = sobrepeso
# - 30 até 40 = obesidade
# - Acima de 40 = obesidade mórbida


peso = float(input('Entre com o valor do seu peso: '))
altura = float(input('Entre com a sua altura: '))
imc = (peso/altura**2)
print( '========== I M C ==========')


if imc < 18.5:
    print(f' O seu IMC é: {imc:.2f}\nVocê está abaixo do peso!')
elif imc >= 18.5 and imc<= 25:
    print(f' O seu IMC é: {imc:.2f}\nVocê está no peso ideal!')
elif imc >= 25 and imc <=30:
    print(f' O seu IMC é: {imc:.2f}\nVocê está com sobrepeso!')
elif imc >= 30 and imc <= 40:
    print(f' O seu IMC é: {imc:.2f}\nVocê está obeso!')

else:
    print(f' O seu IMC é: {imc:.2f}\nVocê está com obesidade mórbida!')