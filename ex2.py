"""EXERCÍCIO 2
O máximo divisor comum (MDC) de dos números inteiros x e y é o maior inteiro que é divisível por x
e y, e pode ser calculado de acordo com a definição abaixo.
Escreva uma função recursiva em Python que calcule o MDC de dois números inteiros positivos."""


def mdc(x, y):
    if x >= y and x % y == 0:
        return y
    elif x < y:
        return mdc(y, x)
    else:
        return mdc(y, x % y)


x = int(input('Valor do X: '))
y = int(input('Valor do Y: '))
print(mdc(x, y))