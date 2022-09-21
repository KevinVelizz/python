from data_stark import lista_personajes


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

#---------------Altura Maxima-------------------------

def calcular_altura_maxima():

    superheroe_mas_alto = lista_personajes[0]
    altura_heroe_mas_alto = float(superheroe_mas_alto["altura"])


    for superheroe in lista_personajes:
        # print(lista_personajes["nombre"])
        # print(lista_personajes["altura"])
        superheroe["altura"] = float(superheroe["altura"])
        if(superheroe["altura"] > altura_heroe_mas_alto):
            altura_heroe_mas_alto = superheroe["altura"]
            nombre_mas_alto = superheroe["nombre"]
            
    print("nombre: {0} - Altura: {1}".format(nombre_mas_alto,altura_heroe_mas_alto))





#---------------Altura minima-------------------------

def calcular_altura_minma():

    superheroe_mas_bajo = lista_personajes[0]
    
    altura_heroe_mas_bajo = float(superheroe_mas_bajo["altura"])

    nombre_mas_bajo = superheroe_mas_bajo["nombre"]


    for superheroe in lista_personajes:
        superheroe["altura"] = float(superheroe["altura"])
        if(superheroe["altura"] < altura_heroe_mas_bajo):
            altura_heroe_mas_bajo = superheroe["altura"]
            nombre_mas_bajo = superheroe["nombre"]
            
    print("nombre: {0} - Altura: {1}".format(nombre_mas_bajo,altura_heroe_mas_bajo))






# #----------------Altura promedio------------


def calcular_altura_promedio():
    contador_altura = 0
    acumulador_altura = 0

    for heroe in lista_personajes:
        heroe = float(heroe["altura"])

        acumulador_altura += heroe
        contador_altura += 1


    print("Altura promedio: {0}".format(acumulador_altura / contador_altura))






#---------------------El mas pesado-------------------------


def calcular_peso_maximo():

    superheroe_mas_pesado = lista_personajes[0]
    heroe_mas_pesado = float(superheroe_mas_pesado["peso"])


    for superheroe in lista_personajes:
        # print(lista_personajes["nombre"])
        # print(lista_personajes["peso"])
        superheroe["peso"] = float(superheroe["peso"])
        if(superheroe["peso"] > heroe_mas_pesado):
            heroe_mas_pesado = superheroe["peso"]
            nombre_mas_alto = superheroe["nombre"]
            
    print("nombre: {0} - peso: {1}".format(nombre_mas_alto,heroe_mas_pesado))








#---------------Perso minima-------------------------

def calcular_peso_minimo():

    superheroe_menos_pesado = lista_personajes[0]
    heroe_menos_pesado = float(superheroe_menos_pesado["peso"])

    for superheroe in lista_personajes:
        superheroe["peso"] = float(superheroe["peso"])
        if(superheroe["peso"] < heroe_menos_pesado):
            heroe_menos_pesado = superheroe["peso"]
            nombre_mas_pesado = superheroe["nombre"]

    print("nombre: {0} - peso: {1}".format(nombre_mas_pesado,heroe_menos_pesado))



#------------crear menu-------------


respuesta = "si"

while(respuesta == "si"):

    pedir_dato = input("ingrese\n1/Calcular altura maxina\n2/Calcular altura minima\n3/Calcular promedio dea alturas\n4/Calcular al mas pesado\n5/Calcular peso minimo\n6/Salir\n>>")


    if(pedir_dato == "1"):
        calcular_altura_maxima()
    elif(pedir_dato == "2"):
        calcular_altura_minma()
    elif(pedir_dato == "3"):
        calcular_altura_promedio()
    elif(pedir_dato == "4"):
        calcular_peso_maximo()
    elif(pedir_dato == "5"):
        calcular_altura_minma()
    elif(pedir_dato == "6"):
        break

    respuesta = input("desea saber otro dato? si o no")
