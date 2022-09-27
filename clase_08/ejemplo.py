

def parse_csv(nombre_archivo:str) -> list:

    lista_rta = []

    with open(nombre_archivo, "r") as archivo:
    # archivo = open(nombre_archivo, "r")

        for linea in archivo:
            # print(linea)
            lista = linea.split(",")
            video = {}
            video["title"] = lista[0]
            video["views"] = int(lista[1])
            video["length"] = int(lista[2])
            video["img_url"] = lista[3]
            video["url"] = lista[4]
            video["date"] = lista[5]
            
            lista_rta.append(video)

    # archivo.close()

    return lista_rta



# lista_brzp = parse_csv("ruta acceso")


print(lista_brzp)






def generar_csv(nombre_archivo:str, lista:list):

    with open(nombre_archivo, "w") as archivo:
        for video in lista:

            mensaje = "{0}, {1},{2},{3},{4},{5}"
            mensaje = mensaje.format(video["title"],
                    video["views"],
                    video["length"],
                    video["img_url"],
                    video["url"],
                    video["date"],)

        archivo.write(mensaje)
        # print(mensaje)


import json

def parse_json(nombre_archivo:str):

    dic_json = {}

    with open(nombre_archivo, "r") as archivo:
      dic_json = json.load(archivo)
    return dic_json["bzrp"]



lista_bzrp = parse_json("url acceso")



# lista_brzp = parse_csv("ruta acceso")
# generar_csv("url acceso", lista_brzp)




def parse_json_manual(nombre_archivo:str) -> list:

    lista_rta = []

    with open(nombre_archivo, "r") as archivo:
        texto_archivo = archivo.read()

        for linea in archivo:
            # print(linea)
            pass

    respuesta = re.findall('"title": "([a-zA-Z0-9\ | #-]+)',texto_archivo)

    respuesta = re.findall('"title": "([^,]+)',texto_archivo)


    print(respuesta)


lista_bzrp = parse_json_manual("url acceso")



# re.findal('"title": "[a-zA-Z0-9\ | #]+',t)



