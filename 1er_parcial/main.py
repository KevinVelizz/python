import re
from time import monotonic_ns
import funciones

'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - 3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir

'''


def starwars_app():
    lista_personajes = funciones.cargar_json(r"1er_parcial\data.json")

    lista_personajes_validada = funciones.normalizar_datos(lista_personajes)

    # print(lista_personajes_validada)

    while(True):

        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            print("1 - Listar los personajes ordenados por altura\n")

            lista = funciones.ordenar_heroes_por_clave(lista_personajes_validada,"height","desc")

            mostrar = funciones.mostrar(lista,"height")

            print(mostrar)

        elif(respuesta=="2"):
            print("2 - Mostrar el personaje mas alto de cada genero\n")

            genero = input("Ingrese el genero: n/a, female, male: ")

            genero_validado = funciones.validar_respuesta(genero,"^n/a|female|male$")

            if(genero_validado != -1):


                nombre = funciones.mostar_personaje_mas_alto_genero(lista,genero_validado)

                print(nombre)
            else:
                print("N/A")
                

        elif(respuesta=="3"):
            print("3 - Ordenar los personajes por peso\n")

            condicion = input("Ingrese desc o asc: ")

            codicion_validado = funciones.validar_respuesta(condicion,"^desc|asc$")

            if(codicion_validado != -1):


                lista = funciones.ordenar_heroes_por_clave(lista_personajes,"mass",codicion_validado)

                mostrar =  funciones.mostrar(lista,"mass")

                print(mostrar)
            else:
                print("N/A")


            print(mostrar)    
        elif(respuesta=="4"):
            print("4 - Armar un buscador de personajes\n")

            respuesta = input("Ingrese el personaje: ")

            funciones.buscador_personajes(lista_personajes_validada,respuesta)

        elif(respuesta=="5"):
            print("5 - Exportar lista personajes a CSV\n")

            funciones.exportar_csv(lista)


        elif(respuesta=="6"):
            break


starwars_app()