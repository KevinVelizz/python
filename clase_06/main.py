
import re
from data_stark_06 import lista_personajes 

'''
 {
    "nombre": "Deadpool",
    "identidad": "Wade Wilson",
    "empresa": "Marvel Comics",
    "altura": "188.0",
    "peso": "95.319999999999993",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "No Hair",
    "fuerza": "35",
    "inteligencia": "good"
  },

'''

# def extraer_iniciales(nombre_heroe:str) -> str:
    
#     '''
#     Extrae las inciales de los nombres.
#     Recibe por parametro un string.
#     Retorna un string.
#     '''
#     if(nombre_heroe.count("the") > 0):
#             nombre_heroe = nombre_heroe.replace("the", "")
            
#     elif(nombre_heroe.count("-") > 0):
#             nombre_heroe = nombre_heroe.replace("-", "")

#     elif(nombre_heroe == ""):
#         retorno = "N/A"

#     lista_nombre = nombre_heroe.split(" ")
#     print(lista_nombre)

#     inicial = " "

#     for elemento in lista_nombre:
#         # nombre_heroe = elemento["nombre"]
#         nombre = elemento[0:1]
#         inicial += "{0}.{1}".format(nombre)
#     print(inicial)

        
        
            
    

# extraer_iniciales("nombre")

# # def inicio(lista:list):
    
# #     nombre = extraer_iniciales(lista)


# #     print(nombre)

# # inicio(lista_personajes)








def extraer_iniciales(nombre_heroe:str) -> str:


    if(nombre_heroe == ""):
        retorno = "N/A"

    elif(type(nombre_heroe) == type(str()) and (len(nombre_heroe) > 0)):

        nombre_heroe = nombre_heroe.upper()
        nombre_heroe = nombre_heroe.replace("THE ", "")
        nombre_heroe = nombre_heroe.replace("-", " ")

        partes_nombre = nombre_heroe.split(" ")

        iniciales = ""

        for una_parte in partes_nombre:
            iniciales += una_parte[0] + "."

        retorno = iniciales


    return retorno

    

# print(extraer_inciales("Howard the Duck"))





def definir_iniciales_nombre(heroe:dict):

    aux_return = False

    if(type(heroe) == type(dict()) and "nombre" in heroe):
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        aux_return = True
    
        # print(heroe)
    return aux_return

# print(type(lista_personajes[0]))

# for heroe in lista_personajes:
#     print(definir_iniciales_nombre(heroe))



def agregar_iniciales_nombre(lista_heroes:list) -> list:

    retorno = False

    if(type(lista_heroes) == type(list()) and len(lista_heroes) > 0):

        for heroe in lista_heroes:
            definir_iniciales_nombre(heroe)
            
            if(not(definir_iniciales_nombre(heroe))):
                retorno = False
                break
            else:
                retorno = True
    else:
        print("El origen de datos no contiene el formato correcto")

    return retorno


# print(agregar_iniciales_nombre(lista_personajes))


def stark_imprimir_nombres_con_iniciales(lista_heroes:list) -> list:

    
    if(agregar_iniciales_nombre(lista_heroes)):

        for heroe in lista_heroes:
            # print(heroe)
            # print(heroe["iniciales"])
            print("* {0} ({1})".format(heroe["nombre"], heroe["iniciales"]))



# print(stark_imprimir_nombres_con_iniciales(lista_personajes))


#----------------2.1---------

def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    
    

    if(type(id_heroe) == type(int()) and (genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB")):


        relleno_largo = 10 - (len(genero_heroe) + 1)
        # print(relleno_largo)
        id_heroe = str(id_heroe).zfill(relleno_largo)


        id_genero_formateado = "{0}-{1}".format(genero_heroe,id_heroe)

        retorno = id_genero_formateado
    else:
        retorno = "N/A"

    return retorno
    # print(id_genero_formateado)

# print((generar_codigo_heroe(1,"asdasdas")))




def agregar_codigo_heroe(heroe:dict, id_heroe:int) -> dict:


    genero_heroe = heroe["genero"]

    codigo_heroe = generar_codigo_heroe(id_heroe, genero_heroe)
    
    if(len(heroe) > 0 and len(codigo_heroe) < 11):
        
        heroe["codigo_heroe"] = codigo_heroe

        retorno = True 

    else:
        retorno = False

    return retorno

# print(agregar_codigo_heroe(lista_personajes[1], 4))

# print(lista_personajes[1])


def stark_generar_codigos_heroes(lista_heroes:list) -> list:

    '''
    Genera los códigos para los heroes
    Recibe por para parametro una lista 
    Retorna una lista
    '''

    contador = 0
    for heroe in lista_heroes:

        contador = contador + 1

        agregar_codigo_heroe(heroe, contador)
        
        if(contador == 1):
          primer_heroe = heroe["codigo_heroe"]

    
    

    print("Se asignaron {0} códigos".format(contador))

    print("*El codigo del primer héroe es: {0}".format(primer_heroe))

    print("*El código del último héroe es: {0}".format(heroe["codigo_heroe"])) 

# stark_generar_codigos_heroes(lista_personajes)



#--------------Sanitizar datos---------------------





def sanitizar_entero(numero_str:str) -> int:

    '''
    La funcion transforma un entero tipo string a int
    Recibe por parametros un string
    Retorna un int
    '''
    encontar_numero_str = re.findall("[a-z]", numero_str)
    # print(encontar_numero_str)

    if(len(encontar_numero_str) == 0): 

        encontar_numero_str = re.findall("^[+-]?[0-9]+$", numero_str)
        print(encontar_numero_str)
        # print(encontar_numero_str)
        numero_str = numero_str.strip()

        # print(encontar_numero_str)
        if(len(encontar_numero_str) == 1):
            
            numero_str = int(numero_str)

            # print(type(numero_str))
            if(type(numero_str) == type(int())):

                if(numero_str > 0):
                    retorno = numero_str
                else:
                    retorno = -2
        else:
            retorno = -3
    else:
        retorno = -1        
        

    return retorno

# sanitizar_entero("20")


def sanitizar_flotante(numero_str:str) -> float:

    encontrar_numero_float = re.findall("[a-z]", numero_str)

    if(len(encontrar_numero_float) == 0):

        encontrar_numero_float = re.findall("^[+-]?[0-9]+(\.[0-9]+)?$", numero_str)


        if(len(encontrar_numero_float) == 1):
            numero_str = float(numero_str)

            if(numero_str > 0):
                retorno = numero_str
            else:
                retorno = -2   
        else:
            retorno = -3     
    else:
        retorno = -1

    return retorno

# print(sanitizar_flotante("20")) 

def sanitizar_string(valor_str:str, valor_por_defecto:str = "-"):

    encontar_string = re.findall("[0-9]", valor_str)

    valor_str = valor_str.replace("/", " ")

    
    if(valor_str == ""):
        valor_str = valor_por_defecto
        retorno = valor_str

    if(valor_str[0] == " " and valor_str[-1] == " "):
        valor_str = valor_str.strip()

    if(encontar_string == []):
       
            transformar_a_minuscula = valor_str.lower()
            retorno = transformar_a_minuscula

    else:
        retorno = "N/A"

    return retorno

# print(sanitizar_string("/sAd/"))

#------Validad enteros

# texto = ["-140", "+10", "20", "-10.52", "-40.32", "asd123"]

# for valor in texto:
#     if re.match("^[+-]?[0-9]+$", valor) is None:
#         print(f"{valor}: No se encontró coincidencia")
#     else:
#         print(f"{valor}: Se encontró coincidencia")


def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str) -> bool:

    
    tipo_dato = tipo_dato.lower()

    bandera = False

    for dato in heroe:
        # print(dato)
        if(dato == clave):
            bandera = True

    if(bandera == True):
        if(tipo_dato == "flotante"):

            heroe[clave] = sanitizar_flotante(heroe[clave])
            retorno = True

        elif(tipo_dato == "string"):    
            heroe[clave] = sanitizar_string(heroe[clave])
            retorno = True

        elif(tipo_dato == "entero"):
            heroe[clave] = sanitizar_entero(heroe[clave])
            retorno = True
        else:
            retorno = False
            print("Tipo de dato no reconocido")

    else:
        print("La clave especificada no existe en el héroe")

    
    return retorno

    # print(heroe)

    



# sanitizar_dato(lista_personajes[0], "altura", "sadas")
# print(lista_personajes[0])



#----------3.5------------------

def stark_normalizar_datos(lista_heroes:list):

    if(type(lista_heroes) == type(list())):

        for dato in lista_heroes:

            sanitizar_dato(dato, "altura", "flotante")
            sanitizar_dato(dato, "peso", "flotante")
            sanitizar_dato(dato, "color_ojos", "string")
            sanitizar_dato(dato, "color_pelo", "string")
            sanitizar_dato(dato, "fuerza", "entero")
            sanitizar_dato(dato, "inteligencia", "string")

            # print(dato)

        print("Datos normalizados")

    else:
         print("Error: Lista de héroes vacía")



# stark_normalizar_datos(lista_personajes)



#-------------4.1-----------------

def generar_indice_nombre(lista_heroes:list):
    '''
    La función genera indices 

    
    '''
    nombre = ""

    if(len(lista_heroes) > 0 and type(lista_heroes[0]) == type(dict())):
        for heroe in lista_heroes:
        
            nombre += heroe["nombre"] + " "

        lista_nombres = re.split(" ", nombre)

    else:
        print("El origen de datos no contiene el formato correcto") 

    print(lista_nombres)
    

# generar_indice_nombre(lista_personajes)





