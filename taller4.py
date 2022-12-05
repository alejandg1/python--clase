import json


def publicaciones():
    profesores= []
    yaguardados=[]
    publicaciones= open('datos/publicacion.json','r')
    datos = json.load(publicaciones)

    for i in datos:
        nombre= i['apellidos']
        cedula= i['cedula']
        if not(yaguardados.__contains__(cedula)):
            yaguardados.append(cedula)
            profesores.append({'nombre':nombre, 'cedula':cedula, 'publicaciones':0})
    for i in profesores:
        cedula=i['cedula']
        for x in datos:
            if cedula == x['cedula']:
                i['publicaciones']+=1
    for i in profesores:
        print(f"el docente {i['nombre']} tiene {i['publicaciones']}")



if __name__ == "__main__":
    publicaciones()