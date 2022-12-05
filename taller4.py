import json
def publicaciones():
    profesores= []
    yaguardados=[]
    publicaciones= open('datos/publicacion.json','r')
    datos = json.load(publicaciones)

    for i in datos:
        if not(yaguardados.__contains__(i['cedula'])):
            yaguardados.append(i['cedula'])
            profesores.append({'nombre':i['apellidos'], 'cedula':i['cedula'], 'publicaciones':0})
    for i in profesores:
        for x in datos:
            if i['cedula'] == x['cedula']:
                i['publicaciones']+=1
    for i in profesores:
        print(f"el docente {i['nombre']} tiene {i['publicaciones']}")

if __name__ == "__main__":
    publicaciones()