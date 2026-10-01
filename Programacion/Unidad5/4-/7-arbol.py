import os

directorio = "/home/fernando/Programacion"


def arbol(ruta, prefijo=""):

    elementos = sorted(os.listdir(ruta))

    for i, elemento in enumerate(elementos):

        ruta_completa = os.path.join(ruta, elemento)

        ultimo = i == len(elementos) - 1

        if ultimo:
            conector = "└── "
        else:
            conector = "├── "

        print(prefijo + conector + elemento)

        if os.path.isdir(ruta_completa):

            if ultimo:
                nuevo_prefijo = prefijo + "    "
            else:
                nuevo_prefijo = prefijo + "│   "

            arbol(ruta_completa, nuevo_prefijo)


print(os.path.basename(directorio) + "/")
arbol(directorio)
