# Estrutura Condicional

### If/Else

A melhor forma de pensar nas condições acima é colocá-las em blocos de **True** ou **False**

If recebe o bloco **True**, enquanto que Else recebe o bloco **False**. A leitura correta, na programação ficaria algo do tipo: *"Se (if) isso acontecer, ok. Caso contrário (else) acontece isso."*

É importante ressaltar que nunca haverá execução para os dois blocos juntos. Sempre será um ou outro, enquanto um for verdadeiro, vai acontecer, senão, o bloco falso entrará em cena.

### Identação

Vejamos a imagem abaixo


![image](https://user-images.githubusercontent.com/87135968/127558539-ae8030fb-bc22-49d3-a39e-454c8e9ddc80.png)

É importante respeitar o agrupamento dessas estruturas. Tudo o que está "colado" no canto esquerdo será executado. Sempre! Já o que se encontra deslocado (identado, tecla tab para deslocar/identar) vai acontecer enquanto for verdade e, mais uma vez, caso não seja, então vai executar o bloco **False**

### Elif

Existe também a possibilidade de algo não ser verdadeiro logo de cara, mas... *e se* for possível provar de outra forma? O comando `elif` entra nessa jogada. Se a sua média for maior do que 7, você passa direto. E se a nota for maior que 4 e menor que 7? Bom, você tá de recuperação. Caso contrário, sua nota sendo menor que 4, você reprova direto. É sutil, mas entre um sim e um não, você pode ter outra possibilidade. Essa é a função do elif