
import functools
import random

numeros = [10, 15, 21, 33, 42, 55]


lista_numeros = list(map(lambda elem: elem * 2, numeros))

# print(lista_numeros)


lista_numeros = list(filter(lambda elem: elem >= 20, numeros))

# print(lista_numeros)

suma = functools.reduce(lambda x, y: x + y, numeros)

# print(suma)

random.shuffle(numeros)

# print(numeros)



l = [{"n":"A","a":"183"}]


# print(list(map(lambda dic: int(dic["a"]), l)))



# def normalizar_elementos(elemento):

#     elemento["a"] = int(elemento["a"])

#     return elemento


# print(list(map(lambda dic: , l)))


# print(normalizar_elementos(l[0]))

# print(list(map(normalizar_elementos, l)))


# lista = list.sort(key=lambda video: video["views"], reverse = True)





