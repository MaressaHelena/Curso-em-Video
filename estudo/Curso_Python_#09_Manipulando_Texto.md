# String
entende-se string sendo uma cadeia de caracteres ou cadeia de texto.
```py
nome = 'Maressa Helena'
```
##### obs: pode ser representada por aspas simples ou dupla

### Fatiamento
Toda string possui índices, isso porque cada parte que foi determinado string ocupa um micro-espaço na memória do computador. Os índices são importantes para a técnica de fatiamento de uma string. 

Usando o exemplo da aula, a frase **Curso em Video Python** possui 21 índices (contando também o espaço dado)
![image](https://user-images.githubusercontent.com/87135968/127064289-afb4b202-cf76-4e2b-b17d-68deae2ff24a.png)

O índice serve de "localizador". Se eu quisesse apenas um `print(frase)` eu teria toda a frase sendo mostrada. Mas no caso, quero só o elemento 9, como ficaria?

```py
frase = 'Curso em Video Python'
elemento = frase[9]
print(elemento)
```
##### obs: lembrar que conta-se um a partir do zero.
##### obs: o python difere letra maíuscula e minúscula

- Uma outra forma de fazer o fatiamento é `frase[9:13]`. Se repararmos na imagem acima, pensamos que retornará 'Video', mas não. Nesse caso, entende-se a informação dada como: "Retorne para mim de 9 à 13, excluindo 13."

```py
frase = 'Curso em Video Python'
elemento = frase[9:13]
print(elemento)
```

- É possível pular caracteres: 
```py
frase = 'Curso em Video Python'
elemento = frase[9:21:2]
print(elemento)
```
##### obs: o 21 não existindo, mas vai acontecer igual ao exemplo anterior. Ele vai excluir o 21 e parar no 20. O 2 representa os saltos de caracteres, no caso, de dois em dois.

- Começando pelo caractere zero
Uma forma de começar pelo caractere zero (primeiro) é simplesmente omitir o primeiro número
```py
frase = 'Curso em Video Python'
elemento = frase[:5]
print(elemento)
```
##### obs: lembrar de que nesse caso, o 5 será ignorado.

- Não determinando o final
É possível eu ter um ínicio e deixar que o python se encarregue do fim. 
```py
frase = 'Curso em Video Python'
elemento = frase[15:]
print(elemento)
```
##### obs: nesse caso, o python vai ler: começa em 15 e para em 20 (que é o máximo de caracteres disponiveis depois do 15)

- Utilizando dois pontos
O uso dos dois pontos determina algumas coisas. No exemplo abaixo, entende-se que: "começa em nove e vai até o final, pulando de 3 em 3"
```py
frase = 'Curso em Video Python'
elemento = frase[9::3]
print(elemento)
```

### Análise
Existem alguns modos para se analisar uma string, podemos fazer uso de `len(frase)`, `frase.count()`

- `len(frase)`
É muito útil quando é preciso saber o comprimento da string. 

- `frase.count()`
tomando como exemplo, o `count()` ajuda a fazer alguma contagem que será especificada dentro dos parentêses. Nesse caso, eu pedi pra contar a letra **o**
```py
frase = 'Curso em Video Python'
elemento = frase.count('o')
print(elemento)
```
Caso eu queira algo mais específico:
```py
frase = 'Curso em Video Python'
elemento = frase.count('o',0,13)
print(elemento)
```
Na situação acima, entende-se: "eu quero contar **o**, no intervalo de 0 à 13 (excluindo 13)"

- `frase.find()`
O comando acima busca na string o que foi determinado dentro dos parentesês. No exemplo abaixo, o retorno será o **número onde se começa a string solicitada. 
```py
frase = 'Curso em Video Python'
elemento = frase.find('deo')
print(elemento) # haverá o retorno do número 11, pois é onde 'deo' começa
```
É possível ter como retorno um número **- 1**. Isso vai acontecer quando for usado o comando `frase.find()` com um termo que não existe sendo especificado. 

```py
frase = 'Curso em Video Python'
elemento = frase.find('Android')
print(elemento) # haverá o retorno do número -1, pois 'Android' não existe na string 'Curso em Video Python'

### Usando operador `in`
Será que existe o termo **Curso** contido na variável `frase =`? O `in` servirá para responder isso com **True** ou **False**
```py
frase = 'Curso em Video Python'
elemento = 'Curso' in frase
print(elemento) # retorna True
```
### Transformação
Uma lista de string é **imutável**, mas existem métodos para fazer algumas alterações.

- `frase.replace()`
É possível fazer uma substituição
```py
frase = 'Curso em Video Python'
elemento = frase.replace('Python','Android')
print(elemento) # retorna 'Curso em Video Android'
```
- `frase.upper()`
Vai deixar toda a string em maiúsculo.
```py
frase = 'Curso em Video Python'
elemento = frase.upper()
print(elemento) # retorna 'CURSO EM VIDEO PYTHON'
```

- `frase.lower()`
Contrária à `frase.upper()`, vai retornar a string toda em minúscula.
```py
frase = 'Curso em Video Python'
elemento = frase.lower()
print(elemento) # retorna 'curso em video python'
```

- `frase.capitalize()`
Vai deixar apenas a **primeira letra** em maiúsculo, todo o resto ficará em minúsculo.

```py
frase = 'Curso em Video Python'
elemento = frase.capitalize()
print(elemento) # retorna 'Curso em video python'
```

- `frase.title()`
Fará uma análise mais profunda na string. Vai fazer um `capitalize()` palavra por palavra atráves da detecção de espaços.
```py
frase = 'Curso em Video Python'
elemento = frase.title()
print(elemento) # retorna 'Curso Em Video Python'
```
- `frase.strip()`
Remove todos os espaços inúteis (no início e no final)
```py
frase = '   Curso em Video Python  '
elemento = frase.strip()
print(elemento) # retorna 'Curso Em Video Python'
```



