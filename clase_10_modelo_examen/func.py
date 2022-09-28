
import re
import json


path = f"clase_10_modelo_examen\data_stark.json"

def cargar_json(path:str) -> list:
    '''
    La funcion trae informacion del archivo json.
    Recibe por parametro un string que es la URL donde se encuentra la información.
    Retorna una Lista.
    '''

    with open(path, "r") as file:
        dicc = json.load(file)

    
    return dicc["heroes"]



lista_heroes = cargar_json(path)

def mostrar(lista:list,clave:str) -> str:
    '''
    Muestra el nombre y dato.
    Recibe por parametro uan lista y un string.
    Retorna un string
    '''
    mensaje = ""
    for heroe in lista:
        mensaje += ("nombre: {0}, {1}: {2}\n".format(heroe["nombre"], clave, heroe[clave]))
    return mensaje
    

def mostrar_dato(dato:str)->str:
    '''
    Imprime el dato ingresaro.
    Recibe por parametro un string.
    Retorna un string.
    '''
    
    print(dato)


def validar_respuesta(respuesta:str,patron_regex:str):
    if respuesta:
        if(re.match(patron_regex,respuesta,re.IGNORECASE)):
            return respuesta
    return -1


# print(validadcion_num("44"))

def listar_heroes(lista:list, cantidad:str)-> str:
    '''
    Lista los seleccion recibidos por el usuario.
    Recibe por parametro una lista.
    Retorna un listado con la cantidad recibida.
    '''
    lista_ordenar = lista[:cantidad].copy()

    
    
    return lista_ordenar


def buscar_max_min(lista:list,clave:str,orden:str) -> int:

    '''
    Buscar el maximo o minimo dependiendo lo ingresado.
    Recibe por parametro una lista y 2 string.
    Retorna un entero
    '''
    retorno = -1
    if(len(lista) > 0):

        i_min_max = 0

        for i in range(len(lista)):
            if((orden == "asc" and lista[i][clave] < lista[i_min_max][clave]) or (orden == "desc" and lista[i][clave] > lista[i_min_max][clave])):
                i_min_max = i
        
        retorno = i_min_max
    
    return retorno



# print(buscar_max_min(lista_heroes,"altura","up"))

def listar_ordernar_heroe(lista:list,clave:str,orden:str) -> list:
    '''
    La funcion ordena la lista recibida.
    Recibe por parametro una lista, y 2 strings.
    Retorna la lista ordenada.
    '''
    if(type(lista) == type(list()) and len(lista) > 0):

        lista_ordernar = lista.copy()

        for i in range(len(lista)):
            index_min_max = buscar_max_min(lista_ordernar[i:],clave,orden) + i
            lista_ordernar[i],lista_ordernar[index_min_max] = lista_ordernar[index_min_max],lista_ordernar[i]

        retorno = lista_ordernar
    else: 
        retorno = "N/A"

    return retorno




def calcular_promedio(lista:list, clave:str,condicion) -> list:

    lista_copia = lista.copy()

    lista_promedio = []

    cantidad_heroes = len(lista)

    acumulador_dato = 0

    for heroe in lista_copia:
        acumulador_dato += heroe[clave]

    
    promedio = acumulador_dato / cantidad_heroes

    # print("El promedio de {0} es: {1}".format(clave, promedio))

    for heroe in lista_copia:
        if((heroe[clave] < promedio) and condicion == "menor"):

            lista_promedio.append(heroe)   

        elif((heroe[clave] > promedio) and condicion == "mayor"):
        
            lista_promedio.append(heroe)
    
    # print(lista_promedio)
    
    return lista_promedio
            
# calcular_promedio(lista_heroes,"altura","mayor")

def buscar_listar_heroe_inteligencia(lista:list,condicion:str) -> list:


    lista_inteligencia = []

    for heroe in lista:
        if(heroe["inteligencia"] == condicion):

            lista_inteligencia.append(heroe["nombre"])
    
    return lista_inteligencia


def exportar_csv(mensaje:str):

    with open ("archivo.csv", "w") as file:
        mensaje = file.write(mensaje)
