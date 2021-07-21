#  Função `print()`

 É responsável por mostrar coisas na tela
```py
print('Olá, Mundo!')
```

Também pode nos ajudar para imprimir um cálculo
```py
print(7+4) # obs: nesse caso não se usam aspas pois eu quero que me retorne um cálculo e não uma mensagem
```
 
## Formatação

Agora, vejamos um tipo de formatação da função `print()`, ela é utilizada para aproximar os elementos contidos no print.

```py
print('7'+'4') # nessa situação, ao inves de imprimir 11 (que é a soma de 4+7), a função irá imprimir '74' pois o + ali significa aproximação
```
_obs: em alguns casos usa-se a vírgula para ''juntar'' os elementos_.

##  Variáveis

Tendo uma variável, devemos atribuir a ela ''objetos'', pois ela vai receber valores. 
```py
nome = 'Maressa Helena' # o igual (=), nesse caso, significa RECEBE! Lê-se: nome recebe Maressa Helena
idade = 20
peso = 50
print(nome, idade, peso)
```
***
# Função `input()`

 A função `input()` é para atribuir uma _interação_.

```py
# nesse exemplo, eu vou perguntar o nome, a idade e o peso da pessoa e a mesma deverá inserir tais informações.
nome = input('Qual é seu nome?') 
idade = input('Quantos anos você tem?')
peso = input('Qual é o seu peso?')
# depois de realizada a interação e as variaveis guardarem as informações perguntadas, o programa irá imprimir todas elas, tal como está em print()
print(nome, idade, peso)  
```