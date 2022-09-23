

lista = [1,2,5,0,3,7,0,4]

def buscar_minimo(lista_a_buscar:list) -> int:

    minimo = 0
    
    for indice in range(len(lista_a_buscar)):

        if(lista_a_buscar[indice] < lista_a_buscar[minimo]):

            minimo = indice
        
        return minimo
        

def nahuel_sort(lista_a_ordenar:list) -> list:
    
    # lista_original = lista.copy() #shallow copy
    lista_recibida = lista_a_ordenar[:] #shallow copy
    # lista_recibida = list(lista) #shallow copy
    
    lista_ordenada = []

    indice_min = 0

    while(indice_min < len(lista_recibida)):

        minimo = buscar_minimo(lista_recibida, indice_min)
        lista_ordenada.append(lista_recibida.pop(minimo))

    return lista_ordenada

print(nahuel_sort(lista))

# print(lista)


def ivan_sort(lista_a_ordenar:list) -> list:

    lista_recibida = lista_a_ordenar[:]

    flag_swap = True

    limite = 1

    while(flag_swap == True):

    
        flag_swap = False #La ultima vuelta
        for i in range(len(lista_recibida)-1):
            if(lista_recibida[i] > lista_recibida[i+1]):

                buffer = lista_recibida[i]
                lista_recibida[i] = lista_recibida[i+1]
                lista_recibida[i+1] = buffer
                flag_swap = True
            # lista_recibida[i], lista_recibida[i+1] = lista_recibida[i+1], lista_recibida[i]

        limite += 1
        
    return lista_recibida   

# print(ivan_sort(lista))



def qsort(lista_a_ordenar:list)-> list:
    copia_lista = lista_a_ordenar[:]
    lista_der = []
    lista_izq = []
    
    if len(lista_a_ordenar) <= 1:
        return lista_a_ordenar
    else:
        pivot = copia_lista[0]
        for elemento in copia_lista[1:]:
            if(elemento > pivot):
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)

    lista_izq = qsort(lista_izq)
    lista_der = qsort(lista_der)
    lista_izq.append(pivot)

    return lista_izq + lista_der
# lista_ordenada = qsort(lista)
# print(lista_ordenada)









    # return lista_ordenada

# buffer = a 

# b = a

# a = buffer



    


# a = 22

# b = 23 

# a,b = b,a

# b = 22 a = 23








#ayuda a encontrar las mas grandes y mas chicos
# carta_pivote = 



























