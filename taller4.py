import json


def publicaciones():
    profesores = []
    yaguardados = []
    articulos = []
    cantidad_profesores = 0
    publicaciones = open('datos/publicacion.json', 'r')
    datos = json.load(publicaciones)

    for i in datos:
        if not (articulos.__contains__(i['articulos'])):
            articulos.append(i['articulos'])

        if not (yaguardados.__contains__(i['cedula'])):
            cantidad_profesores+=1
            yaguardados.append(i['cedula'])
            profesores.append(
                {'nombre': i['apellidos'], 'cedula': i['cedula'], 'publicaciones': 0})
                
    for i in profesores:
        for x in datos:
            if i['cedula'] == x['cedula']:
                i['publicaciones'] += 1
    for i in profesores:
        print(f"el docente {i['nombre']} tiene {i['publicaciones']}")
    print(f" hay {cantidad_profesores} profesores en total")
    print(f"existen {len(articulos)} articulos publicados")


if __name__ == "__main__":
    publicaciones()
