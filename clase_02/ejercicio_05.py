habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]


dic_habilidades={}
habilidades_utn=[]

for habilidad in habilidades:
    hab_utn= []
    for dato in habilidad:
        hab_utn.append(habilidad[dato])
    hab_utn_tupla=tuple(hab_utn)
    habilidades_utn.append(hab_utn_tupla)
    dic_habilidades["habilidades_utn"]=habilidades_utn



print(dic_habilidades)



















# print(habilidades)

# dic_habilidades = {}

# habilidades_utn = []

# for habilidad in habilidades:
#     hab = []
#     for dato in habilidad:
#         # print(habilidad[dato])
#         habilidades_utn.append(habilidad[dato])
#     habilidades_utn_tupla = tuple(habilidades_utn)
#     habilidades_utn.append(hab)

# habilidades_utn_rayo = tuple(hab)


# print(habilidades_utn)

# for habilidad in habilidades:
    

# for habilidad in habilidades:
