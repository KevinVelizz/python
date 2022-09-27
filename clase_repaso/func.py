
import json
import re


path = r"C:\Users\veliz\Desktop\python\clase_repaso\data.json"

def cargar_json(path:str) -> list:
    with open(path, "r") as file:
        buffer_dict = json.load(file)
    # print(buffer_dict)

    return buffer_dict["heroes"]


lista_heroes = cargar_json(path)

def stark_normalizar_datos(lista:list) -> dict:
    '''
    Normaliza los datos de la lista.
    Recibe por parametros una lista.
    Retorna un diccionario.
    '''


    
    if(type(lista) == type([]) and len(lista) > 0):
        # print(lista_personajes)

        for normalizar_datos in lista:
                
                normalizar_datos ["altura"] = float(normalizar_datos["altura"])

                normalizar_datos ["peso"] = float(normalizar_datos["peso"])
                
                normalizar_datos ["fuerza"] = int(normalizar_datos["fuerza"])

        print("Datos normalizados")
        
    else:
        print("Error: Lista de héroes vacía")


# for heroe in lista_heroes:
#     stark_normalizar_datos(lista_heroes)
#     print(heroe)

def mostar(lista:list):
    print("\n")
    for elemento in lista:
        print("{0} - {1} - {2}".format(elemento["nombre"], elemento["identidad"], elemento["peso"]))
    print("\n")


def buscar_minimo_max(lista:list, clave:str,order:str)->int:
    '''
    Buscar un minimo en una lista de elementos dict con clave "length".
    Recibe por parametro una lista de elementos dict con clave -clave-.
    Retorna el indice del elemento minimo o -1 en caso de error.
    '''
    # stark_normalizar_datos(lista)
    # print(lista)

    retorno = -1
    if(len(lista) > 0):
        i_min_max = 0
        for i in range(len(lista)): #que itere desde la posicion 1
            if(order == "down" and lista[i][clave] < lista[i_min_max][clave]) or (order == "up" and lista[i][clave] > lista[i_min_max][clave]):
                i_min_max = i
        retorno = i_min_max
    return retorno

# print(buscar_minimo_max(lista_heroes,"altura", "up"))


def nahuel_sort_repaso(lista:list, clave:str, order:str="up") -> list:

    # stark_normalizar_datos(lista)

    lista_ordenar = lista.copy()
    lista_ordenada = []

    while(len(lista_ordenar) > 0):
        index_min_max = buscar_minimo_max(lista_ordenar,clave,order)
        lista_ordenada.append(lista_ordenar.pop(index_min_max))

    return lista_ordenada

# print(nahuel_sort_repaso(lista_heroes,"altura","up"))

def nahuel_sort_improve(lista:list, key:str, order:str="up") -> list:

    lista_ordenada = lista.copy()
    for i in range(len(lista_ordenada)):
        index_min_max = buscar_minimo_max(lista_ordenada[i:],key,order) + i
        lista_ordenada[i], lista_ordenada[index_min_max] = lista_ordenada[index_min_max],lista_ordenada[i]  
    return lista_ordenada

# ignorecase ignora el tipo de letra, mayus,etc.


def buscar(lista:list,patron:str):
    print("\n")
    for elemento in lista:
        match = re.search(patron,elemento["nombre"],re.IGNORECASE != None)
        if(match):
            nombre = elemento["nombre"]
            palabra ="\033[0;31m" + match.group(0) + "\033[0;m" 
            nombre = nombre.replace(match.group(0), palabra)

            print("{0} - {1} - {2}".format(elemento["nombre"], elemento["fuerza"], elemento["altura"]))
    print("\n")




def exportar_csv(lista:list, path:str):

    with open(path,"w") as file:
        for elemento in lista:
            file.write("{0} - {1} - {2}\n".format(elemento["nombre"], elemento["fuerza"], elemento["altura"]))


#abrir,mostar,buscar,guardar en un csv
#validar numeros funciones numeros, letras, flotantes, una sola letra. 
#doble validacion para encontar el minino o mayor.
#validar letras.


def validar_num(dato:str) -> str:

    dato = re.match("^[-+]?[0-9]+$", dato)

    print(dato)

validar_num("24")