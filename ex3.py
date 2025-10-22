"""EXERCÍCIO 3
Escreva uma função recursiva em Python que receba dois números inteiros A e B, e calcula o resultado
de AB
. Considere que o resultado de AB é igual a A * AB-1
.
Por exemplo: o resultado de 45 pode ser calculado como:

4^5 = 4 * 4^4
4^4 = 4 * 4^3
4^3 = 4 * 4^2
4^2 = 4 * 4^1
4^1 = 4 * 4^0
4^0 = 1 """


def potencia(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b - 1)

print(potencia(4, 3))