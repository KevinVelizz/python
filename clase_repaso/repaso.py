from clase_repaso.pokemon import lista_personajes 

##lista estructura de datos que agrupa datos, int, strings, dict, etc

# lista_pokemones = [
#     "mewtwo", # 0
#     "moltres", # 1
#     "pikachu", # 2
#     "charmander" # 3
# ]


#Append
#agregar un elemento a la lista [Al final de la lista]

# print("lista antes de agregar:{0}".format(lista_pokemones))

#lista_pokemones.append("bulbasaur") #solo agrega datos a una lista

# print("Despues de agregar:{0}".format(lista_pokemones))



#Recorre la lista

#1 Posee indices donde estaran ubicados los elementos que contendra
#2 Los indices son numericos
#3 Los indices son en base 0
#4 Los indices iran del 0 hasta cantidad elementos -1


# for clasico

# print("for clasico")
# for indice in range(0, len(lista_pokemones)):
#     print(lista_pokemones[indice])



# #for-each
# print("\nfor Each")
# for pokemon in lista_pokemones:

#     print(pokemon)



#---------------------------------------------------------------------------

# DICCIONARIOS (dict)


{
    "nombre": "Gamora",
    "identidad": "Gamora Zen Whoberi Ben Titan",
    "empresa": "Marvel Comics",
    "altura": "183.65000000000001",
    "peso": "77.769999999999996",
    "genero": "F",
    "color_ojos": "Yellow",
    "color_pelo": "Black",
    "fuerza": "85",
    "inteligencia": "good"
  },



# heroe_ejemplo = lista_personajes[7]

# print(heroe_ejemplo)


# los_argentos = {
#     "nombre" : "pepe"
# }

# nombres = ["Paola Argento", "fatiga"]

# for nombre in nombres:
#     # Vemos que tiene el diccionario
#     persona = los_argentos["nombre"]

#     print(persona)


# dict_numeros = {
#     "numeros" : [1, 3, 12, 24, 45, 50]
# }

# lista_valores = dict_numeros["numeros"]


# lista_impares = []

# for numero in lista_valores:
#     #numeros pares
#     if numero % 2 == 0:
#         #lo guardo en una lista auxiliar
#         lista_pares.append(numero)

#reemplazar lista
# dict_numeros["numeros"] = lista_pares

#crear otra clave
# dict_numeros["numeros_pares"] = lista_pares


# print(dict_numeros)



# def calcular_numeros_par_impar(lista_numeros: list, resto: int) -> list:
#     '''
#     calcula los numerospares de una lista pasada por parametros y los guarda en una lista auxiliar que solo contenga numeros pares


#     parametros:
#     lista_numeros: la lista original a iterar

#     resto: el valor que voy a evaluar para que me duelva numeros pares o impares
#     retorna = nada

#     '''

#     numeros_filtrados = []
#     for numero in lista_numeros:
#     #numeros pares
#         if numero % 2 == resto:
#             #lo guardo en una lista auxiliar
#             numeros_filtrados.append(numero)

#     return numeros_filtrados


# calcular_numeros_par_impar(lista_valores)

# print(lista_valores)


# Obtengo lista par

# lista_pares = calcular_numeros_par_impar(lista_valores, 0)
# lista_impares = calcular_numeros_par_impar(lista_valores, 1)


# dict_numeros["numero_pares"] = lista_pares
# dict_numeros["numero_impares"] = lista_impares


# print(dict_numeros)





