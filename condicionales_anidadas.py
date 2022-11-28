def beca_academica(estudiantes):
    for i in estudiantes:
        if  95 <= i['promedio']<= 100:
            cumple= True
        else:
            cumple= False
        if  90<=i['asistencia'] <=100:
            cumplea= True
        else:
            cumplea= False
        if i['deuda']==0:
            cumpled= True
        if cumple & cumplea & cumpled:
            i['beca']= True
    for i in estudiantes:
        if i['beca']:
            print(f"beca academica a {i['nombre']} {i['beca']} ")


def run():
    estudiantes= [
        {'nombre': 'Alejandro', 'sexo': 'M', 'carrera': 'sof', 'estado S.E.': 'Medio', 'promedio': 80, 'asistencia': 100, 'beca': False, 'deuda': 0},
        {'nombre': 'ED', 'sexo': 'F', 'carrera': 'bio', 'estado S.E.': 'Medio alto', 'promedio': 99, 'asistencia': 97, 'beca': False, 'deuda': 0},
        {'nombre': 'alguien', 'sexo': 'M', 'carrera': 'soft', 'estado S.E.': 'Medio', 'promedio': 97, 'asistencia': 40, 'beca': False, 'deuda': 0},
        {'nombre': 'Carlos', 'sexo': 'F', 'carrera': 'med', 'estado S.E.': 'medio bajo', 'promedio': 75, 'asistencia': 80, 'beca': False, 'deuda': 0},
        {'nombre': 'Udyr', 'sexo': 'M', 'carrera': 'sof', 'estado S.E.': 'Medio', 'promedio': 78, 'asistencia': 90, 'beca': False, 'deuda': 0},
        {'nombre': 'Martha', 'sexo': 'F', 'carrera': 'sof', 'estado S.E.': 'Medio', 'promedio': 62, 'asistencia': 55, 'beca': False, 'deuda': 0},
        {'nombre': 'Camille', 'sexo': 'F', 'carrera': 'sof', 'estado S.E.': 'Medio', 'promedio': 30, 'asistencia': 90, 'beca': False, 'deuda': 0},
        {'nombre': 'Andres', 'sexo': 'M', 'carrera': 'med', 'estado S.E.': 'bajo', 'promedio': 70, 'asistencia': 60, 'beca': False, 'deuda': 0},
        {'nombre': 'Alison', 'sexo': 'f', 'carrera': 'bio', 'estado S.E.': 'medio', 'promedio': 98, 'asistencia': 80, 'beca': False, 'deuda': 0},
        {'nombre': 'Adrian', 'sexo': 'M', 'carrera': 'med', 'estado S.E.': 'alto', 'promedio': 96, 'asistencia': 90, 'beca': False, 'deuda': 0},
    ]
    beca_academica(estudiantes)
    


if __name__ == "__main__":
    run()