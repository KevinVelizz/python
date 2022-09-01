# Veliz Kevin



respuesta = "si"
bandera_alimento_caro = 0
acumulador_precio_kilo = 0
contador = 0
acumulador_peso = 0

while(respuesta == "si"):

    peso = int(input("Ingrese el peso entre 10 y 100"))
    while(peso < 10 or peso > 100):
        peso = int(input("error ingrese el peso entre 10 y 100"))


    precio_kilo = int(input("Ingrese el precio por kilo"))
    while(precio_kilo < 0):
        precio_kilo = int(input("Error, ingrese el precio por kilo"))

    
    tipo = input("Ingrese el tipo v(vegetal), a(animal), m(mezcla)")
    while(tipo !="v" and tipo !="a" and tipo !="m"):
        tipo = input("Error, ingrese el tipo v(vegetal), a(animal), m(mezcla)")


    acumulador_peso += peso

    if(acumulador_peso > 300):
        porcentaje = 0.75
    elif(acumulador_peso > 100):
        porcentaje = 0.85

    if(bandera_alimento_caro == 0 or precio_kilo > precio_mas_caro):
        precio_mas_caro = precio_kilo
        tipo_precio_caro = tipo
        bandera_alimento_caro = 1


    acumulador_precio_kilo += precio_kilo
    contador+=1





    respuesta = input("Desea ingresar otro dato? si o no")
    

importe_bruto = acumulador_peso * acumulador_precio_kilo


if(acumulador_peso > 300):
    mensaje_descuento = "El descuento es del 25%"
    importe_total = importe_bruto * porcentaje
    mensaje = "El importe total es ", importe_total
elif(acumulador_peso > 100):
    mensaje_descuento = "El descuento es del 15%"
    importe_total = importe_bruto * porcentaje
    mensaje = "El importe total es", importe_total
else:
    mensaje_descuento ="No hubo descuento"
    mensaje = "El importe total es", importe_bruto

promedio = acumulador_precio_kilo / contador
    


print("El importe bruto es", importe_bruto,"\n", mensaje_descuento,"\n", mensaje,"\n" "El tipo de alimento mas caro es", tipo_precio_caro, "\nEl promedio de precio por kilo es", promedio)