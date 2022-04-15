# Ponto Flutuante - Padrão IEEE754
## Calculadora padrão IEEE754 - Precisão simples 32 bits
Em muitas linguagens de progamação, apesar de rotinas de impressão mostrar a fração 1/10 como 0.10000, se exibirmos o número com maior precisão, veremos que o valor real armazenado é um pouco diferente disso.

Desta forma, ao programar devemos ter cuidado com números de ponto flutuante, em especial com acumuladores e comparações.

O padrão utilizado por nossa calculadora é o simples de 32 bits:

![iee754.PNG](http://dwebkit.esy.es/repositorio/img/iee754.png)

* **sinal:** O 1º bit mais à esquerda representa o sinal, se o número for positivo, o sinal é 0, caso contrário é 1
* **expoente:** Os 8 bits no meio representam a potência normalizada, usando a fórmula x = e + 127, onde x é o expoente normalizado.
* **mantissa:** Os 23 bits na extrema direita representam a parte fracionária.
