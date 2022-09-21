
import json
import re
from funciones import mostar_nombre_masculino




def parse_json(url_archivo:str) -> list:

    diccionario_json = {}

    with open("clase_08\data_stark.json", "r") as archivo:

        diccionario_json = json.load(archivo)
        # print(diccionario_json)
        lista_heroes = diccionario_json["heroes"]
        # print(lista_heroes)


    return lista_heroes

# url_archivo = parse_json(r"C:\Users\veliz\Desktop\python\clase_08\data_stark.json")



# print(parse_json(url_archivo))

def imprimir_dato(dato:str) -> str:

    print(dato)


def mostar_nombre_masculino(lista_heroes:list):

    for heroe in lista_heroes:

        if(heroe["genero"] == "M"):

            print("Nombre:{0} | Genero: {1}".format(heroe["nombre"], heroe["genero"]))

    # print(heroe)

mostar_nombre_masculino()


def imprimir_menu_desafio_cinco():
  
    

    menu ="ingrese\nA - mostrar nombres masculinos\nB - mostrar nombres femeninos\nC - Calcular altura mas alta superheroe masculino\nD - Calcular altura mas alta superheroe femenino \nE - Calcular altura mas bajo superheroe masculino\nF - Calcular altura mas baja superheroe femenino\nG - Calcular promedio de altura superhores masculinos\nH - Calcular promedio de altura superheroes femeninos.\nI - Calcular nombre del superhéroe asociado a cada uno de los indicadores anteriores.\nJ - Calcular cuantos superheroes por tipo de color de ojos\nK - Calcular cuantos superheroes por tipo de color de pelo.\nL - Calcular cuantos superheroes tiene cada tipo de inteligencia\nM - Listar todos los superheroes agrupados por color de ojos\nN - Listar todos los superhéroes agrupados por color de pelo.\nO - Listar todos los superhéroes agrupados por tipo de inteligencia\nZ - Salir"


    imprimir_dato(menu)

    
    


def stark_menu_principal_desafio_cinco():

    imprimir_menu_desafio_cinco()

    elegir_letra = input("Ingrese una letra: ")

    if(re.search("[a-ozA-OZ]", elegir_letra)):
        retorno = elegir_letra

    else:
        retorno = -1

    return retorno
    

# print(stark_menu_principal_desafio_cinco())


def stark_marvel_app_5(lista_heroes:list):

    letra_recibida = stark_menu_principal_desafio_cinco()

    

    if(letra_recibida == -1):
        
        print("N/A")
        pass

    letra_recibida = letra_recibida.upper()

    if(letra_recibida == "A"):
       mostar_nombre_masculino(lista_heroes)
    elif(letra_recibida == "B"):
        pass
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
        pass




# stark_menu_principal_desafio_cinco()

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


# url_archivo = parse_json(r"C:\Users\veliz\Desktop\python\clase_08\data_stark.json")