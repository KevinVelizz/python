
import json
import re
from traceback import print_tb


'''
    {
      "nombre": "Howard the Duck",
      "identidad": "Howard (Last name unrevealed)",
      "empresa": "Marvel Comics",
      "altura": "79.349999999999994",
      "peso": "18.449999999999999",
      "genero": "M",
      "color_ojos": "Brown",
      "color_pelo": "Yellow",
      "fuerza": "2",
      "inteligencia": ""
    },
'''

#-----------Punto 1.4---------------------


url_archivo = r"clase_08\data_stark.json"

def leer_archivo(url_archivo:str) -> list:

    diccionario_json = {}

    with open(url_archivo, "r") as archivo:

        diccionario_json = json.load(archivo)
        
        lista_heroes = diccionario_json["heroes"]
        


    return lista_heroes


lista_heroes = leer_archivo(url_archivo)

# print(parse_json(url_archivo))




def primer_heroe_masculino(lista:list)->dict:
    '''
    Encuentra el primer heroe masculino.
    Recibe por parametro una lista.
    Retorna un diccionario.
    '''

    for heroe in lista:

        if(heroe["genero"] == "M"):

            primer_heroe_m = heroe
            break

    return primer_heroe_m


# print(primer_heroe_masculino(lista_heroes))


def primer_heroe_femenino(lista:list)->dict:
    '''
    La funcion encuentra el primer heroe femenino.
    Recibe por parametro una lista.
    Retorna un diccionario.
    '''

    for heroe in lista:
        if(heroe["genero"] == "F"):

            primer_heroe_f = heroe
            break
    
    return primer_heroe_f
            

# print(primer_heroe_femenino(lista_heroes))





def mostar_nombre_masculino(lista_heroes:list) -> str:
    '''
    La funcion muestra los nombres de los heroes masculinos.
    Recibe por parametro una lista.
    Retorna una string
    '''

    for heroe in lista_heroes:

        if(heroe["genero"] == "M"):

            print("Nombre:{0} | Genero: {1}".format(heroe["nombre"], heroe["genero"]))



def mostrar_nombre_femenino(lista_heroes:list):

    for heroe in lista_heroes:
        if(heroe ["genero"] == "F"):
            print("Nombre: {0} | Genero: {1}".format(heroe["nombre"], heroe["genero"]))
        


# mostar_nombre_masculino(lista_heroes)

# def mostrar_

#-----------Punto 1.1---------------------

def imprimir_dato(dato:str) -> str:

    print(dato)

def imprimir_menu_desafio_cinco():

    menu ="ingrese\nA - mostrar nombres masculinos\nB - mostrar nombres femeninos\nC - Calcular altura mas alta superheroe masculino\nD - Calcular altura mas alta superheroe femenino \nE - Calcular altura mas bajo superheroe masculino\nF - Calcular altura mas baja superheroe femenino\nG - Calcular promedio de altura superhores masculinos\nH - Calcular promedio de altura superheroes femeninos.\nI - Calcular nombre del superhéroe asociado a cada uno de los indicadores anteriores.\nJ - Calcular cuantos superheroes por tipo de color de ojos\nK - Calcular cuantos superheroes por tipo de color de pelo.\nL - Calcular cuantos superheroes tiene cada tipo de inteligencia\nM - Listar todos los superheroes agrupados por color de ojos\nN - Listar todos los superhéroes agrupados por color de pelo.\nO - Listar todos los superhéroes agrupados por tipo de inteligencia\nZ - Salir"


    imprimir_dato(menu)
    
#-----------Punto 1.2---------------------

def stark_menu_principal_desafio_cinco():

    imprimir_menu_desafio_cinco()

    elegir_letra = input("Ingrese una letra: ")

    

    if(re.search("[a-ozA-OZ]", elegir_letra)):
        retorno = elegir_letra

    else:
        retorno = -1
    
    if(len(elegir_letra) > 1):
        retorno = -1

    return retorno


# print(stark_menu_principal_desafio_cinco())

#-----------Punto 1.3---------------------

def stark_marvel_app_cinco(lista:list):



    while(True):
        
        letra_recibida = stark_menu_principal_desafio_cinco()

        if(letra_recibida != -1):

            letra_recibida = letra_recibida.upper()

            if(letra_recibida == "A"):
                mostar_nombre_masculino(lista)
                continue
            elif(letra_recibida == "B"):
                mostrar_nombre_femenino(lista)
            elif(letra_recibida == "C"):
                pass
            elif(letra_recibida == "D"):
                pass
            elif(letra_recibida == "E"):
                pass
            elif(letra_recibida == "F"):
                pass
            elif(letra_recibida == "G"):
                pass
            elif(letra_recibida == "H"):
                pass
            elif(letra_recibida == "I"):
                pass
            elif(letra_recibida == "J"):
                pass
            elif(letra_recibida == "K"):
                pass
            elif(letra_recibida == "L"):
                pass
            elif(letra_recibida == "M"):
                pass
            elif(letra_recibida == "N"):
                pass
            elif(letra_recibida == "O"):
                break

        else:
            print("N/A")

# stark_marvel_app_cinco(lista_heroes)




#-----------Punto 1.5---------------------

def guardar_archivo(nombre_archivo:str, contenido:str):
    '''
    La funcion crea un archivo.
    Recibe por parametros dos strings. 
    Retorna un boleano.
    Imprime un mensaje si se crea el archivo.
    '''

    

    if(re.search("(.json|.csv)$", nombre_archivo) != None):
        with open (nombre_archivo, "w+") as archivo:
            informacion_almacenada = archivo.write(contenido)
        if(informacion_almacenada == len(contenido)):
            print("Se creó el archivo: " + nombre_archivo)
            retorno = True
    else:
        retorno = False
    return retorno

# print(guardar_archivo("clase_08\heroes_data.csv", "Hola"))

#-----------Punto 1.6---------------------

def capitalizar_palabras(palabras:str) -> str:
    '''
    Capitaliza las palabras.
    Recibe como parametro.
    Retorna strings.
    '''

    lista_palabras = set(re.findall("[a-zA-Z]+" ,palabras))
    print(lista_palabras)
    
    for palabra in lista_palabras:

        palabras_capitalizadas = palabra.capitalize()

        palabras = re.sub(palabra, palabras_capitalizadas, palabras)
    
    
    return palabras


    # for palabra in lista_palabras:

# capitalizar_palabras("23asdsa sadas aa")

#-----------Punto 1.7---------------------


def obtener_nombre_capitalizado(heroe:dict) -> str:
    '''
    Reutiliza la funcion capitalizar_palabras.
    Recibe por parametro un diccioanario.
    Retorna los strings del diccionario capitalizado.
    '''

    nombre_formatear = capitalizar_palabras(heroe["nombre"])
    # print(nombre_formatear)
    nombre_formateado = "Nombre: {0}".format(nombre_formatear)

    return nombre_formateado

# obtener_nombre_capitalizado(lista_heroes[0])





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

#-----------Punto 1.8---------------------

def obtener_nombre_y_dato(heroe:dict, key:str) -> str:
    '''
    La funcion obtiene un nombre y un dato deseado.
    Recibe por parametros un diccionario y un string.
    Retorna un string.
    '''

    nombre = obtener_nombre_capitalizado(heroe)

    return "{0} | {1} {2}".format(nombre ,key, heroe[key])


# obtener_nombre_y_dato(lista_heroes[0], "altura")



#-----------Punto 2.1---------------------

def es_genero(heroe:dict, genero:str) -> bool:
    '''
    Valida que genero sea un valor deseado.
    Recibe por parametro un diccionario y un string.
    Retorna un verdero o falso.

    '''

    return (heroe["genero"] == genero)


#-----------Punto 2.2---------------------

def stark_guardar_heroe_genero(lista_heroes:list, genero:str):
    '''
    La funcion crea un archivo con el genero deseado.
    Retorna una lista y un string.
    Retorna el archivo.
    '''

    nombre = ""
    retorno = True


    for heroe in lista_heroes:

        if(es_genero(heroe, genero)):
            nombre += obtener_nombre_capitalizado(heroe) + ", "
            
            # for heroe in lista_heroes:
        else:
            retorno = False

    nombre = re.sub( ", $", "", nombre) 
    guardar_archivo("clase_08\heroes_" + genero + ".csv", nombre)

    return retorno

    # imprimir_dato(nuevo)


#-----------Punto 3.1---------------------

def calcular_min_genero(lista:list, clave:str, genero:str) -> dict:
  
    if(genero == "F"):
        heroe_min = primer_heroe_femenino(lista)
        primer_heroe = heroe_min[clave]
    elif(genero == "M"):
        heroe_min = primer_heroe_masculino(lista)
        primer_heroe = heroe_min[clave]  

    for heroe in lista:
        if(es_genero(heroe, genero) == True):  
            if(heroe["genero"] == genero):
                if(heroe[clave] < primer_heroe):
                    primer_heroe = heroe[clave]
                    heroe_min = heroe
        
        else:
            retorno = "N/A"
    
        retorno = heroe_min

    return retorno



#-----------Punto 3.2---------------------


def calcular_max_genero(lista:list, clave:str, genero:str) -> dict:

    if(genero == "F"):
        heroe_max = primer_heroe_femenino(lista)
        primer_heroe = heroe_max[clave]
    elif(genero == "M"):
        heroe_max = primer_heroe_masculino(lista)
        primer_heroe = heroe_max[clave]  

    for heroe in lista:
        if(es_genero(heroe, genero) == True):  
            if(heroe["genero"] == genero):
                if(heroe[clave] > primer_heroe):
                    primer_heroe = heroe[clave]
                    heroe_max = heroe
        else:
            retorno = "N/A"
    
        retorno = heroe_max

    return retorno

print(calcular_max_genero(lista_heroes,"altura","F"))

#-----------Punto 3.3---------------------

def calcular_max_min_dato(lista:list, clave:str, genero:str, tipo:str) -> str:

    if(type(lista) == type(list()) and len(lista) > 0):

        for heroe in lista:

            if(es_genero(heroe, genero) == True):

                if(heroe["genero"] == genero):
                    if(tipo == "minimo"):
                        heroe_max_min = calcular_min_genero(lista,clave,genero)
                        retorno = heroe_max_min
                    elif(tipo == "maximo"):
                        heroe_max_min = calcular_max_genero(lista,clave,genero)
                        retorno = heroe_max_min
            elif():

                retorno = "N/A"
    else:
        retorno = "N/A"
    
    return retorno


# print(calcular_max_min_dato(lista_heroes,"peso","M","maximo"))

#-----------Punto 3.4---------------------


def stark_calcular_imprimir_guardar_heroe_genero(lista:list, genero:str,clave:str,tipo:str) -> bool:
    '''
    Calcula y guarda el dato en un archivo csv.
    Recibe por parametro una lista y 3 strings.
    Retorna verdadero en caso de no haber error en caso contrario falso.
    '''
    

    genero = re.findall("[FfMm]+", genero)

    retorno = True

    if(type(lista) == type(list()) and len(lista) > 0):

        genero = genero[0].upper()
        clave = clave.lower()
        tipo = tipo.lower()

        if(clave == "peso" or clave == "altura" or clave == "fuerza"):
            dato = "Mayor"
            if(tipo == "minimo"):
                dato = "Menor"
            if(tipo == "minimo" or tipo == "maximo"):
                heroe_min_max = calcular_max_min_dato(lista,clave,genero[0],tipo)
                
                data_heroe = "{0} {1}: Nombre: {2} | {3}: {4}".format(dato, clave, heroe_min_max["nombre"], clave, heroe_min_max[clave])
            # imprimir_dato(data_heroe)

            guardar_archivo(f"clase_repaso\heroes_{tipo}_{clave}_{genero}.csv", data_heroe)
        else:
            retorno = False
    else:
        retorno = False
    
    return retorno


# stark_calcular_imprimir_guardar_heroe_genero(lista_heroes,"F", "altura", "minimo")

#-----------Punto 4.1---------------------

def sumar_dato_heroe_genero(lista:list, clave:str, genero:str) -> int:
    '''
    Suma los datos deseados.
    Recibe por parametro una lista, y 3 string.
    Retorna el dato o un -1 en caso de error
    '''
    if(type(lista) == type(list()) and len(lista) > 0):

        suma_de_datos = 0
        for heroe in lista:
            if(type(heroe) == type(dict()) and len(heroe) > 0 and heroe["genero"] == genero):
                # print(heroe[clave])
                if(type(heroe[clave]) == type(float()) or type(heroe[clave]) == type(int())):
                    datos = heroe[clave] 
                    suma_de_datos = suma_de_datos + datos
                    
                else: 
                    retorno = False
                    
                    # print(suma_de_datos)
            else:
                continue
        retorno = suma_de_datos
    else:
        retorno = False
    
    return retorno


#-----------Punto 4.2---------------------

def cantidad_heroes_genero(lista:list,genero:str)->int:
    '''
    La funcion calcula la cantidad total de hereo o heroinas, segun el sexo recibido.
    Recibe por parametro una lista y un string.
    Retorna un entero.
    '''

    contador = 0
    if(type(lista) == type(list()) and len(lista) > 0):
        genero = re.findall("[fFmM]", genero)
        genero = genero[0].upper()
        for heroe in lista:
            if(heroe["genero"] == genero):
                contador = contador + 1

    return contador

#-----------Punto 4.3---------------------

def calcular_promedio_genero(lista:list,clave:str,genero:str) -> int:
    '''
    La funcion calcula el promedio de las claves del genero deseado.
    Recibe por parametro una lista, y 2 strings.
    Retorna el promedio.
    '''

    if(type(lista) == type(list()) and len(lista) > 0):
        cantidad_total_heroes = cantidad_heroes_genero(lista,genero)

        suma_total = sumar_dato_heroe_genero(lista,clave,genero)

        promedio = suma_total / cantidad_total_heroes

    return promedio

#-----------Punto 4.4---------------------

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista:list,clave:str,genero:str) -> bool:
    '''
    La funcion guarda el promedio deseado de cada genero y la guarda en un archivo tipo csv.
    Recibe por parametro una lista y 2 strings.
    Retonra verdadero si se completo con exito, caso contrario falso.
    '''

    retorno = True
    if(type(lista) == type(list()) and len(lista) > 0):


        promedio_genero = calcular_promedio_genero(lista,clave,genero)
        
        print(type(promedio_genero))

        contenido = "{0} promedio {1}: {2:.2f}".format(clave.capitalize(),genero,promedio_genero)

        guardar_archivo(f"clase_08\heroe_promedio_{clave}_{genero}.csv",contenido)
    
    else:
        retorno = "Error: Lista de héroes vacía."
        return False
    
    return retorno


#-----------Punto 5.1---------------------



def app_stark(lista:list) -> str:

    stark_normalizar_datos(lista)

    print(stark_calcular_imprimir_guardar_promedio_altura_genero(lista,"altura","M"))

app_stark(lista_heroes)





