
from stark import lista_personajes 





#-------Funcion para normalizar datos que sean numericos 

def stark_normalizar_datos(lista:list) -> dict:


    
    if(type(lista) == type([]) and len(lista) > 0):
        # print(lista_personajes)

        for normalizar_datos in lista:
                
                normalizar_datos ["altura"] = float(normalizar_datos["altura"])

                normalizar_datos ["peso"] = float(normalizar_datos["peso"])
                
                normalizar_datos ["fuerza"] = int(normalizar_datos["fuerza"])

        print("Datos normalizados")
        
    else:
        print("Error: Lista de héroes vacía")

    # return normalizar_datos

# stark_normalizar_datos(lista_personajes, "altura")
# stark_normalizar_datos(lista_personajes, "peso")
# stark_normalizar_datos(lista_personajes, "fuerza")

# print(lista_personajes)


#--------------- Punto 1.1 -----------------

def obtener_nombre(heroe:dict) -> str:


    nombre_filtrado = heroe["nombre"]

    return nombre_filtrado


# print(obtener_nombre(lista_personajes[1]))



#--------------- Punto 1.2 -----------------

def imprimir_dato(dato:str) -> str:

    print(dato)


#--------------- Punto 1.3 -----------------

def stark_imprimir_nombre_heroes(lista:list):

    ''' 
    Recibe por parametros una lista
    Imprime el nombre de cada heroe

    '''
    if(lista):
        for heroe in lista:
            
            # stark_normalizar_datos(lista)

            imprimir_dato(obtener_nombre(heroe))

        # print(lista_personajes)
            
    else:
        return -1 

# stark_imprimir_nombre_heroes(lista_personajes)


#--------------- Punto 2 -----------------

def obtener_nombre_y_dato(heroe:dict, key:str) -> str:

    return "Nombre:{0} | {1} {2}".format(heroe["nombre"],key, heroe[key])



def prueba(lista:list):

    for heroe in lista:
         imprimir_dato(obtener_nombre_y_dato(heroe, "fuerza"))

# prueba(lista_personajes)

#--------------- Punto 3 -----------------

def stark_imprimir_nombres_alturas(lista:list):

    if lista:    
        for heroe in lista:

            imprimir_dato(obtener_nombre_y_dato(heroe, "altura"))
    else:
        return -1


# stark_imprimir_nombres_alturas(lista_personajes)


#--------------- Punto 4.1 -----------------

def calcular_max(lista:list, clave:str):

    retorno = -1

    heroe_maximo = lista[0]
    

    if(type(lista) == type(list())):
        maximo = lista[0][clave]
        for heroe in lista:
            if(heroe[clave] > maximo):
                heroe_maximo = heroe
                maximo = heroe[clave]
        
        retorno = heroe_maximo
    
    return retorno


#--------------- Punto 4.2 -----------------

def calcular_min(lista:list, clave:str):

    retorno = -1

    heroe_minimo = lista[0]

    if(type(lista) == type(list())):

        minimo= lista[0][clave]
        for heroe in lista:
            if(heroe[clave] < minimo): 
                heroe_minimo = heroe   
                minimo = heroe[clave]

        retorno = heroe_minimo
    return retorno

#--------------- Punto 4.3 -----------------

def calcular_max_min(lista:list, clave:str, tipo:str) -> dict:


    if(tipo == "maximo"):
        retorno = calcular_max(lista,clave)
    elif(tipo == "minimo"):
        retorno = calcular_min(lista,clave)

    
    return retorno



# def calcular_altura_mas_alta(lista:list):



#     heroe = calcular_max(lista, "altura")

#     # print(altura)
#     return heroe
    

# calcular_altura_mas_alta()


# def calcular_altura_minima(lista:list):

#     heroe = calcular_max_min(lista, "altura", "minimo")

#     return heroe

#----------Punto 4.4-------------

def stark_calcular_imprimir_heroe(lista:list, tipo:str, clave:str):

    tipo = tipo.lower()
    
    if(len(lista) > 0):

        dato = "mayor"
        if(tipo == "minimo"):
            dato = "menor"
        if(tipo == "minimo" or tipo == "maximo"):
            heroe_minimo_maximo = calcular_max_min(lista,clave,tipo)
            heroe_min_max = obtener_nombre_y_dato(heroe_minimo_maximo,clave)
            # print(heroe_min_max)
            imprimir_dato("{0} {1}: {2}".format(dato, clave, heroe_min_max ))


def inicio(lista:list):

    stark_normalizar_datos(lista)

    # heroe = calcular_altura_mas_alta(lista)
    heroe_bajo = stark_calcular_imprimir_heroe(lista, "minimo", "peso")

    print(heroe_bajo)

inicio(lista_personajes)









    






