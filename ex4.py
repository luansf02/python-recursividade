"""EXERCÍCIO 4
Escreva uma função recursiva para realizar uma busca em uma lista de números.
A função deve receber como parâmetros a lista e um item para buscar na lista.
Deve retornar True caso o item seja localizado, ou False, caso não seja localizado."""


def busca(lista, item):
    if len(lista) == 0:
        return False
    else:
        if lista[0] == item:
            return True
        else:
            return busca(lista[1:], item)


print(busca([5, 7, 3], 3))
