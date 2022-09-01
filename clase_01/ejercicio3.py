# Veliz Kevin
# Ejercicio Integrador 03

# La división de alimentos de industrias Wayne está trabajando en un pequeño software para cargar datos de heroínas y héroes, para para tener un control de las condiciones de heroes existentes, nos solicitan:
# Nombre de Heroína/Héroe
# EDAD (mayores a 18 años)
# Sexo ("m", "f" o "nb")
# Habilidad ("fuerza", "magia", "inteligencia").
# A su vez, el programa deberá mostrar por consola lo siguiente:
# A-Dar el nombre de Héroe | Heroína de 'fuerza' más joven.
# B-El sexo y nombre de Heroe | Heroína de mayor edad.
# C-La cantidad de Heroinas que tienen habilidades de 'fuerza' o 'magia'.
# D-El promedio de edad entre Heroinas.
# E-El promedio de edad entre Heroes de fuerza.



respuesta = "si"
bandera_fuerza = 0
bandera_mayor_edad = 0
contador_fuerza_magia = 0
acumulador_heroinas = 0
contador_heroinas = 0
acumulador_edad_femenino = 0
acumulador_edad_masculino = 0
contador_masculino = 0

nombre_joven = ""
edad_joven = ""

while(respuesta == "si"):

    nombre_heroe_heroina = input("Ingrese el nombre del heroína/héroe")

    edad = int(input("Ingrese la edad mayor a 18"))
    while(edad < 18):
        edad = int(input("Error, ingrese la edad mayor a 18"))

    sexo = input("Ingrese el sexo f o m o nb")
    while(sexo !="f" and sexo !="m" and sexo !="nb"):
        sexo = input("Error, ingrese el sexo f o m o nb")

    habilidad = input("ingrese la habilidad. fuerza, magia, inteligencia")
    while(habilidad !="fuerza" and habilidad !="magia" and habilidad !="inteligencia"):
        habilidad = input("ingrese la habilidad. fuerza, magia, inteligencia")


    if(habilidad == "fuerza"):
        if(bandera_fuerza == 0 or edad < edad_joven):
            edad_joven = edad
            nombre_joven = nombre_heroe_heroina
            bandera_fuerza = 1
        if(sexo == "m"):
            acumulador_edad_masculino += edad
            contador_masculino += 1

    if(bandera_mayor_edad == 0 or edad > edad_mayor):
        edad_mayor = edad
        nombre_mayor_edad = nombre_heroe_heroina
        sexo_mayor_edad = sexo


    if(sexo == "f"):
        acumulador_edad_femenino += edad
        contador_heroinas += 1
        if(habilidad !="inteligencia"):
            contador_fuerza_magia += 1

    respuesta = input("Desea ingresar otro dato? si o no")


if(bandera_fuerza == 0):
    mensaje_dos = "No se ingresaron heroes/heroinas de fuerza"
else:

    mensaje_dos ="El nombre de Heroe/heroina de fuerza mas joven es:", nombre_joven, "con", edad_joven, "años" 


if(contador_heroinas == 0):
    mensaje = "No se ingresaron heroinas"
else:
    promedio_heroina = acumulador_edad_femenino / contador_heroinas
    mensaje = "El promedio de edad entre heroinas es:", promedio_heroina

if(contador_masculino == 0):
    mensaje_uno = "No se ingresaron heroes de fuerza"
else:
    promedio_heroes_fuerza = acumulador_edad_masculino / contador_masculino
    mensaje_uno = "El promedio de edad entre heroes de fuerza es:", promedio_heroes_fuerza


print(mensaje_dos,"\n" "El sexo y nombre de heroe/heroina de mayor edad es:", sexo_mayor_edad, nombre_mayor_edad, "con", edad_mayor, "años" "\n" "La cantidad de Heroinas que tienen habilidades de fuerza o magia es:", contador_fuerza_magia, "\n", mensaje, "\n", mensaje_uno)