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
    
    else:
        retorno = False
    
    return retorno



def importar_json(path:str) -> list:
    '''
    La funcion importa los datos del json.
    Recibe por parametro la URL del json.
    Retorna la lista que contiene.
    '''

    pass


