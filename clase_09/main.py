

import time



# lista_ordenada = sorted(lista)


# print(lista_ordenada)









lista = [20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4,20,3,6,1,4,8,23,3,4]




def encontrar_minimo(lista_recibida):

    num_min = 0


    for index in range(len(lista_recibida)):
        
        # print(index)

        if(lista_recibida[index] < lista_recibida[num_min]):


            num_min = index
            
    # print(num_min)
    return num_min

# encontrar_minimo(lista)




def nahuel_sort(lista:list) -> list:

    lista_recibida = lista.copy()
    # print(lista_recibida)

    lista_ordenada = []

    while(len(lista_recibida) > 0):
        
        numero_min = encontrar_minimo(lista_recibida)


        lista_ordenada.append(lista_recibida.pop(numero_min))
    
    
    return lista_ordenada
        


# print(nahuel_sort(lista))





def ivan_sort(lista:list) -> list:

    lista_recibida = lista[:]

    

    for j in lista:  
        flag_intercambio = False
        for index in range(len(lista_recibida) - j):
            if(lista_recibida[index] > lista_recibida[index + 1]):

                lista_recibida[index], lista_recibida[index + 1] = lista_recibida[index + 1], lista_recibida[index]

                flag_intercambio = True

        if(flag_intercambio == False):
            break    
    
    return lista_recibida

inicio = time.time()
print(ivan_sort(lista))
final = time.time()

tiempo = final - inicio

print(tiempo)