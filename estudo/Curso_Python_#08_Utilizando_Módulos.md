# Utilizando Módulos

As vezes é preciso utilizar bibliotecas dentro de certos programas. Podemos pensar na imagem abaixo como 3 bibliotecas distintas.

![image](https://user-images.githubusercontent.com/87135968/126701814-8d6005fa-8ab5-4c4f-a02d-42a708395a05.png)

### Usando `import`
A função import vai pegar todo o conteúdo(módulos) da biblioteca. Digamos que eu queria todas as bebidas, então eu preciso utilizar
```py
import bebida
```
### Usando `from`

E se eu quiser utilizar da biblioteca doce, apenas o bolo? Nesse caso, devemos prosseguir da seguinte forma:

```py
from doce import bolo
```
##### obs: podemos pensar que `import` é mais generalista e que `from <alguma coisa> import <coisa>` é mais seletiva

- Exemplo utilizando a biblioteca **math** com `import`
```py
import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f' A raíz quadrada de {num} é: {raiz}')
```
- Exemplo utilizando o módulo `sqrt` da biblioteca **math** com `from import`
```py
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f' A raíz quadrada de {num} é: {raiz}')
```
- Exemplo utilizando o módulo `sqrt` e `floor` da biblioteca **math** com `from import`
```py
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a: {floor(raiz)}')
```