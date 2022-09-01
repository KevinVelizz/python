
precio_caro_barbijo = 0
bandera_barbijo = 0
# item_mas_unidades = 0
cantidad_unidades_barbijo = 0
fabricante_barbijo_caro = ""

unidades_barbijo = 0
unidades_jabon = 0

for i in range(2):

    tipo = input("Ingrese el tipo barbijo, jabon o alcohol")

    while(tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):

        tipo = input("error ingrese el tipo barbijo, jabon o alcohol")


    precio = int(input("Ingrese el precio entre 100 y 300"))


    while(precio < 100 or precio > 300):
        precio = int(input("error ingrese el precio entre 100 y 300"))


    cantidad_unidades = int(input("Ingrese el cantidad de unidades entre 1 y 1000"))

    while(cantidad_unidades < 1 or cantidad_unidades > 1000):

        cantidad_unidades = int(input("Ingrese el cantidad de unidades entre 1 y 1000"))

    marca = input("Ingrese la marca")

    fabricante = input("Ingrese el fabricante")


    if (tipo == "barbijo"):
        if (bandera_barbijo == 0 or precio > precio_caro_barbijo):
            precio_caro_barbijo = precio
            cantidad_unidades_barbijo = cantidad_unidades
            fabricante_barbijo_caro = fabricante

        
    if( i == 0 or cantidad_unidades > item_mas_unidades):
        item_mas_unidades = cantidad_unidades
        fabricante_mas_unidades = fabricante    

    if(tipo == "jabon"):
        unidades_jabon += cantidad_unidades



if(unidades_barbijo > 0):
    mensaje = "La cantidad de jabones es :", unidades_jabon
else:
    mensaje = "No se ingresaron jabones"


print("La cantidad de unidades es", cantidad_unidades_barbijo, "unidades y el fabricante es", fabricante_barbijo_caro,"\nEl item con mas unidades el fabricante es:", fabricante_mas_unidades , "y la cantidad es", item_mas_unidades, "\n",mensaje)








   

