from data_stark import lista_personajes


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

def primero_heroina():

    for heroe in lista_personajes:
        if(heroe["genero"] == "F"):
           return heroe

def primer_masculino():
    for heroe in lista_personajes:
        if(heroe["genero"] == "M"):
            return heroe

# print(primero_heroina())
# print(primer_masculino())





#-----------superheroes género M-------------


def mostar_nombre_masculino():

    for heroe in lista_personajes:

        if(heroe["genero"] == "M"):

            print("Nombre: {0} | Genero: {1}".format(heroe["nombre"], heroe["genero"]))
            
# mostar_nombre_masculino()

#-----------superheroes género F-------------

def mostar_nombre_femenino():

    for heroe in lista_personajes:

        if(heroe["genero"] == "F"):

            print("Nombre: {0} | Genero: {1}".format(heroe["nombre"], heroe["genero"]))

# mostar_nombre_femenino()


#-----------superheroes género M mas alto-------------

def calcular_heroe_mas_alto():

    heroe_mas_alto = primer_masculino()
    

    for heroe in lista_personajes:
        
        heroe["altura"] = float(heroe["altura"])
        if(heroe["genero"] == "M"):
            if(heroe["altura"] > float(heroe_mas_alto["altura"])):
                heroe_mas_alto = heroe

    print("Nombre: {0} | Altura: {1}".format(heroe_mas_alto["nombre"], heroe_mas_alto["altura"]))



# calcular_heroe_mas_alto()



# #-----------superheroes género F mas alto-------------


def calcular_superheroe_mas_alto_femenino():

    femenino_mas_alto = primero_heroina()

    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if(heroe["genero"] == "F"):
            if(heroe ["altura"] > float(femenino_mas_alto["altura"])):
                femenino_mas_alto = heroe

    print("Nombre: {0} | Altura: {1}".format(femenino_mas_alto["nombre"], femenino_mas_alto["altura"]))
    

# calcular_superheroe_mas_alto_femenino()
    

#-----------superheroes género M mas bajo--------------

def calcular_heroe_mas_bajo():

    heroe_mas_bajo = primer_masculino()

    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if(heroe["genero"] == "M"):    

            if(heroe["altura"] < float(heroe_mas_bajo["altura"])):
                heroe_mas_bajo = heroe

    print("Nombre: {0} | Altura: {1}".format(heroe_mas_bajo["nombre"], heroe_mas_bajo["altura"]))


# calcular_heroe_mas_bajo()

#-----------superheroes género F mas bajo-------------

def calcular_heroina_mas_baja():

    heroina_mas_baja = primero_heroina()
    
    for heroe in lista_personajes:
        heroe["altura"] = float(heroe["altura"])
        if(heroe["genero"] == "F"):

            if(heroe["altura"] < float(heroina_mas_baja["altura"])):
               heroina_mas_baja = heroe

    print("Nombre: {0} | Altura: {1}".format(heroina_mas_baja["nombre"], heroina_mas_baja["altura"]))



# calcular_heroina_mas_baja()

#---------promedio altura masculino-------------

def calcular_promedio_masculinos():

    acumulador_altura_masculino = 0
    contador_masculino = 0

    for heroe in lista_personajes:
        
        heroe["altura"] = float(heroe["altura"])

        if(heroe["genero"] == "M"):
            acumulador_altura_masculino += heroe["altura"]
            contador_masculino += 1

    print("El promedio es: {0}".format(acumulador_altura_masculino / contador_masculino))

# calcular_promedio_masculinos()



#-------------promedio altura femenino-----------

def calcular_promedio_altura_femenino():

    acumulador_altura_fememino = 0
    contador_femenino = 0
    
    for heroe in lista_personajes:
        
        heroe["altura"] = float(heroe["altura"])

        if(heroe["genero"] == "F"):
            acumulador_altura_fememino += heroe["altura"]
            contador_femenino += 1

    print("Promedio es: {0}".format(acumulador_altura_fememino / contador_femenino))

# calcular_promedio_altura_femenino()


def nombre_de_los_superheroes_calculados():

    calcular_heroe_mas_alto()
    calcular_heroe_mas_bajo()
    calcular_superheroe_mas_alto_femenino()
    calcular_heroina_mas_baja()
    


# nombre_de_los_superheroes_calculados()


#-------------heroe por color de ojos--------------


def cantidad_superheroes_colores_ojos():

    cantidad_color_de_ojos = {}


    for heroe in lista_personajes:

        heroe["color_ojos"] = heroe["color_ojos"].lower()        

        cantidad_color_de_ojos[heroe["color_ojos"]] = 0

    for heroe in lista_personajes:
        cantidad_color_de_ojos[heroe["color_ojos"]] += 1
    
    
    
    print(cantidad_color_de_ojos)

# cantidad_superheroes_colores_ojos()



#---------ejercicio L------------

def heroe_tipo_inteligencia():

    cantidad_inteligencia = {}

    for heroe in lista_personajes:

        heroe["inteligencia"] = heroe["inteligencia"].lower()

        if(heroe["inteligencia"] == ""):

            heroe["inteligencia"] = "No tiene"    
        

        cantidad_inteligencia[heroe["inteligencia"]] = 0
        

    for heroe in lista_personajes:
        cantidad_inteligencia[heroe["inteligencia"]] += 1

    print(cantidad_inteligencia)


# heroe_tipo_inteligencia()


#----------------heroe por color de pelo------------------

def heroes_por_color_ojos():

    heroe_color_ojos = {}
    

    for heroe in lista_personajes:

        heroe["color_ojos"] = heroe["color_ojos"].lower()
        
        heroe_color_ojos[heroe["color_ojos"]] = 0

    for color_ojo in heroe_color_ojos:
        # print(color_ojo)

        lista_heroe_color_ojo = []

        for heroe in lista_personajes:
            
            if(heroe["color_ojos"] == color_ojo):

                lista_heroe_color_ojo.append(heroe["nombre"])

        heroe_color_ojos[color_ojo] = lista_heroe_color_ojo



    print(heroe_color_ojos)
        
        

# heroes_por_color_ojos()
    


def heroe_por_color_pelo():

    heroe_color_pelo = {}
    
    for heroe in lista_personajes:

        heroe["color_pelo"] = heroe["color_pelo"].lower()

        heroe_color_pelo[heroe["color_pelo"]] = 0

    for color_pelo in heroe_color_pelo:
        # print(color_ojo)

        lista_heroe_color_pelo = []

        for heroe in lista_personajes:
            
            if(heroe["color_pelo"] == color_pelo):

                lista_heroe_color_pelo.append(heroe["nombre"])

        heroe_color_pelo[color_pelo] = lista_heroe_color_pelo


    print(heroe_color_pelo)

# heroe_por_color_pelo()



respuesta = "si"

while(respuesta == "si"):

    pedir_dato = input("ingrese\n1/mostrar nombres masculinos\n2/mostrar nombres femeninos\n3/Calcular altura mas alta superheroe\n4/Calcular altura superheroe \n5/Calcular altura mas alta superheroina\n6/Calcular altura mas baja superheroina\n7/Calcular promedio de altura superhores\n8/Calcular promedio de altura superheroinas\n9/Listar superheroes por cada tipo de color de ojos\n10/Listar superheores por cada tipo de color de pelo\n11/Listar superheroes por inteligencia\n12/Superheroes alto/bajo y superheroinas alta/baja \n13/Salir>>")


    if(pedir_dato == "1"):
        mostar_nombre_masculino()
    elif(pedir_dato == "2"):
        mostar_nombre_femenino()
    elif(pedir_dato == "3"):
        calcular_heroe_mas_alto()
    elif(pedir_dato == "4"):
        calcular_heroe_mas_bajo()
    elif(pedir_dato == "5"):
        calcular_superheroe_mas_alto_femenino()
    elif(pedir_dato == "6"):
        calcular_heroina_mas_baja()
    elif(pedir_dato == "7"):
        calcular_promedio_masculinos()
    elif(pedir_dato == "8"):
        calcular_promedio_altura_femenino()
    elif(pedir_dato == "9"):
        heroes_por_color_ojos()
    elif(pedir_dato == "10"):
        heroe_por_color_pelo()
    elif(pedir_dato == "11"):
        heroe_tipo_inteligencia()
    elif(pedir_dato == "12"):
        nombre_de_los_superheroes_calculados()
    elif(pedir_dato == "13"):
        break



