
import re
from traceback import print_tb
import func


'''
Ejercicio tipo parcial

Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)


Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (asc) o descendente (desc)


Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (asc) o descendente (desc)


Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición: menor o mayor) se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.

Buscar y Listar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda.

tipo de inteligencia good : los que pertenecen a ese

Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]

Aclaraciones:
Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por consola con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original



agregarle algo al codigo a este, parcial. tener capacidad de modificar.
'''

lista_heroes = func.cargar_json(func.path)


def app_stark(lista:list):


    # print(lista_heroes)
     while(True):
        print("1 - Listar los primeros heroe.\n2 - Ordenar y listar heroes por altura.\n3 - Ordenar y listar heroes por fuerza.\n4 - Calcular promedio y mostrar los que superan o no la condicion.\n5 - Buscar y listar heroes por inteligencia.\n6 - Exportar a CSV la lista de heroes ordenada.\n7 - Salir")

        dato = input(">>")


   

        if(dato == "1"):
        
            cantidad = input("Ingrese la cantidad: ")
            cantidad_validado = int(func.validar_respuesta(cantidad,"^[0-9]{1,2}$"))

            if(cantidad_validado != -1):
                if(cantidad_validado > len(lista)):
                    print("N/A")
                    
                else:
                    lista = (func.listar_heroes(lista,cantidad_validado))  
                    mensaje = ""
                    for heroe in lista:
                        mensaje += heroe["nombre"] + "\n"
                    # mensaje = func.mostrar_dato(mensaje)
                    print(mensaje)
                    mensaje_dato_uno = mensaje

            else:
                print("N/A")

        elif(dato == "2"):

            modo = input("Ingrese el modo de ordenar, descendente(desc) o ascendente(asc): ")
            modo_validado = func.validar_respuesta(modo, "^(desc|asc)$")

            if(modo_validado != -1):
                heroe_altura = func.listar_ordernar_heroe(lista,"altura",modo_validado) 
                mensaje_dato_dos = func.mostrar(heroe_altura,"altura")
                
                print(mensaje_dato_dos)

            else:
                print("N/A")


        elif(dato == "3"):
            modo = input("Ingrese el modo de ordenar, descendente(desc) o ascendente(asc): ")
            modo_validado = func.validar_respuesta(modo,"^asc|desc$")

            if(modo_validado != -1):
                    
                heroe_fuerza = func.listar_ordernar_heroe(lista,"fuerza",modo_validado) 
                mensaje_dato_tres = func.mostrar(heroe_fuerza,"fuerza")
                # print(mensaje_dato)

            else:
                print("N/A")

            print(mensaje_dato_tres)
        elif(dato == "4"):
            condicion = input("Ingrese 'menor' para ver los que no superan el promedio y 'mayor' para los que superan: ")
            condicion_clave = input("Ingrese 'fuerza', 'altura', 'peso': ")

            condicion_validado = func.validar_respuesta(condicion,"^mayor|menor$")
            condicion_clave_validado = func.validar_respuesta(condicion_clave,"^fuerza|altura|peso$")

            if(condicion_validado != -1 and condicion_clave_validado != -1):
                    
                promedio_lista = func.calcular_promedio(lista,condicion_clave_validado,condicion_validado)

                mensaje_dato_cuatro = func.mostrar(promedio_lista,condicion_clave_validado)    
    
                func.mostrar_dato(mensaje_dato)

           
        elif(dato == "5"):
            condicion = input("Ingrese good o average o high: ")
            inteligencia = func.buscar_listar_heroe_inteligencia(lista_heroes,condicion)

            mensaje_dato = "Tipo Inteligencia {0}: ".format(condicion)
            
            for personaje in inteligencia:

                mensaje_dato += personaje + ", "

            mensaje_dato = re.sub(", $", "",mensaje_dato)
            print(mensaje_dato)

        elif(dato == "6"):
            
            condicion = input("Cual lista desea exportar? ")
            condicion_validado = int(func.validar_respuesta(condicion,"^[0-9]$"))

            # print(condicion_validado)

            if(condicion_validado  < 5):

                if(condicion_validado == 1):
                    func.exportar_csv(mensaje_dato_uno)
                elif(condicion_validado == 2):
                    func.exportar_csv(mensaje_dato_dos)
                elif(condicion_validado == 3):
                    func.exportar_csv(mensaje_dato_tres)
                elif(condicion_validado == 4):
                    func.exportar_csv(mensaje_dato_cuatro)
            else:
                print("N/A")
            

            # func.exportar_csv(mensaje_dato)
        elif(dato == "7"):
            break
        
        
app_stark(lista_heroes)
