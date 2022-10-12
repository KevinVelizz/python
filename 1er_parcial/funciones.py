
import json
import re


def validar_respuesta(respuesta:str,expresion_regular:str):
    '''
    La funcion valida lo que pasemos por parametro.
    Recibe por parametro 2 strings.
    Retorna int o str.
    '''
    retorno = -1

    if(respuesta):

        if(re.match(expresion_regular,respuesta, re.IGNORECASE)):
            respuesta = respuesta.lower()
            retorno = respuesta
    
    return retorno


def cargar_json(path:str) -> list:
    '''
    La funcion importa los datos del json.
    Recibe por parametro la URL del json.
    Retorna la lista que contiene.
    '''
    with open(path, "r") as file:

        dicc = json.load(file)

    return dicc["results"]


lista_personajes = cargar_json(r"1er_parcial\data.json")

# print(lista_personajes)

def mostrar(lista:list,clave:str) -> str:
    '''
    La funcion imprime un mensaje.
    Recibe por parametro la lista.
    Retorna el mensaje.
    '''
    mensaje = ""
    for heroe in lista:

        mensaje += "Nombre:{0}, {1}:{2}\n".format(heroe["name"],clave,heroe[clave])

    return mensaje

def normalizar_datos(lista:list) -> list:
    '''
    La funcion normaliza los datos, pasando los de tipo str a enteros.
    Recibe por parametro la lista de heroes.
    Retorna la lista normalizada.
    '''

    if(type(lista) == type(list()) and len(lista) > 0):

        lista_copia = lista.copy()

        for heroes in lista_copia:

            heroes["height"] = int(heroes["height"])
            heroes["mass"] = int(heroes["mass"])



        return lista_copia

        # return lista


# lista_personajes = normalizar_datos(normalizar_datos(lista_personajes))
# print(lista_personajes)

def buscar_min_max(lista:list,clave:str,orden:str) -> int:
    '''
    La funcion busca el minimo o maximo segun quiera.
    Recibe por parametro la lista, la clave a buscar y el orden.
    Retorna el indice minimo o maximo.
    '''

    retorno = -1

    if(type(lista) == type(list()) and len(lista) > 0):

        lista_copia = lista.copy()

        min_max_i = 0

        for i in range(len(lista_copia)):

            if((orden == "asc" and lista_copia[i][clave] < lista_copia[min_max_i][clave]) or (orden == "desc" and lista_copia[i][clave] > lista_copia[min_max_i][clave])):

                min_max_i = i

        retorno = min_max_i
        return retorno




def ordenar_heroes_por_clave(lista:list,clave:str,orden:str) -> list:
    '''
    La funcion lista a los personajes por la clave que se coloque.
    Recibe por parametro la lista y la clave.
    Retorna la lista ordenada.
    '''
    retorno = -1
    if(type(lista) == type(list()) and len(lista) > 0):

        lista_copia = lista.copy()


        for i in range(len(lista_copia)):         

            min_max_i = buscar_min_max(lista_copia[i:],clave,orden) + i

            lista_copia[i],lista_copia[min_max_i] = lista_copia[min_max_i],lista_copia[i]

        retorno = lista_copia

        return retorno

    
# print(ordenar_heroes_por_clave(lista_personajes,"height","asc"))




def mostar_personaje_mas_alto_genero(lista:list,genero:str):
    '''
    Muestra el mensaje mas alto por genero.
    Recibe por parametro la lista.
    Retorna el personaje mas alto.
    '''

    if(type(lista) == type(list()) and len(lista) > 0):

        for heroe in lista:

            if(heroe["gender"] == genero):

                heroe_name = heroe["name"]
                break
        
        return heroe_name


def buscador_personajes(lista:list,respuesta:str) -> dict:
    '''
    La funcion busca al personaje deseado.
    Recibe por parametro la lista de personajes.
    '''

    for heroe in lista:

        heroe_buscado = re.search(respuesta,heroe["name"],re.IGNORECASE)

        if(heroe_buscado != None):

            print(heroe)


def exportar_csv(lista:list):
    '''
    La funcion exporta la lista a un archio csv.
    Recibe por parametro la lista.
    '''


    with open("1er_parcial/archivo.csv","w") as file:

        mensaje = "name, height, mass, gender\n"
        for heroe in lista: 

            mensaje += "{0}, {1}, {2}, {3}\n".format(heroe["name"],heroe["height"],heroe["mass"],heroe["gender"])
        

        file.write(mensaje)




# sumar = lambda a: int(a)


# print(sumar("2"))







