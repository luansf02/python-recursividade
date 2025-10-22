"""EXERCÍCIO 5
Escreva uma função recursiva que recebe como parâmetros uma lista de números inteiros e um
número inteiro N. A função deve retornar a quantidade de vezes que N aparece na lista."""


def busca(lista, item):
    if len(lista) == 0:
        return 0
    else:
        if lista[0] == item:
            return 1 + busca(lista[1:], item)
        else:
            return busca(lista[1:], item)


print(busca([3, 5, 7, 3, 3, 6, 3], 3))