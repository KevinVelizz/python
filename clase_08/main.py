
from cgi import print_arguments
from cmath import pi
import json
import re

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

    for heroe in lista:

        if(heroe["genero"] == "M"):

            primer_heroe_m = heroe
            break

    return primer_heroe_m


# print(primer_heroe_masculino(lista_heroes))


def primer_heroe_femenino(lista:list)->dict:
    for heroe in lista:
        if(heroe["genero"] == "F"):

            primer_heroe_f = heroe
            break
    
    return primer_heroe_f
            

# print(primer_heroe_femenino(lista_heroes))





def mostar_nombre_masculino(lista_heroes:list):

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


print(stark_menu_principal_desafio_cinco())

#-----------Punto 1.3---------------------

def stark_marvel_app_cinco(lista:list):
    
    letra_recibida = stark_menu_principal_desafio_cinco()

    respuesta = True

    while(respuesta == True):
        
        if(letra_recibida == -1):
        
            print("N/A")
            continue
    
        letra_recibida = letra_recibida.upper()

        if(letra_recibida == "A"):
            mostar_nombre_masculino(lista)
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

# stark_marvel_app_cinco(lista_heroes)




#-----------Punto 1.5---------------------

def guardar_archivo(nombre_archivo:str, contenido:str):


    retorno = True
    retorno = "Se creó el archivo: " + nombre_archivo

    if (re.search("(.json|.csv)$", nombre_archivo) != None):
        with open (nombre_archivo, "w+") as archivo:
            informacion_almacenada = archivo.write(contenido)
        if(informacion_almacenada == len(contenido)):

            print("se guardó")
            retorno = True
        
    else:
        retorno = False
    
    return retorno

# print(guardar_archivo("clase_08\heroes_data.csv", "asdsa"))

#-----------Punto 1.6---------------------

def capitalizar_palabras(palabras:str):

    lista_palabras = set(re.findall("[a-zA-Z]+" ,palabras))
    
    for palabra in lista_palabras:

        palabras_capitalizadas = palabra.capitalize()

        palabras = re.sub(palabra, palabras_capitalizadas, palabras)
    
    
    return palabras


    # for palabra in lista_palabras:

# capitalizar_palabras("23asdsa sadas aa")

#-----------Punto 1.7---------------------


def obtener_nombre_capitalizado(heroe:dict) -> str:
    '''
    '''
    nombre_formatear = capitalizar_palabras(heroe["nombre"])
    # print(nombre_formatear)
    nombre_formateado = "Nombre: {0}".format(nombre_formatear)

    return nombre_formateado

# obtener_nombre_capitalizado(lista_heroes[0])





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

#-----------Punto 1.8---------------------

def obtener_nombre_y_dato(heroe:dict, key:str) -> str:

    nombre = obtener_nombre_capitalizado(heroe)

    return "{0} | {1} {2}".format(nombre ,key, heroe[key])


# obtener_nombre_y_dato(lista_heroes[0], "altura")



#-----------Punto 2.1---------------------

def es_genero(heroe:dict, genero:str):

    # print(heroe["genero"] == genero)
    return (heroe["genero"] == genero)


    # if(heroe["genero"] == genero):
    #     retorno = True
    
    # else:
    #     retorno = False
    
    # return retorno

# es_genero(lista_heroes[4], "F")


#-----------Punto 2.2---------------------

def stark_guardar_heroe_genero(lista_heroes:list, genero:str):

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

    for heroe in lista:

        if(es_genero(heroe, genero)):

            primer_heroe_dato = heroe[clave]
            heroe_min = heroe
            break

    for heroe in lista:

        if(heroe[clave] < primer_heroe_dato):

            primer_heroe_dato = heroe[clave]
            heroe_min = heroe
        
    return heroe_min
            


#-----------Punto 3.2---------------------


def calcular_max_genero(lista:list, clave:str, genero:str) -> dict:


    for heroe in lista:

        if(es_genero(heroe, genero)):

            primer_heroe_dato = heroe[clave]
            heroe_max = heroe
        
    for heroe in lista:

        if(heroe[clave] > primer_heroe_dato):

            primer_heroe_dato = heroe[clave]
            heroe_max = heroe

    
    return heroe_max































def inicio(lista:list):

    stark_normalizar_datos(lista)

    stark_marvel_app_cinco(lista)

    # heroe = calcular_altura_mas_alta(lista)
    
    # print(obtener_nombre_y_dato(lista[0], "altura"))

    # calcular_min_genero(lista, "peso", "M")
    # print(calcular_max_genero(lista, "peso", "M"))
    # print(stark_guardar_heroe_genero(lista, "M"))

inicio(lista_heroes)