

heroes_para_reclutar = ["Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]



heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}




seleccion = {}

for heroes in heroes_para_reclutar:
    for dato in heroes_info:
        if heroes == dato:
            seleccion[heroes] = heroes_info[heroes]
            seleccion[heroes]["Habilidades"] = set(seleccion[heroes]["Habilidades"])
    


print(seleccion)

# for habilidades in seleccion:
#     if habilidades == set(seleccion[heroes]["Habilidades"]):
#         print(habilidades)



# print(seleccion)


# Preparando todo para reclutar héroes y heroínas para la liga de la justicia, el departamento de HR dispone de una larga lista de justicieros pero solo tiene información detallada de algunos de ellos.
# Es por eso que te piden que desarrolles un pequeño programa el cual basado en la lista 'heroes_para_reclutar' busque en el diccionario 'heroes_info' los que coincidan y los guarde en un nuevo diccionario para luego imprimir por consola todos sus datos. (id, origen, etc)
# TIP: Las habilidades están repetidas, busca la manera de que en el resultado final no existan duplicados, que usarías para eso?