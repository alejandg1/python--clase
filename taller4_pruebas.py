import json
publicaciones = open('datos/publicacion.json', 'r')
datos = json.load(publicaciones)
profesores = []
articulos = []



def menu():
    print("elija la informacion que desea ver: 1. datos de los docentes  2. total de docentes y publicaciones ")
    eleccion = input("ingrese su eleccion:  ")
    match eleccion:
        case "1":
            imprimir()
        case "2":
            print("________________________________________________________________________________________")
            print(f"el total de docentes es: {len(profesores)}")
            print(f"el total de articulos es: {len(articulos)}")
            print("_________________________________________________________________________________________")

def articulo_area():
    guardado=[]
    guardado_area=[]
    for i in datos:
        for docente in profesores:
            if docente['cedula']== i['cedula'] &  (not (guardado.__contains__(i['articulos']))):
                guardado.append(i['articulos'])
                docente['articulos'].append(i['articulos'])
            if docente['cedula']==i['cedula'] & (not (guardado_area.__contains(i['area']))):
                docente['area']==i['area']


def docentes():
    guardado = []
    for i in datos:
        if not (articulos.__contains__(i['articulos'])):
            articulos.append(i['articulos'])

        if not (guardado.__contains__(i['cedula'])):
            guardado.append(i['cedula'])
            profesores.append(
                {'nombre': i['apellidos'], 'cedula': i['cedula'], 'publicaciones': 0, 'area':'', 'articulos':[]})



def publicacion_n():
    for i in profesores:
        for x in datos:
            if i['cedula'] == x['cedula']:
                i['publicaciones'] += 1


def imprimir():
    docentes()
    articulo_area()
    publicacion_n()
    for docente in profesores:
        print(docente)


if __name__ == "__main__":
    menu()
