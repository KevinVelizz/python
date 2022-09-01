lista_nombres = []
lista_apellidos = []

# for i in range(5):
#     nombre = input("n?")
#     apellido = input ("a?")
#     lista_nombres.append(nombre)
#     lista_apellidos.append(apellido)



lista_empleados = []


for i in range(5):
    dic_empleado = {}
    nombre = input("n?")
    apellido = input ("a?")
    dni = input("dni?")
    dic_empleado["nombre"] = nombre
    dic_empleado["apellido"] = apellido
    dic_empleado["dni"] = dni
    lista_empleados.append(dic_empleado)


for empleado in lista_empleados:
    print(empleado["nombre"])

'''
[0] NOMBRE - APELLIDO
[1] NOMBRE - APELLIDO
'''
i = 0

for i in lista_nombres:

    print(
        "[{0}] - {1} - {2}".format(i,nombre,lista_apellidos[i])
        )
    i += 1



