

import re
import json



path = r"C:\Users\veliz\Desktop\python\dale_vos_podes\data.json"
def importar_json(path:str) -> list:
    '''
    La funcion importa los datos del json.
    Recibe por parametro la URL del json.
    Retorna la lista que contiene el json.
    '''

    with open(path,"r") as file:

        diccionario = json.load(file)

    return diccionario["heroes"]



lista_heroes = importar_json(path)



def validar_lista(lista:list) -> bool:
    '''
    La funcion valida que la lista sea de tipo lista y que contenga mas de 0 elementos.
    Recibe por parametro la lista.
    Retorna un booleano.
    '''

    retorno = True

    if(type(lista) == type(list()) and len(lista) > 0):
        for heroe in lista:
            if(type(heroe) != type(dict())):
                retorno = False
                break
    
    else:
        retorno = False
    
    return retorno


# print(lista_heroes)

def mostrar_dato(dato:str):
    '''
    La funcion imprime.
    Recibe el dato a imprimir.
    '''

    print(dato)

def mostrar(lista:list,clave:str) -> str:
    '''
    La funcion itrea la lista y imprime los datos.
    Recibe por parametro la lista y clave ingresada.
    Retorna un mensaje tipo str
    '''

    mensaje = ""
    for heroe in lista:
        mensaje += "Nombre: {0}, {1}: {2}\n".format(heroe["nombre"], clave, heroe[clave])

    return mensaje

def validar_respuesta(respuesta:str,expresion_regular:str):

    '''
    La funcion valida la respuesta ingresada por medio de regEx.
    Recibe por parametro la respuesta ingresada y la expresion.
    Retorna un -1 en caso de no cumplir con la validacion y un mensaje en caso contrario.
    '''

    retorno = -1
    if(respuesta):
        if(re.match(expresion_regular,respuesta,re.IGNORECASE)):
            retorno = respuesta

    return retorno

def listar_primero_heroes(lista:list,cantidad:int) ->list:
    '''
    La funcion lista a los primero heroes de la lista segun la cantidad ingresada.
    Recibe por parametro la lista y la cantidad.
    Retorna una lista.
    '''
    lista_copia = lista[:cantidad].copy()

    return lista_copia


def imprimir_listar_dato(lista:list) ->list:
    '''
    La funcion 
    '''

    if(validar_lista(lista)):

        cantidad = input("Ingrese la cantidad: ")

        cantidad_parseo = int(validar_respuesta(cantidad,"^[0-9]{1,2}$"))

        if(cantidad_parseo != -1):

            if(cantidad_parseo < len(lista)):

                lista = (listar_primero_heroes(lista,cantidad_parseo))

                nombre = ""
                for heroe in lista:

                    nombre += heroe["nombre"] + "\n"

                mensaje = nombre
                print(mensaje)
                return lista
                
            else:
                print("N/A")
    else:

        print("N/A")

# listar_primero_heroes(lista_heroes,"2")


def buscar_min_max(lista:list,clave:str,orden:str):

    retorno = -1

    if(len(lista) > 0):

        min_max = 0

        for i in range(len(lista)):
            if(((orden == "asc" or orden == "menor") and lista[i][clave] < lista[min_max][clave]) or ((orden == "desc" or orden == "mayor") and lista[i][clave] > lista[min_max][clave])):

                min_max = i

        retorno = min_max

        return retorno



def ordenar_lista_clave(lista:list,clave:str,orden:str) -> list:
    '''
    La funcion ordena la lista por clave ingresada y según el orden ingresado.
    Recibe por parametro la lista, la clave y el orden.
    Retorna la lista ordenada.
    '''

    lista_copia = lista.copy()
    for i in range(len(lista)):

        max_min = buscar_min_max(lista_copia[i:],clave,orden) + i

        lista_copia[i],lista_copia[max_min] = lista_copia[max_min],lista_copia[i]

    return lista_copia
   

    


def imprimir_lista_ordenada(lista:list,clave:str) -> list:
    '''
    La funcion imprime la lista ordenada segun la clave.
    Recibe por parametro la lista y la clave.
    Retorna una lista e imprime un mensaje.
    '''

    if(validar_lista(lista)):

        condicion = input("Ingrese asc o desc: ")

        condicion_validada = validar_respuesta(condicion,"^asc|desc$")

        if(condicion_validada != -1):

            condicion_validada = condicion_validada.lower()
            lista = ordenar_lista_clave(lista,clave,condicion_validada)

            mensaje = mostrar(lista,clave)
            print(mensaje)
            return lista
        else:
            print("N/A")
    else:
        print("N/A")


# print(ordenar_lista_altura(lista_heroes,"altura","asc"))


def calcular_promedio(lista:list,clave:str,orden:str) -> str:
    '''
    La funcion calcular el promedio.
    Recibe por parametro la lista, la clave deseada y el orden ingresado.
    Retorna la lista segun el orden ingresado y la clave.
    '''

    contador = len(lista)
    acumulador = 0

    lista_promedio = []

    if(type(lista) == type(list()) and len(lista) > 0):

        lista_copia = lista.copy()

        for heroe in lista_copia:

            acumulador += heroe[clave]


        promedio = acumulador / contador
        print("El promedio es: {0}".format(promedio))

        for heroe in lista_copia:

            if((promedio > heroe[clave]) and orden == "menor"):
                
                lista_promedio.append(heroe)
            
            elif((promedio < heroe[clave]) and orden == "mayor"):

                lista_promedio.append(heroe)
        
    else:
        retorno = "N/A"


    retorno = lista_promedio

    return retorno


def imprimir_dato_promedio(lista:list) ->str:
    '''
    La funcion pide por consola la condicion mayor o menor y la clave para poder mostrar los que pertences a la condicion.
    Recibe por parametro la lista.
    Retorna un mensaje, aquellos que sean menor o mayor que el promedio.
    '''

    condicion_mayor_menor = input("Ingrese menor o mayor: ")
    condicion_clave = input("Ingrese altura o peso o fuerza: ")

    condicion_mayor_menor = validar_respuesta(condicion_mayor_menor,"^mayor|menor$")
    condicion_clave = validar_respuesta(condicion_clave,"^altura|peso|fuerza$")

    if((condicion_mayor_menor and condicion_clave) != -1):

        lista = calcular_promedio(lista,condicion_clave,condicion_mayor_menor)

        mensaje = mostrar(lista,condicion_clave)

        print(mensaje)

        return lista



def listar_heroes_inteligencia(lista:list,tipo:str) -> list:
    '''
    La funcion busca y crea una lista según el tipo de inteligencia ingresado.
    Recibe por parametro la lista de heroes y el tipo.
    Retorna la lista con los datos del tipo correspondiente.
    '''

    lista_copia = lista.copy()

    lista_inteligencia = []

    if(type(lista) == type(list()) and len(lista) > 0):

        for heroe in lista_copia:

            tipo_enviada = re.search(tipo,heroe["inteligencia"],re.IGNORECASE)
            if(tipo_enviada != None):

                lista_inteligencia.append(heroe["nombre"])

        retorno = lista_inteligencia

    else:
        retorno = "N/A"

        
    return retorno


def exportar_lista(lista:list):

    '''
    La funcion exporta la lista ingresada a un archivo csv.
    Recibe por parametro la lista.
    '''
    
    with open("dale_vos_podes/archivo_heroes.csv", "w") as file:

        mensaje = "nombre, identidad, altura, peso, fuerza, inteligencia\n"

        for heroe in lista:

            mensaje += "{0}, {1}, {2}, {3}, {4}, {5}\n".format(heroe["nombre"],heroe["identidad"],heroe["altura"],heroe["peso"],heroe["fuerza"],heroe["inteligencia"])

        file.write(mensaje)
