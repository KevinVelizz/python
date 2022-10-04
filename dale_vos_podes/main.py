import re

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

path = r"C:\Users\veliz\Desktop\python\dale_vos_podes\data.json"

lista_heroes = func.importar_json(path)

def app_stark(lista:list) -> str:


    
    while(True):

        menu = print("Ingrese\n1 - Listar los primeros N héroes.\n2 - Ordenar y Listar héroes por altura.\n3 - Ordenar y Listar héroes por fuerza.\n4 - Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio \n5 - Buscar y Listar héroes por inteligencia\n6 - Exportar a CSV la lista de héroes.\n7 Salir.")

        seleccion = input(">>> ")

        if(seleccion == "1"):

            lista = func.imprimir_listar_dato(lista_heroes)

        elif(seleccion == "2"):

            lista = func.imprimir_lista_ordenada(lista_heroes,"altura")
        elif(seleccion == "3"):
            
            lista = func.imprimir_lista_ordenada(lista_heroes,"fuerza")
            
        elif(seleccion == "4"):
            
            lista = func.imprimir_dato_promedio(lista_heroes)

        elif(seleccion == "5"):
            
            condicion_inteligencia = input("Ingrese good, average, high: ")
                
            lista = func.listar_heroes_inteligencia(lista,condicion_inteligencia)


            mensaje = "Tipo inteligencia {0}: ".format(condicion_inteligencia)
            for heroe in lista:

                mensaje += heroe + ", "
                
            mensaje = re.sub(", $","",mensaje)

            mensaje_cinco = mensaje

            print(mensaje_cinco)


        elif(seleccion == "6"):
            
            func.exportar_lista(lista)

        elif(seleccion == "7"):
            break   


app_stark(lista_heroes)