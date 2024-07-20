import os


def rutas(directorio):
    ## Acá guardamos las rutas
    rutas_fotos = []

    for root, dirs, files in os.walk(directorio):
        for file in files:
            ruta = os.path.join(root, file)
            rutas_fotos.append(ruta)


    return rutas_fotos


dir = "/home/khewa/Escritorio/Personal/Proyectos/chatbot/photos"

fotos = rutas(dir)
"""
### ciclo para imprimir las fotos
for foto in fotos:
    print(foto)
"""