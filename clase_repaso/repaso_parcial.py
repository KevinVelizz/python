
# from func import cargar_json
# from func import *
import func 

# func.cargar_json()

def app():

    # func.cargar_json("x")

    lista_data = func.cargar_json(func.path)

    # print(lista_data)
    
    func.stark_normalizar_datos(lista_data)
    # print(lista_data)

    while(True):
        print('''1 - listar\n2 - ordernar\n3 - buscar\n4 - recargar\n5 - exportar a csv\n6 Salir''')
        respuesta = input(">>>")

        control = "2"

        if(respuesta == "1"):
            top = int(input("\nCantidad de elementos a mostrar"))
            #VALIDAR QUE TOP SEA UN INT Y QUE NO SUPERE LAS OPCIONES.. OBTENER ENTERO MAS CHICO O MAS GRANDE
            func.mostar(lista_data[:top])
        elif(respuesta == "2"):
            func.mostar(func.nahuel_sort_repaso(lista_data,"peso", "down"))
            pass
        elif(respuesta == "3"):
            print("buscar")
        elif(respuesta == "4"):
            patron = input("buscar: ")
            func.buscar(lista_data, patron)
        elif(respuesta == "5"):
            # func.exportar_csv(lista_data, func.path)
            pass
        elif(respuesta == "6"):
            break
    

app()

