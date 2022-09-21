
from pokemon import pokemones 


#01 - Imprimir nombres de pokemones

'''
01.1
Crear la función "obtener_nombre_pokemon" la cual recibirá por
parámetro un diccionario que representará al pokemon, la función deberá obtener el nombre
y retornarlo como un string.

01.2
Crear la función "imprimir_pokemones" la cual recibirá por
parámetro una lista de pokemones e imprimirá sus nombres. Reutilizar 'obtener_nombre_pokemon'

'''

# print(pokemones)

def obtener_nombre_pokemon(pokemon_nombre: dict) -> str:

    nombre_pokemon = pokemon_nombre["nombre"]

    
    return nombre_pokemon

print(obtener_nombre_pokemon(pokemones[0]))


def imprimir_pokemos(pokemones: list):

    for pokemon in pokemones:

        nombre_filtrado = obtener_nombre_pokemon(pokemon)
        print(nombre_filtrado)

# imprimir_pokemos(pokemones)



#02 - Imprimir pokemones que tenga un ID par

# 02.1
# Crear la función "tiene_id_par" la cual recibirá por parámetro un diccionario
# que representará al pokémon y verificará que su id sea par, en caso de que sea par
# retornará True, caso contrário retornará False.

# 02.2
# Crear la función "obtener_id_pokemon" la cual recibirá por
# parámetro un diccionario que representará al pokemon, la función deberá obtener el id
# y retornarlo como un string.

# 02.3
# Crear la función "pokedex_imprimir_pokemon_id_par" la cual recibirá por parámetro
# la lista de pokemones y deberá imprimir solo los que cumplan con la condición de
# tener un ID par. Reutilizar las funciones:
#     'tiene_id_par', 'obtener_nombre_pokemon'




def obtener_id_pokemon(pokemon_id: dict) -> str:

    # retorno = False
    # for pokemon in pokemones:
    #     if(pokemon["id"] % 2 == 0):

    id_pokemon = str(pokemon_id["id"])

    # print(id_pokemon)

    return id_pokemon

        # return id_pokemon

obtener_id_pokemon(pokemones[0])



def tiene_id_par(pokemon: dict) -> bool:

    # for pokemon in pokemones:
    #     if(pokemon)

    if(pokemon["id"] % 2 == 0):
        return True
    elif (pokemon["id"] % 2 == 1):
        return False



# es_par = tiene_id_par(pokemones[1]) 


# print(es_par)

def obtener_nombre_pokemon(pokemon:list) -> str:

    nombre_pokemon = pokemon["nombre"]

    return nombre_pokemon


def pokedex_imprimir_pokemon_id_par(pokemon: list):

    for pokemon in pokemones:

        es_par = tiene_id_par(pokemon)

        if es_par:
            id_par = "Nombre: {0} | Id: {1}".format(obtener_nombre_pokemon(pokemon), obtener_id_pokemon(pokemon))

            print(id_par)


# pokedex_imprimir_pokemon_id_par(pokemones)


'''
03.1
Crear la función "id_multiplo_25" la cual recibe por parámetro un diccionario
que representará al pokémon y verificará que su id múltiplo de 25, en caso de que
lo sea retornará True, caso contrário retornará False.

03.2
Crear la función "pokedex_imprimir_pokemon_id_mul_25" la cual recibirá por parámetro
la lista de pokemones y deberá imprimir solo los que cumplan con la condición de
tener un ID múltiplo de 25. Reutilizar las funciones:
'id_multiplo_25', 'obtener_nombre_pokemon'

'''


# def obtener_nombre_pokemon()


