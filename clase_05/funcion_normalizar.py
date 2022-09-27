from stark import lista_personajes 


#-------Funcion para normalizar datos que sean numericos 

def stark_normalizar_datos(lista:list, clave:str) -> dict:

    '''
    Normaliza los datos numericos de tipo string a int.
    Retorna un diccionario.
    Parametros lista y clave.
    ''' 
    if(type(lista) == type([]) and type(clave) == type("") and len(lista) > 0):
        print(lista_personajes)

        for normalizar_datos in lista:

            print(normalizar_datos)
            
            if(type(normalizar_datos[clave]) == type("")):
                if(clave == "altura"):
                    normalizar_datos["altura"] = float(normalizar_datos["altura"])
                elif(clave == "peso"):
                    normalizar_datos["peso"] = float(normalizar_datos["peso"])
                elif(clave == "fuerza"):
                    normalizar_datos["fuerza"] = int(normalizar_datos["fuerza"])
        print("Datos normalizados")
        
    else:
        print("Error: Lista de héroes vacía")
        # print(normalizar_datos)


stark_normalizar_datos(lista_personajes, 1)



# def obtener_nombre(heroe:dict) -> str:

    





